---
realm: Architecture Practices
kind: pattern
created: 2026-06-24
updated: 2026-07-28
---

# Ports and Adapters

Ports and Adapters addresses the problem of keeping domain and application semantics independent from specific infrastructure, protocols, user interfaces, and external systems.

## Cohesive Formulation

Ports are named attachment points or roles through which a component provides or requires an [[Interfaces|interface]] at a [[Boundaries|boundary]]. Adapters are realization mechanisms that translate between those interface roles, component behavior, and substrate-specific messages without making the port, interface, boundary, channel, and binding synonymous.

The practice asks:

- Which boundary is being crossed?
- Which provided or required interface does the port represent?
- What semantic object enters or leaves the boundary?
- Which observer interprets the input?
- Which [[Interaction Protocols|interaction protocol]] governs the conversation?
- What channel, protocol binding, storage mechanism, UI, or external system realizes the edge?

## In the Model

An inbound adapter admits an external occurrence as an input event relative to an [[Observer|observer]] and supplies the carried value and contract for interpretation as a command, query, event notification, signal, or other role. An outbound adapter realizes an endogenous event, request, signal, reply, query, command intent, or observation as a protocol-specific effect. The adapter preserves a correspondence; it does not collapse transport classification into semantic interpretation.

Enterprise Integration Patterns channel adapters, messaging gateways, messaging mappers, and service activators are specialized endpoint and adapter structures. They should remain outside the semantic authority that decides domain transitions.

## Failure Modes

The pattern fails when adapters leak substrate semantics into the domain, when ports are treated as network endpoints, or when interfaces are described without stating their semantic boundary, protocol, and authority.

## External References

- Gregor Hohpe and Bobby Woolf, [Channel Adapter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html), [Messaging Gateway](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingGateway.html), and [Messaging Mapper](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingMapper.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Observer|observer]], [[Observer Models|observer models]], [[Command|command]], [[Query|query]], [[Observation|observation]], [[Event|event]], [[Messages and Envelopes|messages and envelopes]], [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Compatibility and Evolution|compatibility and evolution]], [[Network|network]], [[Application Hosts|application hosts]], [[Realization|realization]], [[Anti-Corruption Layer|anti-corruption layer]].
