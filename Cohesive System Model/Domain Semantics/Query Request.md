---
realm: Domain Semantics
kind: semantic-construct
created: 2026-11-05
updated: 2026-11-05
---

# Query Request

A query request is an input that an [[Observer|observer]] interprets at its boundary as asking for information rather than a change to modeled state.

A query message may carry an expression that specifies which information to return and how to shape it. The expression can include predicates, selectors, paging parameters, or aggregation rules.

Query interpretation follows this shape:

```txt
Exogenous event
  -> input event at an observer boundary
  -> query intent, relative to the observer and target subject or view
  -> selection of observable, projection, read model, computation, authority, and consistency expectation
  -> observation | value | stream | nil | rejection
```

The observer interprets the request in light of the following factors.

- The specific [[Observer|observer]].
- The observer [[Boundaries|boundary]] and current view of state.
- The [[Observable|observable]], [[Projection Models|projection]], read model, computation, or [[Shape|shape]] being requested.
- [[Authority]], access policy, and disclosure rules.
- Freshness, ordering, and consistency expectations.
- Optional version, cursor, snapshot, or read boundary.

A successful request’s result is usually an [[Observation|observation]] or [[Value|value]]. The query selects or parameterizes how state should become visible, including the requested [[Shape|shape]]; the observation is the contextualized value produced.

A query request does not request a [[Transition|transition]] of the modeled semantic entity state. However, operational state can still change while serving a query: caches may fill, metrics may record, cursors may advance, locks may be acquired, acknowledgments may be emitted, and audit records may be written. Those effects belong to other operational or semantic subjects unless the input is also interpreted as a command for them.

A query request is therefore dual to [[Command|command]] only in a limited modeling sense:

- A command interprets input as intent to change modeled state.
- A query request expresses intent to observe modeled state or derived information.

The distinction is semantic, not transport-level. Request/reply, actor ask, RPC, shared-memory read, stream subscription, and broker-backed fetch can all carry query requests at different interaction layers.

In [[CQRS]], queries are commonly answered from read-side projections, indexes, materialized views, caches, or derived state. The correctness question is boundary-relative: the query result may be current, stale, monotonic for one observer, read-your-writes for one session, or only eventually consistent with authoritative persistence.

## Formal relations

- `distinguished_from`: [[Query]] — The input asks an observer for information; a query defines a derivation that can also be evaluated without receiving a message.
