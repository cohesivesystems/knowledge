---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-07-29
---

# Trace and Feedback

Trace and feedback describe systems where outputs are fed back as future inputs.

In categorical language, traced structure models feedback loops. In system modeling, this appears as event loops, workflows, retry loops, control loops, projections feeding commands, and observers reacting to their own or others' outputs.

Feedback questions:

- Which output becomes which future input?
- Across which boundary does the feedback travel?
- What delay, ordering, buffering, or retry semantics apply?
- Is the feedback stabilizing, amplifying, compensating, or oscillating?
- What prevents duplicate, divergent, or runaway effects?

[[Control Theory|Control theory]] qualifies one class of feedback loop with a controlled variable, objective, controller state, action, actuator, disturbances, timing, and stability criteria. [[Control Models|Control models]] place those roles and their boundary-relative observations and effects in the system graph.

Examples:

- An endogenous event emitted by one [[Observer|observer]] becomes an exogenous event for another.
- A process observes an event and emits a command that later produces another event.
- A projection model feeds a decision process, which emits commands that affect future projection-model state.
- Retry and recovery loops re-drive incomplete work.
- [[Rate Limiting|Rate limiting]] and [[Flow Control|backpressure]] are control feedback over interaction flow.

Feedback must be modeled with boundaries, ordering, idempotency, and recovery semantics. Otherwise the system may accidentally turn a legitimate loop into duplicate effects, [[Deadlock and Livelock|livelock]], or uncontrolled amplification.

When an amplifying loop makes a degraded operating regime persist after its trigger has disappeared, the system exhibits [[Metastability|metastability]]. The loop may raise effective arrivals, reduce effective capacity, or prevent the successful work needed to restore ordinary operation.

Related concepts: [[Behavior|behavior]], [[Control Theory|control theory]], [[Control Models|control models]], [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID control]], [[Flow Views|flow views]], [[Process Graphs|process graphs]], [[Observer|observer]], [[Event|event]], [[Command|command]], [[Retry|retry]], [[Recovery|recovery]], [[Rate Limiting|rate limiting]], [[Flow Control|flow control]], [[Deadlock and Livelock|deadlock and livelock]], [[Metastability|metastability]], [[Queueing Theory|queueing theory]], [[Recursion|recursion]], [[Fixed Points|fixed points]].
