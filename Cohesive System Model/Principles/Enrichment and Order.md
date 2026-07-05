---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-06-29
---

# Enrichment and Order

Enrichment adds structure to relationships. Instead of merely asking whether a relationship exists, an enriched view asks what kind of value the relationship has: order, distance, cost, probability, time, authority, confidence, or information.

In many models, relationships are not just arrows. They carry operational and semantic measures:

- Happens-before or version order.
- Delivery ordering.
- Latency or cost.
- Trust or authority.
- Consistency strength.
- Probability or confidence.
- Information refinement.
- Failure or recovery scope.

Order is the most common enrichment in the Cohesive System Model. Versions, event schedules, workflow histories, broker partitions, and state histories all rely on explicit ordering spaces.

Enrichment helps ask:

- Is this relation merely possible, or ordered, weighted, trusted, timed, or constrained?
- What is the ordering or metric space?
- Does the ordering compose across boundaries?
- Are two paths equivalent, or is one more authoritative, cheaper, faster, newer, or more reliable?

Examples:

- [[Ordering]] defines where events, commands, observations, or effects are sequenced.
- [[Version]] enriches entity state observations with history position.
- [[Delivery Semantics]] enrich interaction edges with guarantees.
- [[Rate Limiting]] and retry policies enrich interactions with control behavior.

Related concepts: [[Ordering|ordering]], [[Version|version]], [[Time|time]], [[Delivery Semantics|delivery semantics]], [[Rate Limiting|rate limiting]], [[Boundaries|boundaries]], [[Concurrency Control|concurrency control]].
