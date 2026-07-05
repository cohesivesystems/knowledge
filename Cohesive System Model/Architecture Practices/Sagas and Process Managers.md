---
realm: Architecture Practices
kind: pattern
---

# Sagas and Process Managers

Sagas and process managers address the problem of coordinating long-running, multi-step work across boundaries where one atomic transaction is unavailable or inappropriate.

## Cohesive Formulation

A [[Sagas and Process Managers|process manager]] is the broader coordinating role: it gives a [[Process|process]] identity, records progress or history, observes inputs, decides next steps, and emits commands or events across boundaries.

The sagas and process managers practice is about [[Processes|processes]], [[Coordination|coordination]], and sometimes [[Durable Execution|durable execution]]:

- A process has identity, state, progress, and recovery behavior.
- It observes events or signals.
- It emits commands to participants.
- It may compensate, retry, time out, or escalate.

[[Process Theories|Process theories]] provide the broader vocabulary for this practice: the process interface, composition shape, feedback loops, equivalence of executions, recovery meaning, and realization obligations should all be explicit.

Sagas and process managers can be implemented without a workflow engine, but they still need explicit persistence, recovery, idempotency, and delivery semantics when they are expected to survive failure or long delays.

## Distinction

Viewed through the process-management role, sagas and [[Durable Execution Engines|durable execution engines]] are both process managers. The key difference is what is being recovered.

A saga is a business-recovery process manager. It treats failure as an invalid, undesirable, or no-longer-achievable business state. Recovery may involve undoing prior business actions, issuing compensating commands, negotiating with external systems, choosing an alternate path, requesting human intervention, or partially completing the process.

A [[Durable Execution Engines|durable execution engine]] is an execution-recovery process manager. It treats failure as an interruption of execution. Recovery restores enough execution context for the same logical computation to continue through persisted workflow state or history, deterministic replay when applicable, durable checkpoints, activity retry, timers, signals, and process, VM, or machine restart.

A saga can be implemented on [[Durable Execution|durable execution]] by making compensation decisions inside resumable workflow code. During resumed execution, the saga checks whether compensation or an alternate path is required, then performs the specific business operation. The saga does not require full durable execution, however. It can also coordinate and recover from event-sourced process history, current-state process records, [[Transactional Outbox|outbox]] and [[Transactional Inbox|inbox]] records, or event subscriptions when those mechanisms preserve identity, ordering, idempotency, and recovery.

In short, durable execution says "continue the same computation." Saga recovery says "the world has changed; decide how the business process should proceed."

## In the Model

A saga can be modeled as an entity-observer: it has state and history, observes events, interprets them relative to a process boundary, and emits commands or endogenous process events.

In a [[Weak Isolation Patterns|weak isolation]] context, compensating actions are asynchronous and eventual. A compensation is not an inverse database update that restores a globally isolated past. It is a new command, transition, or process step whose effect may arrive later, fail, retry, be observed by other participants, and require its own idempotency, ordering, and recovery semantics.

ARIES is useful as a contrast point. A database transaction log can support undo, redo, and partial rollback inside one storage engine's transaction boundary. Its Compensation Log Records record undo actions so recovery can repeat history safely and avoid undoing the same action twice. A saga log or process history supports recovery across multiple boundaries, but its compensating steps are semantic forward actions, not storage-engine undo records or ARIES-style Compensation Log Records.

## Failure Modes

The pattern fails when the process boundary is implicit, when compensation is assumed to be inverse transition, or when delivery and idempotency are ignored. Sagas do not remove consistency problems; they make consistency procedural and temporal.

## External References

- Hector Garcia-Molina and Kenneth Salem, [Sagas](https://www.cs.princeton.edu/techreports/1987/070.pdf), Princeton CS-TR-070-87, 1987.
- C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, and Peter Schwarz, [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging](https://web.stanford.edu/class/cs345d-01/rl/aries.pdf), ACM Transactions on Database Systems, 17(1):94-162, March 1992.

Related concepts: [[Process Theories|process theories]], [[Processes|processes]], [[Coordination|coordination]], [[Weak Isolation Patterns|weak isolation patterns]], [[Weak Isolation Patterns as Architecture Practice|weak isolation patterns as architecture practice]], [[ACID]], [[Write-Ahead Logging|write-ahead logging]], [[Durable Execution|durable execution]], [[Observer|observer]], [[Entity|entity]], [[Command|command]], [[Event|event]], [[Idempotency|idempotency]], [[Ordering|ordering]], [[Retry|retry]], [[Recovery|recovery]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Trace and Feedback|trace and feedback]].
