---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-11-05
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

## Supersession and continuity

Merging two subjects can retire their identities in favor of a survivor or successor without changing an old key. A split can retire the original and record which successors derive from it. Preserve the original history and causal references; do not silently route a request addressed to a retired identity as though it addressed the successor. A contract can return a superseded disposition identifying the successor or successors and require callers to decide how to proceed.

Changing a definition’s name or moving its storage does not itself merge or split any instance. [[Compatibility and Evolution|Compatibility and evolution]] asks separately which instance obligations remain valid across the change.
