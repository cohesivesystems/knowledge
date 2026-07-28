---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-27
tags:
---

# Command

A command is the interpretation of an [[Event|event]] by a given [[Observer|observer]] as an attempted [[Transition|transition]] of a target subject.

Relative to the interpreting observer, the event is an exogenous input event. Relative to the emitter, the carried event is an endogenous output event. These are boundary-relative roles. The carried value and interaction contract may explicitly express command intent, but the emitter does not compel another observer's semantic interpretation.

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

An emitter may express command intent through a target identity, operation name, schema, expected version, or other protocol data. When a message contract carries singular intent toward an understood observer, command interpretation is the expected interpretation and may be operationally unambiguous. The semantic command nevertheless remains observer-relative: the receiver admits and interprets the input as a requested transition for a subject in a specific context and may reject, ignore, or classify an invalid input without accepting the transition.

When the emitter expects a later response, the emission may be modeled as a request [[Effect|effect]]. The request obligation belongs to the emitter's intent and continuation; command interpretation belongs to the receiving observer. Neither relation requires synchronous interaction, and the request is not an event subtype.

A [[Query|query]] is the corresponding observer-relative interpretation of input as a request to observe, compute, or return information without requesting a modeled semantic state transition.

In [[CQRS]], commands belong to the write side: they are interpreted against the authoritative model and may commit transitions that later become visible to [[Query|queries]] through projections, read models, or other reconstitution paths.

## External References

- Gregor Hohpe and Bobby Woolf, [Command Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[Query|query]], [[CQRS]], [[Observer|observer]], [[Authority|authority]], [[Boundaries|boundaries]], [[Entity|entity]], [[Transition|transition]], [[Version|version]], [[Effect|effect]], [[Effects]], [[Messages and Envelopes|messages and envelopes]], [[Interaction|interaction]], [[Concurrency Control|concurrency control]], [[Monads Monoids and Duals|monads monoids and duals]], [[Adjunctions|adjunctions]].
