---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Failure Model
  - Fault Model
  - Fault Assumptions
---

# Failure Models

Failure models state which faults, delays, losses, corruptions, recoveries, and correlated disruptions a system or protocol admits when making a correctness or progress claim.

A guarantee is meaningful only relative to a failure model and [[Boundaries|boundary]]. A replication protocol may tolerate loss of one replica but not loss of an entire failure domain. A durable record may survive process restart but not storage corruption. A consensus protocol may preserve safety through arbitrary delay while requiring partial synchrony, eventual leadership, or quorum availability for progress.

## Faults, Failures, and Detection

A **fault** is a defect or adverse occurrence inside the modeled boundary: a crash, lost message, corrupted block, paused process, exhausted resource, stale route, or unavailable dependency. A **failure** is an externally relevant deviation from the service or semantic outcome promised at a declared boundary. Fault tolerance prevents selected faults from becoming failures; it does not make the faults cease to occur.

Failure detection is an observation made under uncertainty. A timeout can show that an expected event was not observed before a deadline. It cannot by itself distinguish a crashed participant from a delayed, paused, overloaded, partitioned, or already-committed participant. Suspicion may justify a policy action such as retry, failover, fencing, or escalation, but it is not proof of the hidden cause.

## Failure Classes

Useful failure-model distinctions include:

- **Crash-stop:** a participant halts and does not return within the execution being modeled.
- **Crash-recovery:** a participant may restart with only the material covered by its persistence and durability guarantees.
- **Omission:** a send, receive, storage, scheduling, or acknowledgment occurrence is lost or not performed.
- **Delay and partition:** communication or processing takes arbitrarily longer than the observer can safely wait, or required participants cannot communicate.
- **Timing violation:** an assumed bound on delay, clock error, scheduling, lease, or processing is exceeded.
- **Corruption:** retained or transmitted material differs from what the protocol expects, whether detected or silent.
- **Arbitrary or Byzantine behavior:** a participant may deviate from the protocol, equivocate, or present inconsistent evidence to different observers.
- **Resource and overload failure:** finite capacity, queue growth, allocation failure, or retry amplification prevents useful progress.
- **Correlated failure:** several components fail together because they share power, network, storage, software, authority, configuration, operator action, or another fate-sharing boundary.

These classes are not interchangeable. Checksums can detect some corruption but do not establish authority. Replication can tolerate independent copy loss but can amplify correlated software corruption. Retry can overcome some omissions while worsening overload or duplicating an ambiguous effect.

## Safety, Liveness, and Recovery

The failure model should state separately which [[Safety and Liveness|safety]] properties remain invariant and which liveness properties require additional assumptions. A protocol may preserve one committed history while refusing progress without a quorum. Another may continue accepting local work while exposing concurrent histories and later reconciliation.

Recovery extends the failure model across time. Crash-recovery behavior depends on what identity, term, version, acknowledgment, log position, deduplication record, causal metadata, or pending responsibility survives restart. Recovery that loses protocol state can turn an apparently tolerated crash into split authority, duplicate effects, lost commitment, or invalid convergence.

Failure assumptions compose poorly by default. Components that each tolerate one fault may share a dependency or recovery controller and fail together. End-to-end analysis should follow fate sharing through the [[Infrastructure Graph|infrastructure graph]], including control planes, credentials, configuration, region placement, and repair capacity.

## Modeling Checks

- Which faults are admitted, and at which semantic, system, protocol, and substrate boundaries?
- Which faults are independent, and which components share a fate or failure domain?
- What evidence distinguishes suspected, detected, confirmed, and repaired failure?
- Which safety properties must survive every admitted execution?
- Which timing, fairness, quorum, capacity, or eventual-recovery assumptions are required for progress?
- What durable material and identity survive crash and restart?
- Can retry, failover, replay, or repair duplicate an effect or revive stale authority?
- What consumer-visible failure follows when tolerance is exhausted?
- How are failure-model assumptions validated through testing, observation, and recovery exercises?

## External References

- Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly Media, 2017, chapter 8.

Related concepts: [[Distributed Failure Scenarios|distributed failure scenarios]], [[Uncertainty|uncertainty]], [[Safety and Liveness|safety and liveness]], [[Progress Conditions|progress conditions]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Boundaries|boundaries]], [[Service Levels|service levels]], [[Durability|durability]], [[Recovery|recovery]], [[Retry|retry]], [[Acknowledgments|acknowledgments]], [[Authority|authority]], [[Consensus|consensus]], [[Quorum Intersection|quorum intersection]], [[Replica Models|replica models]], [[Partition Models|partition models]], [[CAP Theorem|CAP theorem]], [[Network|network]], [[Infrastructure Graph|infrastructure graph]].
