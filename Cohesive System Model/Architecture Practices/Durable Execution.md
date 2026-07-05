---
realm: Architecture Practices
kind: pattern
created: 2026-06-28
updated: 2026-07-04
---

# Durable Execution

Durable execution is an architecture practice for keeping a logical execution coherent across failure, restart, suspension, timeout, or delayed external work.

Durable execution is not the general operational concern of [[Durability|durability]], and it is not a workflow engine. It is a solution pattern that combines durability of execution material with [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Idempotency|idempotency]], [[Ordering|ordering]], and [[Coordination|coordination]] so execution can resume without changing the semantic meaning of the [[Process|process]].

Its core recovery goal is execution recovery: recover the execution of the same logical computation after failure. A failure is treated as an interruption of execution, not necessarily as a failed business outcome.

Durable execution addresses failure modes where process progress, pending decisions, timers, signals, retries, and recovery context would otherwise be lost or duplicated when the execution host, worker, VM, process, runtime, network path, or external dependency fails independently.

Durable execution composes:

- [[Durability]] of execution material across the relevant failure boundary.
- [[Persistence]] of execution state, history, checkpoints, timers, signals, or pending work.
- [[Reconstitution]] of usable process context after interruption.
- [[Recovery]] behavior that resumes, replays, retries, compensates, or escalates without inventing different semantic history.
- [[Ordering]] of history, signals, decisions, activities, and emitted effects within the relevant boundary.
- [[Idempotency]] at effect boundaries so resumed execution does not duplicate irreversible work.
- [[Coordination]] with entity transitions, external systems, and output events.

Durable execution may be history-based, checkpoint-based, state-machine-based, event-sourced, transaction-log-based, or externally coordinated. Deterministic replay is one realization strategy, not the definition.

Durable execution provides infrastructure-level recovery before it provides application-level compensation. Infrastructure compensation restores execution context so the computation can continue unchanged. Application compensation performs new business operations to reconcile the system with the external world; that is saga or business recovery even when the compensating logic runs inside durable execution.

Durable execution is boundary-relative. A workflow checkpoint, persisted job record, timer record, outbox row, or transaction log entry each says what is durable at its own boundary. None automatically means that the business transaction completed, that an entity transition committed, or that another observer processed the follow-up work.

Durable execution concerns include:

- Process or execution identity.
- Persisted progress state or history.
- Resume and replay semantics.
- Timer, signal, and cancellation durability.
- Activity or step retry semantics.
- Effect emission and deduplication boundaries.
- Compensation or rollback behavior.
- Human, external-system, and long-delay interactions.
- Versioning and migration of process definitions and persisted histories.

Durable execution is [[Realization|realized]] by [[Durable Execution Engines|durable execution engines]], workflow engines, job processors with durable queues, actor reminders plus state providers, database-backed [[Process Managers|process managers]], saga runtimes, transaction managers, or custom coordination code. [[Process Theories|Process theories]] help distinguish this execution-recovery pattern from the broader semantic process and from business-recovery patterns such as [[Sagas|sagas]].

Related concepts: [[Durability|durability]], [[Process Theories|process theories]], [[Process|process]], [[Processes|processes]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Retry|retry]], [[Idempotency|idempotency]], [[Ordering|ordering]], [[Delivery Semantics|delivery semantics]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution Engines|durable execution engines]], [[Workflow Engines|workflow engines]], [[Business Transactions|business transactions]], [[Realization|realization]].
