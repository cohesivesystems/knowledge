---
realm: System Graph
kind: structural-construct
created: 2026-11-05
updated: 2026-11-05
---

# Machine Models

A machine model arranges [[Behavior|behavior]] as a system with configurations, typed inputs, admissible actions, and decisions. Its [[Surfaces|surface]] exposes the actions offered in each configuration. A configuration may be a predicate over authoritative entity state; it need not be a separately stored field.

An edge selects a decision from the current configuration, an input, and explicit observations. Evaluation can propose a state change and owed effects. It does not itself commit an entity [[Transition|transition]] or perform an effect. Connecting two machines still requires checking their protocol roles, assumptions, and outstanding obligations.

A lifecycle machine may constrain a single entity. A machine coordinating work over time may participate in a [[Process Graphs|process graph]]. Neither choice implies a process manager, durable execution, or a runtime process. [[State Machines|State machines]] supply the general modeling principle; [[Process Theories|process theories]] explain the different senses of process.

## Formal relations

- `arranges`: [[Behavior]] — Organizes behavior by configuration and the decisions admissible for each input.
- `arranges`: [[Surfaces]] — Exposes the actions and outcomes currently offered to other participants.
