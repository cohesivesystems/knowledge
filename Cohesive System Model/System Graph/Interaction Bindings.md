---
realm: System Graph
kind: structural-construct
created: 2026-08-02
updated: 2026-08-17
status: draft
aliases:
  - Interaction Binding
  - Channel Binding
  - Protocol Binding
---

# Interaction Bindings

An interaction binding relates the semantic and structural parts of an interaction at one exact boundary without making them identical. It states how [[Interfaces|interface]] contract roles and [[Interaction Protocols|protocol]] roles attach through [[Endpoints|endpoints]] to exact [[Interaction Channels|channel]] directions, and which realization is authorized to carry them.

Bindings are the reconciliation layer among interface, protocol, channel, endpoint, and realization. An interface can have several bindings; one channel can carry several distinguishable interface roles; one protocol can span several channels; and a new binding can preserve an interface contract while changing transport, topology, or endpoint placement.

## Binding Contents

A complete binding may identify:

- the boundary, participants, provided or required ports, and reusable interface roles;
- exact operation, event, request, reply, stream-item, or other carried contracts;
- protocol roles, initiation rules, correlation, and terminal outcomes;
- exact channel definition revision and channel directions;
- the ports and logical endpoints attached to each direction;
- envelope interpretation, framing, codec, and compatibility rules;
- routing, addressing, subscription, or response-target rules;
- required operational properties at each boundary; and
- the attributable realization plan, adapter, and capability evidence.

A binding should reference canonical contracts and channel directions rather than copying them. This preserves identity and evolution independently: revising an endpoint address need not revise a semantic request contract, and revising a contract does not silently retarget an existing channel.

## Request and Reply

A request/reply binding maps one request contract and its terminal reply contracts to two independently identified directions. The binding records whether the directions belong to one coupled exchange or to paired one-way channels.

```text
request contract --bound to--> request direction
reply contract   --bound to--> reply direction
```

The reply direction may be physically coupled to the invocation, selected through an explicit response target, correlated through a shared topic or stream, or observed through another channel. Those choices do not change which reply discharges which request. Correlation, response obligation, timeout, cancellation, and winner rules remain protocol and contract concerns.

## Logical and Physical Binding

A **logical binding** relates contracts, roles, directions, and endpoints in the system graph. A **realization binding** supplies concrete provider or protocol artifacts such as routes, addresses, topics, subscriptions, stream identifiers, codecs, credentials, and client configuration.

The realization binding must be validated against the exact logical definition and capability context. A stale plan, compatible-looking provider name, or raw transport handle is not sufficient authority. Derived artifacts can change while the logical binding remains stable, but a changed realization must still preserve every demanded property at its declared boundary.

Bindings can be layered. A message publication binding may lower into a broker client protocol binding, which lowers into one or more [[Network Channels|network-channel]] bindings. Each layer introduces its own endpoints, identifiers, acknowledgments, failure cuts, and control exchanges. The composed realization must state which upper-layer structure each lower-layer binding preserves and which details it introduces or forgets.

## Distinctions

| Term | Distinction from a binding |
| --- | --- |
| [[Interfaces\|interface]] | Defines available semantic roles and obligations; a binding attaches those roles to structure. |
| [[Interaction Protocols\|interaction protocol]] | Defines legal traces; a binding assigns protocol roles to exact endpoints and directions. |
| [[Interaction Channels\|channel]] | Defines the logical exchange and scoped demands; a binding states what the channel carries for this interaction. |
| [[Endpoints\|endpoint]] | Is one attachment locus; a binding relates the loci on all participating sides. |
| port | Is a particular provided or required occurrence of an interface on a system boundary; a binding connects that occurrence to a channel endpoint. |
| adapter | Translates between bound roles and concrete mechanisms; it is part of realization rather than the binding's semantic authority. |
| address | Names or selects a path, channel, or endpoint; changing an address need not change the logical binding. |

Related concepts: [[Interaction|interaction]], [[Surfaces|surfaces]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Interaction Channels|interaction channels]], [[Endpoints|endpoints]], [[Messages and Envelopes|messages and envelopes]], [[Correlation and Conversations|correlation and conversations]], [[Routing Models|routing models]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Ports and Adapters|ports and adapters]], [[Compatibility and Evolution|compatibility and evolution]], [[Realization|realization]], [[Network Channels|network channels]].

## Formal relations

- `arranges`: [[Interfaces]] — An interaction binding attaches provided and required interface roles to exact channel directions and endpoints.
- `arranges`: [[Interaction Protocols]] — An interaction binding assigns protocol roles to participants and channel directions without redefining their legal traces.
