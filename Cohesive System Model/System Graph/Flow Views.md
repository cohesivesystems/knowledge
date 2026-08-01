---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-08-01
aliases:
  - Flow
  - Flows
---

# Flow Views

Flow views describe movement through the system graph over time.

At the structure level, a flow view is usually a property or projection of a [[Process|process]], [[Process Graphs|process graph]], [[Projection Models|projection model]], [[Interaction|interaction]], or [[Business Transactions|business transaction]]. A flow view arranges how observations, events, commands, notifications, projection updates, process signals, workflow steps, artifacts, or runtime messages move between observer models and entity models. This describes semantic movement and interaction shape, not the concrete protocol, broker, queue, or transport substrate.

[[Business Transactions]] use flow views to compose application-level protocols into domain work such as tender exchange, shipment changes, tracking updates, delivery confirmation, or invoicing.

A flow view is not the whole process. It does not by itself define subject identity, participant roles, durable process state, decisions, policies, compensation, recovery, or completion meaning. Those belong to the process graph or transaction that owns or uses the flow view.

Flow views provide structure for:

- Exogenous event arrival.
- Command interpretation.
- Endogenous event emission.
- Observer-to-observer interaction.
- Projection updates.
- Process progression.
- Recovery and retry paths.

Flow views must be described with their interaction pattern, delivery semantics, ordering scope, failure boundary, and acknowledgment meaning.

[[Flow Operators|Flow operators]] make repeated transformation, filtering, splitting, aggregation, resequencing, scatter-gather, and composed-processing structures explicit. [[Routing Models|Routing models]] make destination and path selection explicit. These structures can appear in a flow view without becoming the semantic process that owns the larger goal and completion meaning.

## Flow Kinds and Arrow Discipline

A flow view should state what each arrow means. At minimum, distinguish:

- **Carried-value or message flow**: which observations, commands, events, effects, artifacts, or other values move between participants.
- **[[Interaction Control Flow|Interaction control flow]]**: which participant actively pushes, fetches, polls, or delivers at each interaction boundary.
- **Causal flow**: which occurrences may have influenced later occurrences.
- **Process progression**: which step, branch, token, state, or decision can follow another.

When a realization projection overlays runtime detail, it should additionally label the **execution trace**: which callback, handler, continuation, task, or activation receives execution opportunity, yields, is preempted, resumes, or completes under [[Scheduling|scheduling]]. This is a runtime projection, not another semantic process edge.

These relations can align, oppose one another, or exist at different abstraction layers. In a polling interaction, data moves from a source to a consumer while the consumer drives the fetch toward the source. A process-progression edge may lower into several such interactions and runtime activations, and a dataflow pipeline may hide local scheduling, callbacks, queues, or drivers. An unqualified arrow should not be assumed to express all of these meanings.

## External References

- Gregor Hohpe and Bobby Woolf, [Pipes and Filters](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html), *Enterprise Integration Patterns*, 2003.
- Enterprise Integration Patterns, [Message Routing and Transformation patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Process|process]], [[Process Graphs|process graphs]], [[Business Transactions|business transactions]], [[Projection Models|projection models]], [[Event|event]], [[Command|command]], [[Observer Models|observer models]], [[Observer|observer]], [[Messages and Envelopes|messages and envelopes]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Flow Operators|flow operators]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Scheduling|scheduling]], [[Runtimes|runtimes]], [[Delivery Semantics|delivery semantics]], [[Coordination|coordination]], [[Ordering|ordering]], [[Trace and Feedback|trace and feedback]], [[Compositionality|compositionality]].
