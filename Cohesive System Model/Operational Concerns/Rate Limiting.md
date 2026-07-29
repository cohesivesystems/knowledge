---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-29
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

Rate limiting often appears with [[Flow Control|flow control and backpressure]], retry, queueing, and [[Admission Control and Load Shedding|admission control]]. A rate limit applies a declared time-based policy or budget; flow control adapts admission or offered work to capacity. They may regulate the same edge without becoming the same concern.

A rate limit may be static or the manipulated variable of a [[Control Models|control model]]. [[Additive Increase Multiplicative Decrease|AIMD]] or [[PID Control|PID control]] can adjust it from capacity observations, but the controller algorithm does not define the limit's subject, window, budget, or exceeded-limit response.

[[Interaction Control Flow|Interaction control flow]] determines which participant has a natural enforcement point. An active driver can reduce fetch cadence or batch size before pushing to a constrained sink. A passive sink in a sender-driven path may instead need to refuse, shed, block, or admit into a bounded queue. The control-flow role does not choose the rate policy; it determines where that policy can regulate progress.

## External References

- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Control Theory|control theory]], [[Control Models|control models]], [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID control]], [[Queueing Theory|queueing theory]], [[Flow Control|flow control]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Scalability|scalability]], [[Retry|retry]], [[Metastability|metastability]], [[Ordering|ordering]], [[Recovery|recovery]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Brokers|brokers]], [[Application Hosts|application hosts]].
