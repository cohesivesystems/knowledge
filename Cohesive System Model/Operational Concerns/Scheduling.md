---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-15
updated: 2026-07-15
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

A randomized scheduler instead returns a distribution over enabled actions. A distributed scheduler can consist of several local policies and arbitration points rather than one observer with a global view.

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

Related concepts: [[Nondeterminism and Choice|nondeterminism and choice]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Authority|authority]], [[Ordering|ordering]], [[Causality|causality]], [[Consistency Models|consistency models]], [[Progress Conditions|progress conditions]], [[Safety and Liveness|safety and liveness]], [[Rate Limiting|rate limiting]], [[Interaction|interaction]], [[Process|process]], [[Observer|observer]], [[Actor Systems|actor systems]], [[Runtimes|runtimes]], [[Compute|compute]], [[Workflow Engines|workflow engines]], [[Realization|realization]].
