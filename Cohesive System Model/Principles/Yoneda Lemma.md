---
realm: Principles
kind: principle
---

# Yoneda Lemma

The Yoneda lemma says, roughly, that an object is determined by how it relates to all other objects through maps into or out of it.

For modeling, the practical lesson is:

> To understand a thing, understand how it can be observed, addressed, transformed, related, and used.

This does not mean internal structure is irrelevant. It means that a concept's role in the system is captured by its relationships and interactions, not only by its representation.

Yoneda-style questions:

- What observations can be made of this object?
- What transitions, commands, or events can target it?
- What maps into it or out of it are meaningful?
- Which observers can distinguish it from another object?
- What behavior is preserved across all relevant interactions?

Examples:

- An [[Entity]] is understood through identity, versions, observations, transitions, emitted events, and invariants.
- An [[Observer]] is understood through what it can observe, interpret, receive, emit, route, and commit.
- A [[Boundaries|boundary]] is understood through what crosses it, what it includes, what it excludes, and which guarantees hold inside it.
- A [[Realization]] is understood through the semantic relationships it preserves and the substrate guarantees it exposes.

The Yoneda lemma is a discipline against representation-only definitions. If two things cannot be distinguished by any relevant observation, interaction, transition, or relation within a boundary, then they may be equivalent for that model even if they differ internally.

Related concepts: [[Entity]], [[Observer]], [[Observation]], [[Interaction]], [[Boundaries]], [[Realization]], [[Equivalence vs Equality]].
