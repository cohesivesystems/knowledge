---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-01
---

# State

A state is the condition or configuration of a subject within a model [[Boundaries|boundary]], modeled as an assignment of values to the subject's relevant dimensions at a time, [[Version|version]], or point in [[Behavior|behavior]].

Unlike an [[Event|event]], state is not occurrence-bearing. It represents what is relative to a subject, boundary, [[Shape|shape]], and point of consideration, not what happened.

In Leslie Lamport's TLA formulation, a state is an assignment of values to variables: a mapping from variable names to values. In this model, those variables can be understood as the named dimensions made visible by a subject, boundary, [[Shape|shape]], or specification.

State is not the same thing as the [[Value|value]] used to read, write, transmit, or compare it. A value may represent all or part of state through a shape. An [[Observation|observation]] is a contextualized value produced by an [[Observable|observable]] acting on state.

The physics analogy is useful but informal: state is what observables act on to produce observations. Different observables may reveal different dimensions of the same underlying state.

State does not inherently carry [[Identity|identity]], [[Version|version]], or lineage. Those belong to composite concepts such as entity state, observations, state records, histories, and provenance metadata.

For an [[Entity|entity]], entity state is state attributed to an [[Identity|identity]] at a [[Version|version]]. The version identifies the point in the entity history at which that state became current. Entity state is not merely a value with metadata; values represent, observe, persist, compare, or update entity state, while identity, version, and events locate it within an entity history. Entity state may be full or partial only relative to a declared [[Shape|shape]], model [[Boundaries|boundary]], or operation.

System state is broader than entity state. It may assign values across multiple subjects, [[Observer|observers]], [[Relations|relations]], stores, queues, [[Processes|processes]], policies, and environmental dimensions inside a boundary. Observers interact with state by observing it and, when authorized, by interpreting input events as [[Command|commands]] that may advance or mutate it through [[Transition|transitions]].

In [[Event-State Duality|event-state duality]]:

- [[Event|Events]] carry occurrence, time, and change information.
- States carry information and become current at a specific version or time.
- For a sequential entity, state at [[Version|version]] `v` is the result of applying the event that produced version `v`.
- Events and states are dual views of [[Behavior|behavior]], not interchangeable representations.

## External References

- Leslie Lamport, [The Temporal Logic of Actions](https://lamport.azurewebsites.net/pubs/lamport-actions.pdf), ACM Transactions on Programming Languages and Systems, 16(3):872-923, May 1994. Section 2.1 defines state in terms of assigning values to variables.

Related concepts: [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[Observable|observable]], [[Observer|observer]], [[Event|event]], [[Event-State Duality|event-state duality]], [[Behavior|behavior]], [[Entity|entity]], [[Identity|identity]], [[Version|version]], [[Boundaries|boundaries]], [[Transition|transition]], [[Relations|relations]], [[Processes|processes]].
