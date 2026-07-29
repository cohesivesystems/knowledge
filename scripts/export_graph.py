#!/usr/bin/env python3
"""Export the Cohesive knowledge graph as JSON."""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
import argparse
import json
from pathlib import Path
import sys

from cohesive_graph import (
    ALLOWED_FORMAL_RELATION_TYPES,
    RELATION_INVERSES,
    load_nodes,
    repo_root_from,
    resolve_links,
)


SCHEMA_VERSION = "0.2.0"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default="dist/graph.json",
        help="Output JSON path. Defaults to dist/graph.json.",
    )
    args = parser.parse_args()

    root = repo_root_from()
    nodes = load_nodes(root)
    resolved, unresolved, collisions = resolve_links(nodes)
    relation_issues = [issue for node in nodes for issue in node.relation_issues]
    unknown_relations = [
        relation
        for node in nodes
        for relation in node.formal_relations
        if relation.relation_type not in ALLOWED_FORMAL_RELATION_TYPES
    ]

    if unresolved or collisions or relation_issues or unknown_relations:
        print(
            "Graph has invalid formal relations or unresolved or ambiguous links. "
            "Run scripts/validate_graph.py.",
            file=sys.stderr,
        )
        return 1

    backlinks: dict[str, list[str]] = defaultdict(list)
    edge_mentions: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    nodes_by_path = {node.path: node for node in nodes}
    nodes_by_id = {node.id: node for node in nodes}
    formal_relations = {
        relation.link: relation
        for node in nodes
        for relation in node.formal_relations
    }

    for link, target in resolved.items():
        source = nodes_by_path[link.source_path]
        formal_relation = formal_relations.get(link)
        edge_type = formal_relation.relation_type if formal_relation else "mentions"
        backlinks[target.path].append(source.id)
        mention: dict[str, object] = {
            "path": link.source_path,
            "line": link.line,
            "raw": link.raw,
        }
        if formal_relation:
            mention["description"] = formal_relation.description
        edge_mentions[(source.id, target.id, edge_type)].append(mention)

    export = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "repository": "https://github.com/cohesivesystems/knowledge",
            "root": "Cohesive System Model.md",
        },
        "relation_types": [
            {
                "type": relation_type,
                "inverse": inverse,
                "symmetric": relation_type == inverse,
            }
            for relation_type, inverse in sorted(RELATION_INVERSES.items())
        ],
        "nodes": [
            {
                "id": node.id,
                "path": node.path,
                "title": node.title,
                "realm": node.realm,
                "kind": node.kind,
                "created": node.created,
                "updated": node.updated,
                "status": node.status,
                "aliases": node.aliases,
                "summary": node.summary,
                "outbound": sorted(
                    {
                        resolved[link].id
                        for link in node.links
                        if link in resolved and resolved[link].id != node.id
                    }
                ),
                "backlinks": sorted(set(backlinks[node.path])),
            }
            for node in sorted(nodes, key=lambda item: item.id)
        ],
        "edges": [
            {
                "source": source,
                "target": target,
                "type": edge_type,
                "inverse": RELATION_INVERSES[edge_type],
                "cross_realm": nodes_by_id[source].realm != nodes_by_id[target].realm,
                "mentions": sorted(mentions, key=lambda item: (str(item["path"]), int(item["line"]))),
            }
            for (source, target, edge_type), mentions in sorted(edge_mentions.items())
        ],
    }

    out_path = (root / args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(export, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(root)} with {len(export['nodes'])} nodes and {len(export['edges'])} edges.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
