#!/usr/bin/env python3
"""Build and verify the CES research review without network access."""
import argparse
import csv
import hashlib
import io
import json
import math
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(root, path):
    def invalid(value):
        raise ValueError("Nonfinite JSON value: " + value)
    return json.loads((root / path).read_text(), parse_constant=invalid)


def positive(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise ValueError(name + ": positive finite numeric value required")
    return value


def cagr(record):
    start = positive(record["base_value_usd_billion"], "base value")
    end = positive(record["forecast_value_usd_billion"], "forecast value")
    first, last = record["base_year"], record["forecast_year"]
    if type(first) is not int or type(last) is not int or last <= first:
        raise ValueError("Forecast years must be ordered integers")
    return 100 * ((end / start) ** (1 / (last - first)) - 1)


def ensure_comparable(records):
    """Require reviewed, matching definitions before any aggregation."""
    if not isinstance(records, list) or len(records) < 2:
        raise ValueError("At least two records required")
    keys = ("scope_id", "category", "base_year", "forecast_year", "currency", "unit", "measure")
    first = records[0]
    for item in records:
        if item.get("category") != "pqc" or item.get("methodology_access") != "full_methods_reviewed" or item.get("pooling_approved") is not True:
            raise ValueError("Public headlines or adjacent categories cannot be pooled")
        if any(item.get(key) != first.get(key) for key in keys):
            raise ValueError("Scope, years, units and measurement must match")
    return True


def validate(root=ROOT):
    errors = []
    def check(value, message):
        if not value:
            errors.append(message)
    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())
    try:
        catalog = read(root, "dossier/sources.json")
        sources = catalog["sources"]
        check(isinstance(sources, list) and bool(sources), "catalog: nonempty source list required")
        if not isinstance(sources, list) or any(not isinstance(item, dict) for item in sources):
            return errors + ["catalog: source records must be objects"]
        ids = [item.get("id") for item in sources]
        check(all(isinstance(x, str) and re.fullmatch(r"[MPDS][0-9]{2}", x) for x in ids), "catalog: malformed source ID")
        safe = [x for x in ids if isinstance(x, str)]
        check(len(safe) == len(set(safe)), "catalog: duplicate IDs")
        source_map = {item["id"]: item for item in sources if isinstance(item.get("id"), str)}
        urls = [item.get("url") for item in sources]
        check(all(nonempty(x) and x.startswith("https://") for x in urls), "catalog: HTTPS primary URL required")
        check(len([x for x in urls if isinstance(x, str)]) == len(set(x for x in urls if isinstance(x, str))), "catalog: duplicate primary URLs")
        access = {"full_pdf_selected_sections", "public_article", "public_summary", "abstract_only",
                  "author_article_and_metadata", "standard_abstract"}
        kinds = {"paper", "market_analysis", "policy_or_deployment", "standard"}
        cutoff = date.fromisoformat(catalog["reviewed_on"])
        for item in sources:
            key = item.get("id", "source")
            for field in ("title", "publisher", "review_locator", "interest", "theme"):
                check(nonempty(item.get(field)), key + ": missing " + field)
            check(item.get("kind") in kinds, key + ": invalid source kind")
            check(item.get("access_scope") in access, key + ": invalid access scope")
            check(date.fromisoformat(item["accessed_on"]) <= cutoff, key + ": access date exceeds review cutoff")
            published = item.get("published")
            if published is not None:
                check(isinstance(published, str) and bool(re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", published)),
                      key + ": malformed publication date")
                normalized = published + ("-01-01" if len(published) == 4 else "-01" if len(published) == 7 else "")
                check(date.fromisoformat(normalized) <= cutoff, key + ": publication after review cutoff")
            review = item.get("review")
            check(isinstance(review, dict), key + ": review required")
            if isinstance(review, dict):
                for field in ("question", "method", "finding", "boundary", "implication"):
                    check(nonempty(review.get(field)), key + ": incomplete critical review")
            if item.get("kind") == "paper":
                check(nonempty(item.get("authors")), key + ": authors required")
                check(nonempty(item.get("venue")), key + ": publication venue or archive required")
                check(item.get("publication_status") in {"journal_article", "conference_paper", "preprint_record"},
                      key + ": publication status required")
            pdf = item.get("pdf")
            if item.get("access_scope") == "full_pdf_selected_sections":
                check(isinstance(pdf, dict), key + ": full-PDF review needs retrieval evidence")
            elif pdf is not None:
                errors.append(key + ": PDF evidence conflicts with declared access scope")
            if isinstance(pdf, dict):
                check(bool(re.fullmatch(r"[0-9a-f]{64}", str(pdf.get("sha256", "")))), key + ": PDF hash required")
                count = pdf.get("pages")
                reviewed = pdf.get("reviewed_pages")
                check(type(count) is int and count > 0, key + ": PDF page count required")
                check(isinstance(reviewed, list) and bool(reviewed), key + ": reviewed page locators required")
                if isinstance(reviewed, list) and type(count) is int:
                    check(all(type(x) is int and 1 <= x <= count for x in reviewed), key + ": reviewed page out of bounds")
        forecasts = read(root, "dossier/forecasts.json")["forecasts"]
        check(isinstance(forecasts, list) and bool(forecasts), "forecasts: records required")
        forecast_ids = []
        for item in forecasts:
            forecast_ids.append(item["id"])
            source = source_map.get(item.get("source_id"))
            check(source is not None and source["kind"] == "market_analysis", "forecast: market source missing")
            check(item.get("currency") == "USD" and item.get("unit") == "billion", "forecast: normalized USD billion required")
            check(item.get("category") in {"pqc", "adjacent_quantum_cryptography"}, "forecast: invalid category")
            check(nonempty(item.get("scope_id")), "forecast: specific scope definition required")
            check(item.get("methodology_access") == "public_summary_only" and item.get("pooling_approved") is False,
                  "forecast: unreviewed methodology cannot authorize pooling")
            check(type(item.get("quoted_cagr_pct")) in {int, float} and math.isfinite(item["quoted_cagr_pct"]), "forecast: finite quoted CAGR required")
            cagr(item)
        check(len(forecast_ids) == len(set(forecast_ids)), "forecasts: duplicate IDs")
        theses = read(root, "dossier/theses.json")["theses"]
        check(isinstance(theses, list) and bool(theses), "theses: nonempty synthesis required")
        for item in theses:
            check(item.get("kind") == "synthesis_inference", "thesis: interpretation must remain an inference")
            for field in ("proposition", "reasoning", "countercase", "next_evidence"):
                check(nonempty(item.get(field)), "thesis: missing " + field)
            refs = item.get("source_ids")
            check(isinstance(refs, list) and bool(refs), "thesis: source references required")
            if isinstance(refs, list):
                check(all(isinstance(x, str) and x in source_map for x in refs), "thesis: unknown source")
        for item in read(root, "dossier/format-benchmarks.json")["references"]:
            sha = item["commit_sha"]
            check(bool(re.fullmatch(r"[0-9a-f]{40}", sha)), "format: immutable commit required")
            check(item.get("endorsement") is False, "format: reference is not endorsement")
            expected = "https://github.com/{}/blob/{}/{}#L{}-L{}".format(
                item["repository"], sha, item["path"], item["line_start"], item["line_end"])
            check(item["url"] == expected, "format: source URL must match the inspected pin")
    except (OSError, KeyError, ValueError, TypeError, AttributeError) as exc:
        errors.append("dossier input: " + str(exc))
    return errors


def summary(root=ROOT):
    catalog = read(root, "dossier/sources.json")
    sources = catalog["sources"]
    return {"reviewed_on": catalog["reviewed_on"], "sources": len(sources),
            "by_kind": dict(sorted(Counter(item["kind"] for item in sources).items())),
            "by_access": dict(sorted(Counter(item["access_scope"] for item in sources).items())),
            "paper_pdf_reviews": sum(item["kind"] == "paper" and "pdf" in item for item in sources),
            "artifact_sha256": {path: hashlib.sha256((root / path).read_bytes()).hexdigest() for path in (
                "dossier/sources.json", "dossier/forecasts.json", "dossier/theses.json",
                "dossier/format-benchmarks.json", "dossier.py")}}


def source_card(item):
    review = item["review"]
    lines = ["### " + item["id"] + " · " + item["title"], "",
             "[" + item["publisher"] + "](" + item["url"] + ") · " + str(item["published"] or "publication date not established"),
             "Access: **" + item["access_scope"] + "**. Locator: " + item["review_locator"] + ".", ""]
    if item.get("publication_status"):
        lines += ["Publication: " + item["venue"] + " · " + item["publication_status"] + ".", ""]
    for key, label in (("question", "Question"), ("method", "Approach"), ("finding", "What it supports"),
                       ("boundary", "Boundary"), ("implication", "Use in this review")):
        lines.append("**" + label + ":** " + review[key])
    lines += ["", "Source context: " + item["interest"], ""]
    return "\n".join(lines)


def outputs(root=ROOT):
    catalog = read(root, "dossier/sources.json")
    sources = catalog["sources"]
    forecasts = read(root, "dossier/forecasts.json")["forecasts"]
    market = ["# Analyst desk", "", "Public summaries, analyst remarks and a selected full-report review are distinguished below.",
              "Licensed report bodies were not accessed merely because a public abstract was available.", ""]
    market += [source_card(item) for item in sources if item["kind"] == "market_analysis"]
    atlas = ["# Paper atlas", "", "The review distinguishes published papers, preprint records, selected full-PDF passages and abstract-level coverage.",
             "Historical results retain their original algorithm versions and measurement conditions.", ""]
    for theme in ("foundations", "resource_estimates", "scheme_design", "protocols", "benchmarks", "cryptanalysis"):
        atlas += ["## " + theme.replace("_", " ").title(), ""]
        atlas += [source_card(item) for item in sources if item["kind"] == "paper" and item["theme"] == theme]
    deployment = ["# Standards and deployment record", "", "Guidance, normative functions, controlled experiments and provider self-reports have different evidentiary roles.", ""]
    deployment += [source_card(item) for item in sources if item["kind"] in {"policy_or_deployment", "standard"}]
    checks = {"currency": "USD", "unit": "billion", "pooled_market_estimate": None,
              "interpretation": "Publisher-specific projections. Arithmetic checks do not validate market definitions or forecasts.",
              "rows": []}
    for item in forecasts:
        computed = cagr(item)
        checks["rows"].append({**item, "calculated_cagr_pct": round(computed, 6),
                              "calculated_minus_quoted_pp": round(computed - item["quoted_cagr_pct"], 6),
                              "eligible_as_pqc_headline": item["category"] == "pqc"})
    stream = io.StringIO()
    fields = ["id", "source_id", "publisher", "category", "scope_id", "base_year", "base_value_usd_billion",
              "forecast_year", "forecast_value_usd_billion", "quoted_cagr_pct", "currency", "unit"]
    writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(forecasts)
    bib = []
    for item in sources:
        title = item["title"].replace("{", "").replace("}", "")
        publisher = item["publisher"].replace("{", "").replace("}", "")
        year = str(item["published"])[:4] if item["published"] else ""
        bib += ["@misc{" + item["id"] + ",", "  title = {{" + title + "}},",
                "  author = {{" + item.get("authors", publisher) + "}},",
                "  year = {" + year + "},", "  url = {" + item["url"] + "},",
                "  note = {Accessed " + item["accessed_on"] + "; " + item["access_scope"] + "}", "}", ""]
    return {"dossier/02-analyst-desk.md": "\n".join(market) + "\n",
            "dossier/04-paper-atlas.md": "\n".join(atlas) + "\n",
            "dossier/05-deployment-record.md": "\n".join(deployment) + "\n",
            "dossier/market-checks.json": json.dumps(checks, indent=2) + "\n",
            "dossier/forecasts.csv": stream.getvalue(),
            "dossier/references.bib": "\n".join(bib),
            "dossier/summary.json": json.dumps(summary(root), indent=2) + "\n"}


def check_outputs(root=ROOT):
    errors = []
    for path, expected in outputs(root).items():
        target = root / path
        if not target.is_file() or target.read_text() != expected:
            errors.append(path + " is stale; review inputs and run python dossier.py --write")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    errors = validate()
    if not errors:
        if args.write:
            for path, text in outputs().items():
                (ROOT / path).write_text(text, encoding="utf-8")
        errors += check_outputs()
    if errors:
        print("\n".join("FAIL: " + item for item in errors))
        return 1
    print("PASS: research corpus, access boundaries, forecast arithmetic and generated review")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
