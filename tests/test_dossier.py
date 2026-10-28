import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ces_dossier", ROOT / "dossier.py")
dossier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dossier)


class DossierEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self.temp.cleanup()

    def change(self, path, transform):
        target = self.root / path
        data = json.loads(target.read_text())
        transform(data)
        target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    def test_current_review_is_consistent(self):
        self.assertEqual(dossier.validate(self.root), [])
        self.assertEqual(dossier.check_outputs(self.root), [])

    def test_duplicate_reference_cannot_inflate_coverage(self):
        self.change("dossier/sources.json", lambda d: d["sources"].append(d["sources"][0].copy()))
        self.assertTrue(any("duplicate" in e for e in dossier.validate(self.root)))

    def test_abstract_cannot_be_presented_as_full_pdf_review(self):
        def change(data):
            item = next(x for x in data["sources"] if x["id"] == "P13")
            item["access_scope"] = "full_pdf_selected_sections"
        self.change("dossier/sources.json", change)
        self.assertTrue(any("retrieval evidence" in e for e in dossier.validate(self.root)))

    def test_pdf_page_locator_must_exist(self):
        def change(data):
            item = next(x for x in data["sources"] if x.get("pdf"))
            item["pdf"]["reviewed_pages"] = [item["pdf"]["pages"] + 1]
        self.change("dossier/sources.json", change)
        self.assertTrue(any("page out of bounds" in e for e in dossier.validate(self.root)))

    def test_publication_after_cutoff_is_rejected(self):
        self.change("dossier/sources.json", lambda d: d["sources"][0].update(published="2027-01-01"))
        self.assertTrue(any("after review cutoff" in e for e in dossier.validate(self.root)))

    def test_publication_status_cannot_be_unsupported_label(self):
        def change(data):
            next(x for x in data["sources"] if x["kind"] == "paper")["publication_status"] = "security_proven"
        self.change("dossier/sources.json", change)
        self.assertTrue(any("publication status" in e for e in dossier.validate(self.root)))

    def test_synthesis_requires_known_sources(self):
        self.change("dossier/theses.json", lambda d: d["theses"][0].update(source_ids=["unknown"]))
        self.assertTrue(any("unknown source" in e for e in dossier.validate(self.root)))

    def test_interpretation_cannot_be_promoted_to_observation(self):
        self.change("dossier/theses.json", lambda d: d["theses"][0].update(kind="measured_market_fact"))
        self.assertTrue(any("remain an inference" in e for e in dossier.validate(self.root)))

    def test_currency_unit_requires_normalization(self):
        self.change("dossier/forecasts.json", lambda d: d["forecasts"][0].update(unit="million"))
        self.assertTrue(any("USD billion" in e for e in dossier.validate(self.root)))

    def test_generated_atlas_cannot_drift(self):
        with (self.root / "dossier/04-paper-atlas.md").open("a") as handle:
            handle.write("Untracked assertion\n")
        self.assertTrue(any("paper-atlas" in e for e in dossier.check_outputs(self.root)))

    def test_immutable_format_reference_cannot_be_a_branch(self):
        self.change("dossier/format-benchmarks.json", lambda d: d["references"][0].update(commit_sha="master"))
        self.assertTrue(any("immutable commit" in e for e in dossier.validate(self.root)))


class ForecastBoundaryTests(unittest.TestCase):
    def record(self):
        return dossier.read(ROOT, "dossier/forecasts.json")["forecasts"][0].copy()

    def test_compound_growth_has_known_reference(self):
        item = self.record()
        item.update(base_value_usd_billion=100, forecast_value_usd_billion=121, base_year=2026, forecast_year=2028)
        self.assertAlmostEqual(dossier.cagr(item), 10.0, places=10)

    def test_invalid_endpoints_are_rejected(self):
        for value in (0, -1, True, float("nan"), float("inf"), "0.6"):
            item = self.record()
            item["base_value_usd_billion"] = value
            with self.assertRaises(ValueError):
                dossier.cagr(item)

    def test_reversed_or_boolean_years_are_rejected(self):
        for first, last in ((2028, 2026), (2026, 2026), (True, 2030)):
            item = self.record()
            item.update(base_year=first, forecast_year=last)
            with self.assertRaises(ValueError):
                dossier.cagr(item)

    def test_public_headlines_cannot_be_pooled(self):
        rows = dossier.read(ROOT, "dossier/forecasts.json")["forecasts"]
        with self.assertRaises(ValueError):
            dossier.ensure_comparable(rows[:2])

    def test_adjacent_category_cannot_become_pqc_consensus(self):
        first = self.record()
        second = first.copy()
        for item in (first, second):
            item.update(methodology_access="full_methods_reviewed", pooling_approved=True)
        second["category"] = "adjacent_quantum_cryptography"
        with self.assertRaises(ValueError):
            dossier.ensure_comparable([first, second])

    def test_scope_difference_survives_a_manual_approval_flag(self):
        first = self.record()
        second = first.copy()
        for item in (first, second):
            item.update(methodology_access="full_methods_reviewed", pooling_approved=True)
        second["scope_id"] = "different-definition"
        with self.assertRaises(ValueError):
            dossier.ensure_comparable([first, second])


if __name__ == "__main__":
    unittest.main()
