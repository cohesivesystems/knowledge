---
realm: Operational Concerns
kind: operational-concern
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Load Distribution
  - Workload Balancing
  - Traffic Balancing
---

# Load Balancing

Load balancing governs how admitted work is distributed among eligible capacity-bearing destinations at a declared boundary so that service, capacity, fairness, locality, and failure objectives can be met.

It is an operational concern that qualifies a [[Routing Models|routing]] or dispatch choice. The system graph states the interaction endpoints, eligible destination set, channels, routing or dispatch locus, topology, affinity, and partition constraints. Load balancing states the policy and required behavior of the choice among those destinations. A DNS responder, proxy, gateway, broker coordinator, client library, runtime dispatcher, scheduler, or work-stealing pool is a possible [[Realization|realization]], not the definition of the concern.

Load balancing is therefore not an intrinsic property of every interaction edge. It applies where an interaction can be assigned across multiple eligible recipients, paths, partitions, replicas, workers, or resource pools. In a particular system graph, an architecturally visible balancing locus may appear as a node, intermediary service, or routing relation; that structural projection does not require a second system-graph concept named *load balancing*.

Load balancing can be viewed as [[Partitioning|partitioning]] and routing traffic. In the ordinary single-destination case, the selection policy partitions requests, connections, messages, or tasks into per-destination traffic flows, and [[Routing Models|routing]] carries each flow to its selected destination. Data partitioning applies the same shape to data: [[Partition Models|partition models]] assign data subjects to placement, ownership, storage, or ordering scopes, and routing directs data operations to the relevant partitions. Fanout, hedging, and replication use overlapping assignment rather than a strict disjoint partition, so their additional delivery and consistency obligations remain explicit.

## Boundary and Eligibility

A balancing claim must identify both the unit of work and the population across which it may be distributed. The work unit may be a request, connection, message, record, task, actor activation, query fragment, partition, tenant, flow, or weighted cost unit. A destination may be a service instance, replica, consumer, worker, shard, region, network path, accelerator, or another capacity-bearing locus.

Eligibility precedes optimization. A destination can be excluded or constrained by:

- interface and protocol compatibility;
- identity, [[Authority|authority]], tenancy, or policy scope;
- partition ownership, ordering, or single-writer rules;
- locality, affinity, residency, or failure-domain policy;
- health, readiness, draining, or recovery state;
- resource capability and current capacity; and
- delivery, durability, consistency, or service-level requirements.

Balancing must not route around a semantic or correctness constraint merely to improve utilization. A replica that can serve a stale read is not necessarily eligible for a linearizable read, and a warm worker with cached state does not acquire authority over that state merely by being selected.

## Policy Families

Common policy families include:

- round-robin, random, or weighted distribution;
- least outstanding work, shortest queue, or least observed load;
- latency, cost, or capacity-aware selection;
- affinity, hashing, rendezvous hashing, or partition-directed selection;
- locality, zone, or failure-domain-aware selection;
- work sharing, work stealing, or pull-based claiming; and
- randomized sampling such as choosing the better of a small number of candidates.

These policies optimize different objectives and observe different state. Equal request counts do not imply equal work, equal resource demand, equal completion time, or equal service. Affinity can improve [[Locality|locality]] while creating hotspots. Spreading work can improve capacity utilization while increasing cache misses, state movement, cross-zone traffic, or correlated dependency load.

Static policies use configured topology, weights, or deterministic keys. Dynamic policies use observations such as queue depth, in-flight work, latency, saturation, health, or recent outcomes. Those observations are delayed and boundary-relative. A target reported as healthy may have no spare capacity, and a target reported as lightly loaded may already have work in transit.

## Control and Stability

Dynamic load balancing is a feedback-control problem. Observations estimate destination state; selection policy changes future arrivals; completions, failures, scaling, and reconfiguration change the observed population again. Measurement delay, synchronized clients, rapidly changing weights, health flapping, and aggressive evacuation can cause oscillation or herd behavior.

The policy should account for:

- observation delay and uncertainty;
- the cost and cadence of membership or weight changes;
- in-flight work when a destination drains, fails, or loses ownership;
- hysteresis, damping, randomized choice, or bounded movement;
- cold-start, cache-warmup, and state-transfer costs;
- reserved capacity for recovery or high-priority work; and
- interaction with autoscaling, retries, failover, and admission control.

Several locally balancing layers need not produce a balanced end-to-end system. Client-side selection, a gateway, a broker, a worker pool, and a database router may each distribute work while concentrating it on the same partition, dependency, authority, or failure domain. The relevant objective must be evaluated at the boundary of useful completion, not only at the nearest dispatcher.

## Distinctions

| Concept | Governing question |
| --- | --- |
| [[Routing Models\|routing]] | Which destination, recipient, or path does the system graph permit or select? |
| **load balancing** | How should admitted work be distributed across eligible capacity so declared operational objectives hold? |
| [[Consumer Coordination\|consumer coordination]] | How do consumers discover, claim, own, and complete available work? |
| [[Scheduling]] | Which enabled and admitted work receives execution opportunity next? |
| [[Flow Control\|flow control]] | How does available capacity regulate how much work may progress across a boundary? |
| [[Admission Control and Load Shedding\|admission control and load shedding]] | Which offered work should be accepted, refused, redirected, degraded, or discarded? |
| [[Scaling Mechanisms\|scaling]] | How is the capacity-bearing population or topology changed? |

These concerns compose. A balancer selects among eligible destinations; admission control may reject work when none has safe capacity; flow control changes how much work reaches the balancing boundary; consumer coordination preserves assignment and ownership; scheduling chooses among work already assigned; and scaling changes the future destination population.

Load balancing also does not by itself provide availability, exactly-once effects, ordering, completion, or fairness. Retrying against a different target can improve liveness while creating duplicate attempts or reordered effects. Session affinity can preserve locality without proving identity, ownership, durability, or consistency. Failover is a change in eligibility under a failure policy, not evidence that the alternate destination can preserve every guarantee of the original.

## Modeling and Measurement Checks

- What unit of work is distributed, and how is its cost estimated?
- At which interaction, routing, dispatch, or claiming boundary is the choice made?
- Which destinations are eligible, and which semantic, authority, locality, partition, or failure constraints restrict them?
- Which objective is being optimized: latency, useful throughput, utilization, fairness, cost, locality, availability, or recovery?
- Which observations drive selection, how stale can they be, and what state is hidden or in flight?
- Is the policy static or dynamic, centralized or distributed, deterministic or randomized?
- What happens to work during draining, failure, membership change, rebalance, or stale ownership?
- How do retries, hedging, fanout, admission, flow control, scheduling, and scaling alter effective load?
- Are fairness and service levels evaluated per tenant, class, key, partition, region, and failure domain rather than only in aggregate?
- Do measurements count arrivals, attempts, assignments, resource cost, acknowledgments, or useful semantic completions?
- Can the balancing loop oscillate, synchronize clients, amplify churn, or enter a [[Metastability|metastable regime]]?

## Formal relations

- `qualifies`: [[Routing Models]] — States the operational policy and objectives by which routing or dispatch distributes admitted work among eligible capacity-bearing destinations at a declared boundary.

## External References

- Google, [Load Balancing at the Frontend](https://sre.google/sre-book/load-balancing-frontend/), *Site Reliability Engineering*, 2016.
- Google, [Load Balancing in the Datacenter](https://sre.google/sre-book/load-balancing-datacenter/), *Site Reliability Engineering*, 2016.

Related concepts: [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Partitioning|partitioning]], [[Partition Models|partition models]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Consumer Coordination|consumer coordination]], [[Service Models|service models]], [[Interfaces|interfaces]], [[Policy Scopes|policy scopes]], [[Boundaries|boundaries]], [[Scalability|scalability]], [[Locality|locality]], [[Fairness|fairness]], [[Scheduling|scheduling]], [[Flow Control|flow control]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Rate Limiting|rate limiting]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Service Levels|service levels]], [[Observability and Provenance|observability and provenance]], [[Trace and Feedback|trace and feedback]], [[Metastability|metastability]], [[Scaling Mechanisms|scaling mechanisms]], [[Network|network]], [[Brokers|brokers]], [[Runtimes|runtimes]], [[Application Hosts|application hosts]], [[Compute|compute]].
