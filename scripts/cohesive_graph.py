#!/usr/bin/env python3
"""Shared graph parsing helpers for the Cohesive knowledge repository."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
import re
from typing import Any


ALLOWED_REALMS = {
    "Principles",
    "Semantic Dynamics",
    "Operational Semantics",
    "System Structure",
    "Realization Substrate",
    "Architecture Practices",
}

ALLOWED_KINDS = {
    "overview",
    "discipline",
    "principle",
    "semantic-construct",
    "structural-construct",
    "operational-semantics",
    "realization-substrate",
    "architecture-practice",
    "pattern",
    "example",
    "reference",
    "glossary",
}

DEFAULT_SOURCES = ("Cohesive System Model.md", "Cohesive System Model")

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")


@dataclass(frozen=True)
class Link:
    source_path: str
    line: int
    raw: str
    target: str
    label: str | None = None


@dataclass
class Node:
    id: str
    path: str
    title: str
    realm: str
    kind: str
    status: str | None
    aliases: list[str] = field(default_factory=list)
    summary: str = ""
    frontmatter: dict[str, Any] = field(default_factory=dict)
    links: list[Link] = field(default_factory=list)
    has_h1: bool = False


def repo_root_from(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists() or (candidate / "Cohesive System Model.md").exists():
            return candidate
    return current


def discover_markdown_files(root: Path, sources: tuple[str, ...] = DEFAULT_SOURCES) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()

    for source in sources:
        path = root / source
        if path.is_file() and path.suffix == ".md":
            resolved = path.resolve()
            if resolved not in seen:
                files.append(path)
                seen.add(resolved)
        elif path.is_dir():
            for markdown in sorted(path.rglob("*.md")):
                if any(part.startswith(".") for part in markdown.relative_to(path).parts):
                    continue
                resolved = markdown.resolve()
                if resolved not in seen:
                    files.append(markdown)
                    seen.add(resolved)

    return sorted(files, key=lambda p: p.relative_to(root).as_posix().lower())


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, 1

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, text, 1

    frontmatter = parse_simple_yaml(lines[1:end_index])
    body = "\n".join(lines[end_index + 1 :])
    if text.endswith("\n"):
        body += "\n"
    return frontmatter, body, end_index + 2


def parse_simple_yaml(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None

    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        stripped = line.strip()
        if current_key and stripped.startswith("- "):
            value = strip_quotes(stripped[2:].strip())
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(value)
            continue

        current_key = None
        if ":" not in line:
            continue

        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()

        if not value:
            data[key] = []
            current_key = key
        elif value.startswith("[") and value.endswith("]"):
            inside = value[1:-1].strip()
            data[key] = [] if not inside else [strip_quotes(v.strip()) for v in inside.split(",")]
        else:
            data[key] = strip_quotes(value)

    return data


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_node(path: Path, root: Path) -> Node:
    rel_path = path.relative_to(root).as_posix()
    text = read_text(path)
    frontmatter, body, body_start_line = parse_frontmatter(text)
    title, has_h1 = extract_title(path, body)
    realm = infer_realm(path, root, frontmatter)
    kind = str(frontmatter.get("kind") or ("overview" if rel_path == "Cohesive System Model.md" else ""))
    status_value = frontmatter.get("status")
    status = str(status_value) if status_value is not None else None
    aliases = normalize_aliases(frontmatter.get("aliases"))

    return Node(
        id=node_id_for_path(path, root),
        path=rel_path,
        title=title,
        realm=realm,
        kind=kind,
        status=status,
        aliases=aliases,
        summary=extract_summary(body),
        frontmatter=frontmatter,
        links=extract_wikilinks(rel_path, body, body_start_line),
        has_h1=has_h1,
    )


def extract_title(path: Path, body: str) -> tuple[str, bool]:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip(), True
    return path.stem, False


def infer_realm(path: Path, root: Path, frontmatter: dict[str, Any]) -> str:
    if "realm" in frontmatter:
        return str(frontmatter["realm"])

    rel_parts = path.relative_to(root).parts
    if len(rel_parts) >= 3 and rel_parts[0] == "Cohesive System Model":
        return rel_parts[1]
    if path.relative_to(root).as_posix() == "Cohesive System Model.md":
        return "Overview"
    return "Unspecified"


def normalize_aliases(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    return []


def extract_summary(body: str) -> str:
    lines = body.splitlines()
    start = 0
    for index, line in enumerate(lines):
        if line.startswith("# "):
            start = index + 1
            break

    paragraph: list[str] = []
    in_fence = False
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not stripped:
            if paragraph:
                break
            continue
        if stripped.startswith("#") or stripped.startswith("- "):
            if paragraph:
                break
            continue
        paragraph.append(stripped)

    return " ".join(paragraph)


def extract_wikilinks(source_path: str, body: str, start_line: int = 1) -> list[Link]:
    links: list[Link] = []
    in_fence = False

    for line_number, line in enumerate(body.splitlines(), start=start_line):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for match in WIKILINK_RE.finditer(line):
            raw = match.group(1).strip()
            target_part, label = split_wikilink(raw)
            if target_part:
                links.append(
                    Link(
                        source_path=source_path,
                        line=line_number,
                        raw=raw,
                        target=target_part,
                        label=label,
                    )
                )

    return links


def split_wikilink(raw: str) -> tuple[str, str | None]:
    if "|" in raw:
        target_part, label = raw.split("|", 1)
    else:
        target_part, label = raw, None

    target = target_part.split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target, label.strip() if label else None


def node_id_for_path(path: Path, root: Path) -> str:
    rel_without_suffix = path.relative_to(root).with_suffix("").as_posix()
    parts = PurePosixPath(rel_without_suffix).parts
    return "/".join(slugify(part) for part in parts)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "node"


def normalize_lookup(value: str) -> str:
    normalized = value.replace("\\", "/").strip()
    if normalized.endswith(".md"):
        normalized = normalized[:-3]
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.casefold()


def build_lookup(nodes: list[Node]) -> tuple[dict[str, Node], dict[str, list[Node]]]:
    lookup: dict[str, Node] = {}
    collisions: dict[str, list[Node]] = {}

    for node in nodes:
        names = {
            node.title,
            Path(node.path).stem,
            Path(node.path).with_suffix("").as_posix(),
            *node.aliases,
        }
        for name in names:
            key = normalize_lookup(name)
            if not key:
                continue
            existing = lookup.get(key)
            if existing and existing.path != node.path:
                collisions.setdefault(key, [existing]).append(node)
            else:
                lookup[key] = node

    return lookup, collisions


def resolve_links(nodes: list[Node]) -> tuple[dict[Link, Node], list[Link], dict[str, list[Node]]]:
    lookup, collisions = build_lookup(nodes)
    resolved: dict[Link, Node] = {}
    unresolved: list[Link] = []

    for node in nodes:
        for link in node.links:
            target = lookup.get(normalize_lookup(link.target))
            if target:
                resolved[link] = target
            else:
                unresolved.append(link)

    return resolved, unresolved, collisions


def load_nodes(root: Path | None = None) -> list[Node]:
    repo_root = root or repo_root_from()
    return [parse_node(path, repo_root) for path in discover_markdown_files(repo_root)]
