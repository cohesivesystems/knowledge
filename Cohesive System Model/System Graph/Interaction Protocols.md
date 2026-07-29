---
realm: System Graph
kind: structural-construct
created: 2026-07-28
updated: 2026-07-28
status: draft
aliases:
  - Interaction Protocol
  - Conversation Protocol
  - Service Protocol
---

# Interaction Protocols

An interaction protocol describes the allowed temporal structure of [[Interaction|interactions]] through an [[Interfaces|interface]]. It constrains not only the values that may be exchanged, but also who may initiate, which interactions may follow, how concurrent attempts relate, and how a conversation completes, fails, or is cancelled.

An interface answers *what may be attempted*. A protocol answers *how attempts may unfold over time*.

## Protocol Contents

A protocol may declare:

- initiator and responder roles;
- request, reply, notification, acknowledgement, and streaming sequences;
- conversational states and allowed transitions;
- correlation and causation rules;
- ordering and concurrency constraints;
- retry, duplication, and idempotency expectations;
- timeout, cancellation, compensation, and failure behavior;
- session or connection lifetime; and
- version negotiation and evolution rules.

These rules may be explicit in a specification or merely assumed by implementations. Unstated protocols are still protocols; they are simply harder to validate, evolve, and operate.

## Related Specifications

| Specification | What it constrains |
| --- | --- |
| [[Interfaces\|Interface]] | Available interaction roles and semantic obligations |
| [[Shape\|Shape or schema]] | Structure of exchanged values |
| Semantic contract | Meaning of interactions, outcomes, and failures |
| Interaction protocol | Legal traces, conversational state, ordering, concurrency, and completion |
| Operational envelope | Quantitative expectations such as capacity, throughput, latency, and queue limits |
| [[Interaction Channels\|Channel]] | Locus through which the interactions move |
| Binding | Concrete encoding, addressing, transport, and runtime mechanisms |

## Operational Envelope

A protocol can expose backpressure, admission, acknowledgement, or maximum-in-flight rules, but throughput and queueing behavior are not properties of a schema alone. They arise from the protocol together with arrival patterns, service time, resource capacity, scheduling, retries, and downstream dependencies.

The operational envelope therefore qualifies an interface-protocol binding with measurable operational concerns, including:

- supported concurrency and serialization scopes;
- expected and maximum throughput;
- latency and deadline expectations;
- boundedness and queue discipline;
- flow-control and overload signals; and
- fairness and priority expectations.

See [[Queueing Theory]], [[Scheduling]], and [[Flow Control]] for the corresponding operational models.

## Opaque Protocols

A service may perform an operation whose domain meaning belongs to an external or intentionally hidden model. The local graph can still specify the interface, protocol, observable outcomes, and guarantees without pretending to own the external semantics.

## Relationships

- [[Service|Services]] realize capabilities under their interface protocols.
- [[Interaction Channels]] carry protocol events but do not define their complete meaning.
- [[Network]] protocols may realize part of a service protocol without being identical to it.
- [[Process Theories|Process structures]] can describe longer-lived conversations that span several interface operations.
- [[Trace and Feedback|Traces]] provide evidence that observed conversations conform to their protocols.

## External References

- [Enterprise Integration Patterns: Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html)
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
