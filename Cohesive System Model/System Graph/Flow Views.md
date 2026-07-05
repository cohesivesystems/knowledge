---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-05
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

Related concepts: [[Process|process]], [[Process Graphs|process graphs]], [[Business Transactions|business transactions]], [[Projection Models|projection models]], [[Event|event]], [[Command|command]], [[Observer Models|observer models]], [[Observer|observer]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Coordination|coordination]], [[Ordering|ordering]], [[Trace and Feedback|trace and feedback]], [[Compositionality|compositionality]].
