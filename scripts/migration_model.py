#!/usr/bin/env python3
"""Synthetic planning scenarios; no cryptography, scanning, probability or security rating."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VULNERABLE = {"RSA-2048", "ECDH-P256"}
ALLOWED_USES = {"key_transport", "key_agreement", "signature", "key_encapsulation", "unknown"}


def number(value, label):
    if isinstance(value, bool):
        raise ValueError(f"{label}: boolean is not a number")
    try:
        result = float(value)
    except (ValueError, TypeError):
        raise ValueError(f"{label}: a nonnegative finite number is required") from None
    if not math.isfinite(result) or result < 0:
        raise ValueError(f"{label}: a nonnegative finite number is required")
    return result


def evaluate(asset, horizon):
    if not isinstance(asset, dict):
        raise ValueError("Asset must be an object")
    horizon = number(horizon, "horizon")
    if horizon == 0:
        raise ValueError("horizon must be positive")
    use = asset.get("use")
    if not isinstance(use, str) or use not in ALLOWED_USES:
        raise ValueError("Unknown cryptographic use")
    lifetime = number(asset.get("confidentiality_years"), "confidentiality_years")
    migration = number(asset.get("migration_years"), "migration_years")
    algorithm = asset.get("algorithm")
    if algorithm is not None and (not isinstance(algorithm, str) or not algorithm.strip()):
        raise ValueError("Algorithm must be null or a nonempty string")
    if not algorithm:
        return {"state": "inventory_gap", "slack_years": None, "reason": "Algorithm is unknown; do not infer protection."}
    if use == "signature":
        return {"state": "signature_review", "slack_years": None, "reason": "Confidentiality timing model does not assess signature forgery or update trust."}
    if algorithm not in VULNERABLE:
        return {"state": "algorithm_review", "slack_years": None, "reason": "Outside the deliberately narrow vulnerable-algorithm set; not a safe finding."}
    if use not in {"key_transport", "key_agreement"}:
        return {"state": "use_review", "slack_years": None, "reason": "Algorithm/use combination needs manual review."}
    slack = horizon - lifetime - migration
    return {"state": "planning_trigger" if slack <= 0 else "positive_slack",
            "slack_years": slack,
            "reason": "Trigger when scenario horizon <= confidentiality lifetime + migration duration; equality triggers."}


def simulate(assets, horizons):
    if not isinstance(assets, list) or not all(isinstance(a, dict) for a in assets):
        raise ValueError("Assets must be an array of objects")
    ids = [a.get("id") for a in assets]
    if not ids or any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        raise ValueError("Asset IDs must be nonempty, unique strings")
    output = []
    for horizon in horizons:
        for asset in assets:
            output.append({"asset_id": asset["id"], "horizon_years": number(horizon, "horizon"),
                           **evaluate(asset, horizon)})
    return output


def report(input_path, horizons):
    raw = Path(input_path).read_bytes()
    inventory = json.loads(raw)
    if not isinstance(inventory, dict) or inventory.get("data_origin") != "synthetic":
        raise ValueError("This demonstration accepts only explicitly synthetic inventories")
    return {"model_version": "1.0", "data_origin": "synthetic", "input_sha256": hashlib.sha256(raw).hexdigest(),
            "interpretation": "A planning heuristic under hypothetical horizons; not a threat forecast, validated risk score, benchmark or security certification.",
            "rows": simulate(inventory["assets"], horizons)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data/synthetic_inventory.json")
    parser.add_argument("--output", type=Path, default=ROOT / "results/migration_scenarios.json")
    parser.add_argument("--horizons", nargs="+", type=float, default=[5, 10, 20])
    args = parser.parse_args()
    result = report(args.input, args.horizons)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    csv_path = args.output.with_suffix(".csv")
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=["asset_id", "horizon_years", "state", "slack_years", "reason"])
    writer.writeheader()
    writer.writerows(result["rows"])
    csv_path.write_text(stream.getvalue(), encoding="utf-8")
    print(f"Wrote {len(result['rows'])} synthetic scenarios to {args.output} and {csv_path}")


if __name__ == "__main__":
    main()
