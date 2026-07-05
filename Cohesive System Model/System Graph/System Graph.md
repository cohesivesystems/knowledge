---
realm: System Graph
kind: reference
created: 2026-07-01
updated: 2026-07-05
---

# System Graph

The system graph is the realm that composes domain semantics into the cohesive system graph of a modeled system.

It asks how semantic roles are placed, composed, owned, related, scoped, and prepared for realization once they are part of a model of a whole system. It describes graph shape: which [[Entity Models|entity models]] exist, which [[Observer Models|observer models]] interpret which [[Boundaries|boundaries]], how [[Process Graphs|process graphs]] coordinate work, which [[Relation Models|relation models]] connect subjects, which [[Projection Models|projection models]] expose derived observations, which [[Policy Scopes|policy scopes]] and [[Invariant Scopes|invariant scopes]] constrain transitions, and where [[Effects|effects]] leave a boundary.

This realm sits between primitive meaning and concrete implementation:

- Domain semantics defines meaning-bearing primitives such as [[Entity|entities]], [[Observer|observers]], [[Process|processes]], [[Relation|relations]], [[Invariant|invariants]], [[Policy|policies]], [[State|state]], [[Event|events]], [[Command|commands]], and [[Query|queries]].
- The system graph arranges those primitives into model-specific ownership, dependency, composition, authority, scope, and correspondence.
- Operational concerns assign guarantees such as [[Persistence|persistence]], [[Coordination|coordination]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Isolation|isolation]], and [[Recovery|recovery]].
- Realization substrate supplies concrete mechanisms such as [[Compute|compute]], [[Runtimes|runtimes]], [[Storage Systems|storage systems]], [[Brokers|brokers]], and [[Workflow Engines|workflow engines]].

Use this realm to answer questions such as:

- What are the system's entity models, observer models, process graphs, relation models, projection models, and boundaries?
- Which participant owns or interprets a piece of state, a transition, a policy, or an invariant?
- How do observations, commands, events, effects, and artifacts move through flow views and business transactions?
- Which relation models make the graph navigable, dependent, constrained, derived, or causally connected?
- Where does a semantic role change meaning because it crosses a boundary?
- Which infrastructure graph projection binds modeled structure to public substrate roles?
- Which structural choices must later be given operational guarantees and concrete realizations?

The system graph does not by itself choose a database, broker, scheduler, workflow engine, service deployment, or runtime. Those choices belong to realization substrate. It also does not by itself assert durability, ordering, isolation, retries, or recovery. Those belong to operational concerns. Its job is to make the shape of the system explicit enough that those later choices can preserve the intended meaning.

Core system graph notes:

- [[Entity Models|entity models]]
- [[Observer Models|observer models]]
- [[Relation Models|relation models]]
- [[Projection Models|projection models]]
- [[Process Graphs|process graphs]]
- [[Business Transactions|business transactions]]
- [[Boundaries|boundaries]]
- [[Effects|effects]]
- [[Policy Scopes|policy scopes]]
- [[Invariant Scopes|invariant scopes]]
- [[Infrastructure Graph|infrastructure graph]]

Secondary views and projections:

- [[Flow Views|flow views]]

Related concepts: [[Compositionality|compositionality]], [[Stuff Structure Property|stuff structure property]], [[Observer|observer]], [[Entity|entity]], [[Process|process]], [[Relation|relation]], [[State|state]], [[Event|event]], [[Command|command]], [[Query|query]], [[Transition|transition]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Interaction|interaction]], [[Realization|realization]].
