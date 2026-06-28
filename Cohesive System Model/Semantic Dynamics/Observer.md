---
realm: Semantic Dynamics
kind: semantic-construct
---

# Observer

An Observer is a locus of interpretation. It is the participant, context, or execution locus relative to which [[Value|values]], [[Observation|observations]], [[Event|events]], [[Command|commands]], [[Query|queries]], [[Boundaries|boundaries]], and [[State|state]] acquire meaning.

Every runtime participant is a potential observer, but an observer is not defined by a particular substrate mechanism. It is realized when some execution context supplies the boundary, state view, authority, and interpretation rules needed to observe and act.

An observer is characterized by:

- Its own [[Identity]], distinct from entity identities.
- Its own [[Boundaries|boundary]].
- A realization context or logical execution context in which interpretation occurs.
- The ability to observe observables, producing [[Observation|Observations]] of [[State]].
- The ability to host, observe, route, or project [[Entity|Entities]] and their [[Event|Events]] within its boundary.
- The ability to receive events from other observers as exogenous events.

An observer may be realized by an OS thread, logical thread, fiber, coroutine, task, actor mailbox turn, workflow activation, request handler, projection run, process step, or entity command handler. In green-thread, fiber, or async runtimes, the observer follows the logical execution context managed by a scheduler, not necessarily the OS thread on which code happens to run.

Addressability of an observer is an operational concern. Some observers have globally addressable identities, such as actors. Others have transient or local identities, such as a request handler or a logical execution context created for a single operation.

Actor systems are important because they make observers addressable: an actor address gives other observers a delivery path to a receiving observer boundary. The address does not necessarily expose state, and it is not automatically the same as an entity identity, though an actor may be used to realize an entity observer.

Entities and [[Process|processes]] can be modeled as observers when they interpret inputs relative to their own state, history, policies, and boundary. A process is often a special kind of entity-observer: it has identity and state, observes events over time, and emits commands or endogenous events as its behavior progresses.

One observer's endogenous event may become another observer's exogenous event.

[[Command|Commands]] and [[Query|queries]] are observer-relative interpretations. The same incoming observation may be interpreted differently or rejected depending on the observer's current view of entity state, projections, invariants, policies, authority, and consistency expectations.

Related concepts: [[Observation]], [[Event]], [[Command]], [[Query]], [[Entity]], [[Process]], [[Boundaries]], [[Realization]], [[Interaction]], [[Delivery Semantics]], [[Concurrency Control]], [[Actor Systems]], [[Runtimes]].
