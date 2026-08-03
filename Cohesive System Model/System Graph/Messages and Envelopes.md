---
realm: System Graph
kind: structural-construct
created: 2026-07-27
updated: 2026-08-02
aliases:
  - Message
  - Messages
  - Message Envelope
  - Message Envelopes
---

# Messages and Envelopes

Messages and envelopes describe the finite carriers used to move values and interaction metadata across system-graph boundaries.

A message is not a new domain-semantic primitive. It is a structural carrier participating in an [[Interaction|interaction]]. Message emission, admission, delivery, and ingress are occurrences. At a receiving boundary, ingress is an exogenous [[Event|event]] carrying a [[Value|value]] whose [[Shape|shape]], contract, addressing, and context provide evidence for semantic interpretation.

## Intent and Interpretation

A message contract may make an intended interpretation explicit:

- A **command message** carries singular intent that an understood observer attempt a transition.
- An **event message** carries a value reporting an occurrence.
- A **document message** carries an observation, state transfer, artifact, or other shaped value.
- A **request message** carries a request effect whose emission establishes an emitter-side response or terminal-failure obligation.
- A **reply message** carries a terminal result that discharges one admitted request when accepted under the request protocol.

These correspondences are strong without being identities. A command message makes command interpretation expected, but the receiving [[Observer|observer]] still admits and interprets the exogenous event relative to its boundary, authority, policies, state, and target subject. An event message may report one domain occurrence while its delivery creates distinct messaging occurrences.

## Envelope Structure

An envelope separates interaction metadata from a carried payload. Depending on the contract, it may include:

- Stable message, emission, request, process, subject, and contract identities.
- Target, channel, route, partition, return address, and reply-path information.
- Correlation and causation links.
- Schema, semantic, payload, and format versions.
- Ordering key, sequence position, deadline, expiration, and retention demands.
- Idempotency basis, attempt identity, and expected version.
- Tenant, authority, classification, trace, and provenance context.

Transport-assigned identifiers do not automatically replace these semantic and protocol identities. An envelope wrapper may add the metadata required by a channel without changing the carried value's domain meaning. A claim-check arrangement may replace a large carried value with a stable reference into [[Storage Systems|storage]], but the reference's authority, lifetime, consistency, and access rules then become part of the interaction contract.

## Identity Across Delivery

The stable identity carried by a message or envelope belongs to the logical emission, request, reply, or other contract role. A provider can add a delivery identity, and every redelivery can create a new attempt identity. A receipt, lock token, acknowledgment subject, or lease can supply temporary authority to settle the current attempt. A cursor can identify a replay position. None of those substrate identities replaces the carried logical identity.

The envelope can carry references needed to relate these layers, but it should not turn them into one universal message identifier. One logical emission may have several provider deliveries and attempts; one delivery attempt may carry both a replay cursor and ephemeral settlement authority; one durable application-progress record may cover several deliveries. See [[Delivery Progress and Settlement|delivery progress and settlement]].

## Structural Boundary

Messages and envelopes state what is carried and how its intended correspondence is declared. [[Interaction Channels|Interaction channels]] state the logical exchanges and directions through which it can move. [[Interaction Bindings|Interaction bindings]] associate carried contract roles with exact directions and [[Endpoints|endpoints]]. [[Routing Models|Routing models]] select paths or recipients. [[Flow Operators|Flow operators]] transform or compose carried values. [[Delivery Semantics|Delivery semantics]] and other operational concerns supply guarantees. [[Brokers|Brokers]], files, [[Network Channels|network channels]], databases, and runtimes realize the carrier and its movement.

## External References

- Gregor Hohpe and Bobby Woolf, [Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Message.html), [Command Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html), [Document Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DocumentMessage.html), and [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html), *Enterprise Integration Patterns*, 2003.
- Gregor Hohpe and Bobby Woolf, [Envelope Wrapper](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EnvelopeWrapper.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Value|value]], [[Shape|shape]], [[Event|event]], [[Effect|effect]], [[Command|command]], [[Observation|observation]], [[Observer|observer]], [[Interaction|interaction]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Flow Operators|flow operators]], [[Correlation and Conversations|correlation and conversations]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Compatibility and Evolution|compatibility and evolution]], [[Network Channels|network channels]], [[Brokers|brokers]], [[Storage Systems|storage systems]].
