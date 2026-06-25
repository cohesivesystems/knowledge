---
realm: Semantic Dynamics
---

# State

Realm: Semantic Dynamics

A State is the condition or configuration of a subject within a model [[Boundaries|boundary]]. It represents what is, relative to the subject, boundary, [[Shape|shape]], and time or version at which it is considered.

In Leslie Lamport's TLA formulation, a state is an assignment of values to variables: a mapping from variable names to values. In this model, those variables can be understood as the named dimensions made visible by a subject, boundary, [[Shape|shape]], or specification.

State is not the same thing as the [[Value|value]] used to read, write, transmit, or compare it. State becomes usable through values and contextualized [[Observation|Observations]] produced by [[Observable|observables]].

State does not inherently carry [[Identity]], [[Version]], or lineage. Those belong to composite concepts such as entity state, observations, state records, histories, and provenance metadata.

For an [[Entity]], entity state is state attributed to an [[Identity]] at a [[Version]]. The version identifies the point in the entity history at which that state became current. Entity state may be full or partial only relative to a declared [[Shape|shape]], model [[Boundaries|boundary]], or operation.

In [[Event-State Duality]]:

- [[Event|Events]] carry occurrence, time, and change information.
- States carry information and become current at a specific version or time.
- For a sequential entity, state at [[Version]] `V` is the result of applying the event that produced version `V`.
- Events and states are dual views of [[Behavior]], not interchangeable representations.

## External References

- Leslie Lamport, [The Temporal Logic of Actions](https://lamport.azurewebsites.net/pubs/lamport-actions.pdf), ACM Transactions on Programming Languages and Systems, 16(3):872-923, May 1994. Section 2.1 defines state in terms of assigning values to variables.

Related concepts: [[Value]], [[Shape]], [[Observation]], [[Event]], [[Event-State Duality]], [[Entity]], [[Identity]], [[Version]], [[Boundaries]], [[Transition]].
