---
realm: Architecture Practices
kind: reference
created: 2026-06-24
updated: 2026-07-04
---

# Sagas and Process Managers

This note connects the dedicated entries for [[Sagas|sagas]] and [[Process Managers|process managers]].

The concepts should not be collapsed. A [[Process Managers|process manager]] is the broader orchestration role: it gives a [[Process|process]] identity, records progress or history, observes inputs, decides next steps, and emits commands or events across boundaries. A [[Sagas|saga]] is a type of process manager specialized for business recovery and compensation.

[[Durable Execution Engines|Durable execution engines]] can also occupy the process-manager role when they own and advance process execution state. Their defining concern is execution recovery: continuing the same logical computation after interruption. A saga's defining concern is domain-level recovery: deciding how the domain process should proceed when the world no longer matches the original path.

The broader coordination distinction is described in [[Orchestration and Choreography|orchestration and choreography]]. Process managers are the orchestration form. Choreography coordinates a process through participant-local rules over shared messages, events, logs, or protocols without one explicit process manager controlling the whole execution.

Related concepts: [[Sagas|sagas]], [[Process Managers|process managers]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Graphs|process graphs]], [[Coordination|coordination]], [[Weak Isolation Patterns|weak isolation patterns]], [[Durable Execution|durable execution]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Recovery|recovery]], [[Idempotency|idempotency]], [[Ordering|ordering]].
