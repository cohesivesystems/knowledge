---
realm: Realization Substrate
kind: realization-substrate
created: 2026-08-02
updated: 2026-08-02
status: draft
aliases:
  - Network Channel
  - Transport Channel
  - Communication Channel
---

# Network Channels

A network channel is a protocol-layer communication locus realized through network addresses, links, paths, datagrams, connections, streams, sessions, frames, buffers, and their control state. It is distinct from the provider-neutral [[Interaction Channels|interaction channel]] and is not a synonym for an application or messaging channel.

Network channels and messaging channels both expose transmission structures such as send, receive, direction, addressing, framing, sequencing, multiplexing, flow control, and completion. Their shared shapes support explicit correspondence. Their meanings and guarantees remain relative to different boundaries.

## Layer-Relative Send and Receive

Asynchronous send and receive form a minimal operation pair at many layers:

```text
send(value) -> local completion
receive()   -> locally admitted value
```

The shared form does not give `send` one universal completion meaning. Completion can report admission to a local socket buffer, protocol stack, broker client, broker store, remote transport peer, messaging endpoint, or application handler. Each layer may introduce its own send, receive, acknowledgment, retry, timeout, and failure occurrences while realizing one higher-layer send.

Likewise, one network receive can deliver bytes or a datagram without admitting a complete message, satisfying a subscription, settling a broker delivery, or activating the intended semantic observer. The correspondence must name the transmitted unit and boundary at every layer.

## Network Channel Forms

Representative network-channel forms include:

- best-effort packet or datagram paths;
- reliable ordered byte-stream directions inside a connection;
- framed message channels inside a connection or session;
- independently identified streams multiplexed over one transport association;
- multicast or group-addressed delivery;
- request/reply exchanges over stateless or connection-oriented application protocols; and
- resumable sessions that preserve bounded protocol state across replacement transport connections.

These forms describe protocol and transport mechanisms. They do not supply broker retention, durable subscription identity, application replay, provider settlement, semantic correlation, or business completion unless an explicit higher-layer composition establishes those properties.

## Correspondence with Messaging Channels

The relation between messaging and network channels is generally many-to-many rather than one channel over one connection.

| Messaging arrangement | Network realization structure | Required correspondence |
| --- | --- | --- |
| direct point-to-point send | one or more datagram, stream, or invocation exchanges | Preserve recipient selection, framing, delivery boundary, and completion meaning. |
| brokered publication | producer-to-broker exchange, broker state, and broker-to-consumer exchanges | Do not identify broker admission, storage, consumer delivery, or application commitment. |
| publish-subscribe | publications plus subscription-control and delivery exchanges across changing sessions | Preserve subscriber identity and fanout independently of connection identity. |
| request/reply | one coupled invocation/session or paired request and reply paths | Preserve two logical directions, request identity, reply correlation, and terminal obligations. |
| durable log or queue | network client protocols composed with retained storage, cursor state, and consumer coordination | Do not derive retention, replay, or progress from transport reliability alone. |
| multiplexed messaging lanes | several logical channels over one connection or transport stream set | Preserve lane discrimination, isolation, ordering scopes, and flow-control ownership. |
| one durable messaging channel across reconnects | a succession of network connections and protocol sessions | Distinguish session resume from replay and preserve stable logical identity across attempts. |

A broker-mediated messaging channel is therefore usually not one network edge. It is a higher-layer channel realized by a graph of network channels, broker storage, routing, consumer state, and control protocols. Conversely, HTTP/2, QUIC, WebSocket subprotocols, or broker client connections can multiplex several logical messaging channels over one network association.

## Preservation Dimensions

Lowering a messaging channel into network channels should state the mapping for each dimension independently:

### Direction and Topology

A one-way messaging direction may use a bidirectional network connection because acknowledgments, credits, negotiation, heartbeats, and failures travel in the reverse direction. Application fanout may be realized by network multicast, repeated unicast, broker-mediated delivery, or several independently established sessions. Similar arrow shape does not establish equivalent topology or failure behavior.

### Framing

A messaging channel carries shaped messages or envelopes. A network channel may preserve those boundaries natively, fragment them into frames or packets, or expose only a byte stream. When boundaries are reconstructed, the codec, maximum sizes, partial-input behavior, and malformed-frame policy become part of the realization evidence.

### Addressing, Endpoints, and Routing

A messaging address may name a topic, queue, subscription, key, reply target, service operation, actor, or logical endpoint. Network addressing may name interfaces, hosts, ports, peers, connections, or streams. [[Interaction Bindings|Bindings]], service discovery, broker routing, gateways, NAT, load balancing, and multiplexing can make the correspondence many-to-many and time-varying.

### Ordering and Reliability

Transport order applies inside a declared stream or connection. Messaging order may instead be scoped to a key, partition, session, topic, or durable log and can survive connection replacement. Transport retransmission can suppress some packet loss while application retries still duplicate messages. Reliability, delivery guarantee, and semantic idempotency remain distinct claims.

### Acknowledgment, Progress, and Settlement

Link acknowledgments, transport acknowledgments, application-protocol responses, broker publish confirmations, consumer settlement, replay cursors, and durable application progress report different occurrences. [[Delivery Progress and Settlement|Delivery progress and settlement]] defines the upper-layer distinctions that a network realization must preserve rather than flatten.

### Flow Control and Congestion Control

Transport receive windows protect transport buffers, while messaging credits, demand, prefetch, queue bounds, consumer concurrency, and admission policy protect other resources. One network flow-control loop may couple several multiplexed messaging channels and create head-of-line or fairness effects. End-to-end regulation therefore composes several local loops rather than inheriting one transport window unchanged.

### Security and Authority

Peer authentication, channel confidentiality, message authenticity, tenant authority, and semantic authorization can terminate at different boundaries. TLS can protect a network hop while a broker decrypts and reroutes the message; end-to-end message protection can outlive transport sessions. A realization must identify which identity and authority each security mechanism establishes.

## Declared Loss and Introduction

A network realization may introduce connection attempts, packets, retransmissions, handshakes, routing changes, fragmentation, buffering, congestion response, heartbeats, and transport-level errors that have no direct upper-layer semantic counterpart. It may forget message types, subscriber identities, domain authority, business correlation, or durable progress unless higher layers encode and preserve them.

The realization is acceptable only when those introduced mechanics do not violate upper-layer requirements and every forgotten distinction is reconstructed, shown irrelevant, or rejected explicitly. A provider name or protocol label alone is not evidence of preservation; the exact configured mode and boundary matter.

## Formal relations

- `may_realize`: [[Interaction Channels]] — A network channel or a graph of network channels can realize an interaction channel when framing, identity, topology, protocol, and operational requirements are preserved.

## External References

- IETF, [RFC 8200: Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200), 2017.
- IETF, [RFC 9293: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293), 2022.
- IETF, [RFC 9000: QUIC](https://www.rfc-editor.org/rfc/rfc9000), 2021.
- Gregor Hohpe and Bobby Woolf, [Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Network|network]], [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Messages and Envelopes|messages and envelopes]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Routing Models|routing models]], [[Interaction Control Flow|interaction control flow]], [[Flow Control|flow control]], [[Delivery Semantics|delivery semantics]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Ordering|ordering]], [[Brokers|brokers]], [[Realization|realization]].
