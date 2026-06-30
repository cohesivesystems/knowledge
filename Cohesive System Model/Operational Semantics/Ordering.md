---
realm: Operational Semantics
kind: operational-semantics
---

# Ordering

Ordering defines the scope within which events, commands, observations, or effects are sequenced.

An ordering relation may be total or partial. A reflexive order convention uses `x <= x`; transitivity means `x <= y` and `y <= z` imply `x <= z`; antisymmetry means `x <= y` and `y <= x` identify the same ordered position. Partiality means that some pairs may be incomparable. A total order adds comparability for every pair.

Strict "before" relations use the non-reflexive form, often written `x < y`. The reflexive closure of a strict before relation gives the corresponding `<=` relation. Distributed systems often use happened-before as a strict partial order, while versions, timestamps, or causal metadata usually expose a reflexive order or preorder over recorded positions.

Ordering is always relative to a space:

- A key.
- A stream.
- A partition.
- An actor identity.
- A transaction.
- A workflow history.
- An entity version history.

An ordered delivery edge does not necessarily mean the domain transition has committed. It only means the delivery mechanism preserves order within its stated boundary.

Ordering supports [[Version Histories|version histories]], replay, projection updates, [[Consistency Models|consistency models]], concurrency control, and coherent behavior over time.

[[Consensus]] can impose an agreed order where the system otherwise has concurrent or incomparable observations. In replicated state-machine designs, a consensus protocol decides each log position so that replicas apply the same operations in the same order.

## Ordering and Causality

Ordering may represent causation or potential causation in models that define the order relation that way, but ordering should not be treated as causal by default. The meaning of an ordering relation is boundary- and mechanism-relative.

Lamport's happened-before relation is a causal-ordering example: if `A` happened before `B`, then information from `A` could have influenced `B`. It preserves possible causal dependence, not proof that `A` actually caused `B`.

Different ordering spaces carry different causal force. Wall-clock order says one timestamp compares before another, but does not by itself imply causation. Broker or delivery order says one message was delivered before another within a stated boundary. [[Version|Version]] order for a sequential [[Entity|entity]] is stronger because a later state is produced from an earlier state by an accepted [[Transition|transition]]. A total order may serialize concurrent work for operational reasons while introducing artificial before/after relations between events that were otherwise independent.

When using an ordering relation, the model should state whether it means causal dependency, possible causation, delivery sequence, commit sequence, version succession, replay order, presentation order, or something narrower.

In distributed systems, [[Time|time]] often arises through ordering rather than wall-clock measurement. A clock, timestamp, stream offset, or [[Version|version]] can be understood as an order-valued projection: categorically, a monotone map or order-valued functor from events or state observations into an ordering space. When that projection is order-preserving, the ordering of versions or timestamps preserves the relevant happened-before relation. Richer metadata such as vector clocks can determine causal order and incomparability more precisely; scalar logical clocks generally preserve causality in one direction without fully characterizing it.

A consistent cut is an ordering-sensitive snapshot: it includes the causal prerequisites of the events, versions, or observations it includes. It is coherent relative to the declared ordering space.

For [[CRDTs]], ordering requirements are type-specific. Some merge functions are insensitive to message order, while operation-based CRDTs may require causal ordering or explicit causal metadata.

Related concepts: [[Delivery Semantics|delivery semantics]], [[Time|time]], [[Version|version]], [[Version Histories|version histories]], [[Consistency Models|consistency models]], [[Consensus|consensus]], [[Event|event]], [[Concurrency Control|concurrency control]], [[CRDTs]], [[Enrichment and Order|enrichment and order]], [[Functoriality|functoriality]], [[Brokers|brokers]], [[Workflow Engines|workflow engines]], [[Actor Systems|actor systems]].
