import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ingest_pptx import extract
from migration_model import evaluate, report, simulate
from validate_project import validate


class EvidenceContractTests(unittest.TestCase):
    def setUp(self):
        self.project = json.loads((ROOT / "project.json").read_text())
        self.evidence = json.loads((ROOT / "evidence.json").read_text())

    def errors(self, submission=False, root=ROOT):
        return validate(self.project, self.evidence, root, submission)

    def test_current_draft_is_valid(self):
        self.assertEqual(self.errors(), [])

    def test_submission_gate_stays_closed(self):
        self.assertTrue(any("ownership" in x for x in self.errors(True)))

    def test_metadata_toggle_is_not_ownership_evidence(self):
        self.project.update(student_verification="verified", artifact_state="reviewed", role="Author", activity_dates="2025")
        errors = self.errors(True)
        self.assertTrue(any("student_record" in x for x in errors))

    def test_technical_evidence_cannot_attest_student_work(self):
        self.project.update(student_verification="verified", verification_evidence_ids=["O-EC5-008"])
        self.assertTrue(any("student_record" in x for x in self.errors()))

    def test_duplicate_ids_rejected(self):
        self.evidence["observations"].append(copy.deepcopy(self.evidence["observations"][0]))
        self.assertIn("evidence: duplicate IDs", self.errors())

    def test_dangling_source_rejected(self):
        self.evidence["observations"][0]["source_id"] = "missing"
        self.assertTrue(any("dangling source" in x for x in self.errors()))

    def test_dangling_claim_support_rejected(self):
        self.evidence["claims"][0]["evidence_ids"] = ["missing"]
        self.assertTrue(any("dangling evidence" in x for x in self.errors()))

    def test_claim_locator_cannot_drift(self):
        self.evidence["claims"][0]["source_locators"][0]["locator"] = "wrong"
        self.assertTrue(any("locators do not match" in x for x in self.errors()))

    def test_verified_observation_requires_read_source(self):
        self.evidence["sources"][0]["access_status"] = "pending_access"
        self.assertTrue(any("needs read source" in x for x in self.errors()))

    def test_slide_run_bounds_checked(self):
        self.evidence["observations"][0]["locator"] = "slide 4; text runs 1-999"
        self.assertTrue(any("out of bounds" in x for x in self.errors()))

    def test_malformed_enum_type_is_reported(self):
        self.project["source_state"] = []
        self.evidence["claims"][0]["kind"] = {}
        self.assertTrue(self.errors())

    def test_malformed_support_type_is_reported(self):
        self.evidence["claims"][0]["evidence_ids"] = [[], None]
        self.assertTrue(any("IDs must be strings" in x for x in self.errors()))

    def test_new_personal_metric_requires_evidence(self):
        self.project["hours"] = 30
        self.assertTrue(any("hours needs located" in x for x in self.errors()))

    def test_proposal_cannot_look_completed(self):
        self.evidence["claims"][-1]["status"] = "supported"
        self.assertTrue(any("proposal kind/status" in x for x in self.errors()))

    def test_derivative_hash_tamper_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "sources", root / "sources")
            shutil.copytree(ROOT / "results", root / "results")
            with (root / "sources/slides.json").open("ab") as f:
                f.write(b" ")
            self.assertTrue(any("local hash mismatch" in x for x in self.errors(root=root)))

    def test_original_export_tamper_rejected(self):
        self.evidence["sources"][0]["checksum_sha256"] = "0" * 64
        self.assertTrue(any("original hash mismatch" in x for x in self.errors()))


class MigrationModelTests(unittest.TestCase):
    def setUp(self):
        self.asset = {"id": "A", "algorithm": "RSA-2048", "use": "key_transport", "confidentiality_years": 5, "migration_years": 2}

    def test_equality_triggers(self):
        self.assertEqual(evaluate(self.asset, 7)["state"], "planning_trigger")

    def test_tiny_positive_slack_is_not_rounded_to_trigger(self):
        result = evaluate(self.asset, 7.00000001)
        self.assertEqual(result["state"], "positive_slack")
        self.assertGreater(result["slack_years"], 0)

    def test_more_migration_time_reduces_slack(self):
        before = evaluate(self.asset, 10)["slack_years"]
        self.asset["migration_years"] += 1
        self.assertEqual(evaluate(self.asset, 10)["slack_years"], before - 1)

    def test_later_horizon_increases_slack(self):
        self.assertEqual(evaluate(self.asset, 11)["slack_years"], evaluate(self.asset, 10)["slack_years"] + 1)

    def test_invalid_numbers_rejected(self):
        for value in (-1, float("nan"), float("inf"), True, None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                evaluate({**self.asset, "migration_years": value}, 10)

    def test_zero_horizon_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(self.asset, 0)

    def test_signature_is_not_confidentiality_score(self):
        self.assertEqual(evaluate({**self.asset, "use": "signature"}, 10)["state"], "signature_review")

    def test_unknown_algorithm_preserves_gap(self):
        self.assertEqual(evaluate({**self.asset, "algorithm": None}, 10)["state"], "inventory_gap")

    def test_pqc_name_is_not_safe_verdict(self):
        self.assertEqual(evaluate({**self.asset, "algorithm": "ML-KEM-768", "use": "key_encapsulation"}, 10)["state"], "algorithm_review")

    def test_duplicate_asset_ids_rejected(self):
        with self.assertRaises(ValueError):
            simulate([self.asset, self.asset], [10])

    def test_generated_results_reproduce(self):
        expected = json.loads((ROOT / "results/migration_scenarios.json").read_text())
        self.assertEqual(report(ROOT / "data/synthetic_inventory.json", [5, 10, 20]), expected)
        self.assertEqual(len(expected["rows"]), 15)

    def test_source_extraction_reproduces(self):
        expected = json.loads((ROOT / "sources/slides.json").read_text())
        self.assertEqual(extract(ROOT / "sources/original.pptx"), expected)
        self.assertEqual([s["slide_number"] for s in expected["slides"]], list(range(1, 13)))


if __name__ == "__main__":
    unittest.main()
