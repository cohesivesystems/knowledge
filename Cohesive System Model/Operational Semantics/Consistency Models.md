---
realm: Operational Semantics
kind: operational-semantics
---

# Consistency Models

Consistency Models constrain which observations are valid for a set of events, transitions, versions, sessions, replicas, and ordering relations.

A consistency model is a predicate over histories. It says which operation results, reads, observations, or replica states are allowed relative to a chosen [[Boundaries|boundary]], [[Ordering|ordering]] space, [[Version Histories|version history]], and subject.

Consistency models are not global by default. A system may provide one model for an entity transition boundary, another for a read model, another for a cache, another for a workflow history, and another for a broker or storage substrate.

## Linearizability

Linearizability requires each operation to appear as if it took effect at a single point between invocation and response. The resulting history must be equivalent to a legal sequential history and must preserve real-time order for non-overlapping operations.

Linearizability is a strong model for shared objects and entity boundaries because it lets observers reason as if each operation happened atomically at some point during its execution. It is usually expensive across distributed boundaries because preserving real-time order requires coordination.

## Sequential Consistency

Sequential consistency requires that the result be explainable by some legal total order of operations that preserves each participant's program order. It does not require that the total order preserve real-time order between operations from different participants.

Sequential consistency is therefore weaker than linearizability. It can preserve each observer's local order while allowing a global explanation that may differ from wall-clock order.

## Causal Consistency

Causal consistency preserves the order of causally related operations while allowing concurrent or unrelated operations to be observed in different orders.

This model is naturally related to [[Time|logical time]], happened-before, vector clocks, and causal metadata. It is useful when the model needs to preserve potential causation without imposing one global total order on independent work.

## Session Consistency

Session consistency is a family of guarantees scoped to one observer, client, process, or session. Common session guarantees include:

- Read-your-writes.
- Monotonic reads.
- Monotonic writes.
- Writes-follow-reads.

Session guarantees make weak or replicated systems easier to use because they preserve a coherent experience for one observer even when different observers may see different replica states.

## Eventual Consistency

Eventual consistency says that replicas converge if updates stop and delivery, reconciliation, or merge eventually completes.

Eventual consistency alone does not say what intermediate observations are allowed, how conflicts are represented, whether causality is preserved, or what merge semantics are valid. Those details must be supplied by [[Version Histories]], [[Ordering]], [[Delivery Semantics]], [[CRDTs]], conflict resolution, or application-specific invariants.

## Relationship To History Shape

Consistency models choose how much history shape must be preserved.

Linearizability and sequential consistency require a legal total order, though they differ on real-time constraints. Causal consistency preserves a partial order. Session consistency preserves an observer-relative slice of history. Eventual consistency focuses on convergence and may tolerate temporary divergence, stale observations, or concurrent incomparable versions.

The design question is not simply "strong" or "weak" consistency. It is which observations must be coherent for which observer, boundary, invariant, and history shape.

## External References

- Maurice P. Herlihy and Jeannette M. Wing, [Linearizability: A Correctness Condition for Concurrent Objects](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf), ACM Transactions on Programming Languages and Systems, 12(3):463-492, July 1990.
- Leslie Lamport, [How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs](https://www.microsoft.com/en-us/research/publication/make-multiprocessor-computer-correctly-executes-multiprocess-programs/), IEEE Transactions on Computers, C-28(9):690-691, September 1979.
- Douglas B. Terry, Alan J. Demers, Karin Petersen, Mike Spreitzer, Marvin Theimer, and Brent Welch, [Session Guarantees for Weakly Consistent Replicated Data](https://www.cs.cornell.edu/courses/cs734/2000FA/cached%20papers/SessionGuaranteesPDIS_1.html), PDIS 1994.
- Werner Vogels, [Eventually Consistent](https://queue.acm.org/detail.cfm?id=1466448), ACM Queue, 2008.

Related concepts: [[Ordering]], [[Version Histories]], [[Version]], [[Time]], [[Observation]], [[Observer]], [[Boundaries]], [[Concurrency Control]], [[Coordination]], [[Delivery Semantics]], [[CRDTs]], [[CQRS]], [[Persistence]], [[Reconstitution]].
