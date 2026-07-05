---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-05
---

# Business Transactions

Business Transactions describe domain-level units of work whose progress, acceptance, rejection, compensation, or completion matters to the business.

A business transaction is not the same as a database transaction. A database transaction is one possible coordination mechanism inside a business transaction. A business transaction may span observer models, entity models, services, brokers, workflow engines, humans, agents, external systems, and time.

At the structure level, a business transaction arranges [[Process Graphs|process graphs]], their [[Flow Views|flow views]], [[Entity Models|entity models]], [[Observer Models|observer models]], [[Command|commands]], [[Query|queries]], [[Event|events]], [[Observation|observations]], and [[Transition|transitions]] into coherent domain work.

Examples include:

- Tender exchange.
- Tender acceptance, rejection, or counteroffer.
- Shipment or order changes.
- Tracking updates.
- Pickup or delivery confirmation.
- Invoice creation, adjustment, approval, or settlement.

## Composition

Business transactions are examples of [[Compositionality|compositionality]]. They are implemented by composing lower-level semantic, operational, and realization layers:

```txt
business transaction
  -> process graph and flow views
  -> commands, queries, events, observations, transitions
  -> application-level interaction protocols
     (request/reply, publish/consume, durable execution, event-sourced commit)
  -> operational concerns
     (persistence, delivery, ordering, retry, idempotency, recovery, coordination)
  -> realization substrate
     (RPC, brokers, workflow engines, event stores, databases)
  -> transport, network, and link protocols
     (TCP, UDP, IP, Ethernet)
  -> physical or electrical protocols
```

Each layer contributes local guarantees. The business transaction is correct only when those guarantees compose into the intended domain semantics. For example, an RPC response, a broker acknowledgment, a workflow checkpoint, and an event-store append may each be successful at their own boundary while still meaning different things for the business transaction.

Application-level pieces include [[Interaction|request/reply]], [[Interaction|publish/consume]], [[Durable Execution|durable execution]] through [[Durable Execution Engines|durable execution engines]], and committed-event persistence through [[Event Sourcing|event sourcing]]. These pieces can be combined, but their guarantees remain scoped to their own boundaries unless coordination composes them into a business-level outcome.

## Modeling Questions

A business transaction should identify:

- The business subject or correlation identity.
- Participating entity models, observer models, people, agents, and external systems.
- Commands that request state transitions.
- Queries and observations needed for decisions.
- Endogenous events that mark accepted domain change.
- Output events, notifications, or documents emitted across boundaries.
- The process state or workflow state, if the transaction is long-lived.
- The commit, rejection, cancellation, timeout, and compensation meanings.
- Interaction modes used between participants.
- Persistence, ordering, retry, idempotency, recovery, and audit requirements.

## Examples

Tender exchange may compose request/reply for quote or tender submission, queries for carrier capacity or rate observations, command handling for accept/reject decisions, published events for tender status changes, and durable workflow state for timeouts or counteroffers.

Shipment changes may compose command validation against current shipment state, related policy observations, expected-version checks, accepted transitions or committed event records, projection updates, and notifications to downstream observers.

Tracking updates may compose high-volume publish/consume interaction, idempotent event ingestion, ordering by shipment or stop, projection reconstitution, and queryable read models for visibility.

Delivery confirmation may compose mobile or external input, observer-relative command interpretation, proof-of-delivery observations, entity transition commitment, output events, and recovery behavior when connectivity is intermittent.

Invoicing may compose delivery and rating observations, invoice entity transitions, approval processes, external accounting interactions, event-sourced audit history, and compensating adjustments.

## Boundaries

Business transaction boundaries are domain boundaries. They define what counts as accepted, rejected, completed, cancelled, expired, compensated, or settled for the business.

Those boundaries rarely coincide exactly with one protocol, process, transaction, or storage boundary. A business transaction may include several local [[ACID]] transactions, several RPC calls, several broker messages, several workflow activations, and several event-store commits. When [[Two-Phase Commit|two-phase commit]] is not used or does not cover the whole business outcome, the model must name the [[Weak Isolation Patterns|weak isolation patterns]] that preserve the relevant [[Invariant|invariants]].

Correct modeling therefore requires naming the boundary for each guarantee:

- Did the transport accept bytes?
- Did the application protocol produce a reply?
- Did the receiver interpret the input as a command or query?
- Did an entity transition commit?
- Did a workflow checkpoint progress?
- Did an output event become durable?
- Did another observer receive, process, or commit the follow-up work?
- Did the business transaction reach its domain-defined completion condition?

Related concepts: [[Process Graphs|process graphs]], [[Flow Views|flow views]], [[Coordination|coordination]], [[Isolation|isolation]], [[ACID]], [[Two-Phase Commit|two-phase commit]], [[Weak Isolation Patterns|weak isolation patterns]], [[Durable Execution|durable execution]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Persistence|persistence]], [[Recovery|recovery]], [[Idempotency|idempotency]], [[Ordering|ordering]], [[Event Sourcing|event sourcing]], [[CQRS]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Brokers|brokers]], [[Network|network]], [[Compositionality|compositionality]].
