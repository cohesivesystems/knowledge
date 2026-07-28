---
realm: System Graph
kind: structural-construct
created: 2026-07-27
updated: 2026-07-27
aliases:
  - Message Channel
  - Message Channels
  - Channel Topology
---

# Interaction Channels

Interaction channels describe the structural loci through which values, messages, observations, signals, requests, replies, and events can move between observer boundaries.

A channel is not the whole [[Interaction|interaction]] and does not determine the semantic role of what it carries. It names a path, shared medium, address space, subscription surface, queue, log, topic, mailbox, stream, or other mediating locus in the system graph. The same channel can carry several semantic roles when their contracts remain distinguishable.

## Channel Topologies

- A **point-to-point channel** directs each delivery to one intended receiver or one effective receiver selected from a competing group.
- A **publish-subscribe channel** makes a publication available to independently interested subscriptions or observers.
- A **typed or datatype channel** constrains admissible message contracts or shapes.
- An **invalid-message or quarantine channel** separates material that cannot be admitted or processed under the active contract and policy.
- A **bridge** relates channels or messaging systems with distinct addressing, formats, guarantees, or administrative boundaries.
- A **message bus** arranges a shared integration surface over multiple channels, contracts, endpoints, and routing rules.

Topology alone does not imply ordering, retention, durability, exactly-once effects, consumer progress, or business completion. Those are operational claims supplied by [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Durability|durability]], [[Consumer Coordination|consumer coordination]], and [[Retention Expiration and Quarantine|retention, expiration, and quarantine]].

## Driving and Buffering

Channel topology also does not determine [[Interaction Control Flow|interaction control flow]]. The model should state separately whether producers push, consumers fetch, or a driver fetches from one port and pushes to another.

A queue commonly presents a passive sink to an active producer and a passive source to an active fetcher. It thereby changes the driver across the channel and allows arrival and departure cadence to vary independently. A push subscription may instead present an active sender toward the subscriber even when the service internally uses queues and worker drivers. These roles are relative to the declared public boundary; internal realization does not silently redefine the public contract.

## Placement and Realization

At one abstraction layer a channel is an edge between observers. At another it is a node with its own state, partitions, subscriptions, cursors, policies, and failure modes. [[Brokers|Brokers]], actor mailboxes, files, database tables, shared memory, sockets, logs, and runtime queues are possible realizations. Their local acknowledgments and identifiers remain scoped to their own boundaries.

## External References

- Gregor Hohpe and Bobby Woolf, [Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html), [Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html), and [Publish-Subscribe Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html), *Enterprise Integration Patterns*, 2003.
- Enterprise Integration Patterns, [Messaging Channels](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Messages and Envelopes|messages and envelopes]], [[Observer Models|observer models]], [[Flow Views|flow views]], [[Routing Models|routing models]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Consumer Coordination|consumer coordination]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Brokers|brokers]], [[Network|network]].
