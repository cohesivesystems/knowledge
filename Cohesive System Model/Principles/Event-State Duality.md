---
realm: Principles
kind: principle
---

# Event-State Duality

Event-state duality is a modeling principle and an instance of [[Duality and Symmetry|duality and symmetry]]: the relationship between two views of [[Behavior|behavior]]:

- [[Event|Events]] emphasize occurrence, ordering, causality, and change.
- [[State|States]] emphasize information, condition, continuity, and samples or cuts through behavior.

The event-state duality relates the semantic constructs [[Event|event]] and [[State|state]], and constrains how the model explains their correspondence.

The duality is not an isomorphism. Event schedules and state histories are mutually informative, but they are not interchangeable artifacts. Event histories can preserve intent, causality, source, and decision context that state samples do not. Different event histories can also converge to the same state.

## Operational Transforms

Events can be folded, integrated, scanned, or applied by an [[Observer|observer]] to produce state samples or behavior:

```txt
event schedule + initial state + accumulation function -> state history or behavior
```

State histories can be compared to derive deltas that an observer may interpret as events:

```txt
state history + observer + detection function -> event schedule
```

Both transforms are model-dependent. They depend on the observer, boundary, accumulation or detection function, available observations, and the semantic purpose of the model.

## Sequential Histories

For a sequential [[Entity|entity]], the state history is linear:

```txt
apply: State x Event -> State

s1 = apply(s0, e1)
s2 = apply(s1, e2)
s3 = apply(s2, e3)
```

In this case, state at [[Version|version]] `V` is the result of applying the endogenous event that produced version `V`.

## Non-Sequential Histories

Not all state histories are sequential. A system such as Git has a non-linear state history with parent links, branch heads, and merges. In such systems, state histories may be directed acyclic graphs, partial orders, or other non-linear structures.

Concurrency control must match the history shape. A linear entity can use expected-version checks to ensure one successor from a current version. A non-sequential history may instead ask whether proposed successors have acceptable parents, whether references may advance, and whether concurrent heads should be rejected, merged, or preserved.

## Philosophical Parallel

Hegel's distinction between being and becoming provides a useful conceptual parallel. [[State]] corresponds loosely to determinate being: what is, relative to a subject, boundary, shape, and point in behavior. [[Event]], [[Transition|transition]], and [[Behavior|behavior]] correspond to becoming: occurrence, change, and the movement by which states become determinate.

The parallel is not a formal identification. In the Cohesive model, state and event remain semantic constructs with observer-relative roles. The useful point is that state is not intelligible apart from the behavior and event histories through which it is determined, while events are not intelligible apart from the states they affect, reveal, or relate.

This also suggests a notion of indeterminate state. An indeterminate state is not necessarily the absence of state. It is a recognized subject, possibility, external process, or pending situation whose relevant dimensions are not yet determined relative to an [[Observer|observer]], [[Boundaries|boundary]], [[Shape|shape]], or [[Version|version]]. Indeterminacy may be epistemic, shape-relative, operational, semantic, or external. State becomes determinate for the model through observation, event interpretation, or a commitment boundary.

Lawvere's categorical discussions of Being and Becoming are related mathematical-philosophical background. They are useful here as orientation toward structure and change, not as replacements for the model's semantic definitions.

## External References

- G. W. F. Hegel, [Book I of *Science of Logic*: Being](https://www.marxists.org/reference/archive/hegel/works/hl/hlbeing.htm).
- F. W. Lawvere, [Some Thoughts on the Future of Category Theory](https://lawverearchives.com/wp-content/uploads/2024/12/1991-some-thoughts-on-the-future-of-category-theory.pdf), 1991.
- Vaughan R. Pratt, [Event-State Duality: The Enriched Case](https://boole.stanford.edu/pub/concur02.pdf), CONCUR 2002. [Springer entry](https://link.springer.com/chapter/10.1007/3-540-45694-5_3)

Related concepts: [[Duality and Symmetry|duality and symmetry]], [[Event|event]], [[State|state]], [[Behavior|behavior]], [[Transition|transition]], [[Entity|entity]], [[Version|version]], [[Observer|observer]], [[Boundaries|boundaries]], [[Shape|shape]], [[Concurrency Control|concurrency control]].
