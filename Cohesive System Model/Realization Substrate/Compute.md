---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-08-01
---

# Compute

Compute is the concrete capacity that executes work: CPU, memory, processes, containers, virtual machines, functions, tasks, nodes, clusters, and other execution resources.

In the cohesive system model, compute participates in [[Realization|realizing]] semantic and operational roles but does not define them. An [[Observer|observer]], [[Entity|entity]], process, projection, or workflow may run on compute, but its meaning comes from the model layer above the substrate.

Compute concerns include:

- Placement.
- Scheduling.
- Resource limits.
- Isolation.
- [[Scaling Mechanisms|Scaling mechanisms]].
- Failure and restart behavior.
- [[Locality]] to storage, brokers, or dependencies.

Compute resources are allocated through [[Scheduling|scheduling]] and local [[Arbitration|arbitration]]. A substrate can expose priority, preemption, affinity, quotas, deadlines, or best-effort execution without defining the fairness or domain-authority semantics expected by the system above it.

Adding compute changes a resource dimension; it does not by itself establish [[Scalability|scalability]]. Effective capacity also depends on [[Admission Control and Load Shedding|admission]], useful parallelism, placement, locality, shared dependencies, contention, coordination, and the churn created while capacity is added, moved, warmed, drained, or removed.

Compute supplies the resource boundary for physical [[Parallelism|parallelism]]. A parallelism claim must identify resources whose execution intervals can actually overlap. Multiple logical tasks, processes, containers, or OS threads may still be temporally multiplexed on one underlying resource, while one application thread may rely on devices or remote nodes progressing in parallel beyond its local boundary.

Related concepts: [[Realization|realization]], [[Parallelism|parallelism]], [[Concurrency|concurrency]], [[Scalability|scalability]], [[Scaling Mechanisms|scaling mechanisms]], [[Locality|locality]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Capacity Planning|capacity planning]], [[Runtimes|runtimes]], [[Application Hosts|application hosts]], [[Infrastructure|infrastructure]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Observer|observer]], [[Process Graphs|process graphs]], [[Recovery|recovery]].

## Formal relations

- `may_realize`: [[Parallelism]] — Supplies distinct execution resources on which compatible work can overlap physically at a declared compute boundary.
