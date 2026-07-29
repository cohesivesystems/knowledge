---
realm: Realization Substrate
kind: pattern
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - AIMD
  - Additive-Increase Multiplicative-Decrease
  - Additive Increase and Multiplicative Decrease
---

# Additive Increase Multiplicative Decrease

Additive increase multiplicative decrease, commonly abbreviated AIMD, is a feedback-control pattern that probes for additional capacity with gradual additive increases and responds to congestion or overload with proportional decreases.

For a bounded control value $w_k$, one basic discrete form is:

$$
w_{k+1} =
\begin{cases}
\min(w_{\max}, w_k + a), & \text{when increase is permitted} \\
\max(w_{\min}, \beta w_k), & \text{when decrease is required}
\end{cases}
$$

Here $a>0$ is the additive step and $0<\beta<1$ is the retained fraction after decrease. The signal, cadence, bounds, units, and rounding rule are part of the realization. Absence of a decrease signal does not inherently prove spare capacity; the policy must say when it counts as permission to probe upward.

## Control Interpretation

AIMD needs:

- A controlled boundary and capacity-bearing resource.
- A manipulated variable such as rate, concurrency, window, permit count, fetch demand, or batch size.
- Evidence classified as increase-permitting, decrease-requiring, or inconclusive.
- An update event or evaluation interval.
- Initial, minimum, and maximum values.
- Additive step $a$, multiplicative factor $\beta$, and integer or unit conversion rules.
- A policy for idle periods, missing feedback, restart, and state transfer.

The characteristic trajectory is a gradual probe followed by a sharper retreat. It usually oscillates around a changing capacity boundary rather than converging to one fixed value. The size and period of that oscillation depend on feedback delay, update cadence, $a$, $\beta$, workload, and the relationship between the controlled value and congestion.

The controller state is at least the current window or control value and may include recent feedback, an epoch, last decrease time, smoothed signals, or recovery mode. It is separate from the controlled resource and from the work admitted under the resulting limit.

## Application beyond Network Windows

TCP congestion control is the best-known realization, but AIMD is not intrinsically a network algorithm. A [[Control Models|control model]] can apply it to:

- **Adaptive concurrency:** add one or a fixed number of permits after healthy completions; multiply the limit down after latency, saturation, timeout, or failure evidence.
- **Adaptive throttling:** increase an admission or pacing rate while objectives hold; decrease it proportionally when overload appears.
- **Adaptive batching:** increase batch size while per-item efficiency improves within latency bounds; reduce it proportionally after deadline, queue-age, memory, or latency pressure.
- **Fetch or prefetch demand:** probe for more in-flight work and retreat when receiver or dependency pressure appears.

Each use requires its own directionality. Increasing batch size may improve throughput but worsen latency; increasing concurrency may improve throughput below saturation and reduce it above the contention knee. A decrease signal must correspond to the actuator's actual effect in the declared operating region.

## Fairness and Distributed Use

The classical AIMD analysis shows convergence toward efficient and fair sharing under particular assumptions about a shared bottleneck, comparable users, synchronous binary feedback, and linear resource allocation. Those conclusions do not automatically transfer to heterogeneous services, unequal work costs, different feedback delays, priorities, minimum reservations, multiple bottlenecks, or per-instance controllers.

Independent controllers can synchronize their decreases and increases, producing aggregate sawtooth load and unused capacity after a common congestion event. Jitter, randomized update times, per-scope budgets, or hierarchical control can reduce correlation. They do not correct a feedback signal that identifies the wrong bottleneck.

Per-instance AIMD limits can also violate a global capacity envelope when replica count changes. If every new instance initializes with the same window, autoscaling can multiply aggregate admission before feedback catches up. The controlled scope, state initialization, and relation to [[Scaling Mechanisms|scaling]] must be explicit.

## Configuration and Stability

- Larger $a$ adapts upward faster but increases overshoot and oscillation amplitude.
- Smaller $\beta$ retreats more aggressively but can underutilize capacity after noisy or transient signals.
- Delayed feedback allows more increase steps before a decrease is observed.
- Smoothing can reject noise while adding detection delay.
- Hysteresis and minimum residence can prevent chattering but slow response.
- Floors preserve minimum progress or reserved service; ceilings enforce safety or quota bounds.
- Quantization matters when rates, batch sizes, or permits are integers.

An AIMD controller can become part of a [[Metastability|metastable]] loop when decreases arrive too late, rejected work retries immediately, or synchronized recovery repeatedly overloads the same dependency. The objective should be useful completion at the controlled boundary, not merely absence of one congestion signal.

## Distinction from PID Control

AIMD commonly acts on classified events or conditions and needs no continuously meaningful numeric error. [[PID Control|PID control]] instead combines proportional, integral, and derivative terms from a numeric error signal sampled over time.

The patterns can be combined. AIMD may select a safe outer concurrency envelope while a faster proportional or PI controller regulates an inner target, or a supervisory policy may switch algorithms by operating regime. Such composition needs explicit authority, state transfer, and time-scale separation.

## Modeling Checks

- What value is increased and decreased, in which unit and scope?
- What evidence permits increase, requires decrease, or leaves the value unchanged?
- What are $a$, $\beta$, the update cadence, bounds, and rounding rules?
- How delayed, noisy, lost, or duplicated can feedback be?
- Does the manipulated variable have the assumed direction throughout the operating region?
- How do several controller instances share a bottleneck and capacity budget?
- How is controller state initialized after idle, restart, scale-out, or ownership transfer?
- What useful-throughput, latency, fairness, and stability evidence validates the policy?

## External References

- Dah-Ming Chiu and Raj Jain, [Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks](https://www.cs.wustl.edu/~jain/papers/cong_av.htm), *Computer Networks and ISDN Systems* 17(1):1-14, 1989.
- Sally Floyd, [RFC 2914: Congestion Control Principles](https://www.rfc-editor.org/rfc/rfc2914.html), especially Section 9.2 on additive increase and multiplicative decrease, 2000.

Related concepts: [[Control Theory|control theory]], [[Control Models|control models]], [[PID Control|PID control]], [[Trace and Feedback|trace and feedback]], [[Flow Control|flow control]], [[Rate Limiting|rate limiting]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Scalability|scalability]], [[Metastability|metastability]], [[Locality|locality]], [[Queueing Theory|queueing theory]], [[Scaling Mechanisms|scaling mechanisms]], [[Policy|policy]], [[Policy Scopes|policy scopes]], [[Observable|observable]], [[Observation|observation]], [[Time|time]], [[Uncertainty|uncertainty]], [[Boundaries|boundaries]], [[Operational Control|operational control]], [[Observability and Provenance|observability and provenance]], [[Runtimes|runtimes]].
