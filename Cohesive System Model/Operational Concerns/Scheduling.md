---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-15
updated: 2026-08-01
status: draft
aliases:
  - Scheduler
  - Schedulers
---

# Scheduling

Scheduling determines which enabled work receives execution opportunity, in what order, on which resources, and under which priority, fairness, deadline, locality, and capacity rules.

The schedulable unit may be a thread, task, continuation, actor activation, message reception, workflow step, timer, transaction, query fragment, consumer assignment, retry, or maintenance operation. Scheduling is the operational concern; an operating-system scheduler, event loop, actor dispatcher, workflow engine, broker coordinator, or database worker pool is a possible realization.

## Scheduler as Choice Resolver

For a finite execution history `h`, a scheduler can be modeled as selecting an enabled action:

```txt
scheduler : History -> EnabledAction
```

This single-action form describes one execution resource. A scheduler for several resources may instead select a compatible set of enabled actions and map each action to a resource. A randomized scheduler returns a distribution over actions or compatible selections. A distributed scheduler can consist of several local policies and arbitration points rather than one observer with a global view.

[[Nondeterminism and Choice|Nondeterminism]] defines the possible continuations. Scheduling resolves some of that multiplicity into one execution. The model should state which information the scheduler may use; a verification scheduler should not silently inspect hidden future random choices, inaccessible participant state, or facts outside its boundary.

Scheduler classifications include:

- Deterministic or randomized.
- Centralized or distributed.
- Preemptive or cooperative.
- Memoryless or history-dependent.
- Priority-, deadline-, quota-, affinity-, or cost-directed.
- Work-conserving or intentionally reserving capacity.
- Adversarial, policy-directed, or optimization-directed.
- Fair, weakly fair, strongly fair, or explicitly unfair.

## Preemptive and Cooperative Execution

A preemptive scheduler may suspend a running unit at a scheduler-controlled point and give another unit execution opportunity. Under cooperative scheduling, the running unit retains execution until it completes, blocks, or reaches an explicit yield or await. Both forms can multiplex several logical tasks over the same resources, but they admit different interleavings, responsiveness, starvation risks, reentrancy conditions, and assumptions about what can change during an activation.

On one execution resource, preemptive multitasking creates temporal overlap in task lifetimes and can present observational [[Parallelism|parallelism]] to a coarser boundary, but only one task executes there at an instant. This realizes [[Concurrency|concurrency]] through temporal multiplexing rather than physical parallelism. Several OS threads time-sliced on one core and several green threads preemptively multiplexed within one OS thread have different schedulers, but both remain single-resource execution at that boundary.

This is execution control, not the successor relation of [[Control Flow|process control flow]]. Scheduling can decide when a broker poll, callback, handler, or continuation runs; it does not decide whether payment authorization semantically follows inventory reservation. A handler outcome may supply the observation used by an authorized transition or process decision, while the scheduler merely supplied the opportunity to compute it.

## Scheduling Order

Scheduler-selection order is not automatically:

- causal order;
- message reception order;
- operation invocation order;
- execution completion order;
- transaction commit order;
- consensus-log order;
- [[Linearization Points|linearization order]];
- visibility or observation order.

An operation selected first may block, yield, retry, fail, or commit after later work. A consistency proof can assign an abstract order different from the physical schedule when the model permits it. These orderings coincide only when the realization establishes the required correspondence.

## Fairness and Progress

[[Fairness]] constrains how scheduling choices behave over complete executions. A fair scheduler can permit arbitrarily long finite delay while excluding infinite starvation. [[Progress Conditions|Progress conditions]] state who completes under which scheduling, interference, and failure assumptions.

Fairness is not a consistency guarantee. A scheduler can fairly execute operations whose observations violate a [[Consistency Models|consistency model]]. An unfair scheduler can preserve safety while denying liveness by postponing work forever.

## Authority and Resources

Scheduling authority is narrower than domain [[Authority|authority]]. A runtime may be authorized to select which eligible task runs next without being authorized to accept a business transition, choose a process outcome, or commit an external effect.

Scheduling also allocates finite compute, memory, I/O, concurrency slots, and queue capacity. Priority, admission, backpressure, rate limits, cancellation, and resource budgets shape which work remains enabled and whether fairness claims are meaningful.

Priority can also introduce [[Deadlock and Livelock|priority inversion]] when higher-priority work waits on a resource owned by lower-priority work. Priority inheritance or ceiling protocols can change the effective schedule within a declared resource model, but do not grant domain authority or prove end-to-end progress outside that boundary.

## Modeling Checks

- What is the schedulable unit and its boundary?
- Which actions are enabled, blocked, pending, cancelled, or expired?
- What information may the scheduler observe?
- Which priorities, deadlines, quotas, affinities, or resource budgets apply?
- What fairness and starvation guarantees are claimed?
- Which failures or pauses invalidate those guarantees?
- Which schedule order is visible to observers, and which abstract order is used for correctness?
- Does the scheduler select execution opportunity or exercise domain authority?

## External References

- Nissim Francez, [Fairness](https://doi.org/10.1007/978-1-4612-4886-6), especially the treatment of explicit schedulers, Springer, 1986.

Related concepts: [[Queueing Theory|queueing theory]], [[Control Flow|control flow]], [[Interaction Control Flow|interaction control flow]], [[Concurrency|concurrency]], [[Parallelism|parallelism]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Authority|authority]], [[Ordering|ordering]], [[Causality|causality]], [[Consistency Models|consistency models]], [[Progress Conditions|progress conditions]], [[Deadlock and Livelock|deadlock and livelock]], [[Safety and Liveness|safety and liveness]], [[Rate Limiting|rate limiting]], [[Interaction|interaction]], [[Process|process]], [[Observer|observer]], [[Actor Systems|actor systems]], [[Runtimes|runtimes]], [[Compute|compute]], [[Workflow Engines|workflow engines]], [[Realization|realization]].
