---
realm: Domain Semantics
kind: semantic-construct
---

# Identity

Identity is what allows a sequence of state observations to be understood as successive versions of the same thing.

For an [[Entity|entity]], identity is stable across the entity lifetime. It is paired with [[Version|version]] to address a particular state in the entity history.

Observers also have identities, distinct from entity identities. Observer identity may be globally addressable, local, transient, or operationally derived depending on the runtime.

An actor address is a kind of addressable observer identity. It may be deliberately aligned with an entity identity, such as one actor per entity, but it may also name a router, shard, process manager, projection worker, or other observer that is not the entity itself.

Identity participates in:

- Entity continuity.
- Observer participation.
- Addressing and routing.
- Concurrency checks.
- Ordered delivery per key or subject.

Related concepts: [[Entity|entity]], [[Observer|observer]], [[Version|version]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Actor Systems|actor systems]], [[Fibrations and Indexed Structure|fibrations and indexed structure]], [[Equivalence vs Equality|equivalence vs equality]].
