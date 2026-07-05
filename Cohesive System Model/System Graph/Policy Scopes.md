---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-05
aliases:
  - Policy Scope
  - Policy Scopes
---

# Policy Scopes

Policy scopes describe where semantic [[Policy|policies]] are attached in the system graph.

At the structure level, a policy scope identifies which observer model, boundary, entity model, process graph, relation model, projection model, transition, or effect a policy governs. Policy scopes explain where a command is accepted, rejected, routed, delayed, retried, compensated, or interpreted differently by different observers. This describes decision scope and meaning, not a specific policy engine or enforcement substrate.

Policy scopes may cover:

- Authority and permissions.
- Validation rules.
- Routing decisions.
- Retry and rate-limiting behavior.
- Coordination choices.
- Retention and replay.
- Recovery and compensation.

Policies are observer-relative when they affect command interpretation inside a specific observer boundary.

Related concepts: [[Policy|policy]], [[Observer Models|observer models]], [[Entity Models|entity models]], [[Process Graphs|process graphs]], [[Relation Models|relation models]], [[Projection Models|projection models]], [[Command|command]], [[Observer|observer]], [[Transition|transition]], [[Invariant Scopes|invariant scopes]], [[Rate Limiting|rate limiting]], [[Retry|retry]], [[Coordination|coordination]].
