---
realm: Domain Semantics
kind: semantic-construct
---

# Entity

An entity is an enduring, identifiable subject whose state evolves over time under controlled transitions.

An entity is defined by:

- A stable [[Identity|identity]] that persists across its lifetime.
- A family of entity-state [[Observation|observations]] across time, indexed by [[Version|version]].
- A current [[State|state]] at any point in time, attributed to identity + version.
- [[Transition|Transitions]] that define how its state may change.
- [[Invariants]] and [[Policies|policies]] that constrain valid changes.
- Effects, primarily the endogenous [[Event|events]] it produces when transitions are committed.

An entity is therefore state + identity + version history + transitions + invariants + policies + effects.

Under the [[Stuff Structure Property|stuff structure property]] lens, an entity is primarily stuff: an identifiable subject. Its transitions, state history, relations, and emitted events provide structure; its invariants and policies express properties that valid evolution must satisfy.

Entity state is a specialized observation: a shaped [[Value|value]] attributed to an entity identity at a version. It may be complete or partial only relative to a declared [[Shape|shape]], projection, transition, or [[Boundaries|boundary]]. Related entities, policies, projections, and environmental facts that affect a transition belong to the transition context, not automatically to the entity's own state.

Identity is what allows a sequence of state observations to be understood as successive versions of the same thing. Version is what allows transitions and concurrency-control mechanisms to distinguish one state sample associated with an entity from another.

An entity is not automatically an [[Observer|observer]], but it may be modeled or realized as one when it interprets inputs relative to its own state, version history, invariants, policies, and boundary. Actor-hosted entities, entity command handlers, and long-running process entities are common examples.

For correctness, the observer that interprets an entity transition must remain aligned with the realization context that commits the transition for the duration of the operation. An actor can provide that alignment by hosting the entity's transition boundary behind an addressable, serialized observer. A stateless request handler, such as one in a web application host, usually realizes only a temporary observer; correctness then depends on explicit concurrency control such as expected-version checks. Session affinity may improve locality, but it is not a correctness mechanism unless it also guarantees exclusive transition ownership.

Related concepts: [[Value|value]], [[Shape|shape]], [[State|state]], [[Identity|identity]], [[Version|version]], [[Observer|observer]], [[Boundaries|boundaries]], [[Transition|transition]], [[Command|command]], [[Event|event]], [[Entity Models|entity models]], [[Stuff Structure Property|stuff structure property]], [[Realization|realization]], [[Concurrency Control|concurrency control]], [[Actor Systems|actor systems]].
