---
realm: Architecture Practices
kind: architecture-practice
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Demand Forecasting and Capacity Planning
  - Capacity Management
  - Resource Capacity Planning
---

# Capacity Planning

Capacity planning is an architecture and operational practice for relating expected demand, service objectives, failure assumptions, and provisioning lead times to the effective capacity and reserve a system must have available.

The practice does not equate raw resources with useful service. It uses a declared [[Scalability|scalability]] profile to relate workload to completed outcomes, identifies bottlenecks and amplification across the [[System Graph|system graph]], and selects public [[Scaling Mechanisms|scaling mechanisms]] and operational controls that can supply or protect capacity before it is needed.

## Conceptual Trace

In [[Stuff Structure Property|stuff, structure, and property]] terms, a capacity plan relates:

- **Stuff:** workload populations, data, requests, events, tenants, resources, replicas, partitions, queues, and retained work.
- **Structure:** service and interaction topology, routing, fanout, feedback, ownership, placement, scheduling, and failure domains.
- **Properties:** throughput, latency, backlog, freshness, correctness, availability, recovery time, fairness, cost, and required headroom.

The plan is not itself a semantic workload, system graph, or infrastructure allocation. It is a cross-realm practice that records assumptions and evidence for how those layers are expected to behave together.

## Demand Model

Demand should be described as a multidimensional scenario rather than one request-rate forecast. Relevant dimensions include:

- Organic growth, launches, migrations, campaigns, batch windows, seasonality, and bursts.
- Dataset and working-set growth, tenants, keys, partitions, geographic span, and retention.
- Workload mix, job size, fanout, read/write ratio, deadlines, priority, and skew.
- Internal amplification from retries, polling, replay, replication, projection, and coordination.
- Concurrent failure, maintenance, deployment, recovery, backfill, and failover work.

External arrivals are not resource demand. One admitted input can create many internal visits, remote calls, writes, messages, retries, or effects. [[Queueing Theory|Service demand]] and visit ratios should be related to useful completion at the same boundary.

Forecasts contain uncertainty. A plan should use ranges and named scenarios, record confidence and lead time, and identify which observations would invalidate its assumptions. A single point forecast can hide correlated bursts, hot partitions, dependency limits, or a change in workload shape.

## Effective Capacity

Effective capacity is the sustainable useful service produced while the declared latency, correctness, availability, backlog, and cost constraints hold. It is not the sum of advertised CPU, instance, partition, storage, or network limits.

Capacity tests should locate bottlenecks, the saturation knee, any retrograde region, and behavior beyond the intended operating envelope. They should distinguish offered work, admitted work, attempts, useful completions, and unfinished backlog. Tests should also cover cold starts, cache loss, skew, degraded dependencies, failover, recovery traffic, and controller actions because nominal steady-state capacity may not be recoverable capacity.

[[Locality]] affects the conversion from resources to capacity. A failover pool with enough nominal compute may still underperform while working sets are cold, state is remote, partitions are moving, or the network carries displaced access. [[Coordination]] and consistency requirements likewise make some work non-parallel or add participant-dependent cost.

Capacity is not necessarily compositional. Each component can pass an isolated test while shared dependencies, synchronized bursts, fanout, or end-to-end tail latency constrain the composed system. See [[Compositionality|compositionality]].

## Headroom, Reserve, and Failure Assumptions

Headroom is capacity intentionally left unused under an ordinary planning condition. Its amount should follow from variability, forecast error, actuation delay, workload growth, and the chosen service objectives rather than one universal utilization target.

Reserve should be scoped by purpose. Serving reserve absorbs demand variation; failure reserve carries displaced work; recovery reserve supports replay, state transfer, cache warming, index rebuild, or catch-up; control-plane reserve keeps observation and intervention available during overload. The same nominal spare resource cannot be counted independently for several simultaneous scenarios unless the plan proves they cannot coincide.

A plan should name its failure assumptions: which node, zone, region, store, broker, network path, authority, or dependency may be unavailable; which maintenance and deployments may overlap; and how long provisioning or repair may take. [[Distributed Failure Scenarios|Distributed failure scenarios]] and [[Recovery|recovery]] define the events and obligations behind reserve calculations.

## Planning and Dynamic Control

Capacity planning and autoscaling operate at different horizons. A plan establishes the expected envelope, quotas, minimums, maximums, lead times, reserves, and escalation points. A [[Control Models|control model]] can adjust capacity inside the realizable part of that envelope through autoscaling or another actuator. It cannot create unavailable quota, shorten physical provisioning lead time, partition an unsplittable authority, or remove a shared bottleneck merely by increasing desired replicas.

[[Admission Control and Load Shedding|Admission control and load shedding]], [[Rate Limiting|rate limiting]], concurrency limits, and [[Flow Control|flow control]] protect the system when demand exceeds effective capacity or new capacity cannot arrive in time. They are part of a capacity strategy, not evidence that sufficient capacity was planned.

Plans should also account for [[Metastability|metastability]]. Recovery from an overloaded regime may require demand below the ordinary sustainable rate, reserved control or recovery capacity, staggered re-entry, or a deliberate reset of backlog, retries, caches, connections, leadership, or assignments.

## Planning Artifacts and Evidence

A useful capacity plan records:

- Workload dimensions, scenarios, forecasts, confidence, and review horizon.
- Useful-completion and service-objective boundaries.
- Resource demands, bottlenecks, locality, coordination, and shared dependencies.
- Load-test and production evidence, including behavior beyond the intended envelope.
- Current effective capacity, headroom, failure and recovery reserves, and cost.
- Scaling mechanisms, quotas, provisioning lead times, and scale lifecycle assumptions.
- Admission, degradation, shedding, and escalation policies when demand exceeds the plan.
- Owners, decision authority, observation signals, trigger thresholds, and review cadence.

The plan should be versioned against workload, service, topology, and realization assumptions. A capacity number without the configuration and evidence that produced it is not portable across versions.

## Failure Modes

- Forecasting only average request rate while ignoring bursts, skew, job size, fanout, or data growth.
- Treating resource inventory or vendor quotas as proven service capacity.
- Counting retries, attempts, or accepted work as useful completions.
- Planning each component independently while overlooking shared or end-to-end bottlenecks.
- Reserving nominal failover capacity without testing cold locality and recovery traffic.
- Depending on autoscaling beyond quota, placement, partition, or provisioning limits.
- Targeting steady-state utilization so tightly that no margin remains for variance or recovery.
- Adding capacity to clients of a constrained dependency and increasing overload.
- Leaving rejection, degradation, or business-priority decisions to an infrastructure default.

## External References

- Google, [Site Reliability Engineering: Demand Forecasting and Capacity Planning](https://sre.google/sre-book/introduction/), in *Site Reliability Engineering*, 2016.
- Neil J. Gunther, [*Guerrilla Capacity Planning: A Tactical Approach to Planning for Highly Scalable Applications and Services*](https://doi.org/10.1007/978-3-540-31010-5), Springer, 2007.
- Neil J. Gunther, [A General Theory of Computational Scalability Based on Rational Functions](https://arxiv.org/abs/0808.1431), 2008.
- John D. C. Little, [A Proof for the Queuing Formula: $L=\lambda W$](https://doi.org/10.1287/opre.9.3.383), *Operations Research* 9(3):383-387, 1961.

Related concepts: [[Architecture Practices|architecture practices]], [[Scalability|scalability]], [[Scaling Mechanisms|scaling mechanisms]], [[Control Theory|control theory]], [[Control Models|control models]], [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID control]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Locality|locality]], [[Metastability|metastability]], [[Queueing Theory|queueing theory]], [[Stuff Structure Property|stuff structure property]], [[Compositionality|compositionality]], [[Trace and Feedback|trace and feedback]], [[System Graph|system graph]], [[Infrastructure Graph|infrastructure graph]], [[Service Models|service models]], [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Boundaries|boundaries]], [[Policy Scopes|policy scopes]], [[Coordination|coordination]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Rate Limiting|rate limiting]], [[Flow Control|flow control]], [[Retry|retry]], [[Recovery|recovery]], [[Distributed Failure Scenarios|distributed failure scenarios]], [[Operational Control|operational control]], [[Observability and Provenance|observability and provenance]], [[Compute|compute]], [[Infrastructure|infrastructure]], [[Storage Systems|storage systems]], [[Network|network]].
