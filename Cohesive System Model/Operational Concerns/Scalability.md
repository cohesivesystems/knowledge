---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-28
updated: 2026-08-03
status: draft
aliases:
  - Scaling
  - System Scalability
  - Computational Scalability
---

# Scalability

Scalability is a system property describing how its sustainable capacity, efficiency, and service quality change as workload, resources, or topology vary, subject to latency, correctness, availability, backlog, and cost bounds at a stated [[Boundaries|boundary]].

A scalability claim is therefore a profile rather than a Boolean label. It must identify what grows, what is added or changed, which outcomes count as useful service, and which constraints must continue to hold. A system may scale with request rate but not dataset size, with independent tenants but not one hot entity, or with reads but not coordinated writes.

[[Scaling Mechanisms|Scaling mechanisms]] such as larger allocations, replication, decomposition, partitioning, and autoscaling can change the profile. Deploying those mechanisms does not by itself establish scalability.

In [[Stuff Structure Property|stuff, structure, and property]] terms, workload and resource populations are stuff, topology and interaction arrangements are structure, and scalability is a property of their behavior together. That property is not automatically [[Compositionality|compositional]]: scalable components can form a system limited by shared dependencies, synchronized demand, fanout, or cross-boundary coordination.

## Scalability Profile

A scalability profile declares at least four groups of quantities:

- **Workload dimensions:** offered and admitted rate, concurrency, dataset or working-set size, tenant or key population, fanout, burstiness, geographic span, and read/write mix.
- **Resource and topology dimensions:** cores, memory, bandwidth, storage service rate, worker slots, replicas, partitions, functional components, regions, and failure domains.
- **Service outcomes:** useful completion throughput, latency distribution, freshness, error and rejection rate, unfinished backlog, availability, recovery progress, and semantic correctness.
- **Efficiency and cost:** resource consumed per useful completion, coordination and reconfiguration work, monetary cost, energy, and operational burden.

A workload reaches capacity-bearing units through [[Interaction|interactions]], [[Interaction Channels|interaction channels]], [[Routing Models|routing]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], and [[Consumer Coordination|consumer coordination]]. Those structures determine fanout, skew, affinity, partition ownership, shared lanes, and head-of-line blocking, so they are part of the profile rather than neutral transport detail.

The completion boundary matters. Offered work, admitted work, execution attempts, physical effects, acknowledged results, and semantically successful completions are different quantities. [[Delivery Semantics|Delivery semantics]], [[Acknowledgments|acknowledgments]], and [[Commit Boundaries|commit boundaries]] state which occurrence is being counted. Retries can increase attempt throughput while useful completion throughput falls. Early rejection can reduce admitted throughput while increasing successful completions at the protected boundary.

Aggregate service outcomes should also be separated by relevant [[Policy Scopes|policy scopes]]. More total throughput does not establish [[Fairness|fairness]] when one tenant, key, partition, region, or priority class is starved.

Related terms should remain distinct:

- **Performance** describes behavior at a particular workload and configuration.
- **Capacity** is the sustainable workload under declared service constraints.
- **Scalability** describes how capacity, efficiency, and service quality change as workload, resources, or topology change.
- **Elasticity** describes how timely and safely capacity can be acquired and released in response to changing demand.
- **Autoscaling** is a [[Scaling Mechanisms|realization mechanism]] intended to provide some elasticity; it is not the property itself.

## Non-Monotonic Scaling and Overload Collapse

More offered work, concurrency, replicas, partitions, or resources do not necessarily produce more useful throughput. Beyond a system's effective capacity, additional work can increase queueing, contention, coordination, retries, state movement, cache disruption, and recovery activity faster than it increases productive service. Useful throughput may plateau and then decline.

```text
offered work
  -> admitted work
  -> execution attempts
  -> successful useful completions
```

This makes apparently counter-intuitive behavior possible. Throttling reduces throughput at an admission boundary while increasing throughput at a useful-completion boundary. A concurrency limit can reduce lock waits, transaction aborts, context switching, memory pressure, cache eviction, quorum work, or cross-partition interference. Retry limits can prevent failed attempts from starving first attempts and recovery work. [[Admission Control and Load Shedding|Load shedding]] can reject work early and cheaply so the admitted population continues to make progress.

The controls have related but distinct scopes:

- [[Admission Control and Load Shedding|Admission control]] decides whether and under which conditions responsibility for offered work is accepted.
- [[Rate Limiting|Rate limiting]] bounds admissions over time.
- Concurrency limiting bounds admitted work that may remain in flight.
- [[Flow Control|Flow control]] propagates capacity information or demand between participants.
- [[Admission Control and Load Shedding|Load shedding]] rejects, samples, or degrades selected work under overload.
- [[Scheduling]] chooses which admitted work receives scarce execution opportunity.
- Throttling is the broader deliberate reduction of offered, admitted, or executing work.

These interventions help only relative to a bottleneck and objective. Throttling below sustainable demand wastes capacity; adding parallelism before saturation may improve throughput. The scaling profile must locate the knee rather than treating either maximum concurrency or minimum load as universally desirable.

Other non-monotonic effects include larger buffers increasing latency and stale work without increasing capacity; replication reducing write capacity; partitioning increasing skew, fanout, or cross-partition coordination; and autoscaling increasing churn around a shared bottleneck.

When overload responses, retries, backlog, cache loss, or controller actions form a reinforcing [[Trace and Feedback|feedback]] loop, the system can enter [[Metastability|a metastable regime]] that persists after the initiating disturbance ends. Returning to healthy throughput may then require admission below the ordinary sustainable rate, reserved recovery capacity, or an explicit operational intervention.

## Universal Scalability Law

The Universal Scalability Law gives a normalized capacity model for a fixed family of configurations and workloads:

$$
C(N)=\frac{N}{1+\alpha(N-1)+\beta N(N-1)}
$$

Here $N$ is the concurrency or resource population, $\alpha$ represents contention or serialized work, and $\beta$ represents coherency or crosstalk whose cost grows with the participant population. With $\beta=0$ and $\alpha>0$, added concurrency approaches a contention-limited ceiling. With $\beta>0$, capacity can peak and then decline. For $\beta>0$ and $0\leq\alpha<1$, the continuous optimum is:

$$
N_{\mathrm{opt}}=\sqrt{\frac{1-\alpha}{\beta}}
$$

The USL is a capacity law, not a latency model; [[Queueing Theory|queueing theory]] provides the complementary vocabulary for utilization, waiting, and backlog.

The law can be fitted to measured capacity across controlled configurations, but the fitted coefficients do not by themselves identify a causal mechanism. The boundary, workload mix, completion meaning, topology, and observation interval must remain comparable. Reconfiguration, nonstationary demand, changing service semantics, or persistent failures can make one fit misleading.

The USL term **coherency** should not be silently renamed coordination. [[Coordination]] is broader. A lock, barrier, singular authority, or serial commit path may contribute primarily to $\alpha$; quorum exchange, cache-coherence traffic, membership communication, or pairwise synchronization may contribute to $\beta$. One coordination mechanism may contribute to both depending on its topology and behavior.

## Contention, Coordination, and Churn

Contention, coordination, and churn form a practical diagnostic vocabulary across realization layers:

| Cost | Local manifestations | Distributed manifestations |
| --- | --- | --- |
| Contention | Locks, run queues, allocators, cache lines, memory bandwidth, connection pools | Hot partitions, leaders, shared databases, brokers, storage devices, network links |
| Coordination | Barriers, cache coherence, stop-the-world phases, shared-state synchronization | Consensus, quorums, global ordering, cross-partition transactions, leases, membership protocols |
| Churn | Thread or process turnover, connection cycling, cache invalidation, warmup, memory movement | Replica joins and leaves, elections, rebalancing, state transfer, routing convergence, repeated recovery |

Churn is not a third USL coefficient. It is time-varying reconfiguration and recovery work that consumes capacity, destroys [[Locality|locality]], changes the active topology, and can increase observed contention or coherency. If stable churn is included in measurements, fitted coefficients may absorb some of its cost descriptively; if churn changes during the experiment, the fixed-configuration interpretation may no longer hold.

Local and distributed costs compose. Adding application replicas may reduce local CPU contention while increasing database contention, connection pressure, membership work, cache invalidation, or cross-replica coordination. [[Synchrony and Asynchrony|Synchronization]] can concentrate these costs at locks, barriers, commit boundaries, quorums, or globally ordered positions, while asynchrony can defer them into queues, retained work, reconciliation, or later coordination. A scaling analysis must follow the bottleneck and feedback loops across the end-to-end [[Infrastructure Graph|infrastructure graph]].

Replicated and partitioned state adds explicit operational choices. [[Consensus]] can preserve one decision or order at quorum cost; [[CRDTs]] can avoid synchronous coordination only for compatible operations and invariants. Neither replication nor partitioning is a general escape from [[Authority|authority]], [[Identity|identity]], consistency, ordering, persistence, or recovery obligations.

[[Capacity Planning|Capacity planning]] uses measured scalability profiles, demand scenarios, provisioning lead times, and failure assumptions to establish capacity and reserve before it is needed. Dynamic scaling acts within that plan; it does not replace the plan's quotas, bottleneck analysis, or overload policy.

## Modeling and Measurement Checks

- What workload dimension is growing, and which dimensions are held fixed?
- What resource or topology dimension is changing?
- What boundary defines admission and useful completion?
- Which latency, correctness, availability, backlog, and cost constraints must hold?
- Are throughput counts attempts, physical effects, acknowledgments, or useful semantic completions?
- Where are the saturation knee, maximum sustainable capacity, and any retrograde region?
- Which contention, coordination, and churn costs are local, and which cross distributed boundaries?
- Does added capacity relieve the bottleneck or amplify demand on a shared dependency?
- Are measurements steady-state, transient, recovering, warming, draining, or rebalancing?
- Can admission control, concurrency reduction, coordination avoidance, or model changes improve capacity more than adding resources?
- Which identities, authorities, delivery, ordering, idempotency, persistence, and recovery guarantees must survive scaling?
- Do aggregate gains preserve fairness and service objectives for each relevant policy scope?

## Formal relations

- `qualifies`: [[Scaling Mechanisms]] — Defines the boundary-relative workload, resource population, useful-completion measure, and constraints by which a scaling mechanism is evaluated.
- `qualifies`: [[Infrastructure Graph]] — States capacity, contention, coordination, and churn properties that must be evaluated across the end-to-end topology.

## External References

- Neil J. Gunther, [A General Theory of Computational Scalability Based on Rational Functions](https://arxiv.org/abs/0808.1431), 2008.
- Neil J. Gunther, [Universal Scalability Law](https://www.perfdynamics.com/Manifesto/USLscalability.html), including its contention and coherency interpretation.
- Google, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/), especially overload protection, load shedding, and retry amplification.

Related concepts: [[Stuff Structure Property|stuff structure property]], [[Compositionality|compositionality]], [[Queueing Theory|queueing theory]], [[Trace and Feedback|trace and feedback]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Capacity Planning|capacity planning]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Locality|locality]], [[Metastability|metastability]], [[Routing Models|routing models]], [[Consumer Coordination|consumer coordination]], [[Coordination|coordination]], [[Recovery|recovery]], [[Boundaries|boundaries]], [[Compatibility and Evolution|compatibility and evolution]].
