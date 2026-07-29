---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-28
updated: 2026-07-29
---

# Durable Execution Engines

Durable execution engines are concrete runtimes or substrate mechanisms that [[Realization|realize]] the [[Durable Execution|durable execution]] architecture practice.

A durable execution engine provides [[Durability|durability]] for enough execution material to resume, replay, retry, or recover process execution after interruption. It may present itself as a workflow engine, durable task runtime, state-machine runtime, saga runtime, process-manager framework, durable job processor, actor runtime with reminders and persisted state, or transaction manager.

Viewed as [[Process Managers|process managers]], durable execution engines manage execution recovery. They recover the execution context of the same logical computation: workflow state or history, checkpoints, timers, signals, scheduled activities, retry state, and pending work. They may host [[Sagas|sagas]], but the saga logic is what decides whether completed business actions require compensation, alternate paths, negotiation, partial completion, or human intervention.

Durable execution engines are not identical to [[Process|processes]]. A semantic process may be advanced through many finite activations or execution attempts governed by [[Durable Execution|durable execution]], and one durable execution engine may host many different process structures. A durable workflow instance, job record, activation, or transaction may realize one execution attempt, one step, one boundary, or one long-lived process instance depending on the model.

A conforming engine interprets a pinned canonical [[Process Graphs|process graph]] rather than treating engine-native delegates, registrations, current code, or workflow names as semantic authority. The continuation identifies the exact supported definition identity, semantic revision, and normalized content identity unless an explicit migration establishes another correspondence.

The engine should distinguish:

- A process instance from one process attempt.
- A process attempt from one finite activation.
- One activation from the tokens and operation attempts it advances.
- Deterministic replay from an operation retry.
- Host recovery of the same attempt from restart of a new attempt.
- Pause and continue from cancellation or termination.
- Definition migration from name-based replacement.

Each activation terminates, reaches quiescence, or reaches an explicit durable cut. Long-lived behavior is realized by persisted continuation, timers, signals, waits, feedback, or repeated finite activations rather than by retaining one live call stack or hiding unrestricted computation inside the process definition.

Durable execution engine concerns include:

- Execution identity and addressing.
- Definition identity, semantic revision, normalized content identity, and compatibility.
- Durable history, state, checkpoints, timers, or queues.
- Complete token sets, fork and join state, typed bindings, and terminal outcomes.
- Replay, resume, or continuation behavior.
- Activity, step, or handler scheduling.
- Signal, event, cancellation, and timeout delivery.
- Retry, backoff, compensation, and escalation support.
- Effect boundaries, idempotency keys, and deduplication records.
- Versioning, migration, and compatibility of persisted execution history.
- Operational visibility, inspection, and repair.

Durable waits require registration before yielding, early-input handling, stable signal or result identities, deduplication, claim and consumption state, deterministic winner selection where exclusive, losing-input disposition, timeout handling, retention, and late or stale input policy. A workflow signal API or broker queue is only a candidate mechanism for those requirements.

Durable effect execution similarly requires stable semantic emission identity across physical attempts, acknowledgment and ambiguous-outcome evidence, and protection against duplicate logical consequences. The engine must not claim physical exactly-once external execution without target evidence.

Workflow engines are one common family of durable execution engine, but the concepts are not identical. Some [[Workflow Engines|workflow engines]] provide rich process modeling without strong durable execution guarantees. Some durable execution engines expose only tasks, jobs, transactions, or state machines rather than workflows.

Related concepts: [[Execution Kernel|execution kernel]], [[Durability|durability]], [[Durable Execution|durable execution]], [[Workflow Engines|workflow engines]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Realization|realization]], [[Runtimes|runtimes]], [[Storage Systems|storage systems]], [[Process Graphs|process graphs]], [[Process|process]], [[Transition Models|transition models]], [[Observer|observer]], [[Effect|effect]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Commit Boundaries|commit boundaries]], [[Recovery|recovery]], [[Retry|retry]], [[Idempotency|idempotency]], [[Ordering|ordering]].
