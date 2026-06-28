#!/usr/bin/env python3
"""Scan public graph files for high-signal private material patterns."""

from __future__ import annotations

import re
import sys

from cohesive_graph import discover_markdown_files, repo_root_from


PATTERNS = {
    "private key": re.compile(r"-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----"),
    "aws access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "openai-like key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "assignment password": re.compile(r"(?i)\b(password|passwd|pwd)\s*[:=]\s*\S+"),
    "assignment api key": re.compile(r"(?i)\b(api[_-]?key|token|secret)\s*[:=]\s*\S+"),
}


def main() -> int:
    root = repo_root_from()
    findings: list[str] = []

    for path in discover_markdown_files(root):
        rel_path = path.relative_to(root).as_posix()
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{rel_path}:{line_number}: possible {label}")

    if findings:
        for finding in findings:
            print(f"error: {finding}", file=sys.stderr)
        print(f"Public scan failed: {len(findings)} finding(s).", file=sys.stderr)
        return 1

    print("Public scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
