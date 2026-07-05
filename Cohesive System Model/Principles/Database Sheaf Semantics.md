---
realm: Principles
kind: principle
created: 2026-06-29
updated: 2026-06-29
status: draft
aliases:
  - Relational Sheaf Semantics
  - Database Instances as Functors
  - Schemas as Categories
  - Local Relational Views
---

# Database Sheaf Semantics

Database Sheaf Semantics views a database schema as a category, a database instance as a structure-preserving functor into sets, and local database views as [[Sheaves and Gluing|sections that can be restricted, compared on overlaps, and sometimes glued]] into a coherent larger instance.

It specializes [[Systems Sheaf Semantics|systems sheaf semantics]] to database structure. Instead of causally valid execution cuts, the base contexts are sub-schemas, views, relation scopes, or query contexts. Instead of distributed state sections, the sections are database instances or local relational observations over those contexts.

## Orientation Glossary

This glossary follows the direction of Spivak's functorial data migration model: schemas are categories, instances are functors, updates are natural transformations, and schema translations induce canonical migration functors.

| Database term                         | Functorial reading                                                                                                                                                                           | Cohesive reading                                                                                               |     |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --- |
| Database schema                       | A category $\mathcal{S}$. Tables, columns, foreign keys, and path equations form the categorical shape of the schema.                                                                        | The declared information shape over which database observations vary.                                          |     |
| Table                                 | An object $T \in \mathcal{S}$.                                                                                                                                                               | A local record type, entity type, relation scope, or typed [[Shape|shape]].                                          |     |
| Column                                | An outgoing morphism from a table object.                                                                                                                                                    | A named attribute projection or navigable observation.                                                         |     |
| Foreign key                           | A morphism $f : T \to U$ between table objects.                                                                                                                                              | A declared dependency or relationship between record scopes.                                                   |     |
| Foreign key path                      | A composite of morphisms.                                                                                                                                                                    | Multi-step navigation whose meaning depends on composition.                                                    |     |
| Primary key                           | The identity arrow $\operatorname{id}_T : T \to T$ in Spivak's categorical normal form.                                                                                                      | The self-identity of a table's row scope.                                                                      |     |
| Path equivalence                      | A commutative diagram in the schema category.                                                                                                                                                | A schema-level [[Invariant|invariants]] saying that two navigations must produce the same observation.                   |     |
| Database instance or database state   | A functor $I : \mathcal{S} \to \mathbf{Set}$, or more generally $I : \mathcal{S} \to \mathcal{V}$ for a value category $\mathcal{V}$.                                                        | The populated database observation over a schema at a point in time.                                           |     |
| Rows of a table                       | The set $I(T)$ assigned to table object $T$.                                                                                                                                                 | Local sections over one schema object.                                                                         |     |
| Column or foreign-key values          | The function $I(f) : I(T) \to I(U)$ assigned to a schema morphism.                                                                                                                           | Record-level navigation induced by the declared schema relation.                                               |     |
| Database update or state transition   | A natural transformation between instances. In Spivak's dictionary, insertion updates are progressive maps $I_0 \to I_1$ and deletion updates are represented regressively as $I_1 \to I_0$. | A structure-preserving [[Transition|transition]] between database states, with direction scoped to the update convention. |     |
| Schema mapping or translation         | A functor between schema categories, respecting path equivalence. Direction matters: a translation $F : \mathcal{C} \to \mathcal{D}$ induces migration functors whose directions differ.     | A structure-preserving relationship between information shapes.                                                |     |
| Pullback migration $\Delta_F$         | Precomposition with a schema functor. For $F : \mathcal{C} \to \mathcal{D}$, $\Delta_F : \mathcal{D}\text{-}\mathsf{Inst} \to \mathcal{C}\text{-}\mathsf{Inst}$.                             | Reindexing, view formation, projection, splitting, or restriction along a schema translation.                  |     |
| Right pushforward migration $\Pi_F$   | Right adjoint to pullback, when the value category has the needed limits. It can express joins.                                                                                              | Assembly by compatibility conditions, often join-like or conjunctive.                                          |     |
| Left pushforward migration $\Sigma_F$ | Left adjoint to pullback, when the value category has the needed colimits. It can express unions and generated unknowns.                                                                     | Assembly by union, quotient, completion, or introduction of witnesses.                                         |     |
| Conjunctive query                     | query behavior expressible through projection and join-like migration, especially pullback and right pushforward patterns.                                                                   | A request for local sections satisfying simultaneous compatibility constraints.                                |     |
| Disjunctive query                     | query behavior expressible through union-like migration, especially left pushforward patterns.                                                                                               | A request that admits alternatives, unions, or generated completions.                                          |     |
| Data migration functor                | One of $\Delta_F$, $\Pi_F$, or $\Sigma_F$, induced by a schema translation.                                                                                                                  | A canonical transformation of database observations that preserves schema and update structure.                |     |
| Basic ETL process                     | In Spivak's dictionary, a pullback functor between instance categories.                                                                                                                      | A structure-preserving view or migration, not merely an imperative row-copying procedure.                      |     |

The important point is structural preservation. Schema relationships become functions between row sets, update relationships become natural transformations, and migration respects the categorical shape of schemas rather than treating tables as unrelated containers.

## Schemas as Categories

A relational schema can be modeled as a category:

$$
\mathcal{S}
$$

Objects represent entity types, relation symbols, attribute domains, or typed [[Shape|record shapes]]. Morphisms represent foreign keys, attribute projections, relationships, inclusion maps, or declared dependencies.

Constraints add equations and admissibility conditions to this structure. Path equalities, keys, cardinality constraints, referential integrity, and domain [[Invariant|invariants]] say which diagrams must commute and which sections count as valid.

This gives [[Relation|relations]] a semantic role beyond storage layout. A relation is a navigable dependency in the schema category, not merely a join condition chosen by a query planner.

## Instances as Functors

The categorical database formulation follows David I. Spivak's functorial data migration model: schemas are categories, instances are set-valued functors, and schema mappings induce canonical data migration functors.

A concrete database is not the schema itself. It is an instance of the schema:

$$
I : \mathcal{S} \to \mathbf{Set}
$$

The functor assigns each schema object a set of rows, values, or identifiers. It assigns each schema morphism a function between those sets. A foreign key from `Order` to `Customer`, for example, becomes a function:

$$
I(\mathsf{orderCustomer}) : I(\mathsf{Order}) \to I(\mathsf{Customer})
$$

[[Functoriality]] requires database navigation to respect identity and composition: staying at a schema object maps to the identity function on its rows, and a declared composite path maps to the same function as the stepwise path it abbreviates. For example, navigating from `Order` to `Customer` and then to `Address` must agree with a declared `Order` to `Address` composite when the schema says those paths are the same.

## Instance Maps and Migrations

For a fixed schema $\mathcal{S}$, a natural transformation between instances

$$
\eta : I \Rightarrow J
$$

assigns each schema object $A$ a function between the corresponding row sets:

$$
\eta_A : I(A) \to J(A)
$$

[[Naturality]] says these functions must commute with the schema relationships. For every schema morphism

$$
f : A \to B
$$

the following equality must hold:

$$
J(f) \circ \eta_A = \eta_B \circ I(f)
$$

In database terms, migrating a row and then following a foreign key must agree with following the old foreign key and then migrating the referenced row. A natural transformation therefore models a structure-preserving map between two instances over the same schema: identifier remapping, row correspondence, normalization, backfill, or representation change that preserves the declared relationships.

Schema migration is a different level of structure. A schema mapping is a functor between schema categories, for example:

$$
F : \mathcal{S} \to \mathcal{T}
$$

In Spivak's formulation, such schema functors induce data migration functors between categories of instances, such as pullback by precomposition and migration by Kan extension. Natural transformations then describe maps between instances, or comparison maps between migration results, with naturality enforcing that the relevant schema structure is preserved.

## Local Views

Applications rarely operate over an entire schema. They usually work over a local context: a subset of tables, attributes, relationships, predicates, or query-visible paths.

If

$$
U \hookrightarrow \mathcal{S}
$$

is a sub-schema or view context, then restricting an instance along that inclusion produces the local view:

$$
I|_U
$$

Restriction forgets tables, attributes, relationships, rows, or predicates outside the chosen context. This is the database analogue of restriction in [[Systems Sheaf Semantics|systems sheaf semantics]], where a richer context is projected down to a smaller one.

Let $\mathsf{Ctx}$ be a category or inclusion-ordered family of local database contexts. A presheaf of database views has the form:

$$
\mathcal{F} : \mathsf{Ctx}^{op} \to \mathbf{Set}
$$

For each context $U$, $\mathcal{F}(U)$ contains the admissible local instances or observations over that context. For each inclusion $V \subseteq U$, the presheaf supplies a restriction map:

$$
\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)
$$

## Compatibility and Gluing

Two local views overlap when they share tables, attributes, identities, keys, or constraints. Local sections

$$
s_U \in \mathcal{F}(U)
$$

and

$$
s_V \in \mathcal{F}(V)
$$

are compatible when they agree on the overlap:

$$
\rho_{U,U \cap V}(s_U) = \rho_{V,U \cap V}(s_V)
$$

A sheaf is a presheaf where compatible local sections glue uniquely. In database terms, if a `Customer`-`Order` view and a `Customer`-`Address` view agree on their shared `Customer` information, then they can be assembled into a coherent `Customer`-`Order`-`Address` view.

The existence and uniqueness clauses matter:

- No gluing means the local database views are inconsistent.
- More than one gluing means the views are underdetermined by their overlap.
- Unique gluing means the local views determine one coherent larger database view.

Uniqueness is always relative to the declared schema, keys, constraints, and notion of equality at the relevant [[Boundaries|boundary]]. A database model may intentionally support partial gluing, gluing up to equivalence, or multiple admissible completions.

## Relational Operations

Familiar relational operations can be read through this local-to-global structure:

- Selection restricts a section to rows satisfying a predicate.
- Projection forgets fields or paths by restricting along a view.
- Joins align sections over shared keys, attributes, or identities.
- Natural joins are gluing operations when overlap agreement is exact.
- Pullbacks model joins that align two views over a shared part.
- Colimits model compatible assembly, union, or quotienting where the schema and constraints permit it.
- Constraints behave like limit or equalizer conditions that select admissible sections.

This interpretation does not replace query planning or storage mechanisms. It explains what a query result means: a [[Query|query]] produces a local section, and integrity constraints determine when local sections can be trusted as parts of a coherent larger instance.

## Cohesive Interpretation

Database Sheaf Semantics connects database structure to several Cohesive concepts:

| Cohesive concept       | Database sheaf interpretation                                                    |                                                   |
| ---------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------- |
| [[Entity Models]]      | Schema objects and typed record shapes                                           |                                                   |
| [[Relation|Relations]]          | Navigable morphisms, foreign keys, dependencies, and overlap structure           |                                                   |
| [[Projection Models]]        | Restrictions or derived local sections                                           |                                                   |
| [[Query]]              | queries                                                                          | Requests for local sections                       |
| [[Persistence]]        | Durable storage of sections, histories, or constraints                           |                                                   |
| [[Reconstitution]]     | Recovering a section from stored rows, events, snapshots, or indexes             |                                                   |
| [[Consistency Models]] | Consistency                                                                      | Conditions under which local views agree and glue |
| [[Boundaries]]         | The scope in which equality, authority, visibility, and admissibility are judged |                                                   |

The main modeling value is diagnostic. When a system maps between relational views, object projections, read models, or API shapes, the model should ask:

- What is the base category of contexts?
- What is a section over each context?
- What does restriction forget or preserve?
- What counts as overlap?
- What compatibility condition is required?
- Does a glued section exist, and is it unique?

This frames mapping as a structure-preserving correspondence between local sections, not merely an imperative transformation between object graphs. It gives a shared language for schema matching, mapping composition, incremental transformation, synchronization, and query generation.

## External References

- David I. Spivak, [Functorial Data Migration](https://arxiv.org/abs/1009.1166), arXiv, 2010; Information and Computation, 217:31-51, 2012. [DOI](https://doi.org/10.1016/j.ic.2012.05.001)

Related concepts: [[Sheaves and Gluing|sheaves and gluing]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Categorical Principles|categorical principles]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Universal Constructions|universal constructions]], [[Fibrations and Indexed Structure|fibrations and indexed structure]], [[Entity Models|entity models]], [[Relation|relations]], [[Projection Models|projection models]], [[Query|query]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Consistency Models|consistency models]], [[Boundaries|boundaries]], [[Storage Systems|storage systems]].
