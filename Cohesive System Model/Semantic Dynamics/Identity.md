---
realm: Semantic Dynamics
---

# Identity

Identity is what allows a sequence of state observations to be understood as successive versions of the same thing.

For an [[Entity]], identity is stable across the entity lifetime. It is paired with [[Version]] to address a particular state in the entity history.

Observers also have identities, distinct from entity identities. Observer identity may be globally addressable, local, transient, or operationally derived depending on the runtime.

An actor address is a kind of addressable observer identity. It may be deliberately aligned with an entity identity, such as one actor per entity, but it may also name a router, shard, process manager, projection worker, or other observer that is not the entity itself.

Identity participates in:

- Entity continuity.
- Observer participation.
- Addressing and routing.
- Concurrency checks.
- Ordered delivery per key or subject.

Related concepts: [[Entity]], [[Observer]], [[Version]], [[Interaction]], [[Delivery Semantics]], [[Actor Systems]], [[Fibrations and Indexed Structure]], [[Equivalence vs Equality]].
