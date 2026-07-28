---
realm: Architecture Practices
kind: pattern
created: 2026-06-24
updated: 2026-07-27
---

# Ports and Adapters

Ports and Adapters addresses the problem of keeping domain and application semantics independent from specific infrastructure, protocols, user interfaces, and external systems.

## Cohesive Formulation

Ports define interaction boundaries. Adapters are realization mechanisms that translate between substrate-specific messages and Cohesive concepts such as [[Command|commands]], [[Query|queries]], [[Observation|observations]], [[Event|events]], and [[Interaction|interactions]].

The practice asks:

- Which boundary is being crossed?
- What semantic object enters or leaves the boundary?
- Which observer interprets the input?
- What protocol, storage, UI, or external system realizes the edge?

## In the Model

An inbound adapter admits an external occurrence as an input event relative to an [[Observer|observer]] and supplies the carried value and contract for interpretation as a command, query, event notification, signal, or other role. An outbound adapter realizes an endogenous event, request, signal, reply, query, command intent, or observation as a protocol-specific effect. The adapter preserves a correspondence; it does not collapse transport classification into semantic interpretation.

Enterprise Integration Patterns channel adapters, messaging gateways, messaging mappers, and service activators are specialized endpoint and adapter structures. They should remain outside the semantic authority that decides domain transitions.

## Failure Modes

The pattern fails when adapters leak substrate semantics into the domain, or when ports are treated as technical interfaces without stating the semantic boundary and authority they represent.

## External References

- Gregor Hohpe and Bobby Woolf, [Channel Adapter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html), [Messaging Gateway](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingGateway.html), and [Messaging Mapper](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingMapper.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Observer|observer]], [[Observer Models|observer models]], [[Command|command]], [[Query|query]], [[Observation|observation]], [[Event|event]], [[Messages and Envelopes|messages and envelopes]], [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Compatibility and Evolution|compatibility and evolution]], [[Network|network]], [[Application Hosts|application hosts]], [[Realization|realization]], [[Anti-Corruption Layer|anti-corruption layer]].
