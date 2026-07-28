---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-27
tags:
---

# Command

A command is the interpretation of an [[Event|event]] by a given [[Observer|observer]] as an attempted [[Transition|transition]] of a target subject.

Relative to the interpreting observer, the event is an exogenous input event. Relative to the emitter, the carried event is an endogenous output event. These are boundary-relative roles: the event does not intrinsically contain a command, and the emitter does not determine how another observer will interpret it.

All inputs to an operation are modeled as input events subject to interpretation. They become commands only when an observer interprets them as attempted transitions for a target subject.

Command interpretation proceeds as follows:

```txt
Endogenous output event at an emitter boundary
  -> exogenous input event at an interpreting observer boundary
  -> attempted transition, relative to the observer and target subject
  -> validation against current entity state, required observations, invariants, policies, authority, and expected version
  -> typed applied, no-change, alternate, conflict, or rejection outcome
```

Commands are not mere messages. They are interpretations made relative to:

- The specific [[Observer|observer]], its [[Boundaries|boundary]] and its current view of state.
- [[Authority]], [[Invariant|invariants]], and [[Policy|policies]].
- The intended transition.
- An optional expected [[Version|version]] or etag.

A command's expected version is a claim carried by the input event, ordinarily based on the emitter's observation of entity state when it formed its request. The receiving observer decides whether that claim is relevant and validates it before accepting the transition and advancing the entity version.

An emitter may express command intent through a target identity, operation name, schema, expected version, or other protocol data. The exogenous event still does not become a command by structure or sender-assigned label alone. It becomes a command only when the receiving observer interprets it as a requested transition for a subject in a specific context.

When the emitter expects a later response, the emission may be modeled as a request [[Effect|effect]]. The request obligation belongs to the emitter's intent and continuation; command interpretation belongs to the receiving observer. Neither relation requires synchronous interaction, and the request is not an event subtype.

A [[Query|query]] is the corresponding observer-relative interpretation of input as a request to observe, compute, or return information without requesting a modeled semantic state transition.

In [[CQRS]], commands belong to the write side: they are interpreted against the authoritative model and may commit transitions that later become visible to [[Query|queries]] through projections, read models, or other reconstitution paths.

Related concepts: [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[Query|query]], [[CQRS]], [[Observer|observer]], [[Authority|authority]], [[Boundaries|boundaries]], [[Entity|entity]], [[Transition|transition]], [[Version|version]], [[Effect|effect]], [[Effects]], [[Interaction|interaction]], [[Concurrency Control|concurrency control]], [[Monads Monoids and Duals|monads monoids and duals]], [[Adjunctions|adjunctions]].
