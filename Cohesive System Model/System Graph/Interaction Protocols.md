---
realm: System Graph
kind: structural-construct
created: 2026-07-28
updated: 2026-08-06
status: draft
aliases:
  - Interaction Protocol
  - Conversation Protocol
  - Service Protocol
---

# Interaction Protocols

An interaction protocol describes the allowed temporal structure of [[Interaction|interactions]] through an [[Interfaces|interface]]. It constrains not only the values that may be exchanged, but also which roles may initiate, which occurrences may follow, how concurrent attempts relate, and how a conversation completes, fails, is cancelled, or remains live.

An interface answers *what roles and obligations are available at a boundary*. A protocol answers *how participation in those roles may unfold over time*. An [[Interaction Channels|interaction channel]] supplies logical exchanges and directions over which protocol occurrences can move. An [[Interaction Bindings|interaction binding]] assigns the interface and protocol roles to exact [[Endpoints|endpoints]] and channel directions.

## Protocol Contents

A protocol may declare:

- initiator, responder, producer, consumer, subscriber, or peer roles;
- request, reply, notification, acknowledgment, settlement, demand, and streaming sequences;
- conversational states and allowed transitions;
- correlation, causation, and response-obligation rules;
- ordering, concurrency, and arbitration constraints;
- retry, duplication, deduplication, and idempotency expectations;
- timeout, cancellation, compensation, and failure behavior;
- half-close, terminal completion, session, or connection lifetime; and
- negotiation, compatibility, versioning, and evolution rules.

These rules may be explicit in a specification or merely assumed by implementations. Unstated protocols are still protocols; they are simply harder to validate, evolve, and operate.

## Interaction Shape and Full Protocol

A protocol-neutral **interaction shape** describes only the coarse morphology that a [[Interaction Channels|channel]] realization must support: fire-and-forget, publication, unary invocation, request stream, response stream, bidirectional stream, datagram, or correlated request/reply.

A full protocol adds the legal trace and meanings omitted by that shape. Two systems may both support unary invocation while disagreeing about admissible retries, cancellation, terminal errors, correlation, authority, or whether a response proves admission, commitment, or only protocol completion. Likewise, two bidirectional streams can expose different half-close, demand, resumption, and failure rules.

The interaction shape therefore belongs with channel topology as a provider-neutral realization demand, while the complete protocol remains the authority for legal conversations.

## Layered Protocols

Protocols compose across abstraction layers:

| Protocol layer | Representative responsibility |
| --- | --- |
| semantic or service protocol | Meaningful operations, participant obligations, admissible outcomes, and business-relative completion |
| interface protocol | Legal use of the roles exposed at one boundary |
| channel protocol | Observable delivery, demand, credit, settlement, cancellation, stream, and continuity behavior at one channel boundary |
| provider or application protocol | HTTP, RPC, AMQP, MQTT, WebSocket, broker, or custom protocol exchanges |
| transport and network protocol | Framing, addressing, streams, datagrams, retransmission, transport flow control, and connection lifecycle |

These layers can share an operation name or edge shape without sharing its meaning. Asynchronous send appears at messaging, runtime, and network boundaries, but completion may mean local buffer admission, broker acceptance, remote protocol receipt, or application commitment. One higher-level occurrence may lower into several request, acknowledgment, control, and retry occurrences at lower layers.

[[Network Channels|Network-channel]] protocols can realize messaging-channel behavior only when their composition with codecs, brokers, storage, adapters, and application logic preserves the required upper-layer trace. A transport connection can disappear and be replaced while a durable subscription protocol continues; a single connection can multiplex many application protocols; and one messaging interaction can use separate network channels for payload, reply, flow control, and recovery.

## Related Specifications

| Specification | What it constrains |
| --- | --- |
| [[Interfaces\|interface]] | Available interaction roles and semantic obligations |
| [[Shape\|shape or schema]] | Structure of exchanged values |
| semantic contract | Meaning of interactions, outcomes, and failures |
| interaction protocol | Legal traces, conversational state, ordering, concurrency, and completion |
| [[Session Types\|session type]] | Formally typed participant-local or projected communication behavior |
| interaction shape | Coarse exchange morphology required from a channel |
| operational envelope | Quantitative expectations such as capacity, throughput, latency, and queue limits |
| [[Interaction Channels\|channel]] | Logical exchange and directions through which occurrences move |
| [[Interaction Bindings\|binding]] | Exact association of contracts and protocol roles with endpoints and channel directions |
| realization binding | Concrete encoding, addressing, transport, provider configuration, and runtime mechanisms |

## Operational Envelope

A protocol can expose backpressure, admission, acknowledgment, settlement, or maximum-in-flight rules, but throughput and queueing behavior are not properties of a schema alone. They arise from the protocol together with arrival patterns, service time, resource capacity, scheduling, retries, and downstream dependencies.

The operational envelope therefore qualifies an interface-protocol-channel binding with measurable operational concerns, including:

- supported concurrency and serialization scopes;
- expected and maximum throughput;
- latency and deadline expectations;
- boundedness and queue discipline;
- flow-control and overload signals; and
- fairness and priority expectations.

See [[Queueing Theory|queueing theory]], [[Scheduling|scheduling]], and [[Flow Control|flow control]] for the corresponding operational models.

## Opaque Protocols

A service may perform an operation whose domain meaning belongs to an external or intentionally hidden model. The local graph can still specify the interface, protocol, observable outcomes, channel binding, and guarantees without pretending to own the external semantics.

## Relationships

- [[Service|Services]] realize capabilities under their interface protocols.
- [[Interaction Channels|Interaction channels]] carry protocol occurrences but do not define their complete meanings or legal traces.
- [[Network Channels|Network channels]] and network protocols can realize parts of a service or channel protocol without being identical to it.
- [[Process Graphs|Process structures]] can describe longer-lived conversations that span several interface operations or protocol sessions.
- [[Session Types|Session types]] can formally constrain participant-local traces, duality, branching, recursion, and endpoint use without automatically supplying the protocol's domain meaning or operational guarantees.
- [[Trace and Feedback|Traces]] provide evidence that observed conversations conform to their protocols.

## Formal relations

- `constrains`: [[Interaction]] — An interaction protocol restricts the legal boundary-relative traces in which participants may take interaction roles.

## External References

- [Enterprise Integration Patterns: Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html)
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)

Related concepts: [[Interfaces|interfaces]], [[Session Types|session types]], [[Process Calculi|process calculi]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Interaction Channels|interaction channels]], [[Messages and Envelopes|messages and envelopes]], [[Correlation and Conversations|correlation and conversations]], [[Interaction Control Flow|interaction control flow]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Flow Control|flow control]], [[Network Channels|network channels]], [[Network|network]], [[Realization|realization]].
