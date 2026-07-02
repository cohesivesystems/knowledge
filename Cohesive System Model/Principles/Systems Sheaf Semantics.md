---
realm: Principles
kind: principle
status: draft
aliases:
  - Sheaf Semantics
  - Sheaf Semantics for Systems
  - Local-to-Global Consistency
  - Local Views and Global Sections
  - Global Sections
  - Observer-Indexed Sheaves
  - Compatibility and Descent
---

# Systems Sheaf Semantics

Systems Sheaf Semantics uses [[Sheaves and Gluing|sheaf-theoretic local-to-global structure]] to model how [[Observation|observations]], [[State|state]], [[Version|versions]], histories, process state, and knowledge vary over contexts such as observers, boundaries, and causally valid cuts of execution.

The goal is to give precise language for a recurring systems question:

- What can be observed locally?
- How does a richer context restrict to a smaller context?
- When do partial views agree on their overlaps?
- When do compatible views assemble into a coherent larger explanation?
- When is there no global explanation, or more than one possible explanation?

In this sense, sheaf semantics is a modeling discipline for [[Consistency Models|consistency]], [[Projections|projection]], [[Reconstitution|reconstitution]], [[Observer|observer-relative interpretation]], and [[Synchrony and Asynchrony|synchronization under asynchrony]].

## Cuts as Contexts
For a distributed execution, let the event structure be a partially ordered set:

$$
E = (\operatorname{events}, \leq)
$$

where

$$
e_1 \leq e_2
$$

means that event $e_1$ happened before event $e_2$.

A **consistent cut** is a downward-closed subset:

$$
C \subseteq E
$$

such that:

$$
e \in C \wedge e' \leq e \Rightarrow e' \in C
$$

The set of consistent cuts forms a lattice:

$$
\mathcal{C}(E)
$$

ordered by inclusion. Meets are intersections and joins are unions:

$$
C_1 \wedge C_2 = C_1 \cap C_2
$$

$$
C_1 \vee C_2 = C_1 \cup C_2
$$

This lattice can serve as a base of contexts. A cut is thus a causally coherent snapshot of an execution.

## Presheaves over Cuts

A systems presheaf over consistent cuts assigns semantic data to each consistent cut:

$$
\mathcal{F} : \mathcal{C}(E)^{op} \to \mathbf{Set}
$$

For each cut $C\subseteq E$, the set $\mathcal{F}(C)$ contains the sections (observations) applicable at that cut. For a Set-valued sheaf, a section (examples below) over a context is an element of the set assigned to that context:

$$
s \in \mathcal{F}(C)
$$

In bundle or fibration language, a section can be pictured as a compatible choice of data lying over that part of the base. In a systems sheaf, a section is a coherent semantic assignment of data over the chosen cut.

A familiar mathematical example is the sheaf of continuous real-valued functions on a topological space $X$:

$$
\mathcal{C}^0(U) = \{ f : U \to \mathbb{R} \mid f \text{ is continuous} \}
$$

for each open set $U \subseteq X$. A section over $U$ is a continuous function defined on $U$. If $V \subseteq U$, restriction sends the function to its ordinary restriction:

$$
\rho_{U,V}(f) = f|_V
$$

Compatible continuous functions on overlapping open sets glue to a continuous function on their union when they agree on the overlaps.

For systems, a section is not necessarily a numerical function. It is a coherent assignment of state, observation, evidence, knowledge, or control information over a context. Let $U \subseteq E$ be a particular consistent cut, understood as an object of $\mathcal{C}(E)$. Depending on the semantic layer, a section might be:

- An entity state observation. A section $s \in \mathcal{F}_{state}(U)$ assigns to each relevant entity the state reconstructed based on the events in $U$.
- A set of current version identifiers. A section $s \in \mathcal{F}_{version}(U)$ assigns to each relevant subject the version, offset, causal head, or history position visible at $U$.
- A workflow or process state. A section $s \in \mathcal{F}_{process}(U)$ assigns each relevant process instance its phase, pending signals, emitted effects, and completion status at $U$.
- A projection state. A section $s \in \mathcal{F}_{projection}(U)$ gives the derived read model or materialized view obtained by applying the projection rules to the events or observations in $U$.
- A set of observed evidence. A section $s \in \mathcal{F}_{evidence}(U)$ contains the evidence records admitted by the events, observers, or sources present in $U$.
- A logical-clock assignment. A section $s \in \mathcal{F}_{clock}(U)$ assigns clock values to events or observers in $U$ while respecting the happened-before order restricted to $U$.
- The commands or transitions enabled at that cut. A section $s \in \mathcal{F}_{enabled}(U)$ identifies which commands or transitions are enabled by the state and observations determined at $U$.
- The knowledge available to an observer at that cut. A section $s \in \mathcal{F}^{O}_{knowledge}(U)$ records what observer $O$ can know from its projection of $U$.

The opposite category accounts for restriction. If

$$
C_1 \subseteq C_2
$$

then the presheaf supplies a restriction map:

$$
\rho_{C_2,C_1} : \mathcal{F}(C_2) \to \mathcal{F}(C_1)
$$

Restriction forgets, hides, projects, or reconstitutes a larger context as a smaller one. It is a semantic operation, not a physical rollback. It requires enough history, lineage, evidence, or version metadata for the earlier view to be meaningful.

## Compatibility and Descent

A coverage on the cut lattice says that a family of cuts covers $U$ when their join is $U$:

$$
U = \bigcup_i C_i
$$

For two cuts, the base diagram is:

$$
\begin{array}{ccc}
C_1 \cap C_2 & \longrightarrow & C_1 \\
\downarrow & & \downarrow \\
C_2 & \longrightarrow & C_1 \cup C_2
\end{array}
$$

Applying the presheaf reverses the arrows:

$$
\begin{array}{ccc}
\mathcal{F}(C_1 \cup C_2) & \xrightarrow{\rho_{C_1 \cup C_2,C_1}} & \mathcal{F}(C_1) \\
\downarrow & & \downarrow \\
\mathcal{F}(C_2) & \xrightarrow{\rho_{C_2,C_1 \cap C_2}} & \mathcal{F}(C_1 \cap C_2)
\end{array}
$$

The vertical arrows are $\rho_{C_1 \cup C_2,C_2}$ and $\rho_{C_1,C_1 \cap C_2}$.

Sections

$$
s_1 \in \mathcal{F}(C_1)
$$

and

$$
s_2 \in \mathcal{F}(C_2)
$$

are compatible when they agree on the overlap:

$$
\rho_{C_1,C_1 \cap C_2}(s_1)
=
\rho_{C_2,C_1 \cap C_2}(s_2)
$$

A sheaf is a presheaf where compatible local sections glue uniquely. That is, there exists a unique section

$$
s \in \mathcal{F}(C_1 \cup C_2)
$$

such that:

$$
\rho_{C_1 \cup C_2,C_1}(s) = s_1
$$

and

$$
\rho_{C_1 \cup C_2,C_2}(s) = s_2
$$

The compatible local sections together with their agreement data are **descent data**. Descent is the passage from that cover-level data to a section over the covered context. In systems terms: independently evolved local histories can be assembled into a larger coherent history when their overlapping parts agree.

Descent is therefore close to gluing (sheaf condition), but the emphasis is slightly different. Gluing names the assembly of compatible local sections. Descent names the principle that compatible local data over a cover is enough to determine, reconstruct, or recognize the corresponding global section.

## Synchrony as Descent

[[Synchrony and Asynchrony|Asynchrony]] preserves event multiplicity: participants can advance through incomparable cuts. A system therefore accumulates local observations that need not share a total order.

Synchronization can be understood as a descent operation: a boundary, protocol, transaction, barrier, consensus decision, or workflow step requires local observations to become compatible and records or selects the glued observation.

This makes a useful distinction:

- No gluing means the local observations are incompatible.
- More than one gluing means the local observations are ambiguous or indeterminate.
- Unique gluing means the local observations determine one coherent larger observation.

Atomic commits, linearization points, workflow barriers, replicated-object decisions, projection checkpoints, and coordinated state transitions can all be read as different ways of enforcing or recording compatibility across local sections.

## Observer-Indexed Semantics

Consistent cuts alone are not enough for Cohesive, because meaning is [[Observer|observer-relative]]. Each observer has its own semantic context (fiber): events it can observe, commands it can interpret, state it can see, policies it can apply, and versions it can distinguish.

A fibered (contextualized) presentation writes:

$$
\pi : \mathsf{Sem} \to \mathsf{Obs}
$$

where $\mathsf{Obs}$ is a category of observers and $\mathsf{Sem}$ is a total category of observer-relative semantic objects. An object of $\mathsf{Sem}$ has the form:

$$
(O,x)
$$

where $O$ is an observer and $x$ is meaningful for that observer.

A semantic translation between observers has the shape:

$$
\begin{array}{ccc}
(O,x) & \longrightarrow & (O',y) \\
\downarrow & & \downarrow \\
O & \xrightarrow{u} & O'
\end{array}
$$

The vertical arrows are applications of $\pi$. This says that the semantic relation lies over an observer relation. One observer's endogenous event becoming another observer's exogenous event is not equality of event objects. It is a structured translation between fibers.

The base can combine observers and cuts:

$$
\mathsf{Ctx} = \{(O,C) \mid O \in \mathsf{Obs},\ C \in \mathcal{C}_O(E)\}
$$

A systems sheaf can then be modeled as:

$$
\mathcal{F} : \mathsf{Ctx}^{op} \to \mathbf{Set}
$$

where $\mathcal{F}(O,C)$ contains sections describing what observer $O$ can observe, know, command, reconstruct, or distinguish at cut $C$.

## Cohesive Interpretation

Systems Sheaf Semantics gives the Cohesive model a compact way to relate several existing concepts:

| Cohesive concept | Sheaf-theoretic interpretation |
| --- | --- |
| Event partial order | Base execution order |
| Consistent cut | Context in the base |
| Observation, state, or history at a cut | Section |
| Projection to an earlier or smaller context | Restriction |
| Shared causality or common view | Overlap |
| Agreement of observers or projections | Compatibility |
| Snapshot reconstruction | Restriction plus descent |
| Synchronization | Compatibility enforced at a boundary |
| Coordinated state transition | Selected glued section |
| Inconsistency | No compatible global section |
| Ambiguity | More than one compatible global section |

The practical value is diagnostic. When a system claims one coherent state, query result, projection, workflow status, or explanation, the model should ask:

- What base of contexts is being used?
- What is a section over each context?
- What information is preserved by restriction?
- What counts as overlap?
- What compatibility condition is required?
- Does a glued section exist, and is it unique?
- Which observer or boundary is allowed to assert the global section?

Not every useful systems structure is literally a sheaf. Some structures are only presheaves. Some have partial gluing. Some glue only up to equivalence. Some require extra operational mechanisms before compatibility can be checked. The failure to satisfy the sheaf condition is itself meaningful: it identifies where lineage, authority, evidence, ordering, or coordination is missing.

Related concepts: [[Sheaves and Gluing|sheaves and gluing]], [[Categorical Principles|categorical principles]], [[Fibrations and Indexed Structure|fibrations and indexed structure]], [[Universal Constructions|universal constructions]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Consistency Models|consistency models]], [[Version Histories|version histories]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Observer|observer]], [[Observation|observation]], [[State|state]], [[Version|version]], [[Event|event]], [[Command|command]], [[Projections|projections]], [[Reconstitution|reconstitution]], [[Coordination|coordination]], [[Consensus|consensus]], [[Boundaries|boundaries]].
