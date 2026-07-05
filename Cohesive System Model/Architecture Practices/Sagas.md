---
realm: Architecture Practices
kind: pattern
aliases:
  - Saga
---

# Sagas

Sagas are [[Process Managers|process managers]] specialized for business recovery across boundaries where one atomic transaction is unavailable, too expensive, or misaligned with the domain process.

A saga coordinates a long-running [[Process|process]] whose completed business actions may need compensating, alternate, partial, or human-mediated follow-up when later facts prevent the original path from completing.

## Cohesive Formulation

A saga is concerned with business recovery. Its goal is to recover the business process when completed business actions cannot simply be retried.

A saga treats failure as an invalid, undesirable, or no-longer-achievable business state. Recovery may involve:

- Issuing compensating commands.
- Undoing or counteracting prior business actions through new semantic work.
- Negotiating with external systems.
- Choosing an alternate path.
- Requesting human intervention.
- Partially completing, expiring, rejecting, or reconciling the process.

A saga can be implemented on [[Durable Execution|durable execution]] by making compensation decisions inside resumable workflow code. During resumed execution, the saga checks whether compensation or an alternate path is required, then performs the specific business operation.

A saga does not require full durable execution. It can also coordinate and recover from event-sourced process history, current-state process records, [[Transactional Outbox|outbox]] and [[Transactional Inbox|inbox]] records, subscriptions, timers, and idempotent command handling when those mechanisms preserve identity, ordering, delivery, and recovery requirements.

## In the Model

A saga can be modeled as an entity-observer: it has state and history, observes events, interprets them relative to a process boundary, and emits commands or endogenous process events.

In a [[Weak Isolation Patterns|weak isolation]] context, compensating actions are asynchronous and eventual. A compensation is not an inverse database update that restores a globally isolated past. It is a new command, transition, or process step whose effect may arrive later, fail, retry, be observed by other participants, and require its own idempotency, ordering, and recovery semantics.

ARIES is useful as a contrast point. A database transaction log can support undo, redo, and partial rollback inside one storage engine's transaction boundary. Its Compensation Log Records record undo actions so recovery can repeat history safely and avoid undoing the same action twice. A saga log or process history supports recovery across multiple boundaries, but its compensating steps are semantic forward actions, not storage-engine undo records or ARIES-style Compensation Log Records.

## Failure Modes

The pattern fails when the process boundary is implicit, when compensation is assumed to be an inverse transition, when retry and idempotency are ignored, or when execution recovery is mistaken for business recovery. Durable execution can keep saga code running; it does not decide whether the business should compensate, continue, pause, or accept a partial outcome.

## External References

- Hector Garcia-Molina and Kenneth Salem, [Sagas](https://www.cs.princeton.edu/techreports/1987/070.pdf), Princeton CS-TR-070-87, 1987.
- C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, and Peter Schwarz, [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging](https://web.stanford.edu/class/cs345d-01/rl/aries.pdf), ACM Transactions on Database Systems, 17(1):94-162, March 1992.

Related concepts: [[Process Managers|process managers]], [[Sagas and Process Managers|sagas and process managers]], [[Orchestration and Choreography|orchestration and choreography]], [[Processes|processes]], [[Coordination|coordination]], [[Weak Isolation Patterns|weak isolation patterns]], [[Weak Isolation Patterns as Architecture Practice|weak isolation patterns as architecture practice]], [[ACID]], [[Write-Ahead Logging|write-ahead logging]], [[Durable Execution|durable execution]], [[Observer|observer]], [[Entity|entity]], [[Command|command]], [[Event|event]], [[Idempotency|idempotency]], [[Ordering|ordering]], [[Retry|retry]], [[Recovery|recovery]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Trace and Feedback|trace and feedback]].
