---
realm: System Graph
kind: structural-construct
created: 2026-07-27
updated: 2026-08-02
status: draft
aliases:
  - Interaction Channel
  - Message Channel
  - Message Channels
  - Channel Topology
---

# Interaction Channels

An interaction channel is a provider-neutral logical exchange through which values, messages, observations, signals, requests, replies, events, or framed data can move among [[Endpoints|endpoints]]. It gives the exchange a stable structural locus, identifies its logical directions, and provides scopes to which required observable properties can be attached.

Channels, [[Interfaces|interfaces]], and [[Interaction Protocols|interaction protocols]] describe distinct aspects of an [[Interaction|interaction]]. An interface defines the roles and semantic obligations available at a boundary. A protocol constrains their legal traces. A channel arranges how occurrences can move between attached endpoints. An [[Interaction Bindings|interaction binding]] relates those distinct structures without making them synonymous.

## Exchanges and Directions

A **channel exchange** is the complete logical channel arrangement. A **channel direction** is one independently identified flow inside that exchange. Direction identity matters because ordering, routing, delivery, progress, settlement, cancellation, and failure may differ by direction.

The minimal exchange forms are:

- A **one-way exchange** has one logical producer-to-consumer direction.
- A **request/reply exchange** has distinct request and reply directions.

Request/reply can be bound in two important ways:

- A **coupled exchange** carries both directions through one invocation, connection, or session channel.
- **Paired channels** carry request and reply through two independently realized one-way channels.

Even in a coupled HTTP, RPC, or session realization, request and reply retain different roles, direction identities, carried emission identities, and completion meanings. Conversely, two correlated broker channels can realize one request/reply protocol without becoming one physical transport connection. The channel topology alone does not establish the semantic obligation that a reply discharges; that belongs to the interface contract, protocol, and binding.

## Channel Dimensions

Channel topology is better described by independent dimensions than by one undifferentiated channel type:

| Dimension | Representative forms |
| --- | --- |
| exchange | one-way, coupled request/reply, paired request/reply |
| distribution | point-to-point, competing consumers, fanout, selective delivery |
| interaction shape | fire-and-forget, publication, unary invocation, request stream, response stream, bidirectional stream, datagram, correlated request/reply |
| routing | operation endpoint, topic or filter, key or session affinity, connection or stream, explicit response target |
| framing | typed value, framed message, datagram, byte stream with reconstructed boundaries |
| mediation | direct, queued, logged, brokered, bridged, or bus-mediated |

An interaction shape is a coarse, protocol-neutral exchange morphology. It says, for example, that one request is followed by a response stream or that two ordered streams are independently active. It is not the complete legal trace, semantic outcome contract, or failure protocol.

Several logical directions or channels may share one underlying locus through [[Multiplexing and Demultiplexing|multiplexing]]. A discriminator can recover a channel, direction, invocation, stream, partition, tenant, or endpoint from the shared flow. Sharing a connection, topic, worker pool, or transport does not erase the distinct interfaces or semantics of the multiplexed lanes.

## Messaging Channels

A messaging channel is an interaction-channel specialization whose carried units are [[Messages and Envelopes|messages or envelopes]] and whose endpoints participate through messaging operations such as publish, send, receive, fetch, subscribe, settle, or replay.

Common arrangements include:

- A **point-to-point channel** selects one intended receiver or one effective receiver from a competing group.
- A **publish-subscribe channel** makes a publication available to independently interested subscriptions or observers.
- A **typed or datatype channel** restricts admissible message contracts or shapes.
- An **invalid-message or quarantine channel** separates material that cannot be admitted or processed under the active contract and policy.
- A **bridge** relates channels or messaging systems with different addressing, formats, guarantees, or administrative boundaries.
- A **message bus** arranges a shared integration surface over multiple channels, contracts, endpoints, and routing rules.

A messaging channel is not necessarily one network connection. Broker-mediated publication commonly composes a producer-to-broker network exchange, durable broker state, and one or more broker-to-consumer exchanges. One messaging channel can survive many network sessions, while one network connection can multiplex many messaging channels. [[Network Channels|Network channels]] give the realization-substrate peer of this channel notion and state the preservation conditions between the layers.

## Scoped Requirements

A channel definition can attach observable requirements to the complete exchange or to one exact direction. Those requirements may concern:

- distribution, routing, acquisition isolation, framing, and boundary preservation;
- retention, replay, delivery guarantees, reliability, and ordering scope;
- [[Delivery Progress and Settlement|durable progress and provider settlement]];
- [[Flow Control|flow control]], stream completion, cancellation, and session continuity;
- [[Commit Boundaries|atomic coupling]] among publication, consumption, state mutation, progress, and settlement;
- transport security and operating limits.

The channel supplies the structural scope for these demands; it does not move their definitions into the System Graph realm. [[Delivery Semantics|Delivery semantics]], [[Ordering|ordering]], [[Durability|durability]], [[Flow Control|flow control]], [[Commit Boundaries|commit boundaries]], security, and capacity remain operational concerns. A concrete target must supply attributable capability evidence for the exact configured mode in which it claims to meet them.

Capabilities from incompatible modes must not be spliced into a fictitious realization. A target that can provide reliable ordered streams in one configuration and unreliable datagrams in another has two coherent alternatives, not one channel with every property. Compiler-like [[Realization|realization]] selects one coherent capability profile, records how each requirement is preserved, and keeps derived topics, subscriptions, addresses, codecs, and client handles outside the channel's semantic authority.

## Identity, Progress, and Settlement

Several channel-relative identities and evidence forms must remain distinct:

- **Logical emission identity** identifies the carried publication, request, reply, or other emission across attempts and realizations.
- **Provider delivery identity** identifies provider-managed redelivery when the provider establishes a stable identity.
- **Delivery-attempt identity** identifies one physical attempt and changes on redelivery.
- **Settlement authority** is the possibly ephemeral receipt, lock, lease, token, or protocol authority needed to alter current provider delivery state.
- **Replay position** selects retained input.
- **Durable application progress** proves what the consuming application has durably applied or left pending.
- **Settlement evidence** proves which provider state was changed after which durable progress boundary.

None of these identities silently substitutes for another. A broker offset is not automatically application progress; a transport acknowledgment is not provider settlement; provider settlement is not business completion.

## Driving and Buffering

Channel topology does not determine [[Interaction Control Flow|interaction control flow]]. The model should state separately whether producers push, consumers fetch, or a driver fetches from one endpoint and pushes to another.

A queue commonly presents a passive sink to an active producer and a passive source to an active fetcher. It changes the driver across the channel and allows arrival and departure cadence to vary independently. A push subscription may instead present an active sender toward the subscriber even when the service internally uses queues and worker drivers. These roles are relative to the declared public boundary; internal realization does not silently redefine the public contract.

## Placement and Realization

At one abstraction layer a channel is an edge between endpoints. At another it is a node with state, partitions, subscriptions, cursors, policies, and failure modes. [[Brokers|Brokers]], actor mailboxes, files, database tables, shared memory, sockets, logs, runtime queues, and [[Network Channels|network channels]] are possible realizations or constituents of realizations. Their acknowledgments, addresses, and identifiers remain scoped to their own boundaries.

## Formal relations

- `arranges`: [[Interaction]] — An interaction channel places logical exchanges and directions among endpoints without defining the carried interaction's semantic role.

## External References

- Gregor Hohpe and Bobby Woolf, [Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html), [Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html), and [Publish-Subscribe Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html), *Enterprise Integration Patterns*, 2003.
- Enterprise Integration Patterns, [Messaging Channels](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Messages and Envelopes|messages and envelopes]], [[Observer Models|observer models]], [[Flow Views|flow views]], [[Routing Models|routing models]], [[Delivery Semantics|delivery semantics]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Ordering|ordering]], [[Consumer Coordination|consumer coordination]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Brokers|brokers]], [[Network Channels|network channels]], [[Network|network]].
