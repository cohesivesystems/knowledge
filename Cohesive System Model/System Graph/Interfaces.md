---
realm: System Graph
kind: structural-construct
created: 2026-07-28
updated: 2026-08-08
status: draft
aliases:
  - Interface
  - Provided Interface
  - Required Interface
---

# Interfaces

An interface is a declared interaction surface at a [[Boundaries|boundary]]. A boundary distinguishes scopes; an interface makes selected crossings of that boundary available and constrains what may cross, in which role, and with what meaning.

Every interface defines or occupies a boundary, but not every boundary is an interface. Ownership, trust, consistency, deployment, and failure boundaries may exist without being designed as crossing points.

## Provided and Required Interfaces

A node provides an interface when it accepts the interface's interactions and assumes its obligations. It requires an interface when its behavior depends on another node providing that interface.

Provided and required interfaces make dependency direction explicit without committing to a particular transport, address, process boundary, or deployment topology. Their roles are attached to [[Interaction Channels|channel]] directions and [[Endpoints|endpoints]] by [[Interaction Bindings|interaction bindings]]. The corresponding realization may use an in-process call, HTTP, RPC, a broker, a file exchange, shared state, or another mechanism without making the mechanism the interface's semantic authority.

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
| interface | What roles, contracts, and obligations are available at this boundary? |
| [[Interaction Protocols\|interaction protocol]] | In which legal traces may participants use those roles? |
| [[Interaction Channels\|interaction channel]] | Through which logical exchange and directions can occurrences move? |
| [[Endpoints\|endpoint]] | At which attachment locus does a participant enter or leave a channel direction? |
| [[Interaction Bindings\|interaction binding]] | Which exact contracts and protocol roles attach to which endpoints and directions? |
| realization | Which mechanisms preserve that bound structure and its required properties? |

The relationships are many-to-many. One interface can have local, HTTP, RPC, broker, file, or runtime bindings. One channel can carry several distinguishable interfaces. One protocol can span several interfaces and channels. One endpoint can multiplex a namespace of operations while several physical endpoints realize one logical interface through replication or failover.

## Related Terms

| Term | Cohesive distinction |
| --- | --- |
| [[Boundaries\|boundary]] | Separates scopes or authorities. An interface is a designed crossing of a boundary. |
| [[Shape\|shape or schema]] | Describes exchanged value structure. It does not by itself define meaning or legal interaction sequences. |
| contract | States semantic obligations and guarantees associated with an interface role. |
| API | Is a concrete or published interface description, often coupled to a particular binding or toolchain. |
| port | Is a component's named attachment role through which it provides or requires an interface. |
| [[Endpoints\|endpoint]] | Is the bound attachment locus through which a port participates in a channel arrangement. |
| adapter | Translates among interface roles, component behavior, messages, and realization mechanisms. |
| address | Names or selects an endpoint, participant, channel, or mediating locus under a routing interpretation. |

## Relationships

- [[Interaction|Interactions]] cross boundaries under interface roles and contracts.
- [[Ports and Adapters]] separate an interface role from the mechanisms that realize or consume it.
- [[Service|Services]] encapsulate internal structure behind provided interfaces and declare dependencies through required interfaces.
- [[Service Models|Service models]] connect logical services by their provided and required interfaces and bindings.
- [[Service Levels|Service levels]] qualify interface outcomes with measurable objectives and accountable commitments.
- [[Realization|Realization]] binds interface roles to concrete channels, protocols, endpoints, addresses, adapters, and runtime mechanisms.

## Formal relations

- `arranges`: [[Interaction]] — An interface arranges which interaction roles and semantic obligations are available at a declared boundary.
- `distinguished_from`: [[Boundaries]] — A boundary separates scopes and contexts, whereas an interface declares selected interaction roles and obligations available across that boundary.

## External References

- [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

Related concepts: [[Boundaries|boundaries]], [[Interaction|interaction]], [[Interaction Protocols|interaction protocols]], [[Interaction Channels|interaction channels]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Ports and Adapters|ports and adapters]], [[Service Models|service models]], [[Compatibility and Evolution|compatibility and evolution]], [[Network Channels|network channels]], [[Realization|realization]].
