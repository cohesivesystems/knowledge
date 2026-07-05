---
realm: Architecture Practices
kind: pattern
aliases:
  - Process Manager
---

# Process Managers

Process managers are an orchestration pattern for coordinating a [[Process|process]] across participants, time, effects, and failure boundaries.

A process manager is a logical coordinating role, not necessarily one permanent physical node. It gives a process identity, records process state or history, observes inputs, decides next steps, emits commands or events, handles timeouts and retries, and decides when the process has completed, failed, compensated, or escalated.

## Cohesive Formulation

In the model, a process manager is an [[Observer|observer]] that may also be modeled as an [[Entity|entity]] when it has identity, durable state, versioned history, or lifecycle transitions of its own.

Process manager responsibilities include:

- Defining the process subject or correlation identity.
- Recording progress, pending work, emitted effects, deadlines, and observed results.
- Deciding which participant should act next.
- Sending commands, signals, or events across [[Boundaries|boundaries]].
- Interpreting replies, events, timeouts, cancellations, and failures.
- Preserving [[Ordering|ordering]], [[Idempotency|idempotency]], delivery, and recovery meanings.
- Deciding completion, rejection, compensation, partial completion, or escalation.

Process managers are the explicit-control side of [[Orchestration and Choreography|orchestration and choreography]]. They are useful when the process needs one logical locus that can observe enough state to direct work and recover progress.

## Relation to Sagas and Durable Execution

A [[Sagas|saga]] is a process manager specialized for business recovery. It decides how a process should proceed when completed business actions cannot simply be retried.

A [[Durable Execution Engines|durable execution engine]] can play the process-manager role when it owns and advances execution state for a process. Its defining concern is execution recovery: restore enough context for the same logical computation to continue. The business policy that decides compensation, alternate paths, partial completion, or human intervention belongs to the process manager or saga logic running on top of that execution substrate.

Not every process manager is a saga, and not every durable execution engine use is a process manager. A durable job runner may resume one task without owning a larger process, while a hand-written event-sourced process manager may coordinate a long-running process without using a full durable execution engine.

## Examples

- A saga orchestrator that reserves inventory, charges payment, arranges shipment, and issues compensating commands when a later step fails.
- An index rebuild coordinator that records covered partitions, assigns work to workers, tracks progress, retries failed ranges, and decides when the rebuild is complete.
- A backfill or migration controller that persists checkpoints, leases work, and prevents stale workers from committing after losing ownership.
- A human approval workflow that records pending approvers, reminders, expiry, escalation, and final acceptance or rejection.
- A durable workflow instance that schedules activities, records signals and timers, and resumes after host failure.

The physical owner can change across failures or leases. What makes the design orchestrated is that one logical role owns process execution state and directs participant work for the run.

## Failure Modes

The pattern fails when the process boundary is implicit, when process state is not durable enough for the claimed recovery behavior, when emitted effects are not idempotent, or when the process manager's view of participant work is mistaken for the business outcome itself.

Related concepts: [[Orchestration and Choreography|orchestration and choreography]], [[Sagas|sagas]], [[Process|process]], [[Processes|processes]], [[Coordination|coordination]], [[Observer|observer]], [[Entity|entity]], [[Durable Execution|durable execution]], [[Durable Execution Engines|durable execution engines]], [[Workflow Engines|workflow engines]], [[Recovery|recovery]], [[Retry|retry]], [[Idempotency|idempotency]], [[Ordering|ordering]], [[Boundaries|boundaries]], [[Business Transactions|business transactions]].
