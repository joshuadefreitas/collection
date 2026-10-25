import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import validate  # noqa: E402

EXAMPLE = json.loads((ROOT / "examples" / "collection.example.json").read_text())


def mutated(change):
    registry = copy.deepcopy(EXAMPLE)
    change(registry)
    return registry


class ContractTests(unittest.TestCase):
    def test_example_is_valid(self):
        self.assertEqual(validate.problems(EXAMPLE), [])

    def test_example_covers_every_type_and_status_rule(self):
        types = {a["type"] for a in EXAMPLE["artifacts"]}
        statuses = {a["status"] for a in EXAMPLE["artifacts"]}
        self.assertEqual(types, {"tool", "study", "note"})
        self.assertTrue({"experimental", "archived"} <= statuses)

    def test_empty_registry_is_valid(self):
        self.assertEqual(validate.problems({"schema_version": "1", "updated": "2026-01-01", "artifacts": []}), [])

    def test_rejections(self):
        cases = {
            "tool without version": lambda r: r["artifacts"][0].pop("version"),
            "tool without licence": lambda r: r["artifacts"][0].pop("license"),
            "study without non_claim": lambda r: r["artifacts"][1].pop("non_claim"),
            "study without repo": lambda r: r["artifacts"][1].pop("repo"),
            "experimental without status_note": lambda r: r["artifacts"][2].pop("status_note"),
            "archived without status_note": lambda r: r["artifacts"][3].pop("status_note"),
            "bad status": lambda r: r["artifacts"][0].update(status="live"),
            "bad type": lambda r: r["artifacts"][0].update(type="app"),
            "bad id": lambda r: r["artifacts"][0].update(id="Bad Id"),
            "http url": lambda r: r["artifacts"][0].update(canonical_url="http://example.com"),
            "bad date": lambda r: r["artifacts"][0].update(published="01/01/2026"),
            "no topics": lambda r: r["artifacts"][0].update(topics=[]),
            "too many topics": lambda r: r["artifacts"][0].update(topics=[f"t{i}" for i in range(7)]),
            "destination state in registry": lambda r: r["artifacts"][0].update(hacker_news_ready=True),
            "submission history in registry": lambda r: r["artifacts"][0].update(submitted=["reddit"]),
            "unknown top-level field": lambda r: r.update(metrics={}),
            "wrong schema version": lambda r: r.update(schema_version="2"),
            "bad evidence kind": lambda r: r["artifacts"][0]["evidence"][0].update(kind="tweet"),
            "visual without alt": lambda r: r["artifacts"][0]["visual"].pop("alt"),
            "tool without visual": lambda r: r["artifacts"][0].pop("visual"),
            "study without visual": lambda r: r["artifacts"][1].pop("visual"),
            "experimental tool without visual": lambda r: r["artifacts"][0].update(status="experimental", status_note="x") or r["artifacts"][0].pop("visual"),
            "empty status_note": lambda r: r["artifacts"][2].update(status_note=""),
            "blank status_note": lambda r: r["artifacts"][2].update(status_note="   \n"),
            "blank claim": lambda r: r["artifacts"][0].update(claim="  "),
            "blank summary": lambda r: r["artifacts"][0].update(summary=""),
            "blank title": lambda r: r["artifacts"][0].update(title=""),
            "blank version": lambda r: r["artifacts"][0].update(version=" "),
            "blank licence": lambda r: r["artifacts"][0].update(license=""),
            "blank non_claim": lambda r: r["artifacts"][1].update(non_claim=" "),
            "blank visual alt": lambda r: r["artifacts"][0]["visual"].update(alt=" "),
            "bad updated date": lambda r: r.update(updated="25/10/2026"),
        }
        for name, change in cases.items():
            with self.subTest(name):
                self.assertTrue(validate.problems(mutated(change)), f"{name} was accepted")

    # The contract is written down here on purpose, not read from the schema under test:
    # deriving it from the schema would make the test pass for any schema.
    REQUIRED_TOP = ["schema_version", "updated", "artifacts"]
    REQUIRED_ARTIFACT = ["id", "type", "status", "title", "claim", "summary", "topics",
                         "canonical_url", "published", "last_verified"]

    def test_required_fields_are_exactly_the_contract(self):
        schema = json.loads(validate.SCHEMA.read_text())
        self.assertEqual(sorted(schema["required"]), sorted(self.REQUIRED_TOP))
        self.assertEqual(sorted(schema["$defs"]["artifact"]["required"]), sorted(self.REQUIRED_ARTIFACT))

    def test_every_required_field_is_enforced(self):
        for field in self.REQUIRED_TOP:
            with self.subTest(f"top-level {field}"):
                self.assertTrue(validate.problems(mutated(lambda r, f=field: r.pop(f))))
        for field in self.REQUIRED_ARTIFACT:
            with self.subTest(f"artifact {field}"):
                self.assertTrue(validate.problems(mutated(lambda r, f=field: r["artifacts"][0].pop(f))))

    def test_archived_tool_and_note_need_no_visual(self):
        registry = mutated(lambda r: None)
        archived = next(a for a in registry["artifacts"] if a["status"] == "archived")
        self.assertNotIn("visual", archived)
        self.assertEqual(validate.problems(registry), [])
        note = next(a for a in registry["artifacts"] if a["type"] == "note")
        self.assertNotIn("visual", note)

    def test_example_uses_only_reserved_example_hosts(self):
        text = json.dumps(EXAMPLE)
        self.assertNotIn("github.com", text)
        self.assertIn("example.com", text)


if __name__ == "__main__":
    unittest.main()
