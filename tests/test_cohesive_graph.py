from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cohesive_graph import (  # noqa: E402
    ALLOWED_FORMAL_RELATION_TYPES,
    RELATION_INVERSES,
    extract_formal_relations,
    extract_wikilinks,
)
from export_graph import SCHEMA_VERSION, collect_realm_peers  # noqa: E402
import validate_graph  # noqa: E402


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

    def test_realm_peer_relation_is_allowed_and_symmetric(self) -> None:
        body = """## Formal relations

- `realm_peer_of`: [[CQRS]] — Treats the same named pattern from another realm.
"""

        relations, issues = extract_formal_relations("Example.md", body)

        self.assertEqual(issues, [])
        self.assertEqual(relations[0].relation_type, "realm_peer_of")
        self.assertIn("realm_peer_of", ALLOWED_FORMAL_RELATION_TYPES)
        self.assertEqual(RELATION_INVERSES["realm_peer_of"], "realm_peer_of")


class RealmPeerValidationTests(unittest.TestCase):
    def test_realm_peer_must_cross_realms(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            realm = root / "Cohesive System Model" / "Architecture Practices"
            realm.mkdir(parents=True)
            (realm / "First.md").write_text(
                """---
realm: Architecture Practices
kind: architecture-practice
created: 2026-07-30
updated: 2026-07-30
---

# First

## Formal relations

- `realm_peer_of`: [[Second]] — Incorrectly relates two entries in one realm.
""",
                encoding="utf-8",
            )
            (realm / "Second.md").write_text(
                """---
realm: Architecture Practices
kind: architecture-practice
created: 2026-07-30
updated: 2026-07-30
---

# Second
""",
                encoding="utf-8",
            )

            errors = StringIO()
            with patch.object(validate_graph, "repo_root_from", return_value=root):
                with redirect_stderr(errors):
                    result = validate_graph.main()

        self.assertEqual(result, 1)
        self.assertIn("must cross realms", errors.getvalue())


class RealmPeerExportTests(unittest.TestCase):
    def test_collects_realm_peers_on_both_endpoints(self) -> None:
        peers = collect_realm_peers(
            [
                ("architecture/cqrs", "substrate/cqrs", "realm_peer_of"),
                ("architecture/cqrs", "semantics/command", "mentions"),
                ("architecture/cqrs", "substrate/cqrs", "realm_peer_of"),
            ]
        )

        self.assertEqual(peers["architecture/cqrs"], ["substrate/cqrs"])
        self.assertEqual(peers["substrate/cqrs"], ["architecture/cqrs"])
        self.assertNotIn("semantics/command", peers)
        self.assertEqual(SCHEMA_VERSION, "0.4.0")


if __name__ == "__main__":
    unittest.main()
