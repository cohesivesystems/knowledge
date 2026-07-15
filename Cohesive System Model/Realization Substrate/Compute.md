---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-07-15
---

# Compute

Compute is the concrete capacity that executes work: CPU, memory, processes, containers, virtual machines, functions, tasks, nodes, clusters, and other execution resources.

In the cohesive system model, compute participates in [[Realization|realizing]] semantic and operational roles but does not define them. An [[Observer|observer]], [[Entity|entity]], process, projection, or workflow may run on compute, but its meaning comes from the model layer above the substrate.

Compute concerns include:

- Placement.
- Scheduling.
- Resource limits.
- Isolation.
- Scaling.
- Failure and restart behavior.
- Locality to storage, brokers, or dependencies.

Compute resources are allocated through [[Scheduling|scheduling]] and local [[Arbitration|arbitration]]. A substrate can expose priority, preemption, affinity, quotas, deadlines, or best-effort execution without defining the fairness or domain-authority semantics expected by the system above it.

Related concepts: [[Realization|realization]], [[Runtimes|runtimes]], [[Application Hosts|application hosts]], [[Infrastructure|infrastructure]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Observer|observer]], [[Process Graphs|process graphs]], [[Recovery|recovery]].
