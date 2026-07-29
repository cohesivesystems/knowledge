---
realm: Realization Substrate
kind: pattern
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - PID
  - PID Controller
  - Proportional Integral Derivative Control
  - PI Control
  - PD Control
---

# PID Control

PID control is a feedback-control pattern that forms a control action from proportional, integral, and derivative contributions of an error signal.

For reference $r(t)$, observed output $y(t)$, and error $e(t)=r(t)-y(t)$, an ideal continuous form is:

$$
u(t)=u_0 + K_p e(t) + K_i\int_0^t e(\tau)\,d\tau + K_d\frac{de(t)}{dt}
$$

$u$ is the requested manipulated value, $u_0$ is an optional bias, and $K_p$, $K_i$, and $K_d$ are controller gains. Actual digital controllers use sampled and often filtered forms, output bounds, state initialization, and a declared sign convention.

The equation does not establish that increasing $u$ increases $y$. A concurrency actuator, throttle, batch size, or queue drain rate can have different and even non-monotonic effects across operating regions. Controller direction must follow the measured input-output relationship at the controlled boundary.

## Proportional, Integral, and Derivative Terms

- The **proportional** term reacts to current error. Larger proportional gain responds more strongly but can overshoot or oscillate when delay and inertia are significant.
- The **integral** term accumulates error. It can remove steady-state offset but retains memory and can continue growing while the actuator is saturated.
- The **derivative** term reacts to error trend. It can add damping or anticipation but amplifies measurement noise and is sensitive to sampling and filtering.

Setting one or more gains to zero yields common variants:

- **P control** uses current error only.
- **PI control** adds accumulated error and is useful when steady-state offset matters but derivative evidence is too noisy.
- **PD control** adds trend response without integral correction.
- **PID control** combines all three terms when the controlled dynamics and observation quality justify them.

The names identify controller structure, not a guarantee of stability or performance.

## Digital Realization

A digital realization must define:

- Sampling interval or event cadence and the time basis used by integral and derivative calculations.
- Error sign, scaling, units, normalization, and target changes.
- Numerical integration and differentiation methods.
- Filtering, missing-data, outlier, stale-signal, and counter-reset behavior.
- Output clamps, quantization, rate-of-change limits, and actuator acceptance.
- Initialization, restart, controller-state persistence, and mode transfer.
- Gain values, tuning evidence, and the operating region for which they are valid.

Irregular sampling requires actual elapsed time rather than assuming one fixed interval. Windowed latency percentiles, queue depth, and utilization are already filtered or aggregated observations; applying another filter changes lag and phase. Controller design should use the timing of the measurement path, not only the evaluation timer.

## Saturation and Integral Windup

Software actuators are bounded. Concurrency cannot fall below a safe minimum or exceed quota; batch size is integral and bounded; rate may be clamped; capacity may be requested but unavailable. When the computed action exceeds those bounds, the actuator saturates.

If the integral continues accumulating error while saturated, it can **wind up**. After the error reverses, the stored integral can keep driving the controller in the old direction, producing overshoot and slow recovery. Anti-windup mechanisms include conditional integration, integral clamping, back-calculation from achieved output, or tracking the actually applied actuator value.

Requested and achieved action must therefore remain distinct. Feeding the unclamped request back as though it were applied hides saturation and weakens anti-windup behavior.

## Derivative, Setpoint, and Mode Handling

Direct differentiation amplifies noise. Practical controllers often filter the derivative and may differentiate the observation rather than the error so a setpoint step does not produce a large derivative kick. The exact choice changes behavior and must be part of the realization contract.

Changing targets, gains, algorithms, manual settings, or controller ownership can produce discontinuous output. **Bumpless transfer** initializes controller state or bias so the applied action does not jump unnecessarily during a mode change. A deadband can suppress small reactions near the target, and hysteresis can prevent rapid mode switching, but both introduce deliberate error regions.

## Adaptive Throttling, Batching, and Concurrency

A [[Control Models|control model]] can use P, PI, PD, or PID control for:

- **Adaptive throttling:** regulate latency, saturation, queue age, or rejection by changing admission rate or pacing.
- **Adaptive batching:** balance formation latency and per-item efficiency by changing batch size or flush delay.
- **Adaptive concurrency:** regulate useful throughput, latency, or resource pressure by changing permits or in-flight work.

These software-controlled systems are often nonlinear, workload-dependent, and delayed. Tail latency may change abruptly near saturation, useful throughput can decline after the concurrency knee, and changing batch size alters both service demand and observation cadence. One globally fixed gain set may not remain valid across light load, saturation, recovery, and changed dependency behavior.

Gain scheduling, supervisory modes, clamps, or a hybrid controller can address distinct operating regions. Such additions need explicit switching and state-transfer semantics. They do not justify applying PID where the error is not meaningfully numeric or the actuator relationship is unknown.

## Distributed and Interacting Controllers

Per-instance PID controllers can act on a shared dependency while observing only local latency. Their integral terms may all increase during an apparent local deficit, collectively pushing the dependency further into overload. Autoscaling, retry, load balancing, and admission controllers add other loops and delays.

The [[Control Theory|control-theory]] model should therefore include the composed boundary. Controller gains, sampling, saturation, and stability evidence from one instance do not prove stability after replica count, routing, workload mix, locality, or dependency topology changes. Coordinated limits, hierarchical control, or distinct time scales may be required.

## Distinction from AIMD

[[Additive Increase Multiplicative Decrease|AIMD]] reacts to classified increase and decrease conditions with asymmetric discrete updates. PID uses the magnitude and history of a numeric error. AIMD naturally probes and retreats in a sawtooth pattern; PID is ordinarily tuned for regulation or tracking around an operating region.

Neither is universally superior. AIMD may be more robust when only binary congestion evidence is trustworthy. PI or PID may regulate a measurable target more closely when the input-output relation, timing, and saturation behavior are sufficiently characterized.

## Modeling Checks

- What are $r$, $y$, $e$, and $u$, with which units and sign convention?
- Is the manipulated variable's direction monotone in the intended operating region?
- What are the sampling, measurement, actuation, and settling delays?
- Which P, I, and D terms are enabled, with which gains and tuning evidence?
- How are noise, aggregation, missing observations, and irregular sampling handled?
- What bounds and rate limits constrain the actuator?
- Which anti-windup rule uses the actually applied action?
- How are setpoint changes, manual mode, algorithm changes, restart, and ownership transfer made bumpless?
- Which other control loops and shared resources can change the effective plant?
- What observations demonstrate stability, useful throughput, fairness, and recovery across operating regimes?

## External References

- Karl J. Åström and Richard M. Murray, [PID Control](https://www.cds.caltech.edu/~murray/books/AM05/pdf/am08-pid_19Jul11.pdf), Chapter 10 of *Feedback Systems: An Introduction for Scientists and Engineers*.
- Karl J. Åström and Tore Hägglund, *Advanced PID Control*, ISA, 2006.

Related concepts: [[Control Theory|control theory]], [[Control Models|control models]], [[Additive Increase Multiplicative Decrease|additive increase multiplicative decrease]], [[Trace and Feedback|trace and feedback]], [[Observable|observable]], [[Observation|observation]], [[Policy|policy]], [[Policy Scopes|policy scopes]], [[State|state]], [[Time|time]], [[Uncertainty|uncertainty]], [[Boundaries|boundaries]], [[Operational Control|operational control]], [[Observability and Provenance|observability and provenance]], [[Flow Control|flow control]], [[Rate Limiting|rate limiting]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Scheduling|scheduling]], [[Scalability|scalability]], [[Metastability|metastability]], [[Locality|locality]], [[Queueing Theory|queueing theory]], [[Scaling Mechanisms|scaling mechanisms]], [[Runtimes|runtimes]], [[Compute|compute]].
