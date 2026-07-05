---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-06-29
---

# CRDTs as Architecture Practice

CRDTs are a distributed-systems practice for designing replicated state that can accept concurrent updates and converge without synchronous coordination for every update.

The technical semantics are captured by [[CRDTs]].

## Problem

CRDTs address the problem of coordination under partitions, replication, offline updates, and low-latency local writes.

## Cohesive Formulation

The practice moves part of the coordination problem into the algebra of the data type:

- State-based CRDTs converge by merge.
- Operation-based CRDTs converge by commutative operations under delivery assumptions.
- Persistence and recovery must preserve causal metadata needed for convergence.
- Invariants must be compatible with the merge or operation algebra, or else require additional coordination.

## In the Model

CRDTs are suitable when the domain can tolerate temporary divergence and the intended state evolution can be modeled with monotonic merge or commutative updates.

The [[CALM Theorem|CALM theorem]] generalizes this practice beyond CRDT implementations: monotone application logic is the part of the system that can usually remain coordination-free.

Related concepts: [[CRDTs]], [[CALM Theorem|CALM theorem]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Invariants|invariants]], [[Storage Systems|storage systems]], [[Compositionality|compositionality]].
