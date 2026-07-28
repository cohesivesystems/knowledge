---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-07-27
aliases:
  - Consumer Groups
  - Subscription Coordination
---

# Consumer Coordination

Consumer coordination describes how eligible observers discover, claim, receive, schedule, and complete work made available through an interaction channel.

Consumer activation and work assignment are distinct:

- A **polling consumer** chooses when to request or inspect available work.
- An **event-driven consumer** is activated when the runtime or channel reports available work.
- **Competing consumers** arbitrate which eligible consumer receives or claims each item.
- A **dispatcher** assigns admitted work among consumers.
- A **selective consumer** declares or applies an eligibility predicate.
- A **durable subscriber** preserves subscription identity and consumption position across disconnection or failure.

These arrangements realize [[Observer Models|observer models]] and [[Interaction Channels|channel topologies]]; they do not define the semantic role of the carried value.

They also expose different [[Interaction Control Flow|interaction-control roles]]. A polling consumer is an active fetcher at the channel boundary. An event-driven consumer is a passive sink relative to the runtime or channel that activates it. That public activation may still be realized internally by a hidden polling driver, queue, callback dispatcher, or worker pool, so push or pull must always be stated at a declared boundary.

## Coordination Obligations

The model should state:

- Subscription, group, member, assignment, lease, cursor, claim, and delivery identities.
- Whether one item is delivered to one member, each subscription, or several recipients.
- Partition affinity, ordering scope, exclusivity, and rebalancing rules.
- Poll cadence, activation fairness, concurrency limits, backpressure, and starvation risks.
- Which acknowledgment advances which cursor or releases which claim.
- What happens when a consumer loses ownership while its work is still running.
- How durable subscription state is retained, expired, reset, replayed, or migrated.

Competing consumption is an [[Arbitration|arbitration]] and [[Scheduling|scheduling]] problem. Fair scheduling does not imply eventual delivery when partitions, poison work, expired retention, unavailable consumers, or lost cursor state prevent progress. Fencing or expected assignment epochs may be required to prevent a stale consumer from committing after ownership changes.

## External References

- Enterprise Integration Patterns, [Messaging Endpoint patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).
- Gregor Hohpe and Bobby Woolf, [Polling Consumer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PollingConsumer.html), [Event-Driven Consumer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html), and [Competing Consumers](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html), *Enterprise Integration Patterns*, 2003.
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Observer Models|observer models]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Brokers|brokers]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Ordering|ordering]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Authority|authority]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Recovery|recovery]].
