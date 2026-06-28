---
realm: Semantic Dynamics
kind: semantic-construct
---

# Time

Time is the dimension in which occurrences, changes, histories, and behaviors are ordered or compared.

In the model, [[Value|values]] and [[Observation|observations]] do not carry intrinsic occurrence time. Time belongs to [[Event|Events]], version histories, and [[Behavior|Behaviors]].

For an [[Entity]], time is reflected operationally by its ordered sequence of versions. A state becomes current at the version or time produced by the event that caused it.

Time may be represented by clocks, event positions, versions, sequence numbers, workflow history positions, stream offsets, or other ordering mechanisms depending on the realization substrate.

Logical clocks model time as event ordering rather than wall-clock measurement. In distributed systems, this may produce partial orders where some events are concurrent or incomparable.

Vector clocks refine logical time by tracking causal position across multiple participants. They are useful when a model must distinguish causally ordered events or state observations from concurrent or incomparable ones rather than forcing everything into one total order. A [[Version]] in a distributed or replicated history may use vector-clock-like metadata as its realization.

## External References

- Leslie Lamport, [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf), Communications of the ACM, 21(7):558-565, July 1978.
- Friedemann Mattern, [Virtual Time and Global States of Distributed Systems](https://homes.cs.washington.edu/~arvind/cs425/doc/mattern89virtual.pdf), 1989.

Related concepts: [[Value]], [[Event]], [[Behavior]], [[Version]], [[State]], [[Ordering]].
