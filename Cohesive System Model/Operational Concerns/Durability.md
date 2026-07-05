---
realm: Operational Concerns
kind: operational-concern
status: draft
aliases:
  - durable state
  - durable material
  - durability boundary
---

# Durability

Durability answers: which facts, histories, effects, decisions, or execution material survive which failures?

Durability is an operational concern tied to failure, fate sharing, and recovery. A durability claim is always boundary-relative: it says what remains available, reconstructable, or authoritative after a declared failure boundary is crossed.

Durability is related to [[Persistence|persistence]], but it is not identical to persistence. Persistence selects what material is recorded. Durability states which failures that material is expected to survive and whether it remains usable for [[Reconstitution|reconstitution]], [[Recovery|recovery]], audit, replay, deduplication, or coordination.

## Failure and Fate Sharing

Durability depends on what fails together.

Two components fate-share when they are lost, restarted, partitioned, corrupted, or made unavailable together often enough that one cannot be treated as durable evidence for the other. Writing process state to the memory of the worker that may crash is not durable across worker crash. Writing it to a replicated store may be durable across one worker crash but not necessarily across data-center loss, operator deletion, correlated software corruption, or a broken replication protocol.

Durability claims should therefore name:

- The material being protected.
- The boundary at which the claim holds.
- The failure modes considered.
- The fate-sharing assumptions between writer, store, replicas, logs, queues, timers, and external systems.
- The recovery procedure that can use the material after failure.
- The cases where the material may be missing, duplicated, stale, corrupted, or ambiguous.

## Durable Material

Durable material may include:

- Entity state records and versions.
- Committed event histories.
- Transaction logs and write-ahead logs.
- Outbox and inbox records.
- Idempotency keys and deduplication records.
- Workflow histories, process state, checkpoints, timers, signals, and pending work.
- Broker logs, offsets, cursors, and acknowledgments.
- Replica state, CRDT causal metadata, consensus logs, and membership records.
- Audit evidence, operator decisions, and repair records.

The durability of one material does not automatically make a larger process durable. A durable outbox row may preserve publication responsibility without proving that a downstream observer received or processed the event. A durable workflow history may preserve execution context without proving that an external payment, email, shipment, or human approval completed.

## Relation to Recovery

Durability is meaningful only with a recovery interpretation. Durable material should let the system return to coherent operation without inventing histories, losing accepted facts, duplicating irreversible effects, or weakening the boundary's consistency claim.

For example:

- A transaction log is durable enough when recovery can redo committed work and avoid exposing uncommitted work.
- An event stream is durable enough when reconstitution and projection can rebuild the intended observations.
- An outbox is durable enough when accepted local transitions and publication responsibility survive the failure boundary.
- A process checkpoint is durable enough when execution can resume or repair without changing the process meaning.

[[Durable Execution|Durable execution]] is an architecture practice built from this concern. It uses durable execution material plus recovery, reconstitution, idempotency, ordering, and coordination to address interruption of logical execution.

Related concepts: [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Distributed Failure Scenarios|distributed failure scenarios]], [[Commit Boundaries|commit boundaries]], [[Acknowledgments|acknowledgments]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Consensus|consensus]], [[Write-Ahead Logging|write-ahead logging]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Event Sourcing|event sourcing]], [[Durable Execution|durable execution]], [[Durable Execution Engines|durable execution engines]], [[Storage Systems|storage systems]], [[Brokers|brokers]].
