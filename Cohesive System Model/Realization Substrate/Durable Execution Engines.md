---
realm: Realization Substrate
---

# Durable Execution Engines

Realm: Realization Substrate

Durable Execution Engines are concrete runtimes or substrate mechanisms that [[Realization|realize]] [[Durable Execution]].

A durable execution engine persists enough execution material to resume, replay, retry, or recover process execution after interruption. It may present itself as a workflow engine, durable task runtime, state-machine runtime, saga runtime, process-manager framework, durable job processor, actor runtime with reminders and persisted state, or transaction manager.

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

Workflow engines are one common family of durable execution engine, but the concepts are not identical. Some [[Workflow Engines]] provide rich process modeling without strong durable execution guarantees. Some durable execution engines expose only tasks, jobs, transactions, or state machines rather than workflows.

Related concepts: [[Durable Execution]], [[Workflow Engines]], [[Realization]], [[Runtimes]], [[Processes]], [[Process]], [[Observer]], [[Coordination]], [[Persistence]], [[Reconstitution]], [[Recovery]], [[Retry]], [[Idempotency]], [[Ordering]].
