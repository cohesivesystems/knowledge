---
realm: System Structure
kind: structural-construct
---

# Flows

Flows describe movement through the system graph over time.

At the structure level, a flow is usually a property or view of a [[Process|process]], [[Processes|process structure]], projection, interaction, or business transaction. A flow arranges how observations, events, commands, notifications, projection updates, process signals, workflow steps, artifacts, or runtime messages move between observers and entities. This describes semantic movement and interaction shape, not the concrete protocol, broker, queue, or transport substrate.

[[Business Transactions]] use flows to compose application-level protocols into domain work such as tender exchange, shipment changes, tracking updates, delivery confirmation, or invoicing.

A flow is not the whole process. It does not by itself define subject identity, participant roles, durable process state, decisions, policies, compensation, recovery, or completion meaning. Those belong to the process or transaction that owns or uses the flow.

Flows provide structure for:

- Exogenous event arrival.
- Command interpretation.
- Endogenous event emission.
- Observer-to-observer interaction.
- Projection updates.
- Process progression.
- Recovery and retry paths.

Flows must be described with their interaction pattern, delivery semantics, ordering scope, failure boundary, and acknowledgment meaning.

Related concepts: [[Process|process]], [[Processes|processes]], [[Business Transactions|business transactions]], [[Event|event]], [[Command|command]], [[Observer|observer]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Coordination|coordination]], [[Ordering|ordering]], [[Trace and Feedback|trace and feedback]], [[Compositionality|compositionality]].
