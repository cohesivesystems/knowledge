---
realm: Architecture Practices
kind: reference
created: 2026-07-28
updated: 2026-07-28
aliases:
  - Distributed Systems Patterns
  - Distributed Systems Pattern Catalog
---

# Patterns of Distributed Systems

Patterns of Distributed Systems, by Unmesh Joshi, collects recurring implementation structures used in distributed storage, messaging, system management, and compute infrastructure.

## Cohesive Correspondence

| Pattern family | Representative patterns | Cohesive correspondence |
| --- | --- | --- |
| Time, order, and versions | Lamport Clock, Hybrid Clock, Generation Clock, Version Vector, Versioned Value | [[Time|time]], [[Causality|causality]], [[Version|version]], [[Ordering|ordering]], and [[Version Histories|version histories]] |
| Replication and agreement | Leader and Followers, Majority Quorum, Paxos, Replicated Log, Consistent Core | [[Consensus|consensus]], consistency models, durability, arbitration, and [[Consensus Protocols|consensus protocols]] |
| Partitioning and storage | Fixed Partitions, Key-Range Partitions, Write-Ahead Log, Segmented Log, High-Water Mark, Low-Water Mark | persistence, reconstitution, retention, storage systems, and log realization |
| Interaction and progress | HeartBeat, Gossip Dissemination, Request Batch, Request Pipeline, Request Waiting List, State Watch, Idempotent Receiver | interaction, delivery, scheduling, liveness, correlation, observability, and recovery |
| Serialization and local order | Singular Update Queue, Single-Socket Channel | concurrency control, interaction channels, ordering scopes, runtimes, and network substrate |

The catalog gravitates toward operational concerns and realization substrate. It explains mechanisms that can establish a scoped guarantee; it usually does not define the domain meaning carried by that guarantee.

## Boundary of Adoption

A replicated-log entry is not automatically a domain [[Event|event]]. A leader is not automatically a domain [[Authority|authority]]. A version vector detects causal relationships among replica versions but does not decide whether concurrent domain changes are semantically compatible. A write-ahead log provides storage recovery material and is not automatically [[Event Sourcing|event sourcing]]. A singular update queue can serialize execution without validating a domain transition.

These distinctions make the catalog valuable realization evidence: Cohesive can say which semantic or system-graph structure a distributed pattern realizes and exactly which ordering, durability, consistency, or progress claim it supports.

## External References

- Unmesh Joshi, [Catalog of Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/), 2023.
- Unmesh Joshi, *Patterns of Distributed Systems*, Addison-Wesley Professional, 2023.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Consensus|consensus]], [[Consistency Models|consistency models]], [[Causality|causality]], [[Ordering|ordering]], [[Version Histories|version histories]], [[Persistence|persistence]], [[Durability|durability]], [[Interaction|interaction]], [[Scheduling|scheduling]], [[Recovery|recovery]], [[Consensus Protocols|consensus protocols]], [[Storage Systems|storage systems]], [[Write-Ahead Logging|write-ahead logging]], [[Event Sourcing|event sourcing]].
