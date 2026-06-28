---
realm: Principles
kind: principle
---

# Algebras And Coalgebras

Algebras and coalgebras provide complementary ways to model construction and behavior.

An algebra consumes structure into a value:

```txt
F A -> A
```

A coalgebra unfolds a value into observable structure or next behavior:

```txt
A -> F A
```

## Algebras

Algebras are useful for folds, accumulation, interpretation, and summarization.

Examples:

- Folding committed [[Event|events]] into [[State]] samples.
- Accumulating observations into a projection.
- Interpreting a command value into a transition decision.
- Reducing validation results into accept, reject, or nil.

## Coalgebras

Coalgebras are useful for behavior, observation, transition systems, and processes that expose next steps.

Examples:

- A state machine exposing possible next transitions.
- A process exposing its next required input, timeout, or command.
- A behavior exposing current value and future evolution.
- An observer exposing what it can observe, emit, or request next.

Algebras and coalgebras are connected to [[Event-State Duality]]. Folding events into state is algebraic. Observing state for possible events or future behavior is coalgebraic. Neither side fully replaces the other.

Related concepts: [[Behavior]], [[Event-State Duality]], [[Event]], [[State]], [[Transition]], [[Observer]], [[Processes]], [[Duality and Symmetry]].
