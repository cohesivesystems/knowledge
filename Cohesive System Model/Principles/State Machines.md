---
realm: Principles
kind: principle
created: 2026-06-30
updated: 2026-06-30
aliases:
  - State Machine
  - Transition System
  - Labelled Transition System
  - Labeled Transition System
  - Moore Machine
  - Mealy Machine
  - Finite State Transducer
---

# State Machines

State machines are a modeling principle for [[Behavior|behavior]] described by current [[State|state]], admissible [[Transition|transitions]], inputs, and outputs.

A common input-output step form is:

```txt
(Input, State) -> (Output, State)
```

This form makes explicit that an input is interpreted relative to current state, producing both an output and a next state. The output may be empty, observational, or effectful depending on the model boundary.

State-machine thinking is not tied to functional programming, imperative programming, object orientation, actors, workflows, databases, or distributed protocols. The same transition structure may be expressed as a pure reducer, a method on a mutable object, an actor turn, a database transaction, a workflow step, an event-sourced aggregate, or a replicated log application. Those are realization choices over the same underlying behavioral shape.

## Common Forms

Labelled transition systems describe states connected by labelled transitions:

```txt
s --label--> s'
```

The labels may represent inputs, events, actions, commands, observations, or protocol messages. A labelled transition system may be nondeterministic: a state and label can admit multiple possible successor states.

Moore machines separate transition from output:

```txt
transition: (Input, State) -> State
output: State -> Output
```

The observable output depends on the resulting state, not directly on the input that produced it.

Mealy machines make output part of the transition step:

```txt
step: (Input, State) -> (Output, State)
```

The output depends on both the input and the current state.

Finite state transducers are state machines with finite state sets and input/output alphabets. They translate input strings, traces, or event sequences into output strings, traces, or event sequences while moving through finite control states.

These forms are useful reference points, but Cohesive does not require every state machine to be finite, deterministic, total, or sequential. Version histories, distributed executions, workflows, CRDT replicas, and processes may need partial orders, branching histories, merge transitions, unavailable transitions, or observer-relative projections.

## Cohesive Interpretation

In Cohesive terms, state machines relate:

- [[State|state]] as the condition being advanced.
- [[Transition|transitions]] as admissible movement between states.
- [[Command|commands]], [[Event|events]], observations, signals, or messages as inputs.
- Endogenous events, observations, acknowledgments, emitted [[Effects|effects]], or nil as outputs.
- [[Behavior|behavior]] as the resulting run, trace, or state history.

An [[Entity|entity]] can be modeled as a state machine when commands are interpreted against current entity state and committed as controlled transitions. A [[Process|process]] can be modeled as a state machine when its state records phase, pending work, timeouts, decisions, and emitted effects. A projection can be modeled as a state machine when source events are folded into derived observation state.

Cohesive provides multiple implementation paths by composing operational concerns:

- [[Reconstitution|Reconstitution]] recovers the state or observation needed to interpret the next input.
- [[Persistence|Persistence]] chooses which state, history, checkpoints, events, or effect records become durable truth.
- Execution serialization, [[Ordering|ordering]], and [[Concurrency Control|concurrency control]] determine which attempted transitions may be interpreted and committed together or one at a time.
- [[Effects|Effects]] and [[Commit Boundaries|commit boundaries]] define which outputs are accepted, persisted, published, retried, acknowledged, or compensated.

This composition keeps the state-machine model separate from the mechanism that realizes it. A single behavioral model can be realized through current-state storage, event sourcing, actor identity serialization, workflow histories, replicated logs, CRDT merge rules, or database transactions when the chosen mechanisms preserve the required transition semantics.

## Sheaf View

[[Systems Sheaf Semantics|Systems sheaf semantics]] provides a way to examine state-machine behavior across observers, boundaries, cuts, and projections. A run, trace, state history, enabled-transition set, or output history can be treated as a section over a context.

Restriction maps can hide labels, select a time interval, project to one [[Observer|observer]], reduce state shape, or expose only a read model. Compatibility asks whether partial views of the machine agree where they overlap. Gluing and descent ask whether compatible local runs determine a coherent larger behavior.

This is especially useful when the state machine is distributed, observer-relative, partially observed, or non-sequential. The question is not only "what is the next state?" but also "which local state-machine views are compatible, and what global behavior do they determine, if any?"

Related concepts: [[State|state]], [[Transition|transition]], [[Behavior|behavior]], [[Event|event]], [[Command|command]], [[Observation|observation]], [[Observer|observer]], [[Entity|entity]], [[Process|process]], [[Reconstitution|reconstitution]], [[Persistence|persistence]], [[Effects|effects]], [[Ordering|ordering]], [[Concurrency Control|concurrency control]], [[Event-State Duality|event-state duality]], [[Algebras and Coalgebras|algebras and coalgebras]], [[Trace and Feedback|trace and feedback]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Sheaves and Gluing|sheaves and gluing]].
