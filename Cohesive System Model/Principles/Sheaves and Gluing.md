---
realm: Principles
kind: principle
created: 2026-06-29
updated: 2026-07-01
status: draft
aliases:
  - Sheaf
  - Sheaves
  - Presheaf
  - Presheaves
  - Pre-sheaf
  - Pre-sheaves
  - Gluing
  - Local-to-Global Structure
  - Systems of Observations
---

# Sheaves and Gluing

Sheaves and gluing provide a local-to-global principle for systems of observations: many observers, contexts, processors, time intervals, schemas, views, or execution cuts may each see part of a system, and the model needs to say when those partial views agree enough to form a coherent larger view.

As a modeling principle, sheaves and gluing describe how local [[Observation|observations]] must be reconciled into global views before the model can claim a consistent picture of system [[State|state]].

The mathematical term **sheaf** is useful here because it separates several questions that are often collapsed in system design:

- What information is visible in each local context?
- How does a broader view restrict to a narrower view?
- When do different local views agree on their overlap?
- When can compatible local views be glued into a larger view?
- Is the glued view unique, absent, or underdetermined?

In the Cohesive System Model, a sheaf should usually be read as a structured system of observations, not as a claim that the implemented system literally uses sheaf theory.

## Local Definition

A **presheaf** is a structure-preserving assignment from a base category of information contexts to a category of observations. The base category might consist of schemas, consistent cuts, execution contexts, communication neighborhoods, time intervals, processors, observers, or boundaries. Its morphisms represent relationships among those contexts: inclusion, restriction, refinement, projection, causal extension, visibility, or comparison.

Formally, a presheaf has the shape:

$$
\mathcal{F} : \mathsf{Ctx}^{op} \to \mathsf{Obs}
$$

where $\mathsf{Ctx}$ is the base category and $\mathsf{Obs}$ is a category of observation spaces, often $\mathbf{Set}$ but sometimes a category of structured collections such as ordered sets, histories, traces, schemas, or evidence objects.

The opposite category is important (although relative). With the common convention that a morphism

$$
i : V \to U
$$

means that $V$ is a narrower context, view, or part of $U$, the presheaf maps that base relationship to a restriction operation in the opposite direction:

$$
\mathcal{F}(i) : \mathcal{F}(U) \to \mathcal{F}(V)
$$

For example, a relationship between schemas induces restriction from database instances over a larger schema to views over a smaller schema. A relationship between execution cuts induces restriction from observations over the broader cut to observations over the narrower cut.

The functorial aspect is crucial: relationships in the information base are mapped to relationships among observations while preserving identities and composition. Restricting from $U$ to $U$ changes nothing, and restricting from $W$ to $V$ through $U$ agrees with restricting directly when the base relationships compose that way.

A **sheaf** is a presheaf with an additional local-to-global condition for a chosen notion of cover. If local observations over a cover agree on their overlaps, then they can be glued into a unique observation over the covered context. The sheaf condition says that compatible local perspectives determine a coherent larger perspective.

## Base Categories

The base category represents the information structure over which observations vary. Its objects are contexts of observation. Its arrows say when one context can be restricted, projected, included, refined, or compared with another.

Examples of base categories include:

- A database schema, sub-schema lattice, query context, or family of relational views.
- An event structure, causality order, or lattice of consistent cuts.
- Execution contexts such as workflow steps, actor turns, job attempts, transactions, or process phases.
- Communication neighborhoods such as replicas, peers, partitions, shards, subscribers, or service boundaries.
- Intervals of time, clock regions, version ranges, stream offsets, or snapshots.
- Processors, hosts, runtimes, storage nodes, queues, or distributed participants.
- Observer scopes such as users, services, policies, bounded contexts, or read-model consumers.

The base captures an information order. A broader context includes enough structure to restrict to narrower contexts. For consistent cuts, this often appears as a downward-closed condition: if a view includes an event, version, observation, or effect, it should also include the causal prerequisites needed for that view to be coherent.

This downward-closed property makes explicit a fact that is often implicit in systems: broader views carry narrower views inside them, and restriction should reveal those narrower views without inventing new information.

The base is not just indexing machinery. Its category, ordering, and cover structure do much of the modeling work:

- Objects say what counts as a local perspective.
- Arrows say which perspectives can be restricted or compared.
- Overlaps say where independently produced observations must agree.
- Covers say which local perspectives jointly constitute a broader view.
- Downward closure says that coherent views include their prerequisites.
- Incomparability says that concurrent perspectives need not collapse into one total order.

This is the topological aspect of sheaf language in system modeling. The chosen "open sets" may be cuts, neighborhoods, intervals, schemas, participants, or boundaries rather than literal open subsets of a space, but they still encode visibility, causality, locality, and comparison.

## Sections and Restriction

For each context $U$, the collection $\mathcal{F}(U)$ contains the sections (e.g., observations) meaningful over $U$:

$$
s \in \mathcal{F}(U)
$$

A section is a local observation, assignment, state, view, explanation, command set, or evidence set over a context. When $V$ is a narrower context than $U$, the presheaf provides a restriction map:

$$
\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)
$$

Restriction can forget, hide, project, aggregate, reconstitute, redact, or translate information. The important requirement is that restriction is part of the model, not an accidental implementation detail.

## Labeled Transition Systems

A labeled transition system is a familiar software-engineering model: states are connected by labeled transitions, and a run is a path through those transitions. In Cohesive terms, this relates [[State|state]], [[Transition|transition]], [[Event|event]], and [[Behavior|behavior]].

Sheaf language shifts the emphasis. Instead of treating an object primarily as state with methods, it treats a system of objects through observed behavior over contexts. A run of the system corresponds to a compatible family of local observations. Each observer may see only a projection of the execution: a subset of labels, a partial trace, a local state history, a read model, a clock interval, a participant-local view, or a redacted explanation.

The sheaf organizes those partial views into one mathematical object:

- The base category records execution contexts, observers, cuts, participants, or time intervals.
- Sections record the traces, observations, states, commands, or evidence visible in each context.
- Restriction maps implement projection: hiding labels, forgetting participants, selecting a time interval, redacting fields, or coarsening state.
- Compatibility says that two projected views agree where they overlap.
- Gluing says when compatible local views determine a coherent run, snapshot, behavior, or explanation.

This gives sheaves a natural setting for concurrency. Concurrent observers may occupy incomparable contexts. Their observations do not need a single global timestamp to be meaningful. They need enough overlap, causality, lineage, and compatibility information to determine whether a larger execution view exists.

## The Sheaf Condition

The sheaf condition addresses the issue that different observers can have different perspectives on the same system.

Local sections over contexts $U_i$ are compatible when their restrictions agree on overlaps. For two contexts $U$ and $V$, compatibility has the shape:

$$
\rho_{U,U \cap V}(s_U) =
\rho_{V,U \cap V}(s_V)
$$

A sheaf is a presheaf where compatible local sections glue uniquely into a section over the covered context. If $U$ and $V$ cover $W$, then compatible sections

$$
s_U \in \mathcal{F}(U)
$$

and

$$
s_V \in \mathcal{F}(V)
$$

determine a unique section

$$
s_W \in \mathcal{F}(W)
$$

whose restrictions recover $s_U$ and $s_V$.

For systems, the existence and uniqueness clauses diagnose consistency:

- No gluing means the local views are inconsistent, unauthorized, causally invalid, or missing required evidence.
- More than one gluing means the local views are compatible but underdetermined.
- Unique gluing means the local views determine one coherent larger observation, state, explanation, or transition boundary.

The sheaf condition therefore gives precise language for observer-relative disagreement. Different observers may legitimately see different local sections. The model must say what overlap they share, what agreement means there, and who or what is allowed to assert the glued global section.

## Example Sheaves

Several recurring structures in distributed systems can be read as sheaves:

| Sheaf            | Base category                                                                                                                          | Sections                                                                                                                            |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Evidence sheaf   | observers, sources, services, logs, sensors, or trust domains ordered by visibility, authority, or projection.                         | Observations, records, measurements, messages, logs, or attestations attached to each observer or source.                           |
| State sheaf      | Consistent cuts, version intervals, entity scopes, aggregates, snapshots, or event-history prefixes ordered by inclusion or causality. | Reconstructed entity state over compatible evidence, versions, events, or snapshots.                                                |
| Process sheaf    | Workflow steps, saga phases, participant subsets, signal scopes, process cuts, or business-transaction boundaries.                     | Workflow, saga, or business-process progress over subsets of participants, steps, signals, and effects.                             |
| Projection sheaf | query contexts, API shapes, read-model schemas, report scopes, DTO fields, or consumer-visible view boundaries.                        | DTOs, read models, reports, materialized views, and API responses derived from state or evidence.                                   |
| Command sheaf    | transition contexts ordered by available state, authority, policy, version, boundary, and required observations.                       | Admissible transitions enabled by local state, policy, authority, and observed contex no t.                                         |
| Version sheaf    | Stream prefixes, offsets, vector-clock regions, causal heads, replica views, or history positions ordered by causality.                | Visible version identifiers, stream offsets, vector clocks, causal heads, or history positions over observers and cuts.             |
| Identity sheaf   | Bounded contexts, identifier namespaces, entity-resolution scopes, account graphs, or subject-continuity regions.                      | Identifier correspondence, entity resolution, aliases, and subject continuity across observers or bounded contexts.                 |
| Lineage sheaf    | Derivation graphs, source scopes, transformation steps, causal dependency regions, or evidence chains.                                 | Source records, derivation paths, causal dependencies, transformation history, and trust evidence for reconstructed views.          |
| Policy sheaf     | observer roles, tenants, jurisdictions, process phases, data classifications, or authority boundaries.                                 | Local authorization, validation, routing, retention, or admissibility rules scoped by observer, boundary, tenant, or process phase. |
| Invariant sheaf  | entity scopes, aggregate boundaries, relation scopes, process windows, or consistency-checking regions.                                | Constraints that can be checked locally, on overlaps, or only after gluing a larger context.                                        |
| Recovery sheaf   | Failure domains, restart contexts, checkpoint intervals, retry scopes, compensation scopes, or durable log prefixes.                   | Checkpoints, logs, retry state, compensation state, and reconstitution material available over failure and restart contexts.        |
| Knowledge sheaf  | observers, principals, monitors, bounded contexts, evidence scopes, or epistemic accessibility relations.                              | What each observer can know, distinguish, trust, or prove from the evidence visible in its context.                                 |

Not every useful structure satisfies the sheaf condition. Some structures are only presheaves. Some glue only partially, only with coordination, or only up to [[Equivalence vs Equality|equivalence]]. Some require authority, lineage, time, ordering, or consensus before compatibility can be tested. Those failures are part of the model rather than defects in the vocabulary.


## External References

- [Sheaf (mathematics)](https://en.wikipedia.org/wiki/Sheaf_%28mathematics%29), Wikipedia.
- [sheaf](https://ncatlab.org/nlab/show/sheaf), nLab.

Related concepts: [[Systems Sheaf Semantics|systems sheaf semantics]], [[Database Sheaf Semantics|database sheaf semantics]], [[Categorical Principles|categorical principles]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Universal Constructions|universal constructions]], [[Compositionality|compositionality]], [[Equivalence vs Equality|equivalence vs equality]], [[Observer|observer]], [[Observation|observation]], [[State|state]], [[Transition|transition]], [[Event|event]], [[Behavior|behavior]], [[Version|version]], [[Process|process]], [[Command|command]], [[Projections|projections]], [[Consistency Models|consistency models]], [[Coordination|coordination]], [[Consensus|consensus]], [[Boundaries|boundaries]].
