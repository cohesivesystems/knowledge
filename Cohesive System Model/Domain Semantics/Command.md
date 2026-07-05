---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-01
tags:
---

# Command

A command is an observer-relative interpretation of an input event as an attempted [[Transition|transition]].

All inputs to an operation are modeled as input [[Event|events]] subject to interpretation. They become commands only when an [[Observer|observer]] interprets them as attempted transitions for a target subject.

Command interpretation proceeds as follows:

```txt
Exogenous event
  -> input event at an observer boundary
  -> command intent, relative to the observer and target subject
  -> validation against current entity state, required observations, invariants, policies, authority, and expected version
  -> accepted transition | nil | rejection
```

Commands are not mere messages. They are interpretations made relative to:

- The specific [[Observer|observer]], its [[Boundaries|boundary]] and its current view of state.
- Authority, [[Invariants|invariants]], and [[Policies|policies]].
- The intended transition.
- An optional expected [[Version|version]] or etag.

A command's expected version is the version of entity state the observer believed was current when it formulated the command. The transition runtime checks that expectation before accepting the transition and advancing the entity version.

An exogenous event does not become a command by structure alone. It becomes a command only when interpreted as a requested transition for a subject in a specific context.

A [[Query|query]] is the corresponding observer-relative interpretation of input as a request to observe, compute, or return information without requesting a modeled semantic state transition.

In [[CQRS]], commands belong to the write side: they are interpreted against the authoritative model and may commit transitions that later become visible to [[Query|queries]] through projections, read models, or other reconstitution paths.

Related concepts: [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[Query|query]], [[CQRS]], [[Observer|observer]], [[Boundaries|boundaries]], [[Entity|entity]], [[Transition|transition]], [[Version|version]], [[Concurrency Control|concurrency control]], [[Monads Monoids and Duals|monads monoids and duals]], [[Adjunctions|adjunctions]].
