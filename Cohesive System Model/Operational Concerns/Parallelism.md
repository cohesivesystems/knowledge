---
realm: Operational Concerns
kind: operational-concern
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Physical Parallelism
  - Observational Parallelism
---

# Parallelism

Parallelism describes overlapping execution of work on distinct execution resources at a declared boundary.

The resources may be CPU cores, hardware threads, worker processes, accelerators, devices, machines, or independently executing distributed participants. Merely creating several OS threads does not establish physical parallelism if one core time-slices them. Conversely, application code using one OS thread may interact with storage, network, device, or remote work that progresses in physical parallel beyond the application-thread boundary.

## Physical and observational parallelism

**Physical parallelism** means that execution intervals actually overlap on distinct resources at the boundary being described.

**Observational parallelism** means that a higher-level observer sees independently progressing work and cannot distinguish the realization from physical parallel execution using the observations exposed at that boundary. The lower realization may instead use temporal multiplexing on one resource.

This correspondence can be expressed as a projection:

```text
project : LowerExecutionTrace -> HigherProcessTrace
```

Cooperative interleaving, preemptive interleaving, and physical parallel execution may project to the same higher trace when they preserve declared causality, branch identity, join behavior, observations, outcomes, and progress guarantees. The apparent parallelism is then a valid abstraction, not a claim that lower-level instructions execute simultaneously.

The correspondence fails when the higher contract depends on physical overlap. Minimum completion time, aggregate CPU throughput, simultaneous sampling, interaction with distinct physical resources, or another timing- or capacity-sensitive guarantee cannot be justified by single-resource multiplexing alone.

## Temporal multiplexing

Temporal multiplexing realizes [[Concurrency|concurrent]] logical work by alternating execution intervals on a shared resource. Cooperative scheduling changes work at completion, blocking, yield, or await points. Preemptive scheduling may interrupt a running unit at scheduler-controlled points.

With one OS thread, a runtime can preemptively multiplex green threads, fibers, or logical tasks only if it provides a user-level preemption mechanism. With several OS threads on one CPU core, the operating system can preemptively time-slice those threads. In both cases lifetimes overlap and several tasks make progress over an interval, but only one unit executes on that resource at any instant.

Preemption can expose race conditions and harmful interleavings even without physical parallelism because shared state may be observed between steps that one task expected to keep adjacent. Cooperative execution usually admits fewer interruption points, but neither form removes the need to state atomicity and synchronization boundaries.

## Relationship to concurrency

Concurrency supplies logical scheduling freedom: the model does not establish an order between selected occurrences or branches. Parallelism is one possible execution strategy for exploiting that freedom. Physical parallelism is not required to realize a concurrent structure: interleaved execution can preserve its branch, dependency, and join rules.

A realization may also introduce internal parallelism beneath one logically ordered step, provided the step's external dependency, observation, and completion meanings remain unchanged. Parallelism claims must therefore name both the logical unit and the physical resource boundary.

[[Fork and Join|Fork and join]] commonly exposes concurrent branches that may be interleaved, multiplexed preemptively, executed simultaneously, or distributed. The fork-join graph remains stable across those choices when the realization preserves its dependency and join rules.

## Modeling checks

- Which execution intervals and resources are claimed to overlap?
- Is the claim physical or only observational at the stated boundary?
- Which lower scheduling and context-switch events are hidden by the higher projection?
- What causal, ordering, fork, join, result, and progress properties must every realization preserve?
- Does any timing, throughput, or simultaneous-observation guarantee require actual physical overlap?
- Where can preemption introduce additional observable interleavings?

Related concepts: [[Concurrency|concurrency]], [[Fork and Join|fork and join]], [[Scheduling|scheduling]], [[Runtimes|runtimes]], [[Compute|compute]], [[Ordering|ordering]], [[Causality|causality]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Progress Conditions|progress conditions]], [[Scalability|scalability]], [[Locality|locality]], [[Isolation|isolation]], [[Boundaries|boundaries]], [[Observer|observer]], [[Realization|realization]].

## Formal relations

- `qualifies`: [[Concurrency]] — States how logically incomparable work may exhibit overlapping progress or simultaneous execution at a declared execution-resource boundary without making physical parallelism part of the logical definition.
