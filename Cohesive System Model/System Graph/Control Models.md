---
realm: System Graph
kind: structural-construct
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Control Model
  - Control Block
  - Control Blocks
  - cohesive.control
---

# Control Models

Control models place adaptive observation, decision, and actuation loops in the system graph.

A `Cohesive.Control` block authors one control model. It identifies what is observed, what objective and policy govern regulation, what controller state is retained, what bounded action may be proposed, which participant is authorized to actuate it, and which later observations close the loop. It does not prescribe one algorithm, runtime, metric system, or infrastructure controller.

[[Control Theory|Control theory]] supplies the source discipline. [[Observable|Observables]], [[Observation|observations]], [[Policy|policies]], [[Observer Models|observer models]], [[Effects]], and [[Interaction|interactions]] supply the semantic and structural trace. [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID]], thresholds, hysteresis, and model-based controllers are possible realization choices.

## Structural Roles

A control model should identify:

- **Controlled boundary:** the service, interaction edge, queueing center, runtime, resource, or infrastructure scope whose behavior is regulated.
- **Controlled variable:** the quantity or outcome to regulate, such as useful throughput, latency, queue age, backlog, rejection rate, saturation, batch formation delay, or in-flight work.
- **Observable and observation:** how the variable becomes visible, including its unit, aggregation, time window, provenance, and uncertainty.
- **Reference or objective:** a setpoint, target range, service objective, capacity envelope, or optimization criterion governed by a [[Policy Scopes|policy scope]].
- **Controller policy and state:** the decision rule and retained material needed across evaluations.
- **Manipulated variable:** the value the controller proposes to change, such as rate, permits, batch size, wait interval, replica target, or fetch demand.
- **Actuator and authority:** the participant and [[Interfaces|interface]] through which an authorized action is requested.
- **Actuation evidence:** acknowledgment, observation, or result that distinguishes requested, accepted, applied, and effective action.
- **Disturbances and constraints:** demand, failures, dependency behavior, quotas, bounds, fairness, safety, and operational limits outside the controller's direct choice.

The controlled variable and manipulated variable must not be conflated. Queue age may be controlled by changing concurrency; latency may be controlled by changing admission rate; batch efficiency may be controlled by changing batch size and maximum wait. The model should state the expected direction and operating region because the relationship can reverse near saturation.

## State and Authority

Controller state is distinct from the state being controlled:

- **Controlled-system state** belongs to the modeled service, entity, process, queue, runtime, or infrastructure boundary.
- **Controller state** includes previous observations, error accumulation, smoothed estimates, AIMD windows, PID integrals, derivative history, mode, and last decision.
- **Actuator state** records the currently requested, accepted, or enforced setting.
- **Policy state** records targets, bounds, gains, step sizes, budgets, and configuration revisions.

A control block does not acquire domain [[Authority|authority]] merely by observing a metric or emitting an action. Its actuator authority must be explicit and bounded. Adjusting concurrency, admission, or batch size usually exercises [[Operational Control|operational authority]], not authority to accept a business transition, change authoritative entity state, or redefine completion semantics.

If controller state affects future behavior, restart and ownership transfer need an explicit policy. State may be durably restored, safely reinitialized, reconstructed from recent observations, or deliberately forgotten. A stale controller must be fenced when multiple realizations could actuate the same scope.

## Adaptive Resource Uses

The same control structure can regulate several mechanisms while preserving their different meanings:

| Use | Representative controlled variables | Manipulated variables | Important constraints |
| --- | --- | --- | --- |
| Adaptive throttling | latency, useful throughput, rejection, saturation, queue age | admission rate, token rate, pacing interval, accepted fraction | [[Admission Control and Load Shedding|admission obligations]], retry amplification, fairness, shared dependencies |
| Adaptive batching | per-item cost, completion latency, queue age, backlog, batch fill | maximum batch size, minimum size, formation wait, flush trigger | deadlines, ordering, partial batches, effect and commit boundaries |
| Adaptive concurrency | useful throughput, latency, saturation, lock or pool pressure | permits, workers, fetch count, in-flight limit | contention knee, locality, downstream capacity, scheduling and ownership |

One block can manipulate more than one variable, but coupled actuators make attribution and tuning harder. Separate blocks can instead control rate, concurrency, and batching at different time scales. Their shared objectives and conflict policy must then be explicit.

## Evaluation and Actuation

A control evaluation is one finite observer activation:

```text
observations + target + controller state
  -> control decision
  -> bounded action proposal + next controller state
```

The decision does not itself change the controlled system. An [[Effect|effect]] or interaction carries the action to an actuator, and later evidence establishes whether the action was accepted, applied, and effective. Controller state and action responsibility may need one [[Commit Boundaries|commit boundary]] when a lost or duplicated actuation would be harmful.

Evaluation cadence can be periodic, event-driven, completion-driven, or hybrid. The model should specify how missing data, sparse traffic, counter resets, partial windows, outliers, stale observations, and delayed actuation affect the next decision. A controller that evaluates faster than the controlled system settles can repeatedly react to its own unfinished actions.

## Composition and Modes

Control models may be:

- Open-loop, feedback, feedforward, or hybrid.
- Centralized, distributed, hierarchical, cascaded, or peer-to-peer.
- Stateless between evaluations or stateful across a history.
- Continuous-valued, quantized, thresholded, or mode-switching.
- Single-input/single-output or coupled across several observations and actuators.

Composition must identify overlapping observation and actuation scopes. A local concurrency controller, global admission controller, autoscaler, partition rebalancer, and retry controller can each be reasonable alone while forming an unstable or [[Metastability|metastable]] loop together. Time-scale separation, precedence, shared budgets, coordination, and supervisory modes are possible composition tools; none makes stability automatic.

## Realization and Lowering

A `Cohesive.Control` realization lowers into:

- An [[Observer Models|observer model]] that samples or receives observations and evaluates the controller policy.
- A scheduler, timer, completion callback, stream window, or runtime activation that supplies evaluation cadence.
- Local or durable controller-state storage with explicit initialization and recovery.
- An actuator adapter for a rate limiter, admission controller, batcher, semaphore, worker pool, consumer, scheduler, deployment controller, or other public substrate role.
- Metrics, traces, decision records, configuration revision, and actuation evidence for [[Observability and Provenance|observability and provenance]].

The lowering must preserve units, boundaries, timing assumptions, target and policy revision, controller state identity, action bounds, authority, and the difference between requested and achieved action. It should also declare what happens when the selected algorithm is unsupported, observations are unavailable, or actuation fails.

## Modeling Checks

- What does the block control, observe, and manipulate?
- What is the target, unit, operating range, and applicable policy scope?
- What are the observation and actuation delays and the evaluation cadence?
- Which state belongs to the controller, controlled system, actuator, and policy?
- Who is authorized to change the manipulated variable, and at which boundary?
- What evidence distinguishes proposed, accepted, applied, and effective action?
- Which clamps, safety envelopes, fairness rules, and degraded modes apply?
- How does the block initialize, persist or forget state, restart, recover, and transfer ownership?
- Which other control blocks share the same resource, observation, or actuator?
- Which realization algorithm is selected, and which assumptions make it valid?

Related concepts: [[Control Theory|control theory]], [[Observer Models|observer models]], [[Observable|observable]], [[Observation|observation]], [[Observer|observer]], [[Policy|policy]], [[Policy Scopes|policy scopes]], [[Effects]], [[Effect|effect]], [[Interaction|interaction]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Boundaries|boundaries]], [[Authority|authority]], [[Identity|identity]], [[State|state]], [[Time|time]], [[Uncertainty|uncertainty]], [[Trace and Feedback|trace and feedback]], [[Operational Control|operational control]], [[Observability and Provenance|observability and provenance]], [[Commit Boundaries|commit boundaries]], [[Persistence|persistence]], [[Durability|durability]], [[Reconstitution|reconstitution]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Scheduling|scheduling]], [[Rate Limiting|rate limiting]], [[Flow Control|flow control]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Scalability|scalability]], [[Locality|locality]], [[Metastability|metastability]], [[Scaling Mechanisms|scaling mechanisms]], [[Additive Increase Multiplicative Decrease|additive increase multiplicative decrease]], [[PID Control|PID control]], [[Runtimes|runtimes]], [[Compute|compute]], [[Infrastructure Graph|infrastructure graph]].
