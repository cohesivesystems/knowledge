---
realm: Architecture Practices
kind: pattern
created: 2026-06-24
updated: 2026-08-17
---

# Ports and Adapters

Ports and Adapters addresses the problem of keeping domain and application semantics independent from specific infrastructure, protocols, user interfaces, and external systems.

## Cohesive Formulation

An [[Interfaces|interface]] is a reusable intentional interaction type projected on a [[Surfaces|surface]]. Ports are particular boundary occurrences through which a component provides or requires that interface. [[Endpoints|Endpoints]] are the bound loci through which those port roles participate in particular [[Interaction Channels|channel]] arrangements. Adapters are realization mechanisms that translate among interface roles, component behavior, messages, and substrate mechanisms without making the port, endpoint, interface, surface, boundary, channel, or [[Interaction Bindings|binding]] synonymous.

The practice asks:

- Which boundary is being crossed?
- Which interface type and provided or required orientation does the port instantiate?
- What semantic object enters or leaves the boundary?
- Which observer interprets the input?
- Which [[Interaction Protocols|interaction protocol]] governs the conversation?
- Which endpoint and channel directions are attached by the interaction binding?
- What channel realization, protocol binding, storage mechanism, UI, or external system realizes the edge?

## In the Model

An inbound adapter admits an external occurrence as an input event relative to an [[Observer|observer]] and supplies the carried value and contract for interpretation as a command, query, event notification, signal, or other role. An outbound adapter realizes an endogenous event, request, signal, reply, query, command intent, or observation as a protocol-specific effect. The adapter preserves a correspondence; it does not collapse transport classification into semantic interpretation.

Enterprise Integration Patterns channel adapters, messaging gateways, messaging mappers, and service activators are specialized endpoint and adapter structures. They should remain outside the semantic authority that decides domain transitions.

## Failure Modes

The pattern fails when adapters leak substrate semantics into the domain, when ports are treated as concrete network endpoints, when endpoint addresses become semantic identity, or when interfaces are described without stating their semantic boundary, protocol, binding, and authority.

## Formal relations

- `corresponds_to`: [[Clean Architecture]] — Shares a dependency-direction and boundary-separation structure while retaining distinct interface-role and layering vocabularies.

## External References

- Gregor Hohpe and Bobby Woolf, [Channel Adapter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html), [Messaging Gateway](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingGateway.html), and [Messaging Mapper](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingMapper.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Surfaces|surfaces]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Observer|observer]], [[Observer Models|observer models]], [[Command|command]], [[Query|query]], [[Observation|observation]], [[Event|event]], [[Messages and Envelopes|messages and envelopes]], [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Compatibility and Evolution|compatibility and evolution]], [[Network Channels|network channels]], [[Network|network]], [[Application Hosts|application hosts]], [[Realization|realization]], [[Anti-Corruption Layer|anti-corruption layer]].
