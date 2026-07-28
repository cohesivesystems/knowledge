---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-27
---

# Rate Limiting

Rate Limiting constrains how quickly work may be accepted, dispatched, delivered, or processed.

Rate limiting protects observers, entities, dependencies, brokers, and storage systems from overload. It is part of the control semantics that shape execution across boundaries.

A rate limit should define:

- The subject being limited, such as identity, observer, tenant, entity, route, queue, or dependency.
- The window or budget.
- The response when the limit is exceeded.
- Whether delayed work preserves ordering.
- Whether retries are allowed and how they are scheduled.

Rate limiting often appears with backpressure, retry, queueing, and admission control.

[[Interaction Control Flow|Interaction control flow]] determines which participant has a natural enforcement point. An active driver can reduce fetch cadence or batch size before pushing to a constrained sink. A passive sink in a sender-driven path may instead need to refuse, shed, block, or admit into a bounded queue. The control-flow role does not choose the rate policy; it determines where that policy can regulate progress.

## External References

- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Queueing Theory|queueing theory]], [[Retry|retry]], [[Ordering|ordering]], [[Recovery|recovery]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Brokers|brokers]], [[Application Hosts|application hosts]].
