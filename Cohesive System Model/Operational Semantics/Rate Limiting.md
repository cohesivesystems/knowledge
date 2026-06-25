---
realm: Operational Semantics
---

# Rate Limiting

Realm: Operational Semantics

Rate Limiting constrains how quickly work may be accepted, dispatched, delivered, or processed.

Rate limiting protects observers, entities, dependencies, brokers, and storage systems from overload. It is part of the control semantics that shape execution across boundaries.

A rate limit should define:

- The subject being limited, such as identity, observer, tenant, entity, route, queue, or dependency.
- The window or budget.
- The response when the limit is exceeded.
- Whether delayed work preserves ordering.
- Whether retries are allowed and how they are scheduled.

Rate limiting often appears with backpressure, retry, queueing, and admission control.

Related concepts: [[Retry]], [[Ordering]], [[Recovery]], [[Interaction]], [[Brokers]], [[Application Hosts]].
