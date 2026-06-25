---
realm: Semantic Dynamics
---

# Event

Realm: Semantic Dynamics

An Event is a time-bearing occurrence with a [[Value|value]]. It marks, reports, or induces change depending on how it is interpreted by an [[Observer]] relative to a [[Boundaries|boundary]].

Structurally, an event is a [[Value|value]] with a notion of occurrence. Semantically, an event's role is observer- and boundary-relative.

Relative to an [[Observer]]'s [[Boundaries|boundary]]:

- An **exogenous** event arrives from outside the observer [[Boundaries|boundary]].
- An **input event** is an exogenous event in the role of entering a system or observer.
- A [[Command]] is an input event interpreted as an attempted [[Transition]] for a target subject.
- A [[Query]] is an input event or incoming value interpreted as a request to observe, compute, or return information.
- An **endogenous** event is committed within the observer's own semantic history.
- An **output event** is an endogenous event emitted across a [[Boundaries|boundary]].
- A **nil** endogenous event means the observer interpreted the input but no domain transition was committed for the target entity.

The same occurrence may therefore be an output event for one system, an exogenous input event for another, and a command or query only after interpretation by an observer relative to that system's boundary, current state, policies, authority, and target subject.

In [[Event Sourcing|event-sourced]] semantics, the relevant events are committed endogenous events:

```txt
decide: current state + command/input + observations + policies -> endogenous event | nil | rejection
apply: current state + endogenous event -> next state
```

Only committed endogenous events advance entity version and become part of the event-sourced state history. Attempted inputs, rejected commands, retries, telemetry, and nil outcomes may be recorded elsewhere, but they are not state actions for the target entity unless committed inside that entity boundary.

Events participate in [[Event-State Duality]]:

- Events can be folded or integrated into current [[State]].
- State can be observed for differences, transitions, or threshold crossings that emit new events.
- Event streams can form [[Behavior]].
- Behavior can be sampled or detected as events.
- Event-state duality is not an isomorphism: event histories and state histories are mutually informative but not mutually substitutable.

Related concepts: [[Value]], [[Shape]], [[Observation]], [[State]], [[Event-State Duality]], [[Behavior]], [[Observer]], [[Boundaries]], [[Command]], [[Query]], [[Transition]], [[Version]], [[Event Sourcing]].
