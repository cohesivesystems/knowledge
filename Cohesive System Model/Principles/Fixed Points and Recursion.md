---
realm: Principles
---

# Fixed Points And Recursion

Fixed points and recursion describe self-referential definitions, repeated behavior, and systems whose outputs feed future inputs.

A fixed point is a value that is unchanged by a function:

```txt
f(x) = x
```

In modeling, fixed points appear when a whole is defined by a recursive equation or when behavior stabilizes under repeated application.

Examples:

- A [[Behavior]] can be described by recursive equations over time.
- A process can define its next state in terms of prior state and incoming events.
- Retry and recovery loops continue until success, rejection, exhaustion, or compensation.
- Projections may be rebuilt by replaying all source events until the projected state reaches the same result as incremental updates.
- Recursive system structure appears when processes spawn sub-processes or observers route to observers.

Fixed-point thinking helps distinguish productive recursion from accidental loops. A retry policy without limits, backoff, idempotency, or recovery semantics is not a meaningful fixed point; it is an uncontrolled loop.

Related concepts: [[Behavior]], [[Processes]], [[Retry]], [[Recovery]], [[Projections]], [[Event-State Duality]], [[Trace and Feedback]].
