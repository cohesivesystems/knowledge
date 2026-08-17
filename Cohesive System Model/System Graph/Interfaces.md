---
realm: System Graph
kind: structural-construct
created: 2026-07-28
updated: 2026-08-17
status: draft
aliases:
  - Interface
---

# Interfaces

An interface is a reusable intentional interaction type projected on a [[Surfaces|surface]]. It declares roles and meanings that can be instantiated at system boundaries without identifying the reusable type with any one participant, address, endpoint, or realization.

A [[Ports and Adapters|port]] is a particular occurrence of an interface on a system [[Boundaries|boundary]]. A port provides or requires the interface under boundary-specific ownership, policy, scope, assumptions, and evidence. A surface may project several interfaces through several ports and may expose guarantees, resource constraints, or evidence that are not themselves interaction types.

## Provided and Required Ports

A system provides or requires an interface through a port on its surface. A provided port undertakes the provider-side obligations of the interface and governing protocol. A required port records the compatible capability and obligations on which the system depends.

Provided and required ports make dependency direction explicit without committing to a particular transport, address, process boundary, or deployment topology. Their interface and protocol roles are attached to [[Interaction Channels|channel]] directions and [[Endpoints|endpoints]] by [[Interaction Bindings|interaction bindings]]. The corresponding realization may use an in-process call, HTTP, RPC, a broker, a file exchange, shared state, or another mechanism without making the mechanism the interface's semantic authority.

## Contents

An interface may declare:

- named operations, events, observations, streams, or other interaction roles;
- accepted and produced [[Shape|shapes]] or schemas;
- direction, initiation, and expected outcomes;
- semantic preconditions, postconditions, invariants, and failure meanings;
- one or more governing [[Interaction Protocols|interaction protocols]];
- compatibility and evolution rules; and
- required [[Service Levels|service-level]] and other operational guarantees at the crossing.

The interface need not reveal the internal entities, relations, processes, storage, or collaborating services that realize the capability.

## Interface, Protocol, Channel, and Binding

| Term | Governing question |
| --- | --- |
| [[Surfaces\|surface]] | Which externally relevant boundary semantics does the system expose, require, or claim? |
| interface | Which reusable intentional interaction type governs the participating roles? |
| [[Ports and Adapters\|port]] | Which occurrence of that interface is provided or required by this system? |
| [[Interaction Protocols\|interaction protocol]] | In which legal traces may participants use those roles? |
| [[Interaction Channels\|interaction channel]] | Through which logical exchange and directions can occurrences move? |
| [[Endpoints\|endpoint]] | At which attachment locus does a participant enter or leave a channel direction? |
| [[Interaction Bindings\|interaction binding]] | Which exact contracts and protocol roles attach to which endpoints and directions? |
| realization | Which mechanisms preserve that bound structure and its required properties? |

The relationships are many-to-many. One interface can have local, HTTP, RPC, broker, file, or runtime bindings. One channel can carry several distinguishable interfaces. One protocol can span several interfaces and channels. One endpoint can multiplex a namespace of operations while several physical endpoints realize one logical interface through replication or failover.

## Related Terms

| Term | Cohesive distinction |
| --- | --- |
| [[Boundaries\|boundary]] | Separates scopes or authorities. A port instantiates an interface at that boundary. |
| [[Surfaces\|surface]] | Organizes externally relevant boundary semantics. An interface is a reusable interaction type projected on that surface. |
| [[Shape\|shape or schema]] | Describes exchanged value structure. It does not by itself define meaning or legal interaction sequences. |
| contract | States semantic obligations and guarantees associated with an interface role. |
| API | Is a concrete or published interface description, often coupled to a particular binding or toolchain. |
| port | Is a particular boundary occurrence through which a system provides or requires an interface. |
| [[Endpoints\|endpoint]] | Is the bound attachment locus through which a port participates in a channel arrangement. |
| adapter | Translates among interface roles, component behavior, messages, and realization mechanisms. |
| address | Names or selects an endpoint, participant, channel, or mediating locus under a routing interpretation. |

## Relationships

- [[Interaction|Interactions]] cross boundaries under interface roles and contracts.
- [[Ports and Adapters]] separate an interface role from the mechanisms that realize or consume it.
- [[Service|Services]] encapsulate internal structure behind surfaces whose ports provide or require interfaces.
- [[Service Models|Service models]] connect logical services through those ports, interfaces, and bindings.
- [[Service Levels|Service levels]] qualify interface outcomes with measurable objectives and accountable commitments.
- [[Realization|Realization]] binds interface roles to concrete channels, protocols, endpoints, addresses, adapters, and runtime mechanisms.

## Formal relations

- `arranges`: [[Interaction]] — An interface arranges reusable interaction roles and semantic obligations that ports project at declared boundaries.
- `distinguished_from`: [[Boundaries]] — A boundary separates scopes and contexts, whereas an interface is a reusable interaction type that ports instantiate at selected boundaries.

## External References

- [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

Related concepts: [[Surfaces|surfaces]], [[Boundaries|boundaries]], [[Interaction|interaction]], [[Interaction Protocols|interaction protocols]], [[Interaction Channels|interaction channels]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Ports and Adapters|ports and adapters]], [[Service Models|service models]], [[Compatibility and Evolution|compatibility and evolution]], [[Network Channels|network channels]], [[Realization|realization]].
