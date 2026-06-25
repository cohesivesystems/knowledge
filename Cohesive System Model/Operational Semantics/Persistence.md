---
realm: Operational Semantics
---

# Persistence

Realm: Operational Semantics

Persistence answers: what is made durable and authoritative?

In the cohesive system model, persistence chooses which view of the system is recorded as the durable basis for future execution, reconstitution, coordination, or audit.


Durable forms may include:

- Current-state records as [[Observation|observations]].
- [[Event Sourcing|Event-sourced]] histories of committed endogenous [[Event|events]].
- Outbox records.
- Actor state providers.
- Workflow histories.
- Process state.
- [[Projections|Projection]] state as derived observations.
- [[CRDTs|CRDT]] replica state, deltas, operations, and causal metadata.

Persistence is not a single technology choice. It is a semantic decision about what the system treats as recoverable truth inside a boundary.

For [[CRDTs]], persistence must preserve enough replica state, operation history, delta history, and causal metadata for merge and convergence semantics to remain valid after restart, compaction, replication, or recovery.

In [[CQRS]], persistence usually names the authoritative write-side material from which read-side observations are reconstituted or projected.

Persistence and [[Reconstitution]] form a useful [[Duality and Symmetry|duality]]: persistence makes selected material durable, while reconstitution turns durable material back into usable observations. The duality is not perfect because persistence choices determine what can later be reconstituted.

Related concepts: [[Reconstitution]], [[Duality and Symmetry]], [[State]], [[Observation]], [[Event]], [[Event Sourcing]], [[CRDTs]], [[CQRS]], [[Storage Systems]], [[Workflow Engines]], [[Actor Systems]].
