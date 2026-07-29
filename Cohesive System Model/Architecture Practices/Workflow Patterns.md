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

Workflow Patterns is a research-based pattern language for recurring requirements in process-aware information systems and workflow languages. The original catalog identifies twenty implementation-independent control-flow patterns. The broader initiative also catalogs data, resource assignment, exception handling, and event-log imperfections.

## Cohesive Correspondence

The control-flow patterns describe how enabled work proceeds, branches, joins, repeats, completes, or is withdrawn within a [[Process Graphs|process graph]]. Their distinctions become operational obligations when a process structure is realized.

| Pattern family | Representative workflow patterns | Cohesive correspondence and operational boundary |
| --- | --- | --- |
| Sequencing | Sequence | A process-graph precedence relation constrains [[Control Flow\|control flow]] and [[Causality\|causality]]. A realization must preserve activation and completion order without implying that both activities share one thread, host, or transaction. |
| Branching | Parallel Split, Exclusive Choice, Multi-Choice | A process graph introduces concurrency or [[Nondeterminism and Choice\|choice]]. The model must state who evaluates a guard or makes a choice, whether exactly one or any nonempty subset of branches is selected, and which branch activations occurred. |
| Joining and synchronization | Synchronization, Simple Merge, Synchronizing Merge, Multi-Merge, Discriminator | A join must distinguish waiting for every branch, waiting only for branches actually activated, continuing once for one exclusive arrival, continuing once per arrival, and continuing after the first arrival while suppressing the rest until reset. These choices determine [[Ordering\|ordering]], progress, duplicate activation, and [[Deadlock and Livelock\|deadlock]] behavior. |
| Multiple instances | Multiple Instances without Synchronization; with a Priori Design-Time Knowledge; with a Priori Run-Time Knowledge; without a Priori Run-Time Knowledge | Repeated instances require an [[Identity\|identity]] and cardinality rule, an interval during which new instances may be created, and an explicit completion or synchronization condition. Realizations must define [[Scheduling\|scheduling]], [[Concurrency Control\|concurrency control]], correlation, and cancellation per instance and for the collection. |
| State-sensitive routing | Deferred Choice, Interleaved Parallel Routing, Milestone | Routing depends on [[State\|state]] or interaction with an [[Observer\|observer]], rather than only on a locally evaluated guard. A realization must preserve exclusive signal consumption, eligibility windows, mutual exclusion, and the authority to resolve the route. |
| Iteration | Arbitrary Cycles | A process graph may revisit earlier structure without a syntactically nested loop. Its realization must preserve recurrence identity, exit conditions, progress, and [[Fairness\|fairness]] without creating untracked work. |
| Termination | Implicit Termination | A process instance completes when no work remains enabled or active. The boundary must say which activities, instances, waits, signals, and child processes count toward completion; runtime quiescence alone does not establish semantic completion. |
| Cancellation | Cancel Activity, Cancel Case | Cancellation withdraws one activity or the remaining work of a process instance. It requires a declared scope and [[Authority\|authority]], propagation rules, treatment of in-flight effects, and [[Recovery\|recovery]] behavior; stopping execution does not undo an effect already committed. |

Workflow [[Control Flow|control flow]] means branch, token, and process progression. It is distinct from EIP's [[Interaction Control Flow|interaction control flow]], which identifies the active driver of a distributed interaction. One workflow edge may lower into several push, pull, queue, driver, call, timer, or shared-state interactions.

The distinctions among patterns are substantive. Parallel Split differs from Multi-Choice because one activates every branch while the other selects a subset. Synchronization, Synchronizing Merge, Multi-Merge, and Discriminator respond differently to activated branches and arriving completions. Exclusive Choice resolves a modeled decision; Deferred Choice allows the operating environment to resolve the route through the first accepted event.

The catalog is therefore useful for assessing whether a process language or [[Workflow Engines|workflow engine]] can express required structures. Structural support is not sufficient realization evidence: durable joins, waits, cancellation, exclusive signal consumption, late input, recovery, and migration require explicit operational semantics.

### Beyond Control Flow

The initiative's other catalogs qualify the same process structures from additional perspectives. Data patterns distinguish the visibility, interaction, transfer, and routing of [[Value|values]] and [[Observation|observations]]. Resource patterns distinguish allocation, offer, start, delegation, and work distribution among observer models, people, agents, and runtimes. Exception-handling patterns describe how failures interrupt and recover activities or process instances. Event-log imperfection patterns identify missing, duplicated, disordered, imprecise, or incorrectly correlated evidence used to reconstruct process behavior. These are corresponding concerns, not alternate names for the control-flow patterns.

Workflow-net soundness provides a complementary verification view over [[Deadlock and Livelock|deadlocks and livelocks]], unreachable activities, and proper completion. The result applies to the modeled control-flow net; external interaction failures, runtime capacity, delivery, and recovery still require separate operational claims.

## Boundary of Adoption

A workflow pattern does not define the domain purpose or authority of a [[Process|process]]. Exclusive Choice supplies branch structure; it does not decide which domain policy may choose a branch. Multiple Instances supplies cardinality structure; it does not identify the business subjects or completion meaning. Resource assignment supplies a work-allocation shape; it does not grant domain authority merely because a worker is scheduled.

## External References

- Workflow Patterns Initiative, [Workflow Patterns](http://www.workflowpatterns.com/).
- Workflow Patterns Initiative, [Control-Flow Patterns](http://www.workflowpatterns.com/patterns/control/).
- Wil M. P. van der Aalst, Arthur H. M. ter Hofstede, Bartek Kiepuszewski, and Alistair P. Barros, [Workflow Patterns](https://doi.org/10.1023/A:1022883727209), *Distributed and Parallel Databases* 14:5-51, 2003.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Process Theories|process theories]], [[Process|process]], [[Process Graphs|process graphs]], [[Control Flow|control flow]], [[Flow Views|flow views]], [[Interaction Control Flow|interaction control flow]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Causality|causality]], [[Identity|identity]], [[State|state]], [[Observer|observer]], [[Deadlock and Livelock|deadlock and livelock]], [[Ordering|ordering]], [[Concurrency Control|concurrency control]], [[Fairness|fairness]], [[Workflow Engines|workflow engines]], [[Durable Execution|durable execution]], [[Scheduling|scheduling]], [[Arbitration|arbitration]], [[Authority|authority]], [[Recovery|recovery]], [[Observability and Provenance|observability and provenance]].
