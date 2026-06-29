---
realm: Architecture Practices
kind: pattern
---

# Sagas and Process Managers

Sagas and process managers address the problem of coordinating long-running, multi-step work across boundaries where one atomic transaction is unavailable or inappropriate.

## Cohesive Formulation

The sagas practice is about [[Processes]], [[Coordination]], and sometimes [[Durable Execution]]:

- A process has identity, state, progress, and recovery behavior.
- It observes events or signals.
- It emits commands to participants.
- It may compensate, retry, time out, or escalate.

Sagas and process managers can be implemented without a workflow engine, but they still need explicit persistence, recovery, idempotency, and delivery semantics when they are expected to survive failure or long delays.

## Practice Interpretation

A saga can be modeled as an entity-observer: it has state and history, observes events, interprets them relative to a process boundary, and emits commands or endogenous process events.

In a [[Weak Isolation Patterns|weak isolation]] context, compensating actions are asynchronous and eventual. A compensation is not an inverse database update that restores a globally isolated past. It is a new command, transition, or process step whose effect may arrive later, fail, retry, be observed by other participants, and require its own idempotency, ordering, and recovery semantics.

## Failure Modes

The pattern fails when the process boundary is implicit, when compensation is assumed to be inverse transition, or when delivery and idempotency are ignored. Sagas do not remove consistency problems; they make consistency procedural and temporal.

## External References

- Hector Garcia-Molina and Kenneth Salem, [Sagas](https://www.cs.princeton.edu/techreports/1987/070.pdf), Princeton CS-TR-070-87, 1987.

Related concepts: [[Processes]], [[Coordination]], [[Weak Isolation Patterns]], [[Weak Isolation Patterns as Architecture Practice]], [[Durable Execution]], [[Observer]], [[Entity]], [[Command]], [[Event]], [[Idempotency]], [[Ordering]], [[Retry]], [[Recovery]], [[Workflow Engines]], [[Durable Execution Engines]], [[Trace and Feedback]].
