---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-01
---

# Query

A query is an observer-relative interpretation of an input event as a request to observe, compute, or return information without requesting a modeled semantic state transition.

Query interpretation follows this shape:

```txt
Exogenous event
  -> input event at an observer [[Boundaries|boundary]]
  -> query intent, relative to the observer and target subject or view
  -> selection of observable, projection, read model, computation, authority, and consistency expectation
  -> observation | value | stream | nil | rejection
```

Queries are not mere messages. They are interpretations made relative to:

- The specific [[Observer|observer]].
- The observer [[Boundaries|boundary]] and current view of state.
- The [[Observable|observable]], [[Projections|projection]], read model, computation, or [[Shape|shape]] being requested.
- Authority, access policy, and disclosure rules.
- Freshness, ordering, and consistency expectations.
- Optional version, cursor, snapshot, or read boundary.

A query's result is usually an [[Observation|observation]] or [[Value|value]]. The query selects or parameterizes how state should become visible, including the requested [[Shape|shape]]; the observation is the contextualized value produced.

A query does not request a [[transition]] of the modeled semantic entity state. However, operational state can still change while serving a query: caches may fill, metrics may record, cursors may advance, locks may be acquired, acknowledgments may be emitted, and audit records may be written. Those effects belong to other operational or semantic subjects unless the query is also interpreted as a command for them.

Query is therefore dual to [[Command|command]] only in a limited modeling sense:

- A command interprets input as intent to change modeled state.
- A query interprets input as intent to observe modeled state or derived information.

The distinction is semantic, not transport-level. Request/reply, actor ask, RPC, shared-memory read, stream subscription, and broker-backed fetch can all carry queries at different interaction layers.

In [[CQRS]], queries are commonly answered from read-side projections, indexes, materialized views, caches, or derived state. The correctness question is boundary-relative: the query result may be current, stale, monotonic for one observer, read-your-writes for one session, or only eventually consistent with authoritative persistence.

Related concepts: [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[Observable|observable]], [[Observer|observer]], [[Boundaries|boundaries]], [[State|state]], [[Command|command]], [[Interaction|interaction]], [[CQRS]], [[Projections|projections]], [[Reconstitution|reconstitution]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]].
