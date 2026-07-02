---
realm: Operational Concerns
kind: operational-concern
---

# Isolation

Isolation describes what concurrent operations are allowed to observe of one another while they execute.

In the Cohesive model, isolation is boundary-relative. It may describe a database transaction, an entity transition boundary, an actor turn, a workflow step, a projection update, a read model, or another realization context. It answers: which concurrent effects are visible, hidden, delayed, rejected, serialized, or allowed to interleave?

Isolation is related to, but not identical with, [[Consistency Models|consistency models]]. A consistency model constrains which histories and observations are valid. Isolation describes how concurrent operations are separated or exposed while those histories are being produced.

## Isolation Levels and Anomalies

Common isolation levels include:

- **Read committed**, where reads avoid uncommitted writes but may observe different committed values over time.
- **Repeatable read**, where repeated reads of the same item remain stable within a transaction boundary, depending on the implementation.
- **Snapshot isolation**, where a transaction reads from a stable snapshot and usually commits only if write conflicts are acceptable.
- **Serializable isolation**, where concurrent transactions are equivalent to some serial execution.

Note that serializable isolation is not the same as [[Consistency Models|linearizability]]. Serializable isolation provides *some* legal serial order. Linearizability, or strict serializability for transactions, additionally preserves real-time order for non-overlapping operations.

Common anomalies include dirty reads, non-repeatable reads, phantoms, lost updates, read skew, and write skew. These names are useful only when the affected boundary is explicit.

## Isolation and Entity Transitions

For an [[Entity|entity]], isolation is often realized by expected-version checks, actor serialization, compare-and-swap operations, locks, or transaction isolation in a storage system.

Isolation for an entity transition is not only about the target entity row or actor state. A transition often validates against additional [[Observation|observations]] or facts: related entities, policy state, capacity, inventory, account balances, read models, external facts, or environmental state.

Inside one RDBMS transaction, the transaction manager may control the visibility and stability of those reads according to the chosen isolation level. Outside that boundary, the observer may not have enough information to know whether related observations changed between reading them and accepting the transition.

Strong isolation can make a transition easier to reason about because the observer can validate against a coherent view of current state and related observations. Weak isolation can improve availability or throughput, but then the model must say which anomalies are acceptable and which patterns prevent invariant violations.

One weak-isolation pattern is to carry additional versioning information in the transition context: related entity versions, read-model positions, policy versions, inventory reservation versions, or causal metadata. The transition can then reject, retry, compensate, reserve, or accept based on whether those related observations are still valid enough for the invariant being protected.

## Relationship to ACID

In [[ACID]], isolation is one part of a transaction contract. Outside a single ACID boundary, isolation must be reconstructed with explicit [[Concurrency Control|concurrency control]], [[Coordination|coordination]], [[Ordering|ordering]], idempotency, compensation, reservations, escrow, or other [[Weak Isolation Patterns|weak isolation patterns]].

## External References

- Hal Berenson, Philip A. Bernstein, Jim Gray, Jim Melton, Elizabeth J. O'Neil, and Patrick E. O'Neil, [A Critique of ANSI SQL Isolation Levels](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf), SIGMOD 1995.

Related concepts: [[ACID]], [[Consistency Models|consistency models]], [[Concurrency Control|concurrency control]], [[Coordination|coordination]], [[Version|version]], [[Ordering|ordering]], [[Entity|entity]], [[Transition|transition]], [[Observation|observation]], [[Weak Isolation Patterns|weak isolation patterns]].
