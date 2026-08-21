---
realm: Architecture Practices
kind: reference
created: 2026-08-17
updated: 2026-08-17
status: draft
aliases:
  - Reactive Systems
  - Reactive System
---

# Reactive Manifesto

The Reactive Manifesto is a 2014 architecture declaration that characterizes reactive systems as responsive, resilient, elastic, and message-driven. It presents responsiveness as the intended service outcome, resilience and elasticity as ways to preserve that outcome through failure and changing workload, and asynchronous message passing as the interaction foundation supporting isolation, delegation, load management, and location transparency.

In Cohesive, this is a named cross-realm bundle rather than a new primitive or a guarantee established by adopting the label. Each claim must be restated at a declared [[Boundaries|boundary]], connected to the relevant system structure and operational concerns, and justified by a realization that preserves those requirements.

## Cohesive Correspondence

| Reactive trait | Cohesive correspondence | Qualification |
| --- | --- | --- |
| Responsive | [[Service Levels\|service levels]], [[Queueing Theory\|queueing theory]], [[Observability and Provenance\|observability and provenance]], and [[Operational Control\|operational control]] | Timely and consistent response is an observer- and boundary-relative service outcome. It requires an explicit latency or completion indicator, objective, workload scope, and evidence source rather than the unqualified adjective *responsive*. |
| Resilient | [[Failure Models\|failure models]], [[Boundaries\|boundaries]], [[Durability\|fate sharing]], [[Recovery\|recovery]], [[Replica Models\|replica models]], [[Partition Models\|partition models]], and [[Distributed Failure Scenarios\|distributed failure scenarios]] | Remaining responsive through failure depends on which faults are admitted, which components share a fate, where failure is contained, what material survives, and how authority and work recover. Replication, isolation, and delegation are design choices whose guarantees remain scoped. |
| Elastic | [[Scalability\|scalability]], [[Capacity Planning\|capacity planning]], [[Control Models\|control models]], [[Scaling Mechanisms\|scaling mechanisms]], [[Load Balancing\|load balancing]], and [[Admission Control and Load Shedding\|admission control and load shedding]] | Elasticity is the timely and safe acquisition and release of effective capacity under changing demand. Autoscaling, replication, and sharding are possible mechanisms; none proves elasticity or continued responsiveness by itself. |
| Message-driven | [[Interaction Modes\|interaction modes]], [[Asynchronous Interaction Design\|asynchronous interaction design]], [[Messages and Envelopes\|messages and envelopes]], [[Interaction Channels\|interaction channels]], [[Interaction Protocols\|interaction protocols]], [[Flow Control\|flow control]], and [[Synchrony and Asynchrony\|synchrony and asynchrony]] | Explicit asynchronous messaging separates emission, admission, delivery, interpretation, commitment, and recovery boundaries. Loose coupling, backpressure, location transparency, and non-blocking execution require additional protocol and realization claims; they do not follow from using messages alone. |

## Practices and Boundaries

### Define responsiveness as service behavior

Responsiveness should be expressed through [[Service Levels|service-level]] indicators and objectives such as completion latency, availability, freshness, rejection rate, or oldest-work age for a stated consumer population and workload. Averages alone do not establish the manifesto's emphasis on consistent response or reliable upper bounds. Percentiles, deadline attainment, tail behavior, and degraded outcomes need explicit observation rules.

[[Queueing Theory|Queueing theory]], [[Capacity Planning|capacity planning]], and [[Observability and Provenance|observability and provenance]] provide the capacity model and evidence needed to interpret those objectives. A quick transport acknowledgment or admission decision is not necessarily a timely semantic completion.

### Contain failure and make recovery explicit

Resilience begins with a [[Failure Models|failure model]] and explicit fate-sharing boundaries. [[Partition Models|Partition models]] and [[Replica Models|replica models]] can arrange failure domains, redundant roles, and recovery paths, while [[Recovery|recovery]] states how coherent operation resumes. Replication improves availability only for the faults, authority transitions, and correlated-failure assumptions its protocol covers.

The manifesto's recovery delegation is a responsibility and protocol relationship, not one universal mechanism. [[Actor Model|Actor supervision]], a service failover controller, a process manager, or an operator can each realize a form of delegated recovery at a different boundary. The model must still identify who observes failure evidence, who has authority to restart or replace work, what is fenced, and what state survives.

Isolation is similarly overloaded. Failure containment, resource isolation, authority separation, transactional [[Isolation|isolation]], and independent deployment are different claims. A reactive design should name the one it depends on rather than infer all of them from a component boundary.

### Adapt capacity without hiding stability costs

[[Scalability|Scalability]] distinguishes elasticity from general capacity growth and from the mechanisms used to produce it. [[Scaling Mechanisms|Scaling mechanisms]] may resize resources, add or remove replicas, partition work, rebalance ownership, or change topology under a feedback controller. Effective capacity arrives only after allocation, readiness, routing, state transfer, authority handoff, and recovery obligations are satisfied.

Elastic control also needs a response when capacity cannot arrive in time. [[Flow Control|Flow control]], [[Rate Limiting|rate limiting]], [[Admission Control and Load Shedding|admission control and load shedding]], bounded queues, and priority policies protect useful progress. Scaling, retry, and recovery loops can instead amplify overload or create [[Metastability|metastability]] when they compete for the same constrained resources.

### Use messages as explicit interaction boundaries

The manifesto's message-driven claim combines several distinct selections from the broader [[Interaction Modes|interaction-mode]] profile:

- **Mediation:** components use explicit [[Messages and Envelopes|message]] carriers through [[Interaction Channels|channels]] rather than treating direct invocation or shared state as the component interaction primitive.
- **Synchronization:** send, receipt, processing, and reply remain separate [[Synchrony and Asynchrony|asynchronous]] occurrences unless a protocol explicitly joins them through acknowledgment, response, rendezvous, or commit.
- **Component structure:** logical addressing, isolation, mailboxes, placement, and supervision can be realized by [[Actor Model|actor-style]] systems, but the actor model is one realization of the profile rather than its definition.
- **Runtime progress:** a pending logical operation can suspend its continuation so an OS thread can execute other work instead of remaining occupied by the wait. This non-blocking runtime property is separate from logical asynchrony and depends on the selected runtime, I/O, scheduling, and [[Progress Conditions|progress]] mechanisms.

These selections vary independently. An asynchronous message send can still block an OS thread when a mailbox is full or a transport call waits. A direct invocation can return a future whose continuation resumes without blocking a thread. Shared-state observation can be polled or signaled asynchronously. [[Asynchronous Interaction Design|Asynchronous interaction design]] accounts for the commit, capacity, ordering, acknowledgment, timeout, cancellation, and recovery meanings created by the selected profile.

Message-driven is broader than [[Event-Driven Architecture|event-driven architecture]]. Messages may carry commands, requests, replies, events, observations, control signals, credits, or failure reports. Calling every message an event would erase the participant intent and protocol role that the carrier is meant to preserve.

Backpressure is capacity feedback made effective through [[Flow Control|flow control]]. A queue merely accumulates work unless it is bounded and its capacity state changes upstream admission or demand.

Location-transparent addressing can give local and remote interaction a similar programming form, especially in [[Actor Systems|actor systems]], but that is not always desirable. A uniform address must not conceal [[Locality|locality]], latency, serialization, bandwidth, transport cost, partitions, topology, delivery ambiguity, security, administration, or failure boundaries from the system and operational models. The [[Fallacies of Distributed Computing|fallacies of distributed computing]] make these hidden assumptions explicit. Placement constraints, data affinity, region or zone selection, failure-domain separation, and prohibitions on remote execution may need to remain visible even when physical coordinates do not.

## Composition Limit

The manifesto says reactive properties should apply at every scale, but [[Compositionality|composition]] is not automatic. Components that each meet a latency target can violate the end-to-end target through serial dependencies, fanout, retries, shared bottlenecks, correlated failures, or reconfiguration. Message boundaries can isolate cadence while introducing backlog and recovery coupling. Replicas can improve read capacity while reducing write capacity or enlarging coordination cost.

A reactive-system claim should therefore state the observer, service boundary, workload envelope, failure model, topology, protocol, and realization configuration at which responsiveness, resilience, and elasticity have been demonstrated.

## Modeling Checks

- Which service outcome and response-time distribution define responsiveness, for which observer and workload?
- Which faults and correlated failure domains must the system tolerate while preserving that outcome?
- Where are failure, resource, authority, and commit boundaries, and which of them are intentionally isolated?
- Who observes and classifies failure, who has recovery authority, and what durable material supports recovery?
- Which workload signal drives elastic action, and how long until requested capacity becomes effective capacity?
- How are admission, flow control, shedding, and degraded service handled when scaling is late or impossible?
- Which message roles, channels, protocols, acknowledgments, ordering scopes, and completion meanings are explicit?
- Which parts of location transparency are programming convenience, and which locality and failure differences remain operationally visible?
- Which interaction-mode, synchronization, actor-structure, and runtime-progress claims are intended, and which are merely suggested by the word *message-driven*?
- Which claims compose end to end, and which must be re-established for the larger system boundary?

## Formal relations

- `documents`: [[Service Levels]] — Maps manifesto responsiveness to measurable, boundary-relative service outcomes rather than treating it as an intrinsic component label.
- `documents`: [[Failure Models]] — Maps manifesto resilience to explicit fault assumptions, containment scopes, fate sharing, and recovery obligations.
- `documents`: [[Scalability]] — Maps manifesto elasticity to timely and safe capacity adaptation while keeping the property distinct from autoscaling and other mechanisms.
- `documents`: [[Interaction Modes]] — Decomposes message-driven design into explicit mediation, exchange morphology, synchronization, interaction-control, and runtime-progress choices.
- `documents`: [[Asynchronous Interaction Design]] — Maps manifesto message-driven design to the architectural obligations created by independently progressing interaction stages.
- `documents`: [[Progress Conditions]] — Separates non-blocking runtime progress from the logical asynchrony of send, receipt, processing, and reply occurrences.
- `documents`: [[Locality]] — Qualifies location transparency as selective addressing indirection that must preserve latency, placement, cost, and failure consequences.

## External References

- Jonas Bonér, Dave Farley, Roland Kuhn, and Martin Thompson, [The Reactive Manifesto](https://www.reactivemanifesto.org/), version 2.0, September 16, 2014.
