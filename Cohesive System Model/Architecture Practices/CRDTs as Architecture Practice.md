---
realm: Architecture Practices
kind: architecture-practice
---

# CRDTs As Architecture Practice

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

## Practice Interpretation

CRDTs are suitable when the domain can tolerate temporary divergence and the intended state evolution can be modeled with monotonic merge or commutative updates.

Related concepts: [[CRDTs]], [[Coordination]], [[Persistence]], [[Reconstitution]], [[Delivery Semantics]], [[Ordering]], [[Invariants]], [[Storage Systems]], [[Compositionality]].
