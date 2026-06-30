---
realm: Operational Semantics
kind: operational-semantics
---

# Durable Execution

Durable Execution is the operational semantics by which a process can continue coherently across failure, restart, suspension, timeout, or delayed external work.

Durable execution is not a workflow engine. It is the guarantee that process progress, pending decisions, timers, signals, retries, and recovery context are preserved well enough for execution to resume without changing the semantic meaning of the [[Process|process]].

Durable execution depends on:

- [[Persistence]] of execution state, history, checkpoints, timers, signals, or pending work.
- [[Reconstitution]] of usable process context after interruption.
- [[Recovery]] behavior that resumes, replays, retries, compensates, or escalates without inventing different semantic history.
- [[Ordering]] of history, signals, decisions, activities, and emitted effects within the relevant boundary.
- [[Idempotency]] at effect boundaries so resumed execution does not duplicate irreversible work.
- [[Coordination]] with entity transitions, external systems, and output events.

Durable execution may be history-based, checkpoint-based, state-machine-based, event-sourced, transaction-log-based, or externally coordinated. Deterministic replay is one realization strategy, not the definition.

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

Durable execution is [[Realization|realized]] by [[Durable Execution Engines|durable execution engines]], workflow engines, job processors with durable queues, actor reminders plus state providers, database-backed process managers, saga runtimes, transaction managers, or custom coordination code.

Related concepts: [[Process|process]], [[Processes|processes]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Retry|retry]], [[Idempotency|idempotency]], [[Ordering|ordering]], [[Delivery Semantics|delivery semantics]], [[Durable Execution Engines|durable execution engines]], [[Workflow Engines|workflow engines]], [[Business Transactions|business transactions]], [[Realization|realization]].
