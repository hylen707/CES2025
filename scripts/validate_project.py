#!/usr/bin/env python3
"""Project semantic/type checks, not a general-purpose JSON Schema implementation."""
import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"source_observation", "retrospective_analysis", "proposal"}
SOURCE_TYPES = {"activity_primary", "standard", "government_guidance", "vendor_primary", "generated", "student_record"}


def validate(project, evidence, root, submission=False):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())
    def choice(value, options):
        return isinstance(value, str) and value in options
    if not isinstance(project, dict) or not isinstance(evidence, dict):
        return ["project and evidence must be objects"]
    required_p = {"schema_version", "ec_id", "title", "source_state", "artifact_state", "student_verification", "activity_dates", "hours", "role", "impact", "retrospective_preparation_date", "preparation_note"}
    check(required_p <= project.keys(), "project: missing required fields")
    check(not (project.keys() - required_p - {"verification_evidence_ids", "personal_field_evidence"}), "project: unexpected fields")
    check(project.get("schema_version") == "1.0", "project: unsupported schema version")
    check(project.get("ec_id") == "EC5", "project: ec_id must be EC5")
    for key in ("title", "preparation_note"):
        check(nonempty(project.get(key)), f"project: {key} must be a nonempty string")
    check(choice(project.get("source_state"), {"read", "pending_access", "partial"}), "project: invalid source_state")
    check(choice(project.get("artifact_state"), {"draft", "reviewed"}), "project: invalid artifact_state")
    check(choice(project.get("student_verification"), {"pending", "verified"}), "project: invalid student_verification")
    for key in ("activity_dates", "role", "impact"):
        check(project.get(key) is None or nonempty(project.get(key)), f"project: {key} must be null or nonempty string")
    hours = project.get("hours")
    check(hours is None or (isinstance(hours, (int, float)) and not isinstance(hours, bool) and 0 <= hours < float("inf")), "project: hours must be null or finite nonnegative number")
    try:
        date.fromisoformat(project.get("retrospective_preparation_date", ""))
    except (ValueError, TypeError):
        errors.append("project: preparation date must be ISO date")
    check(set(evidence) == {"sources", "observations", "claims"}, "evidence: expected sources, observations, claims only")
    for key in ("sources", "observations", "claims"):
        if not isinstance(evidence.get(key), list):
            errors.append(f"evidence: {key} must be an array")
    if any(not isinstance(evidence.get(k), list) for k in ("sources", "observations", "claims")):
        return errors
    sources, observations, claims = evidence["sources"], evidence["observations"], evidence["claims"]
    all_ids = []
    for category, records in (("source", sources), ("observation", observations), ("claim", claims)):
        for record in records:
            if not isinstance(record, dict):
                errors.append(f"{category}: record must be an object")
                continue
            check(nonempty(record.get("id")), f"{category}: nonempty id required")
            if nonempty(record.get("id")):
                all_ids.append(record["id"])
    check(len(all_ids) == len(set(all_ids)), "evidence: duplicate IDs")
    sm = {s.get("id"): s for s in sources if isinstance(s, dict) and nonempty(s.get("id"))}
    om = {o.get("id"): o for o in observations if isinstance(o, dict) and nonempty(o.get("id"))}
    for s in sources:
        if not isinstance(s, dict):
            continue
        sid = s.get("id", "source")
        source_required = {"id", "title", "url", "type", "access_status", "accessed_on", "locator_scheme", "notes"}
        source_optional = {"version", "checksum_sha256", "local_checksum_sha256", "local_path", "original_path"}
        check(source_required <= s.keys(), f"{sid}: missing required source fields")
        check(not (s.keys() - source_required - source_optional), f"{sid}: unexpected source fields")
        for k in ("title", "url", "locator_scheme", "notes"):
            check(nonempty(s.get(k)), f"{sid}: missing {k}")
        check(choice(s.get("type"), SOURCE_TYPES), f"{sid}: invalid source type")
        check(choice(s.get("access_status"), {"read", "partial", "pending_access"}), f"{sid}: invalid access status")
        if s.get("access_status") == "read":
            try:
                date.fromisoformat(s.get("accessed_on", ""))
            except (ValueError, TypeError):
                errors.append(f"{sid}: read source requires accessed_on ISO date")
        for key in ("checksum_sha256", "local_checksum_sha256"):
            if s.get(key) is not None:
                check(isinstance(s[key], str) and bool(re.fullmatch(r"[0-9a-f]{64}", s[key])), f"{sid}: invalid {key}")
        if s.get("local_path"):
            if not isinstance(s["local_path"], str):
                errors.append(f"{sid}: local_path must be a string")
                continue
            path = (Path(root) / s["local_path"]).resolve()
            check(path.is_relative_to(Path(root).resolve()), f"{sid}: local_path escapes root")
            if path.is_relative_to(Path(root).resolve()):
                check(path.is_file(), f"{sid}: local file missing")
                if path.is_file():
                    check(nonempty(s.get("local_checksum_sha256")), f"{sid}: local file requires local_checksum_sha256")
                    if s.get("local_checksum_sha256"):
                        check(hashlib.sha256(path.read_bytes()).hexdigest() == s["local_checksum_sha256"], f"{sid}: local hash mismatch")
        if "original_path" in s:
            if not nonempty(s["original_path"]):
                errors.append(f"{sid}: invalid original_path")
            else:
                original = (Path(root) / s["original_path"]).resolve()
                contained = original.is_relative_to(Path(root).resolve())
                check(contained and original.is_file(), f"{sid}: original file missing or outside root")
                if contained and original.is_file():
                    check(hashlib.sha256(original.read_bytes()).hexdigest() == s.get("checksum_sha256"), f"{sid}: original hash mismatch")
    for o in observations:
        if not isinstance(o, dict):
            continue
        oid = o.get("id", "observation")
        check(set(o) == {"id", "text", "source_id", "locator", "status", "limitations"}, f"{oid}: missing or unexpected observation fields")
        for k in ("text", "source_id", "locator", "limitations"):
            check(nonempty(o.get(k)), f"{oid}: missing {k}")
        check(choice(o.get("status"), {"verified_source_content", "generated", "pending"}), f"{oid}: invalid status")
        source = sm.get(o.get("source_id")) if isinstance(o.get("source_id"), str) else None
        check(source is not None, f"{oid}: dangling source_id")
        if o.get("status") != "pending" and source:
            check(source.get("access_status") == "read", f"{oid}: verified observation needs read source")
            check((o.get("status") == "generated") == (source.get("type") == "generated"), f"{oid}: generated status/source mismatch")
        if o.get("source_id") == "S-EC5-001" and nonempty(o.get("locator")):
            match = re.fullmatch(r"slide ([1-9][0-9]*); text runs? ([1-9][0-9]*)(?:-([1-9][0-9]*))?", o["locator"])
            check(match is not None, f"{oid}: precise slide/text locator required")
            if match:
                try:
                    extracted = json.loads((Path(root) / "sources/slides.json").read_text(encoding="utf-8"))
                    slides = {slide["slide_number"]: slide for slide in extracted["slides"]}
                    slide_no, start = int(match[1]), int(match[2])
                    end = int(match[3] or match[2])
                    check(slide_no in slides and 1 <= start <= end <= len(slides.get(slide_no, {}).get("text", [])), f"{oid}: slide/text run out of bounds")
                except (OSError, ValueError, KeyError, TypeError):
                    errors.append(f"{oid}: cannot verify slide/text run bounds")
    for c in claims:
        if not isinstance(c, dict):
            continue
        cid = c.get("id", "claim")
        check(set(c) == {"id", "text", "kind", "evidence_ids", "source_locators", "reasoning", "counterargument", "limitation", "status"}, f"{cid}: missing or unexpected claim fields")
        for k in ("text", "reasoning", "counterargument", "limitation"):
            check(nonempty(c.get(k)), f"{cid}: missing {k}")
        check(choice(c.get("kind"), KINDS), f"{cid}: invalid kind")
        check(choice(c.get("status"), {"supported", "qualified", "proposed", "pending"}), f"{cid}: invalid status")
        check((c.get("kind") == "proposal") == (c.get("status") == "proposed"), f"{cid}: proposal kind/status mismatch")
        ids = c.get("evidence_ids")
        check(isinstance(ids, list) and bool(ids), f"{cid}: nonempty evidence_ids required")
        if not isinstance(ids, list):
            continue
        check(all(isinstance(i, str) for i in ids), f"{cid}: evidence IDs must be strings")
        safe_ids = [i for i in ids if isinstance(i, str)]
        check(len(safe_ids) == len(set(safe_ids)), f"{cid}: duplicate evidence IDs")
        for i in safe_ids:
            check(i in om, f"{cid}: dangling evidence_id {i}")
            if i in om and not choice(c.get("status"), {"pending", "proposed"}):
                check(om[i].get("status") != "pending", f"{cid}: supported claim cites pending observation")
        locators = c.get("source_locators")
        check(isinstance(locators, list) and bool(locators), f"{cid}: source_locators required")
        actual = set()
        if isinstance(locators, list):
            for loc in locators:
                if isinstance(loc, dict) and set(loc) == {"source_id", "locator"} and nonempty(loc.get("source_id")) and nonempty(loc.get("locator")):
                    actual.add((loc["source_id"], loc["locator"]))
                else:
                    errors.append(f"{cid}: invalid source locator")
        expected = {(om[i].get("source_id"), om[i].get("locator")) for i in safe_ids if i in om and nonempty(om[i].get("source_id")) and nonempty(om[i].get("locator"))}
        check(actual == expected, f"{cid}: locators do not match cited observations")
    if project.get("source_state") == "read":
        check(any(s.get("type") == "activity_primary" and s.get("access_status") == "read" for s in sm.values()), "project: read state requires read activity source")
    personal = project.get("personal_field_evidence", {})
    check(isinstance(personal, dict), "project: personal_field_evidence must be an object")
    if not isinstance(personal, dict):
        personal = {}
    check(not (set(personal) - {"activity_dates", "hours", "role", "impact"}), "project: unexpected personal_field_evidence field")
    def located_student_records(ids):
        if not isinstance(ids, list) or not ids or not all(isinstance(i, str) for i in ids):
            return False
        if len(ids) != len(set(ids)):
            return False
        for i in ids:
            record = om.get(i)
            if not record or record.get("status") != "verified_source_content" or not nonempty(record.get("locator")):
                return False
            source = sm.get(record.get("source_id")) if isinstance(record.get("source_id"), str) else None
            if not source or source.get("type") != "student_record" or source.get("access_status") != "read":
                return False
        return True
    for field in ("activity_dates", "hours", "role", "impact"):
        if project.get(field) is not None:
            check(located_student_records(personal.get(field)), f"project: {field} needs located student_record evidence")
    if "verification_evidence_ids" in project:
        ids = project["verification_evidence_ids"]
        check(isinstance(ids, list) and all(isinstance(i, str) for i in ids), "project: verification_evidence_ids must be an array of IDs")
    if project.get("student_verification") == "verified":
        check(located_student_records(project.get("verification_evidence_ids")), "project: verified student ownership needs located student_record evidence")
    if submission:
        check(project.get("source_state") == "read", "submission: source reading incomplete")
        check(project.get("artifact_state") == "reviewed", "submission: artifact review incomplete")
        check(project.get("student_verification") == "verified", "submission: student ownership/verification pending")
        check(nonempty(project.get("role")), "submission: student role unverified")
        check(nonempty(project.get("activity_dates")), "submission: activity dates unverified")
        check(bool(observations) and bool(claims), "submission: evidence or claims missing")
        check(all(s.get("access_status") == "read" for s in sm.values()), "submission: unread sources")
        check(all(o.get("status") != "pending" for o in om.values()), "submission: pending observations")
        check(all(isinstance(c, dict) and c.get("status") != "pending" for c in claims), "submission: pending claims")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--submission", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        project = json.loads((args.root / "project.json").read_text(encoding="utf-8"))
        evidence = json.loads((args.root / "evidence.json").read_text(encoding="utf-8"))
        errors = validate(project, evidence, args.root, args.submission)
    except (OSError, json.JSONDecodeError) as exc:
        errors = [f"Cannot read project records: {exc}"]
    result = {"mode": "submission" if args.submission else "draft", "passed": not errors, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else
          (f"{result['mode']}: PASS" if not errors else f"{result['mode']}: FAIL\n" + "\n".join(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
