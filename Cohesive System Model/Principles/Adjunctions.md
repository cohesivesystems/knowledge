---
realm: Principles
kind: principle
---

# Adjunctions

Adjunctions describe paired constructions that translate between domains in the best available way, even when the translations are not inverses.

An adjunction often appears when one side freely adds structure and the other forgets or extracts structure. The unit and counit explain what is gained, forgotten, approximated, or recovered when moving between the two sides.

Modeling questions:

- What are the two domains being related?
- Which direction freely constructs, completes, or embeds?
- Which direction forgets, observes, extracts, or reconstitutes?
- What is preserved by the round trip?
- What is lost or only approximated?

Examples:

- Syntax and semantics: syntax may freely generate expressions, while semantics interprets them in a model.
- [[Persistence]] and [[Reconstitution]]: persistence selects durable material, while reconstitution recovers usable observations from that material.
- Specification and implementation: a specification constrains possible implementations; an implementation realizes or satisfies the specification only up to declared boundaries.
- Free process descriptions and workflow realizations: a process model may describe possible steps, while a workflow engine realizes a constrained executable form.

Adjunctions are useful because many important pairs are not equalities or isomorphisms. They are structured approximations with explicit directionality.

Related concepts: [[Duality and Symmetry]], [[Persistence]], [[Reconstitution]], [[Realization]], [[Command]], [[Transition]], [[Workflow Engines]].
