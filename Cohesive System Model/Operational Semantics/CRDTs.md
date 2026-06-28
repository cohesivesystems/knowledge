---
realm: Operational Semantics
---

# CRDTs

CRDTs, conflict-free replicated data types, are replicated data types designed so that independently updated replicas converge without requiring synchronous coordination for every update.

The earlier terminology distinguishes two related families:

- **Convergent replicated data types**, or CvRDTs: state-based CRDTs whose replica states are merged by a monotonic, associative, commutative, idempotent join.
- **Commutative replicated data types**, or CmRDTs: operation-based CRDTs whose concurrent operations commute, assuming the required delivery guarantees.

In both cases, the data type carries part of the coordination semantics. Instead of resolving arbitrary conflicts after the fact, the type is designed so that concurrent updates have a deterministic convergence rule.

CRDTs are useful when:

- Replicas must accept updates while disconnected or partitioned.
- Low-latency local writes matter more than immediate global agreement.
- The domain operation can be modeled with monotonic merge or commutative updates.
- Observers can tolerate temporary divergence while replicas converge.

CRDTs do not remove consistency concerns. They move some consistency requirements into the algebra of the data type and into the delivery, persistence, and metadata rules around it.

Operational requirements include:

- Merge or operation semantics must be deterministic.
- Required causal, reliable, or exactly-once effects must be stated at the correct [[Boundaries|boundary]].
- Metadata such as versions, dots, vector clocks, causal contexts, tombstones, or replica identifiers may be part of the replicated state.
- Compaction, retention, and garbage collection must preserve convergence.
- Invariants that are not monotonic or commutative may still require coordination, escrow, reservations, or a different design.

In the Cohesive System Model, a CRDT is a coordination strategy for replicated state. It can realize a projection, cache, collaborative object, replicated aggregate, presence set, counter, register, map, graph, or other structure whose update algebra preserves convergence.

Persistence for CRDTs must preserve enough state, operation history, delta history, or causal metadata for replicas to recover and continue converging. Persisting only the visible value may be insufficient if convergence depends on hidden metadata.

CRDT convergence is not the same as immediate consistency. At a given observation boundary, two observers may see different values until updates propagate and merge. The model must make that staleness, ordering, and convergence boundary explicit.

## External References

- Marc Shapiro, Nuno Preguiça, Carlos Baquero, and Marek Zawirski, [A comprehensive study of Convergent and Commutative Replicated Data Types](https://inria.hal.science/inria-00555588/en/), INRIA Research Report 7506, January 2011. [PDF](https://inria.hal.science/inria-00555588v1/document)
- Marc Shapiro, Nuno Preguiça, Carlos Baquero, and Marek Zawirski, [Conflict-free Replicated Data Types](https://inria.hal.science/hal-00932836v1/document), SSS 2011.
- Nuno Preguiça, Carlos Baquero, and Marc Shapiro, [Conflict-free Replicated Data Types](https://arxiv.org/abs/1805.06358), arXiv, 2018.

Related concepts: [[Coordination]], [[Persistence]], [[Reconstitution]], [[Delivery Semantics]], [[Ordering]], [[State]], [[Observation]], [[Projections]], [[Recovery]], [[Storage Systems]], [[Boundaries]], [[Compositionality]], [[Monads Monoids and Duals]], [[Algebras and Coalgebras]].
