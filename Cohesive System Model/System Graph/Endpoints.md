---
realm: System Graph
kind: structural-construct
created: 2026-08-02
updated: 2026-08-17
status: draft
aliases:
  - Endpoint
  - Interaction Endpoint
  - Message Endpoint
  - Messaging Endpoint
---

# Endpoints

An interaction endpoint is a boundary-relative attachment locus at which a participant, through a port or adapter, sends to or receives from one or more [[Interaction Channels|channel]] directions under an [[Interfaces|interface]] and [[Interaction Protocols|protocol]] binding.

An endpoint is not automatically the participant, [[Observer|observer]], interface, port, address, channel, or adapter. It identifies where those roles meet in one interaction arrangement. The same observer may participate through several endpoints, and one endpoint may activate different observer instances over time.

## Logical Endpoint

In the system graph, a logical endpoint can state:

- its boundary, port orientation, and interface role;
- the channel directions it may emit to or admit from;
- its sender, sink, source, or fetcher role in [[Interaction Control Flow|interaction control flow]];
- admissible contracts, routing selectors, or subscription role;
- the observer or service responsibility activated by ingress; and
- the guarantees required at the attachment boundary.

A port is the particular occurrence through which a component provides or requires an interface on a [[Surfaces|surface]]. An endpoint is the bound attachment locus through which that port participates in a particular channel arrangement. A port can therefore have several endpoint bindings, and an endpoint can expose a multiplexed interface namespace.

## Endpoint Specializations

| Term | Boundary-relative meaning |
| --- | --- |
| **messaging endpoint** | Attaches a producer, consumer, subscriber, dispatcher, gateway, or service activator to a messaging channel. |
| **operation or service endpoint** | Supplies a routing and dispatch locus for named operations or resources. |
| **reply endpoint** | Admits replies selected by invocation scope, correlation, or an explicit response target. |
| **network endpoint** | Terminates or participates in a concrete protocol-layer exchange through an address, socket, connection, stream, or peer association. |
| **runtime endpoint** | Exposes a callback, queue reader, actor mailbox attachment, worker port, or other runtime activation locus. |

These are related uses of the same attachment notion at different abstraction layers, not interchangeable objects. One logical messaging endpoint may be realized by many network endpoints because of replication, failover, load balancing, reconnection, or partitioning. One network endpoint or connection may multiplex many messaging endpoints, interface operations, or logical streams.

## Addressing and Routing

An address names or selects an endpoint, channel, participant, or mediating locus under a routing interpretation. Addressability is not intrinsic to endpoint identity. An endpoint can be discovered dynamically, selected by content or key, represented by a durable subscription, scoped to one invocation, or remain local and implicit.

A URL, topic name, queue name, actor address, socket tuple, stream identifier, callback registration, or subscription identifier can participate in endpoint realization. None establishes the endpoint's semantic authority by itself. [[Routing Models|Routing]] determines how selectors lead to eligible endpoints; [[Interaction Bindings|interaction bindings]] state which endpoint role is intended.

## Activation and Interpretation

Delivery to an endpoint does not itself interpret the carried value. A messaging endpoint, gateway, service activator, polling consumer, or event-driven consumer can activate an [[Observer Models|observer model]], but the observer boundary still supplies authority, state view, and interpretation rules. Likewise, successful transmission to a network endpoint does not prove admission at the messaging endpoint or commitment by the receiving observer.

Related concepts: [[Interaction|interaction]], [[Boundaries|boundaries]], [[Surfaces|surfaces]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Interaction Channels|interaction channels]], [[Observer|observer]], [[Observer Models|observer models]], [[Interaction Control Flow|interaction control flow]], [[Routing Models|routing models]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Ports and Adapters|ports and adapters]], [[Network Channels|network channels]], [[Network|network]], [[Application Hosts|application hosts]], [[Brokers|brokers]].

## Formal relations

- `arranges`: [[Interaction]] — Endpoints place boundary-relative attachment loci through which participants enter or leave interaction-channel directions.
- `distinguished_from`: [[Observer]] — An endpoint is a bound attachment locus, whereas an observer supplies interpretation, state view, authority, and decision context.
