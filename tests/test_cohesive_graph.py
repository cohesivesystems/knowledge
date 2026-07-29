from pathlib import Path
import sys
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cohesive_graph import extract_formal_relations, extract_wikilinks  # noqa: E402


class FormalRelationParsingTests(unittest.TestCase):
    def test_extracts_typed_relation_with_rationale(self) -> None:
        body = """# Example

## Formal relations

- `bundles`: [[Service|service role]] — Aligns responsibility and realization.
"""

        relations, issues = extract_formal_relations("Example.md", body, 10)

        self.assertEqual(issues, [])
        self.assertEqual(len(relations), 1)
        relation = relations[0]
        self.assertEqual(relation.relation_type, "bundles")
        self.assertEqual(relation.link.target, "Service")
        self.assertEqual(relation.link.label, "service role")
        self.assertEqual(relation.link.line, 14)
        self.assertEqual(
            relation.description, "Aligns responsibility and realization."
        )
        self.assertIn(relation.link, extract_wikilinks("Example.md", body, 10))

    def test_rejects_relation_without_rationale(self) -> None:
        body = """## Formal relations

- `arranges`: [[Service]]
"""

        relations, issues = extract_formal_relations("Example.md", body)

        self.assertEqual(relations, [])
        self.assertEqual(len(issues), 1)
        self.assertIn("rationale", issues[0].message)

    def test_ignores_example_inside_fence(self) -> None:
        body = """```md
## Formal relations

- `arranges`: [[Service]] — Example only.
```
"""

        relations, issues = extract_formal_relations("Example.md", body)

        self.assertEqual(relations, [])
        self.assertEqual(issues, [])


if __name__ == "__main__":
    unittest.main()
