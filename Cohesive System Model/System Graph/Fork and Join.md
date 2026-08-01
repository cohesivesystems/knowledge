---
realm: System Graph
kind: structural-construct
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Fork-Join
  - Fork Join
  - Fork-Join Structure
---

# Fork and Join

Fork and join are paired process-graph structures that expand one continuation into several branch activations and later synchronize selected branch completions into a continuation.

The pairing is a structural duality: a fork is one-to-many decomposition or activation, while a join is many-to-one synchronization and recomposition. It is not an assertion that every fork must execute branches simultaneously or that every join combines carried values.

For two branches `A` and `B`, the basic dependency shape is:

```text
fork < A < join
fork < B < join
```

The graph establishes no `A < B` or `B < A` edge unless the branch definitions add one. Their relevant occurrences are therefore [[Concurrency|concurrent]] relative to this process relation. The join reintroduces order by making the continuation depend on the completions selected by its join rule.

## Fork semantics

A fork must identify which branches are enabled, how each branch is identified, and which inputs, tokens, observations, or values each branch receives. Activating all branches differs from selecting a subset through choice. Copying one control token differs from splitting a composite value, and distributing requests differs from assigning their execution resources.

Forked branches may share a predecessor while retaining different participants, authority, failure boundaries, deadlines, and effects. Lack of branch order does not prove that the branches commute or that they cannot conflict over shared state or invariants.

## Join semantics

A control-flow join determines which branch completions are required before the continuation becomes enabled. Common rules include waiting for all activated branches, an explicitly selected subset, a quorum, the first accepted completion, or one completion per arriving branch. The rule must define treatment of branches that fail, time out, are cancelled, were never enabled, or complete after the join has advanced.

A value aggregation or reduction is related but distinct. It combines branch results into a value for the enclosing computation. A control-flow join may discard results, while an aggregator may combine asynchronous values without representing a task continuation.

When result combination can observe arrival order, different schedules may produce different results. A portable graph must therefore declare a stable reduction order, require an order-insensitive operation such as an appropriate commutative and associative combine, or admit the resulting [[Nondeterminism and Choice|nondeterminism]].

## Realization correspondence

The same fork-join structure may be realized by:

- cooperative async tasks interleaved on one thread;
- preemptively multiplexed tasks or threads on one execution resource;
- physically [[Parallelism|parallel]] workers on several resources;
- actors, workflow activations, device operations, or distributed participants.

The realization must preserve branch identity, logical dependencies, the completion set, result-combination rule, cancellation and failure meanings, and whether completion order is observable. Scheduler selections, context switches, worker placement, and thread identity remain lower-level facts unless the process boundary exposes them.

Durable fork-join additionally requires persistent active-branch and completion state. A join that waits for a branch that was never enabled or can no longer complete creates a structural workflow deadlock rather than merely a slow runtime wait.

## Modeling checks

- Which branches are enabled, and which occurrences remain unordered?
- Is the fork splitting control, values, work, or interactions?
- Which branch completions satisfy the join?
- Does the join only synchronize control, or also combine results?
- How are failure, cancellation, timeout, late completion, and duplicate completion handled?
- Is result or completion order observable, fixed, order-insensitive, or nondeterministic?
- Which fork, join, and branch state must survive interruption?

Related concepts: [[Process|process]], [[Process Graphs|process graphs]], [[Control Flow|control flow]], [[Concurrency|concurrency]], [[Parallelism|parallelism]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Flow Operators|flow operators]], [[Workflow Patterns|workflow patterns]], [[Ordering|ordering]], [[Causality|causality]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Scheduling|scheduling]], [[Deadlock and Livelock|deadlock and livelock]], [[Recovery|recovery]], [[Runtimes|runtimes]], [[Workflow Engines|workflow engines]], [[Boundaries|boundaries]].

## Formal relations

- `arranges`: [[Process]] — Gives a semantic process explicit branch activation, concurrent progression, synchronization, and continuation structure without selecting its runtime realization.
