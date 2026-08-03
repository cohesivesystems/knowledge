---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Admission Control
  - Load Shedding
  - Overload Control
---

# Admission Control and Load Shedding

Admission control decides whether, when, and under which conditions work may enter a bounded system, service, queue, resource, process, or authority scope. Load shedding deliberately refuses, drops, cancels, expires, samples, redirects, or degrades selected work when serving everything would violate more important service or progress constraints.

The two concerns are related but not identical. Admission control governs the boundary where responsibility for work is accepted. Load shedding is an overload response that may operate at that boundary or, with stricter obligations, on work already admitted. Both seek to preserve useful service rather than maximize accepted attempts.

## Admission Boundary

An admission decision should identify:

- The offered unit of work and its identity, class, tenant, cost, priority, deadline, and authority.
- The [[Boundaries|boundary]] being protected and the constrained resource or downstream dependency.
- The observations and [[Policy Scopes|policy scope]] used to decide.
- Whether the outcome is accept, refuse, defer, redirect, degrade, sample, or admit under a narrower contract.
- What response, acknowledgment, retry advice, or terminal outcome communicates that decision.
- Which accepted obligations begin at admission and which begin only at a later [[Commit Boundaries|commit boundary]].

Refusal before acceptance does not create the same obligations as discarding work after acceptance. Once an interface or [[Interaction Protocols|interaction protocol]] has established responsibility, shedding cannot silently erase it. Cancellation, expiry, quarantine, compensation, reconciliation, or terminal failure must preserve the declared [[Delivery Semantics|delivery]], acknowledgment, and effect meanings.

Admission success is also not useful completion. It states that work crossed one boundary under one policy. The work may still wait, fail, retry, commit, or complete at later boundaries.

## Load Shedding

Load shedding protects a constrained boundary by spending little or no additional work on selected demand. Early shedding is usually cheaper because it avoids queueing, parsing, allocation, fanout, remote calls, locks, transactions, and effects that would otherwise be abandoned later.

Common policies include:

- Rejecting new work when concurrency, queue age, memory, saturation, or another capacity signal crosses a threshold.
- Reserving capacity for high-priority, recovery, control-plane, or already-admitted work.
- Serving a cheaper degraded result under an explicitly weaker contract.
- Sampling or coalescing observations when every individual update is not required.
- Expiring work whose deadline or usefulness horizon has passed.
- Redirecting work only when the alternate boundary has capacity and preserves the required semantics.

Shedding policy must state who bears the loss and how it is observed. Aggregate success can hide systematic rejection of one tenant, key, region, or work class, so [[Fairness|fairness]], priority, quotas, and starvation behavior are part of the claim.

## Related Controls

Admission control composes with several controls without becoming synonymous with them:

| Concern | Primary question |
| --- | --- |
| [[Rate Limiting\|Rate limiting]] | How quickly may a subject offer, admit, or execute work under a time-based budget? |
| Concurrency limiting | How much admitted work may remain in flight at once? |
| [[Flow Control\|Flow control]] | How does capacity information or demand regulate work across an interaction edge? |
| [[Control Models\|Adaptive feedback control]] | How should observations regulate a manipulated limit or policy toward an objective? |
| [[Scheduling]] | Which admitted work receives the next execution opportunity? |
| Circuit breaking | Should attempts to a dependency be suppressed because its recent outcomes indicate unavailability or failure? |
| [[Routing Models\|Routing]] | Which eligible destination or path should receive the work? |
| [[Scaling Mechanisms\|Autoscaling]] | Should resource capacity or topology be changed in response to observed demand? |

One system may apply all of these at different boundaries. A global rate budget can coexist with per-tenant concurrency limits, receiver-issued credits, priority scheduling, dependency circuit breakers, route selection, and a capacity controller.

## Useful Throughput and Stability

Admission control can increase [[Scalability|useful throughput]] when unrestricted arrivals would push the system into a contention, coordination, queueing, or coherency-dominated region. Reducing admission at one boundary can increase successful completions at another by lowering aborts, timeouts, retries, context switching, cache disruption, and recovery work.

For admitted arrival rate $\lambda$ and sustainable effective service capacity $\mu$, persistent admission above capacity grows backlog when $\lambda>\mu$. A safe policy needs margin for variability, tail service demand, failures, and measurement delay rather than targeting equality continuously.

Admission and shedding are [[Trace and Feedback|feedback]] controls. Delayed or correlated decisions can oscillate, shift overload downstream, or synchronize clients into retries. A refusal that immediately produces an unbudgeted retry is deferred amplification rather than effective load reduction.

These loops are also important defenses against [[Metastability|metastability]]. Recovery may require reducing admitted work below the ordinary sustainable rate so backlog, retry populations, caches, pools, leadership, or replicas can return to a healthy regime. Recovery and control traffic may need reserved capacity so the mechanism required to escape overload is not itself shed.

## Failure Modes

- A limit protects the front end while a shared downstream dependency remains overloaded by fanout or retries.
- Work is rejected after expensive processing has already consumed the constrained resource.
- Retry advice causes synchronized or unlimited re-entry.
- Per-instance limits allow aggregate admission to grow with replica count and overwhelm a shared dependency.
- A global limit preserves aggregate throughput while starving one tenant, partition, or priority class.
- Health or utilization signals arrive too late, causing alternating over-admission and underuse.
- Already-admitted obligations are dropped without a valid cancellation, expiry, or terminal-failure meaning.
- Recovery, telemetry, or control-plane work is shed together with ordinary demand, preventing stabilization.

## Modeling Checks

- Where does offered work become admitted responsibility?
- Which resource, authority, or downstream boundary is being protected?
- What quantity is limited: requests, bytes, cost units, concurrency, memory, queue age, or another demand measure?
- Which observation proves capacity pressure, and how delayed or incomplete can it be?
- Which work classes may be refused, delayed, degraded, or reserved?
- What does the caller observe, and which retry behavior is safe?
- What happens to work already admitted or partially committed?
- Can local policies compose without exceeding a shared distributed limit?
- Does the policy maximize useful completions rather than attempts or raw utilization?
- Which intervention restores progress if the system enters a metastable regime?

## External References

- Google, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/), especially overload protection, early rejection, load shedding, and retry amplification.
- Hao Xu and Juan A. Colmenares, [Admission Control with Response Time Objectives for Low-latency Online Data Systems](https://arxiv.org/abs/2312.15123), 2023.

Related concepts: [[Scalability|scalability]], [[Metastability|metastability]], [[Control Theory|control theory]], [[Control Models|control models]], [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID control]], [[Queueing Theory|queueing theory]], [[Trace and Feedback|trace and feedback]], [[Boundaries|boundaries]], [[Policy Scopes|policy scopes]], [[Authority|authority]], [[Identity|identity]], [[Interaction|interaction]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Commit Boundaries|commit boundaries]], [[Rate Limiting|rate limiting]], [[Flow Control|flow control]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Routing Models|routing models]], [[Retry|retry]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Operational Control|operational control]], [[Observability and Provenance|observability and provenance]], [[Scaling Mechanisms|scaling mechanisms]].
