---
realm: Semantic Dynamics
kind: semantic-construct
tags:
---

# Command

A Command is an observer-relative interpretation of an input event as an attempted [[Transition]].

All inputs to an operation are modeled as input [[Event|events]] subject to interpretation. They become commands only when an [[Observer]] interprets them as attempted transitions for a target subject.

Command interpretation proceeds as follows:

```txt
Exogenous event
  -> input event at an observer boundary
  -> command intent, relative to the observer and target subject
  -> validation against current entity state, required observations, invariants, policies, authority, and expected version
  -> accepted transition | nil | rejection
```

Commands are not mere messages. They are interpretations made relative to:

- The specific [[Observer]], its [[Boundaries|boundary]] and its current view of state.
- Authority, [[Invariants|invariants]], and [[Policies|policies]].
- The intended transition.
- An optional expected [[Version|version]] or etag.

A command's expected version is the version of entity state the observer believed was current when it formulated the command. The transition runtime checks that expectation before accepting the transition and advancing the entity version.

An exogenous event does not become a command by structure alone. It becomes a command only when interpreted as a requested transition for a subject in a specific context.

A [[Query]] is the corresponding observer-relative interpretation of input as a request to observe, compute, or return information without requesting a modeled semantic state transition.

Related concepts: [[Value]], [[Shape]], [[Observation]], [[Query]], [[Observer]], [[Boundaries]], [[Entity]], [[Transition]], [[Version]], [[Concurrency Control]], [[Monads Monoids and Duals]], [[Adjunctions]].
