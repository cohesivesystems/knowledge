---
realm: Principles
---

# Monads Monoids And Duals

Monads, monoids, and their duals provide recurring patterns for sequencing, accumulation, context, observation, and composition.

## Monoids

A monoid is a type of compositional structure with an identity and associative combination:

```txt
empty : M
combine : M x M -> M
```

Monoids appear when events, observations, logs, effects, partial results, or policies can be accumulated without caring about grouping. Ordering may still matter if the monoid is non-commutative.

Examples:

- Appending event log segments.
- Combining validation results.
- Merging independent telemetry.
- Accumulating projection updates.

## Comonoids

A comonoid is the dual pattern: instead of combining parts into a whole, it supports copying, decomposing, or extracting views from a whole.

Comonoid-like structure appears in observation, context, projection, and fanout:

- Duplicating a value into several observation paths.
- Extracting multiple views from state.
- Broadcasting an event to multiple observers.
- Splitting context into parts needed by different transitions.

## Monads

A monad is a pattern for sequencing computations that produce structured effects:

```txt
pure : A -> M A
bind : M A -> (A -> M B) -> M B
```

Monadic structure appears when operations must be sequenced through effects such as validation, persistence, retries, asynchronous execution, command interpretation, or transition decisions.

## Comonads

A comonad is the dual pattern: it emphasizes context, observation, extraction, and context-dependent transformation:

```txt
extract : W A -> A
extend : W A -> (W A -> B) -> W B
```

Comonad-like structure appears when values are interpreted with surrounding context, such as observations, windows over streams, state plus neighborhood, or an observer's view of a boundary.

These structures are not naming decorations. They matter when the model needs laws: associativity, identity, sequencing coherence, context preservation, or lawful extraction.

Related concepts: [[Behavior]], [[Observation]], [[Observer]], [[Event]], [[Transition]], [[Projections]], [[Duality and Symmetry]], [[Compositionality]].
