---
realm: System Graph
kind: reference
created: 2026-07-01
updated: 2026-08-14
---

# System Graph

The system graph is the compositional, boundary-relative graph of a modeled system as a whole, in which semantic subjects and roles become explicit nodes and relations with declared placement, interaction, ownership, scope, and boundaries.

It records how semantic roles compose across boundaries and which operational properties a [[Realization|realization]] must preserve.

This realm sits between primitive meaning and concrete implementation:

- Domain semantics defines meaning-bearing primitives such as [[Entity|entities]], [[Observer|observers]], [[Process|processes]], [[Interaction|interactions]], [[Relation|relations]], [[Invariant|invariants]], [[Policy|policies]], [[State|state]], [[Event|events]], [[Command|commands]], and [[Query|queries]].
- The system graph arranges those primitives into model-specific ownership, dependency, composition, authority, scope, and correspondence.
- Operational concerns state required properties and guarantees such as [[Persistence|persistence]], [[Coordination|coordination]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Isolation|isolation]], and [[Recovery|recovery]].
- Realization substrate supplies concrete mechanisms such as [[Compute|compute]], [[Runtimes|runtimes]], [[Storage Systems|storage systems]], [[Brokers|brokers]], and [[Workflow Engines|workflow engines]].

## Cross-Realm Correspondence

The domain-semantic graph states meaning-bearing subjects, roles, relations, and interactions. The system graph arranges that meaning into model-specific structure, and [[Realization|realization]] mappings relate the structure to substrate mechanisms that can preserve it at declared boundaries. These mappings are typed correspondences rather than identities: one semantic role may participate in several system-graph structures, and one system-graph structure may be distributed across several realization mechanisms.

![Correspondence from domain semantics through the system graph to realization substrate](../../assets/diagrams/cross-realm-projection.svg)
*The system graph makes composition, placement, interaction, ownership, scope, and boundaries explicit between domain meaning and concrete realization. Operational concerns qualify nodes, edges, and mappings.*

See [[System Language and Realization#Cross-Realm Projection|cross-realm projection]] for the fuller realization [[Judgement|judgement]] and its preservation requirements.

Use this realm to answer questions such as:

- What are the system's entity models, transition models, observer models, control models, process graphs, relation models, projection models, replica models, partition models, and boundaries?
- Which participant owns or interprets a piece of state, a transition, a policy, or an invariant?
- How do observations, commands, events, effects, and artifacts move through flow views and business transactions?
- How are interactions among participants arranged through interfaces, protocols, occurrences, flows, messages, channels, routes, multiplexing, and boundaries?
- How are entities, relations, queries, and processes allocated to logical services without identifying those services with their code or deployment realizations?
- Which relation models make the graph navigable, dependent, constrained, derived, or causally connected?
- Where does a semantic role change meaning because it crosses a boundary?
- Which infrastructure graph projection binds modeled structure to public substrate roles?
- Which structural choices must later be given operational guarantees and concrete realizations?

The system graph does not by itself choose a database, broker, scheduler, workflow engine, service deployment, or runtime. Those choices belong to realization substrate. It also does not by itself assert durability, ordering, isolation, retries, or recovery. Those belong to operational concerns. Its job is to make the shape of the system explicit enough that those later choices can preserve the intended meaning.

For an accessible introduction to systems, surfaces, connections, composites, guarantees, and evidence, see [[System Composition Algebra|system composition algebra]].

Core system graph notes:

- [[Entity Models|entity models]]
- [[Transition Models|transition models]]
- [[Observer Models|observer models]]
- [[Control Models|control models]]
- [[Relation Models|relation models]]
- [[Projection Models|projection models]]
- [[Replica Models|replica models]]
- [[Partition Models|partition models]]
- [[Process Graphs|process graphs]]
- [[Business Transactions|business transactions]]
- [[Boundaries|boundaries]]
- [[Surfaces|surfaces]]
- [[Bounded Context|bounded contexts]]
- [[Interfaces|interfaces]]
- [[Interaction Protocols|interaction protocols]]
- [[Service Models|service models]]
- [[Effect Models|effects]]
- [[Messages and Envelopes|messages and envelopes]]
- [[Interaction Channels|interaction channels]]
- [[Routing Models|routing models]]
- [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]]
- [[Flow Operators|flow operators]]
- [[Policy Scopes|policy scopes]]
- [[Invariant Scopes|invariant scopes]]
- [[Infrastructure Graph|infrastructure graph]]

Secondary views and projections:

- [[Flow Views|flow views]]

Related concepts: [[System Language and Realization|system language and realization]], [[Compositionality|compositionality]], [[Stuff Structure Property|stuff structure property]], [[Execution Kernel|execution kernel]], [[Observer|observer]], [[Entity|entity]], [[Process|process]], [[Interaction|interaction]], [[Service|service]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Realization|realization]].
