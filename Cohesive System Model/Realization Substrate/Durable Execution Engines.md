---
realm: Realization Substrate
kind: realization-substrate
---

# Durable Execution Engines

Durable execution engines are concrete runtimes or substrate mechanisms that [[Realization|realize]] [[Durable Execution|durable execution]].

A durable execution engine persists enough execution material to resume, replay, retry, or recover process execution after interruption. It may present itself as a workflow engine, durable task runtime, state-machine runtime, saga runtime, process-manager framework, durable job processor, actor runtime with reminders and persisted state, or transaction manager.

Viewed as [[Sagas and Process Managers|process managers]], durable execution engines manage execution recovery. They recover the execution context of the same logical computation: workflow state or history, checkpoints, timers, signals, scheduled activities, retry state, and pending work. They may host sagas, but the saga logic is what decides whether completed business actions require compensation, alternate paths, negotiation, partial completion, or human intervention.

Durable execution engines are not identical to [[Process|processes]]. A semantic process may be advanced by many durable executions, and one durable execution engine may host many different process structures. A durable workflow instance, job record, activation, or transaction may realize one execution attempt, one step, one boundary, or one long-lived process instance depending on the model.

Durable execution engine concerns include:

- Execution identity and addressing.
- Durable history, state, checkpoints, timers, or queues.
- Replay, resume, or continuation behavior.
- Activity, step, or handler scheduling.
- Signal, event, cancellation, and timeout delivery.
- Retry, backoff, compensation, and escalation support.
- Effect boundaries, idempotency keys, and deduplication records.
- Versioning, migration, and compatibility of persisted execution history.
- Operational visibility, inspection, and repair.

Workflow engines are one common family of durable execution engine, but the concepts are not identical. Some [[Workflow Engines|workflow engines]] provide rich process modeling without strong durable execution guarantees. Some durable execution engines expose only tasks, jobs, transactions, or state machines rather than workflows.

Related concepts: [[Durable Execution|durable execution]], [[Workflow Engines|workflow engines]], [[Sagas and Process Managers|sagas and process managers]], [[Realization|realization]], [[Runtimes|runtimes]], [[Processes|processes]], [[Process|process]], [[Observer|observer]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Retry|retry]], [[Idempotency|idempotency]], [[Ordering|ordering]].
