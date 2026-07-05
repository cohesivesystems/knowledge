---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-06-29
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

Examples:

- An endogenous event emitted by one [[Observer|observer]] becomes an exogenous event for another.
- A process observes an event and emits a command that later produces another event.
- A projection feeds a decision process, which emits commands that affect future projection state.
- Retry and recovery loops re-drive incomplete work.
- Rate limiting and backpressure are control feedback over interaction flow.

Feedback must be modeled with boundaries, ordering, idempotency, and recovery semantics. Otherwise the system may accidentally turn a legitimate loop into duplicate effects, livelock, or uncontrolled amplification.

Related concepts: [[Behavior|behavior]], [[Flows|flows]], [[Processes|processes]], [[Observer|observer]], [[Event|event]], [[Command|command]], [[Retry|retry]], [[Recovery|recovery]], [[Rate Limiting|rate limiting]], [[Fixed Points and Recursion|fixed points and recursion]].
