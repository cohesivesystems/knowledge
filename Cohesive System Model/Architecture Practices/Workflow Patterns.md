---
realm: Architecture Practices
kind: reference
created: 2026-07-28
updated: 2026-07-29
aliases:
  - Workflow Pattern Language
  - Workflow Patterns Initiative
---

# Workflow Patterns

Workflow Patterns is a research-based collection of recurring capabilities and problems in process-aware information systems and workflow languages. Its principal perspectives are control flow, data, resource assignment, exception handling, and event-log imperfections.

## Cohesive Correspondence

| Workflow perspective | Cohesive correspondence |
| --- | --- |
| Control-flow patterns | [[Process Graphs\|process-graph]] sequencing, choice, concurrency, synchronization, merge, cancellation, recurrence, and completion structure |
| Data patterns | [[Value\|values]], [[Observation\|observations]], process coordination state, [[Shape\|shapes]], input/output placement, and [[Flow Views\|flow views]] |
| Resource patterns | [[Observer Models\|observer models]], [[Authority\|authority]], [[Scheduling\|scheduling]], [[Arbitration\|arbitration]], work assignment, people, agents, and [[Runtimes\|runtimes]] |
| Exception-handling patterns | Timeout, cancellation, retry, compensation, [[Recovery\|recovery]], escalation, and terminal process outcomes |
| Event-log imperfection patterns | [[Observability and Provenance\|observability and provenance]], missing or ambiguous evidence, ordering, correlation, and process-mining data quality |

Workflow [[Control Flow|control flow]] means branch, token, and process progression. It is distinct from EIP's [[Interaction Control Flow|interaction control flow]], which identifies the active driver of a distributed interaction. One workflow edge may lower into several push, pull, queue, driver, call, timer, or shared-state interactions.

The catalog is especially useful for assessing whether a process language or [[Workflow Engines|workflow engine]] can express required structures. Structural support is not sufficient realization evidence: durable joins, waits, cancellation, exclusive signal consumption, late input, recovery, and migration require explicit operational semantics.

Workflow-net soundness provides a complementary verification view over [[Deadlock and Livelock|deadlocks and livelocks]], unreachable activities, and proper completion. The result applies to the modeled control-flow net; external interaction failures, runtime capacity, delivery, and recovery still require separate operational claims.

## Boundary of Adoption

A workflow pattern does not define the domain purpose or authority of a [[Process|process]]. Exclusive Choice supplies branch structure; it does not decide which domain policy may choose a branch. Multiple Instances supplies cardinality structure; it does not identify the business subjects or completion meaning. Resource assignment supplies a work-allocation shape; it does not grant domain authority merely because a worker is scheduled.

## External References

- Workflow Patterns Initiative, [Workflow Patterns](http://www.workflowpatterns.com/).
- Workflow Patterns Initiative, [Control-Flow Patterns](http://www.workflowpatterns.com/patterns/control/).
- Wil M. P. van der Aalst, Arthur H. M. ter Hofstede, Bartek Kiepuszewski, and Alistair P. Barros, [Workflow Patterns](https://doi.org/10.1023/A:1022883727209), *Distributed and Parallel Databases* 14:5-51, 2003.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Process Theories|process theories]], [[Process|process]], [[Process Graphs|process graphs]], [[Control Flow|control flow]], [[Flow Views|flow views]], [[Interaction Control Flow|interaction control flow]], [[Deadlock and Livelock|deadlock and livelock]], [[Workflow Engines|workflow engines]], [[Durable Execution|durable execution]], [[Scheduling|scheduling]], [[Arbitration|arbitration]], [[Authority|authority]], [[Recovery|recovery]], [[Observability and Provenance|observability and provenance]].
