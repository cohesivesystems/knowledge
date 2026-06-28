---
realm: Operational Semantics
---

# Reconstitution

Reconstitution answers: how is usable state recovered?

Reconstitution turns persisted material back into current, usable [[Observation|observations]] of [[State]] so that [[Observer|Observers]], [[Entity|Entities]], workflows, projections, and processes can continue operating.

Common strategies include:

- Load the latest record and produce an observation.
- Replay [[Event Sourcing|event-sourced]] committed events and fold them into a current observation.
- Load a snapshot plus subsequent events.
- Restore [[CRDTs|CRDT]] replica state and causal metadata so merge semantics remain valid.
- Resume [[Durable Execution|durable execution]] state, checkpoints, or workflow history.
- Activate an actor by identity.
- Rebuild a projection as an observation.

The chosen strategy depends on what [[Persistence]] made durable and what the observer needs in order to interpret new inputs.

In [[CQRS]], reconstitution often happens on the [[Query|query]] side through projections, materialized views, caches, indexes, or other read models derived from authoritative write-side persistence.

Reconstitution and [[Persistence]] form a useful [[Duality and Symmetry|duality]]: persistence records selected material as recoverable truth, while reconstitution recovers usable observations from that material. The result can only be as complete as the persisted material and the reconstitution rules allow.

Related concepts: [[Persistence]], [[Durable Execution]], [[Duality and Symmetry]], [[Observation]], [[Query]], [[State]], [[Event]], [[Event Sourcing]], [[CRDTs]], [[CQRS]], [[Projections]], [[Workflow Engines]], [[Durable Execution Engines]], [[Actor Systems]].
