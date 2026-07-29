---
realm: System Graph
kind: structural-construct
created: 2026-07-28
updated: 2026-07-28
status: draft
aliases:
  - Interface
  - Provided Interface
  - Required Interface
---

# Interfaces

An interface is a declared interaction surface at a [[Boundaries|boundary]]. A boundary distinguishes scopes; an interface makes selected crossings of that boundary possible and constrains what may cross, in which role, and with what meaning.

This distinction is important: every interface defines or occupies a boundary, but not every boundary is an interface. Ownership, trust, consistency, and deployment boundaries may exist without being designed as crossing points.

## Provided and Required Interfaces

A node provides an interface when it accepts the interface's interactions and assumes its obligations. It requires an interface when its behavior depends on another node providing that interface.

Provided and required interfaces make dependency direction explicit without committing to a particular transport, address, process boundary, or deployment topology. The same interface may be realized by an in-process call, HTTP, RPC, a broker, a file exchange, or another [[Interaction Channels|interaction channel]].

## Contents

An interface may declare:

- named operations, events, or other interaction roles;
- accepted and produced [[Shape|shapes]] or schemas;
- direction, initiation, and expected outcomes;
- semantic preconditions, postconditions, invariants, and failure meanings;
- a governing [[Interaction Protocols|interaction protocol]];
- compatibility and evolution rules; and
- required guarantees at the crossing.

The interface need not reveal the internal entities, relations, processes, storage, or collaborating services that realize the capability.

## Related Terms

| Term | Cohesive distinction |
| --- | --- |
| [[Boundaries\|boundary]] | Separates scopes or authorities. An interface is a designed crossing of a boundary. |
| [[Shape\|Shape or schema]] | Describes the structure of exchanged values. It does not by itself define their meaning or legal interaction sequences. |
| Contract | States semantic obligations and guarantees associated with an interface. |
| [[Interaction Protocols\|interaction protocol]] | Constrains the temporal structure of interactions through an interface. |
| API | A concrete or published interface description, often coupled to a particular binding or toolchain. |
| Port | A named attachment point or role through which a component provides or requires an interface. |
| [[Interaction Channels\|channel]] | The locus that carries interactions between interface endpoints. |
| Adapter | Translates between an interface and a component or realization substrate. |

## Relationships

- [[Interaction|Interactions]] cross boundaries through interfaces.
- [[Ports and Adapters]] separate an interface role from the mechanisms that realize or consume it.
- [[Service|Services]] encapsulate internal structure behind provided interfaces and declare dependencies through required interfaces.
- [[Service Models|Service models]] connect logical services by their provided and required interfaces.
- [[Realization|Realization]] binds interfaces to concrete channels, protocols, addresses, and runtime mechanisms.

## External References

- [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
