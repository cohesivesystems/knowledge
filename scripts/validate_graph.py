#!/usr/bin/env python3
"""Validate the public Cohesive knowledge graph."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

from cohesive_graph import ALLOWED_REALMS, load_nodes, repo_root_from, resolve_links


def main() -> int:
    root = repo_root_from()
    nodes = load_nodes(root)
    resolved, unresolved, collisions = resolve_links(nodes)

    errors: list[str] = []
    warnings: list[str] = []

    for key, collision_nodes in sorted(collisions.items()):
        paths = ", ".join(sorted({node.path for node in collision_nodes}))
        errors.append(f"Ambiguous link name '{key}' maps to multiple notes: {paths}")

    for node in nodes:
        validate_node(node, errors, warnings)

    for link in unresolved:
        errors.append(
            f"Unresolved wikilink in {link.source_path}:{link.line}: [[{link.raw}]]"
        )

    inbound = Counter(target.path for target in resolved.values())
    orphan_paths = [
        node.path
        for node in nodes
        if node.path != "Cohesive System Model.md" and inbound[node.path] == 0
    ]
    if orphan_paths:
        warnings.append(f"{len(orphan_paths)} notes have no inbound links.")

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        print(
            f"Graph validation failed: {len(errors)} error(s), {len(warnings)} warning(s).",
            file=sys.stderr,
        )
        return 1

    print(
        f"Validated {len(nodes)} graph notes and {len(resolved)} wikilinks "
        f"with {len(warnings)} warning(s)."
    )
    return 0


def validate_node(node, errors: list[str], warnings: list[str]) -> None:
    if node.path == "Cohesive System Model.md":
        return

    if not node.has_h1:
        errors.append(f"Missing first-level heading in {node.path}")

    if node.realm not in ALLOWED_REALMS:
        errors.append(f"Invalid or missing realm in {node.path}: {node.realm!r}")

    path = Path(node.path)
    parts = path.parts
    if len(parts) >= 3 and parts[0] == "Cohesive System Model":
        folder_realm = parts[1]
        if folder_realm in ALLOWED_REALMS and node.realm != folder_realm:
            errors.append(
                f"Realm mismatch in {node.path}: frontmatter has "
                f"{node.realm!r}, folder implies {folder_realm!r}"
            )

    if node.status and node.status not in {"draft", "stable", "deprecated"}:
        warnings.append(f"Unexpected status in {node.path}: {node.status!r}")


if __name__ == "__main__":
    raise SystemExit(main())
