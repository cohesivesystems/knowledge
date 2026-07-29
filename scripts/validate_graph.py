#!/usr/bin/env python3
"""Validate the public Cohesive knowledge graph."""

from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import re
import sys

from cohesive_graph import (
    ALLOWED_FORMAL_RELATION_TYPES,
    ALLOWED_KINDS,
    ALLOWED_REALMS,
    load_nodes,
    repo_root_from,
    resolve_links,
)


ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

RELATION_SOURCE_REALMS = {
    "arranges": "System Graph",
    "qualifies": "Operational Concerns",
    "bundles": "Architecture Practices",
    "may_realize": "Realization Substrate",
}


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

    seen_relations: set[tuple[str, str, str]] = set()
    for node in nodes:
        for relation in node.formal_relations:
            target = resolved.get(relation.link)
            if target is None:
                continue
            key = (node.id, target.id, relation.relation_type)
            if key in seen_relations:
                errors.append(
                    f"Duplicate formal relation in {node.path}:{relation.link.line}: "
                    f"{relation.relation_type} -> {target.title}"
                )
            seen_relations.add(key)
            if node.id == target.id:
                errors.append(
                    f"Self-referential formal relation in {node.path}:{relation.link.line}: "
                    f"{relation.relation_type}"
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
    for issue in node.relation_issues:
        errors.append(f"{issue.source_path}:{issue.line}: {issue.message}")

    for relation in node.formal_relations:
        relation_type = relation.relation_type
        if relation_type not in ALLOWED_FORMAL_RELATION_TYPES:
            errors.append(
                f"Unknown formal relation type in {node.path}:{relation.link.line}: "
                f"{relation_type!r}"
            )
            continue

        expected_realm = RELATION_SOURCE_REALMS.get(relation_type)
        if expected_realm and node.realm != expected_realm:
            errors.append(
                f"Formal relation {relation_type!r} in {node.path}:{relation.link.line} "
                f"must originate in realm {expected_realm!r}, not {node.realm!r}"
            )

        if relation_type == "documents" and node.kind not in {
            "reference",
            "glossary",
            "overview",
        }:
            errors.append(
                f"Formal relation 'documents' in {node.path}:{relation.link.line} "
                f"must originate from a reference-like node, not kind {node.kind!r}"
            )

    created = validate_date_field(node, "created", errors)
    updated = validate_date_field(node, "updated", errors)
    if created and updated and updated < created:
        errors.append(
            f"Updated date precedes created date in {node.path}: "
            f"created={node.created!r}, updated={node.updated!r}"
        )

    if node.path == "Cohesive System Model.md":
        if node.kind != "overview":
            errors.append(f"Top-level overview must have kind 'overview': {node.kind!r}")
        return

    if not node.has_h1:
        errors.append(f"Missing first-level heading in {node.path}")

    if node.realm not in ALLOWED_REALMS:
        errors.append(f"Invalid or missing realm in {node.path}: {node.realm!r}")

    if not node.kind:
        errors.append(f"Missing kind in {node.path}")
    elif node.kind not in ALLOWED_KINDS:
        errors.append(f"Invalid kind in {node.path}: {node.kind!r}")

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


def validate_date_field(node, field: str, errors: list[str]) -> date | None:
    value = getattr(node, field)
    if value is None:
        errors.append(f"Missing {field} date in {node.path}")
        return None

    if not ISO_DATE_RE.fullmatch(value):
        errors.append(f"Invalid {field} date in {node.path}: {value!r}")
        return None

    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"Invalid {field} date in {node.path}: {value!r}")
        return None


if __name__ == "__main__":
    raise SystemExit(main())
