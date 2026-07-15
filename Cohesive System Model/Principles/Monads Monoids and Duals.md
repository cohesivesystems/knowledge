---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-07-15
---

# Monads Monoids and Duals

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

### Nondeterminism Monads

[[Nondeterminism and Choice|Nondeterministic]] computations illustrate why the particular monad matters:

- A list monad represents ordered enumeration with multiplicity.
- A powerset monad represents extensional alternatives where order and duplicates are forgotten.
- A multiset monad retains multiplicity without presentation order.
- A discrete distribution monad represents weighted outcomes.
- The Giry monad extends probabilistic computation to probability measures on measurable spaces.
- A lazy stream or logic monad can expose potentially infinite search and its fairness behavior.

The choice operation can separately be associative, commutative, idempotent, or none of these beyond the laws explicitly supplied. Monad associativity governs rebracketing of sequencing; it does not imply commutativity of independent effects or [[Reduction, Evaluation, and Confluence|confluence]] of evaluation paths.

## Comonads

A comonad is the dual pattern: it emphasizes context, observation, extraction, and context-dependent transformation:

```txt
extract : W A -> A
extend : W A -> (W A -> B) -> W B
```

Comonad-like structure appears when values are interpreted with surrounding context, such as observations, windows over streams, state plus neighborhood, or an observer's view of a boundary.

These structures are not naming decorations. They matter when the model needs laws: associativity, identity, sequencing coherence, context preservation, or lawful extraction.

## External References

- Eugenio Moggi, [Notions of Computation and Monads](https://doi.org/10.1016/0890-5401(91)90052-4), *Information and Computation* 93(1):55-92, 1991.
- Michèle Giry, [A Categorical Approach to Probability Theory](https://doi.org/10.1007/BFb0079007), in *Categorical Aspects of Topology and Analysis*, 1982.

Related concepts: [[Programming Paradigms|programming paradigms]], [[Functional Programming|functional programming]], [[Relational and Logic Programming|relational and logic programming]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Behavior|behavior]], [[Observation|observation]], [[Observer|observer]], [[Event|event]], [[Transition|transition]], [[Projection Models|projection models]], [[Duality and Symmetry|duality and symmetry]], [[Compositionality|compositionality]].
