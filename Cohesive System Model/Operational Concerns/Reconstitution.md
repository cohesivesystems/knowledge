---
realm: Operational Concerns
kind: operational-concern
---

# Reconstitution

Reconstitution answers: how is usable state recovered?

Reconstitution turns persisted material back into current, usable [[Observation|observations]] of [[State|state]] so that [[Observer|observers]], [[Entity|entities]], workflows, projections, and processes can continue operating.

Common strategies include:

- Load the latest record and produce an observation.
- Replay [[Event Sourcing|event-sourced]] committed events and fold them into a current observation.
- Load a snapshot plus subsequent events.
- Restore [[CRDTs|CRDT]] replica state and causal metadata so merge semantics remain valid.
- Resume [[Durable Execution|durable execution]] state, checkpoints, or workflow history.
- Activate an actor by identity.
- Rebuild a projection as an observation.

The chosen strategy depends on what [[Persistence|persistence]] made durable and what the observer needs in order to interpret new inputs.

In [[CQRS]], reconstitution often happens on the [[Query|query]] side through projections, materialized views, caches, indexes, or other read models derived from authoritative write-side persistence.

In database recovery, reconstitution may be hidden inside the storage engine. ARIES-style recovery reconstructs a coherent database state from pages, checkpoints, and [[Write-Ahead Logging|write-ahead log]] records by replaying redo and undo work according to transaction status and log sequence numbers.

Reconstitution and [[Persistence|persistence]] form a useful [[Duality and Symmetry|duality]]: persistence records selected material as recoverable truth, while reconstitution recovers usable observations from that material. The result can only be as complete as the persisted material and the reconstitution rules allow.

Related concepts: [[Persistence|persistence]], [[Recovery|recovery]], [[ACID]], [[Write-Ahead Logging|write-ahead logging]], [[Durable Execution|durable execution]], [[Duality and Symmetry|duality and symmetry]], [[Observation|observation]], [[Query|query]], [[State|state]], [[Event|event]], [[Event Sourcing|event sourcing]], [[CRDTs]], [[CQRS]], [[Projections|projections]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Actor Systems|actor systems]].
