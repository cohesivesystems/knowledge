---
realm: Domain Semantics
kind: semantic-construct
created: 2026-07-05
updated: 2026-07-05
aliases:
  - Invariants
---

# Invariant

An invariant is a validity constraint that must hold for a modeled subject, transition, process, relation, or boundary.

Invariants rule out states, observations, transitions, process steps, or composed outcomes that would violate the domain meaning of the model. They are semantic constraints before they are validation code, database constraints, locks, coordination protocols, or runtime checks.

An invariant is meaningful only with an explicit scope. It may constrain one entity, several related entities, a process state, a projection model, a business transaction, a boundary, or a relationship between observations. The system graph records that attachment through [[Invariant Scopes|invariant scopes]].

When an invariant constrains a transition, a failed invariant means the transition is rejected for the target subject and no accepted domain change occurs for that subject. Operational traces, error observations, retries, or compensations may still occur at other boundaries.

Related concepts: [[Entity|entity]], [[State|state]], [[Observation|observation]], [[Command|command]], [[Transition|transition]], [[Process|process]], [[Relation|relation]], [[Boundaries|boundaries]], [[Invariant Scopes|invariant scopes]], [[Policy|policy]], [[Coordination|coordination]], [[Concurrency Control|concurrency control]].
