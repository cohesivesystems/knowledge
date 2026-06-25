---
realm: System Structure
---

# Flows

Realm: System Structure

Flows describe movement through the system graph over time.

At the structure level, a flow arranges how observations, events, commands, notifications, projection updates, process signals, workflow steps, or runtime messages move between observers and entities. This describes semantic movement and interaction shape, not the concrete protocol, broker, queue, or transport substrate.

[[Business Transactions]] use flows to compose application-level protocols into domain work such as tender exchange, shipment changes, tracking updates, delivery confirmation, or invoicing.

Flows provide structure for:

- Exogenous event arrival.
- Command interpretation.
- Endogenous event emission.
- Observer-to-observer interaction.
- Projection updates.
- [[Processes]] progression.
- Recovery and retry paths.

Flows must be described with their interaction pattern, delivery semantics, ordering scope, failure boundary, and acknowledgment meaning.

Related concepts: [[Business Transactions]], [[Event]], [[Command]], [[Observer]], [[Interaction]], [[Delivery Semantics]], [[Coordination]], [[Ordering]], [[Trace and Feedback]], [[Compositionality]].
