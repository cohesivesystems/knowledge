---
realm: Principles
kind: principle
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Logical Concurrency
  - Concurrent Occurrences
---

# Concurrency

Concurrency is the boundary-relative absence of an established ordering between occurrences or enabled work.

For occurrences `a` and `b`, an observer at boundary `B` may treat them as concurrent relative to an ordering relation `<` when neither direction is known or entailed:

```text
concurrent_B(a, b) iff not known_B(a < b) and not known_B(b < a)
```

When the authored dependency relation is complete for the boundary, this is structural incomparability: the model supplies neither an `a < b` path nor a `b < a` path. When an observer has incomplete evidence, it is only absence of ordering knowledge. Unknown order must not be strengthened into proof that no dependency exists outside the observer's view.

[[Happened-Before|Happened-before]] gives a common causal-order instance. Two occurrences are concurrent relative to happened-before when neither happened before the other. Other models may use process precedence, data dependency, version ancestry, interaction, or another declared ordering relation. The relation and boundary must be named because two occurrences may be concurrent in one projection and ordered in a richer one.

## Concurrency and independence

Concurrency does not by itself establish semantic independence. Concurrent operations may still contend for one invariant, authority, lock, resource, entity version, effect boundary, or capacity budget. Independence is a stronger claim that relevant variations, reorderings, or compositions do not change the admitted outcome or violate a constraint. Commutativity and [[Reduction, Evaluation, and Confluence|confluence]] can make some concurrent alternatives observationally harmless.

Concurrency also does not imply wall-clock overlap, different threads, or simultaneous execution. A scheduler may serialize or interleave concurrent work while preserving the same logical dependency structure. [[Concurrency Control|Concurrency control]] is the separate concern of admitting, rejecting, serializing, merging, or otherwise reconciling concurrent histories where their effects meet.

## Concurrency, asynchrony, and parallelism

[[Synchrony and Asynchrony|Asynchrony]] and concurrency answer different questions. An asynchronous operation separates its begin and completion occurrences; those occurrences remain causally ordered. Concurrency asks whether distinct occurrences or branches have an established order between them. An async program can therefore be sequential, and a concurrent structure can be executed without an async language feature.

Async programming models make the separation useful by representing logical continuation dependencies without binding each pending operation to a physical thread. An `await` introduces a dependency from completion to continuation. Starting sibling operations before a later join can leave them concurrent when the program introduces no order among them.

[[Parallelism]] is an execution property and a cross-realm correspondence rather than the dual of concurrency. The same concurrent structure may be realized through cooperative interleaving, preemptive temporal multiplexing, simultaneous execution on distinct resources, or distributed execution. These realizations are equivalent only relative to the observations and guarantees preserved at the higher boundary.

## Fork and join

[[Fork and Join|Fork and join]] make concurrency explicit in a process structure. A fork establishes a common predecessor for several branches. The branches are concurrent when the graph establishes no order among their relevant occurrences. A join then establishes dependencies from the required branch completions to a continuation and may separately combine their results.

The join limits the scope of the concurrency: branch work may be incomparable within the forked region while every admitted continuation occurrence follows the completions required by the join rule.

## Modeling checks

- Which observer, boundary, and ordering relation define concurrency?
- Is the relation complete for that boundary, or is ordering merely unknown from partial evidence?
- Which branch or occurrence pairs are incomparable?
- Do incomparable operations share invariants, authority, state, effects, or finite resources?
- Which additional orders may a scheduler, log, sequencer, or runtime introduce without changing meaning?
- Which observations distinguish interleaving from physical parallel execution?

Related concepts: [[Ordering|ordering]], [[Happened-Before|happened-before]], [[Causality|causality]], [[Fork and Join|fork and join]], [[Process Graphs|process graphs]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Parallelism|parallelism]], [[Scheduling|scheduling]], [[Runtimes|runtimes]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Concurrency Control|concurrency control]], [[Isolation|isolation]], [[Boundaries|boundaries]], [[Observer|observer]].
