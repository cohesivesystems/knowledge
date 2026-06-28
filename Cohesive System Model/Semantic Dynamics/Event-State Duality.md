---
realm: Semantic Dynamics
---

# Event-State Duality

Event-state duality is an instance of [[Duality and Symmetry]]: the relationship between two views of [[Behavior]]:

- [[Event|Events]] emphasize occurrence, ordering, causality, and change.
- [[State|States]] emphasize information, condition, continuity, and samples or cuts through behavior.

The duality is not an isomorphism. Event schedules and state histories are mutually informative, but they are not interchangeable artifacts. Event histories can preserve intent, causality, source, and decision context that state samples do not. Different event histories can also converge to the same state.

## Operational Transforms

Events can be folded, integrated, scanned, or applied by an [[Observer]] to produce state samples or behavior:

```txt
event schedule + initial state + accumulation function -> state history or behavior
```

State can be observed for differences, transitions, threshold crossings, or samples that produce events:

```txt
state history + observer + detection function -> event schedule
```

Both transforms are model-dependent. They depend on the observer, boundary, accumulation or detection function, available observations, and the semantic purpose of the model.

## Sequential Histories

For a sequential [[Entity]], the state history is linear:

```txt
apply: State x Event -> State

s1 = apply(s0, e1)
s2 = apply(s1, e2)
s3 = apply(s2, e3)
```

In this case, state at [[Version]] `V` is the result of applying the endogenous event that produced version `V`.

## Non-Sequential Histories

Not all state histories are sequential. A system such as Git has a non-linear state history with parent links, branch heads, and merges. In such systems, state histories may be directed acyclic graphs, partial orders, or other non-linear structures.

Concurrency control must match the history shape. A linear entity can use expected-version checks to ensure one successor from a current version. A non-sequential history may instead ask whether proposed successors have acceptable parents, whether references may advance, and whether concurrent heads should be rejected, merged, or preserved.

## External References

- Vaughan R. Pratt, [Event-State Duality: The Enriched Case](https://boole.stanford.edu/pub/concur02.pdf), CONCUR 2002. [Springer entry](https://link.springer.com/chapter/10.1007/3-540-45694-5_3)

Related concepts: [[Duality and Symmetry]], [[Event]], [[State]], [[Behavior]], [[Entity]], [[Version]], [[Observer]], [[Boundaries]], [[Concurrency Control]].
