---
realm: Principles
kind: discipline
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Feedback Control
  - Closed-Loop Control
  - Control Systems
---

# Control Theory

Control theory is the discipline of regulating the behavior of a dynamical system through observation, decision, actuation, and feedback over time.

In Cohesive, control theory supplies language for adaptive throttling, batching, concurrency, autoscaling, queue regulation, congestion response, scheduling parameters, cache or resource allocation, and physical control without making those concerns identical. [[Control Models|Control models]] place this structure in the system graph, while [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID control]], threshold policies, and model-based controllers are possible realizations.

Control theory is distinct from [[Control Flow|control flow]], [[Interaction Control Flow|interaction control flow]], and [[Operational Control|operational control]]. Control flow describes progression, interaction control flow describes which participant drives an interaction, and operational control describes authorized intervention. Feedback control describes how observations of behavior are used to regulate future behavior.

## Basic Control Loop

A control loop identifies:

- The **controlled system**, traditionally called the *plant*, whose behavior is being regulated.
- A **controlled variable** or output $y$ whose behavior matters.
- An [[Observable|observable]] or sensor that produces an [[Observation|observation]] of $y$.
- A **reference**, setpoint, target range, or objective $r$.
- An **error** or other decision signal derived from the target and observation.
- A **controller** that selects a control action $u$ under a [[Policy|policy]].
- An **actuator** that attempts to apply $u$ to the controlled system.
- **Disturbances** $d$ that affect behavior but are not selected by the controller.
- Optional controller state $z$, such as an integral, previous error, smoothed estimate, window, or last decision.

A boundary-relative discrete formulation is:

$$
\begin{aligned}
y_k &= H(x_k) \\
u_k &= K(r_k, y_k, z_k) \\
x_{k+1} &= F(x_k, u_k, d_k) \\
z_{k+1} &= G(z_k, r_k, y_k, u_k)
\end{aligned}
$$

$x$ is controlled-system state, $y$ is observed output, $u$ is the requested control action, $d$ is disturbance, and $z$ is controller state. The functions are descriptive placeholders, not requirements that every controller use a known linear model or expose the controlled state directly.

The requested action and achieved actuation are separate occurrences. A controller may request concurrency `20`, batch size `100`, or admission rate `500/s` before the actuator accepts, applies, or makes that setting effective. Feedback should observe achieved behavior rather than assume the request took effect.

## Open-Loop, Feedback, and Feedforward Control

**Open-loop control** chooses action without observing the controlled result. A static batch size, scheduled rate change, or fixed concurrency limit is open-loop relative to the omitted feedback boundary even if it uses configuration or a forecast.

**Feedback control** uses observed output or error to change future action. Feedback can reject disturbances and model error, but delay, noise, saturation, and excessive gain can make it oscillate or diverge.

**Feedforward control** changes action from an observed or predicted disturbance before its effect appears in the controlled output. A launch forecast may pre-provision capacity; a known record-size estimate may select a batch size. Feedforward depends on the disturbance model and is commonly combined with feedback that corrects residual error.

These classifications are boundary-relative. A controller can be feedforward with respect to predicted demand and feedback-controlled with respect to measured latency in the same realization.

## Dynamics and Time

A useful model states the controller's time semantics:

- Sampling or event cadence.
- Measurement window, aggregation, filtering, and provenance.
- Observation, transport, decision, actuation, and settling delays.
- Controller and controlled-system state retained between decisions.
- Output bounds, quantization, rate-of-change limits, and unavailable actions.
- Timeouts, missing observations, stale signals, restart, and recovery behavior.

The controlled system can be nonlinear and time-varying. Increasing concurrency may raise throughput below saturation and lower it above the contention knee. Increasing batch size may reduce per-item overhead while increasing formation latency. One gain or actuator direction may therefore be valid only within a declared operating region.

Software controls are often discrete, delayed, quantized, and partially observed. Metrics arrive in windows, integer permits cannot change fractionally, work already in flight cannot disappear instantly, and an actuator may require warmup or drain. A controller designed as though observation and actuation were instantaneous can become unstable even if its arithmetic is correct.

## Control Objectives and Properties

Common objectives and properties include:

- **Regulation:** keep an output near a target despite disturbances.
- **Tracking:** follow a changing reference.
- **Stability:** bounded disturbances and state do not produce unbounded or self-sustaining deviation under the declared model.
- **Steady-state error:** residual difference after transients settle.
- **Transient response:** rise, overshoot, undershoot, oscillation, and settling after a change.
- **Disturbance rejection:** limit the effect of changes not selected by the controller.
- **Robustness:** preserve acceptable behavior under model error, noise, delay, workload variation, and component changes.
- **Control effort:** resource, disruption, churn, or cost imposed by actuation.
- **Constraint satisfaction:** remain inside safety, fairness, authority, and capacity envelopes while pursuing the target.

Control stability is not identical to [[Safety and Liveness|safety or liveness]]. A controller can converge to an operationally forbidden setting, remain safely bounded while never reaching a useful target, or preserve local stability while moving overload to another boundary. Control objectives must be qualified by system semantics and operational obligations.

When feedback creates a history-dependent degraded regime that persists after its initiating disturbance ends, the system exhibits [[Metastability|metastability]]. Hysteresis can be an intentional control technique that prevents rapid switching, while metastable hysteresis describes an operating regime whose sustaining loop prevents ordinary recovery; the terms should not be conflated.

## Controller Families and Related Notions

- **Threshold or bang-bang control** selects among discrete actions when an observation crosses one or more thresholds.
- **Deadband and hysteresis** suppress action or require different entry and exit thresholds near a target to reduce chattering.
- **[[Additive Increase Multiplicative Decrease|AIMD]]** probes upward gradually and retreats proportionally after a congestion signal.
- **[[PID Control|P, PI, PD, and PID control]]** combine present error, accumulated error, and error trend.
- **Gain scheduling** selects controller parameters for a declared operating region.
- **Adaptive control** changes controller parameters or structure from observations of the controlled system.
- **Model-predictive control** selects bounded actions by optimizing predicted behavior over a finite horizon.
- **Cascade control** nests a faster inner loop inside a slower outer loop.
- **Supervisory control** selects modes, targets, limits, or controller configurations rather than directly regulating every actuation.

Filters such as moving averages and exponentially weighted estimates can reduce noise but add lag. Clamps and slew-rate limits protect actuators but create saturation behavior. Integral anti-windup, derivative filtering, bumpless transfer, jitter, and stabilization windows address specific implementation pathologies; they do not replace a correct boundary and control objective.

## Distributed and Composed Control

Several local controllers can interact through shared resources without observing one another directly. Per-instance concurrency controllers can collectively overload a shared database; an autoscaler can add clients while each client reduces its local rate; a queue controller and retry controller can create a reinforcing loop.

Control properties are therefore not automatically [[Compositionality|compositional]]. A model should identify shared controlled variables, overlapping actuators, nested loops, relative time scales, controller authority, and which loop wins when objectives conflict. Randomization or jitter can reduce synchronized action, but it cannot reconcile incompatible objectives or duplicate authority.

The controlled system in control theory may be a physical process, runtime, queue, service, interaction path, or whole infrastructure graph. It is not automatically a semantic [[Process|process]], [[Process Graphs|process graph]], workflow, or process manager. [[Process Theories|Process theories]] relate these uses through interfaces, observation, state evolution, composition, and feedback without collapsing them.

## Modeling Checks

- What is the controlled boundary, system, variable, and objective?
- Which observable produces the feedback, with what delay, window, consistency, and uncertainty?
- Which participant owns the controller state and which authority permits actuation?
- What action is requested, and what observation proves it became effective?
- Is the loop open-loop, feedback, feedforward, cascaded, distributed, or a composition?
- What are the sampling, delay, saturation, quantization, and settling assumptions?
- Which stability, tracking, transient, robustness, fairness, and control-effort properties are required?
- What happens with missing, duplicated, stale, delayed, or contradictory observations?
- How does the controller initialize, restart, recover, and transfer ownership?
- Which other controllers share its observations, resources, or actuators?

## External References

- Karl J. Åström and Richard M. Murray, [Feedback Systems: An Introduction for Scientists and Engineers](https://fbsbook.org/), Princeton University Press, 2008.
- Karl J. Åström and Richard M. Murray, [PID Control](https://www.cds.caltech.edu/~murray/books/AM05/pdf/am08-pid_19Jul11.pdf), Chapter 10 of *Feedback Systems*.

Related concepts: [[Process Theories|process theories]], [[Trace and Feedback|trace and feedback]], [[Control Models|control models]], [[Control Flow|control flow]], [[Interaction Control Flow|interaction control flow]], [[Operational Control|operational control]], [[Flow Control|flow control]], [[Observable|observable]], [[Observation|observation]], [[Observer|observer]], [[Policy|policy]], [[Policy Scopes|policy scopes]], [[Behavior|behavior]], [[State|state]], [[Time|time]], [[Uncertainty|uncertainty]], [[Interaction|interaction]], [[Effect Models]], [[Boundaries|boundaries]], [[Compositionality|compositionality]], [[Safety and Liveness|safety and liveness]], [[Metastability|metastability]], [[Scalability|scalability]], [[Locality|locality]], [[Scheduling|scheduling]], [[Rate Limiting|rate limiting]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Scaling Mechanisms|scaling mechanisms]], [[Additive Increase Multiplicative Decrease|additive increase multiplicative decrease]], [[PID Control|PID control]], [[Runtimes|runtimes]], [[Infrastructure Graph|infrastructure graph]].
