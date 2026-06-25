---
realm: Principles
---

# Enrichment And Order

Realm: Principles

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

Related concepts: [[Ordering]], [[Version]], [[Time]], [[Delivery Semantics]], [[Rate Limiting]], [[Boundaries]], [[Concurrency Control]].
