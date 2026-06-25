---
realm: System Structure
---

# Policies

Realm: System Structure

Policies describe where decision rules are attached in the system graph.

At the structure level, policies guide or constrain interpretation, authorization, routing, coordination, or execution. They explain why a command is accepted, rejected, routed, delayed, retried, compensated, or interpreted differently by different observers. This describes decision scope and meaning, not a specific policy engine or enforcement substrate.

Policies may cover:

- Authority and permissions.
- Validation rules.
- Routing decisions.
- Retry and rate-limiting behavior.
- Coordination choices.
- Retention and replay.
- Recovery and compensation.

Policies are observer-relative when they affect command interpretation inside a specific observer boundary.

Related concepts: [[Command]], [[Observer]], [[Transition]], [[Invariants]], [[Rate Limiting]], [[Retry]], [[Coordination]].
