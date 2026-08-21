---
realm: Operational Concerns
kind: reference
created: 2026-08-17
updated: 2026-08-17
status: draft
aliases:
  - Fallacies of Distributed Systems
  - Eight Fallacies of Distributed Computing
  - Deutsch Fallacies
  - "Deutsch's Fallacies"
---

# Fallacies of Distributed Computing

The Fallacies of Distributed Computing are a compact checklist of invalid assumptions commonly made when software interaction crosses network, process, administrative, or other independently governed boundaries. The catalog is associated with L. Peter Deutsch and other contributors at Sun Microsystems.

The fallacies are not a theorem, a complete [[Failure Models|failure model]], or a claim that every remote interaction fails. They are prompts to replace silent optimism with explicit boundaries, assumptions, measurements, protocols, and recovery behavior.

## Cohesive Correspondence

| Fallacious assumption | Cohesive correction |
| --- | --- |
| Network interaction is reliable | [[Failure Models\|Failure models]] must admit loss, delay, partition, crash, corruption, overload, and correlated disruption as appropriate. [[Delivery Semantics\|Delivery]], [[Acknowledgments\|acknowledgment]], retry, idempotency, and [[Recovery\|recovery]] claims remain scoped to specific boundaries. |
| Latency can be treated as zero | [[Service Levels\|Service levels]], [[Queueing Theory\|queueing theory]], and [[Locality\|locality]] make response-time distributions, distance, serialization, queueing, and dependency fanout visible. A remote operation cannot safely inherit the cost model of a local call. |
| Bandwidth is effectively unlimited | Payload size, framing, fanout, replay, replication, repair, and control traffic consume finite [[Network\|network]] and processing capacity. [[Flow Control\|Flow control]], admission, batching, compression, retention, and [[Capacity Planning\|capacity planning]] require declared units and bottlenecks. |
| The network is inherently secure | Every crossed [[Boundaries\|boundary]] requires explicit trust, identity, authentication, authorization, confidentiality, integrity, and audit decisions. [[Authority\|Semantic authority]] and transport reachability are not substitutes for those controls. |
| Topology remains fixed | Placement, membership, routes, leaders, partitions, replicas, and dependencies change through scaling, deployment, failover, migration, and repair. [[Infrastructure Graph\|Infrastructure graphs]], [[Routing Models\|routing]], [[Compatibility and Evolution\|compatibility]], and recovery must represent coexistence and transition. |
| One administrator controls the system | Distributed systems cross teams, accounts, providers, regions, organizations, policies, credentials, and change cadences. [[Authority\|Authority]], [[Policy Scopes\|policy scopes]], interfaces, and compatibility boundaries must identify who can decide and change what. |
| Transport has no meaningful cost | Communication consumes latency, bandwidth, CPU, memory, serialization work, storage, energy, money, and operational attention. [[Locality\|Locality]], service levels, capacity planning, and realization evidence must account for the selected cost boundary. |
| The network and its participants are homogeneous | Protocol, schema, runtime, architecture, provider, capability, and version differences are normal. [[Interfaces\|Interfaces]], [[Interaction Protocols\|protocols]], and [[Compatibility and Evolution\|compatibility and evolution]] must state negotiation, coexistence, and unsupported cases. |

Several rows expose areas that the current public graph does not yet give dedicated operational entries. In particular, security and administrative governance are only partially expressible through [[Authority|authority]], [[Policy|policy]], [[Policy Scopes|policy scopes]], [[Boundaries|boundaries]], and [[Observability and Provenance|observability and provenance]]. This reference records the obligation without pretending those concepts form a complete security or governance model.

## Location Transparency

Location transparency separates a logical name or interface from a participant's current physical placement. That indirection can support mobility, routing, replication, failover, and a stable programming surface. It does not make local and remote interaction operationally equivalent.

An abstraction becomes hazardous when uniform syntax conceals latency, partial failure, serialization, bandwidth, topology, security, administration, or transport cost from the model and from the policies responsible for handling them. A location-transparent actor address or service reference may hide coordinates from application code while the system graph still exposes placement, network, failure, authority, and recovery boundaries.

Location transparency is therefore a selective interface property, not a universal design goal. Some consumers need explicit locality constraints, co-location guarantees, region or zone selection, data-sovereignty boundaries, affinity, failure-domain separation, or a rule that an operation must not become remote. The useful discipline is to hide coordinates where they are irrelevant while preserving their operational consequences.

Jim Waldo, Geoff Wyant, Ann Wollrath, and Sam Kendall's *A Note on Distributed Computing* gives the stronger warning behind this distinction: distributed interactions differ intrinsically from single-address-space interactions because latency, memory access, concurrency, and partial failure cannot be abstracted away safely.

## Modeling Checks

- Which network, process, runtime, storage, authority, or administrative boundaries does the interaction cross?
- Which failures, delays, partitions, topology changes, and compatibility differences are admitted?
- Which observations establish delivery, completion, latency, capacity, security, and cost claims?
- Which participant owns retry, timeout, failover, upgrade, credential, and recovery decisions?
- Does a uniform interface conceal a remote boundary whose failure or cost changes caller behavior?
- Which placement facts may remain hidden, and which operational consequences must remain explicit?
- Which fallacy is still being assumed rather than replaced by a modeled requirement and supporting evidence?

## Formal relations

- `documents`: [[Failure Models]] — Organizes recurring invalid reliability and failure assumptions that must be replaced by explicit fault, delay, recovery, and progress models.
- `documents`: [[Locality]] — Relates latency, transport cost, placement, and location transparency to boundary-relative access and interaction costs.
- `documents`: [[Compatibility and Evolution]] — Relates changing topology, administration, and heterogeneity to explicit coexistence, negotiation, and migration requirements.
- `documents`: [[Network]] — Qualifies network realization with finite reliability, latency, bandwidth, security, topology, administrative, cost, and heterogeneity assumptions.

## External References

- Peter Jausovec, [Fallacies of distributed systems](https://blogs.oracle.com/developers/fallacies-of-distributed-systems), Oracle Developers, November 27, 2020.
- Software Engineering Radio, [L. Peter Deutsch on the Fallacies of Distributed Computing](https://se-radio.net/2021/07/episode-470-l-peter-deutsch-on-the-fallacies-of-distributed-computing/), episode 470, July 27, 2021.
- Jim Waldo, Geoff Wyant, Ann Wollrath, and Sam Kendall, [A Note on Distributed Computing](https://waldo.scholars.harvard.edu/publications/note-distributed-computing), Sun Microsystems Laboratories Technical Report SMLI TR-94-29, 1994.
