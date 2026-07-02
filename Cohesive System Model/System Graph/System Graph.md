---
realm: System Graph
kind: reference
---

# System Graph

The system graph is the realm that organizes domain semantics into a semantic graph of a modeled system.

It asks how semantic roles are placed, composed, owned, related, and scoped once they are part of a model of a whole system. It describes graph shape: which [[Entity Models|entity models]] exist, which [[Observers|observers]] interpret which [[Boundaries|boundaries]], how [[Processes|processes]] coordinate work, which [[Projections|projections]] expose state, which [[Policies|policies]] and [[Invariants|invariants]] constrain transitions, and where [[Effects|effects]] leave a boundary.

This realm sits between primitive meaning and concrete implementation:

- Domain semantics defines meaning-bearing primitives such as [[Entity|entities]], [[Observer|observers]], [[Process|processes]], [[State|state]], [[Event|events]], [[Command|commands]], and [[Query|queries]].
- The system graph arranges those primitives into model-specific ownership, dependency, composition, and authority.
- Operational concerns assign guarantees such as [[Persistence|persistence]], [[Coordination|coordination]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Isolation|isolation]], and [[Recovery|recovery]].
- Realization substrate supplies concrete mechanisms such as [[Compute|compute]], [[Runtimes|runtimes]], [[Storage Systems|storage systems]], [[Brokers|brokers]], and [[Workflow Engines|workflow engines]].

Use this realm to answer questions such as:

- What are the system's entity models, observers, processes, projections, and boundaries?
- Which participant owns or interprets a piece of state, a transition, a policy, or an invariant?
- How do observations, commands, events, effects, and artifacts move through flows and business transactions?
- Which relations make the graph navigable, dependent, constrained, derived, or causally connected?
- Where does a semantic role change meaning because it crosses a boundary?
- Which structural choices must later be given operational guarantees and concrete realizations?

The system graph does not by itself choose a database, broker, scheduler, workflow engine, service deployment, or runtime. Those choices belong to realization substrate. It also does not by itself assert durability, ordering, isolation, retries, or recovery. Those belong to operational concerns. Its job is to make the shape of the system explicit enough that those later choices can preserve the intended meaning.

Core system graph notes:

- [[Entity Models|entity models]]
- [[Relations|relations]]
- [[Observers|observers]]
- [[Projections|projections]]
- [[Processes|processes]]
- [[Flows|flows]]
- [[Business Transactions|business transactions]]
- [[Policies|policies]]
- [[Invariants|invariants]]
- [[Boundaries|boundaries]]
- [[Effects|effects]]

Related concepts: [[Compositionality|compositionality]], [[Stuff Structure Property|stuff structure property]], [[Observer|observer]], [[Entity|entity]], [[Process|process]], [[State|state]], [[Event|event]], [[Command|command]], [[Query|query]], [[Transition|transition]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Interaction|interaction]], [[Realization|realization]].
