---
realm: System Structure
---

# Processes

Realm: System Structure

Processes describe how multi-step work is arranged across time, observers, entities, and external systems.

A process may be a domain process, saga, process manager, durable workflow, orchestration, choreography, or operational procedure. The model treats it as structure when it gives coherence to a series of related observations, commands, events, and transitions. This describes coordination shape and participant roles, not the workflow engine or scheduler that realizes it.

[[Business Transactions]] are domain-level process structures whose progress, acceptance, rejection, compensation, or completion matters to the business. They may use one process or several cooperating processes.

Processes may maintain their own process state and may coordinate several participants without making every participant part of one transaction.

A process may be modeled as a special kind of [[Entity|entity]] and [[Observer|observer]] when it has its own identity, durable state or history, and rules for interpreting incoming events, signals, or commands over time.

Process concerns include:

- The subject or correlation identity.
- Participant observers and entities.
- Current process state.
- Steps, decisions, and transitions.
- Compensation or recovery behavior.
- Delivery and retry expectations.

Related concepts: [[Business Transactions]], [[Coordination]], [[Workflow Engines]], [[Observer]], [[Entity]], [[Event]], [[Command]], [[State]], [[Recovery]], [[Policies]], [[Invariants]].
