---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-06-29
---

# Duality and Symmetry

Duality and symmetry are principles for recognizing paired concepts that explain one another through reversal, complementarity, or mirrored structure.

A duality is not necessarily an isomorphism. Dual concepts may determine each other only partially, lossy transformations may exist in one direction, and extra context may be required to move between them. The point is to identify the shared structure and the direction of contrast without confusing dual things for the same thing or for unrelated things.

Common dualities or symmetries in the model include:

- [[Event-State Duality]]: event schedules and state histories are dual views of [[Behavior|behavior]], but they are not interchangeable representations.
- Syntax and semantics: syntax carries form; semantics gives interpretation.
- Input and output: an output event at one boundary may be an input event at another.
- Client and server: each side defines a complementary interaction role relative to a protocol boundary.
- [[Persistence]] and [[Reconstitution|reconstitution]]: one makes material durable; the other turns durable material back into usable observations.
- Monads and comonads: one commonly models effectful construction or sequencing; the other commonly models context, observation, or extraction.
- Parallelism and [[Concurrency Control|concurrency]]: parallelism concerns simultaneous execution; concurrency concerns coordination of interleavings and conflicts.

Duality helps the model ask:

- What changes when the arrows, roles, or direction of interpretation are reversed?
- What information is preserved in both directions?
- What information is lost in one direction?
- What extra boundary, observer, policy, or context is required to translate between the two sides?
- Is the relationship a true isomorphism, an adjunction, a projection, an approximation, or only an analogy?

Symmetry is often broken by boundaries, observers, time, authority, or commitment. For example, input and output appear symmetric as interaction roles, but a receiving [[Observer|observer]] may reject, reinterpret, or ignore an incoming event. Persistence and reconstitution appear symmetric as write/read roles, but persistence choices determine which histories, observations, and versions can actually be reconstituted.

Recognizing dualities keeps the model honest. It prevents event histories from being treated as identical to state histories, syntax from being mistaken for semantics, broker delivery from being mistaken for domain commitment, and realization substrate from being mistaken for the semantic role it realizes.

Related concepts: [[Event-State Duality|event-state duality]], [[Event|event]], [[State|state]], [[Behavior|behavior]], [[Observer|observer]], [[Boundaries|boundaries]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Interaction|interaction]], [[Concurrency Control|concurrency control]].
