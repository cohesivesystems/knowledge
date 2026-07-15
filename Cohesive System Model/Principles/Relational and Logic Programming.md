---
realm: Principles
kind: discipline
created: 2026-07-13
updated: 2026-07-14
status: draft
aliases:
  - Relational Programming
  - Logic Programming
  - Relational Computation
---

# Relational and Logic Programming

Relational and logic programming are approaches in which programs state which combinations of values, facts, or terms hold or are admissible, rather than prescribing only a function from distinguished inputs to distinguished outputs.

This perspective connects several traditions that should be related without being collapsed:

- Mathematical relations and their categorical generalizations.
- Relational algebra, relational calculus, SQL, and language-integrated query.
- Deductive databases and Datalog.
- Graph data, triple stores, ontologies, and knowledge representation.
- Logic and constraint logic programming in languages such as Prolog and miniKanren.

These traditions share declarative and relational structure, but they differ in what counts as a fact, how relations are derived, which variables may be supplied by a query, how absence and negation are interpreted, and which operational procedure searches for answers.

For Cohesive, relational programming exposes common computational structure across several otherwise distinct problems: expressing correspondences between shapes, querying across data sources, deriving views and dependencies, tracing the effects of change, and working with ontology-backed semantics. Formulating these problems in terms of relations, facts, constraints, rules, and queries makes a unified programming model possible, with shared composition and tooling, without erasing the differences among the problems. This also reflects the broader Cohesive practice of giving structure multiple explicit interpretations: the same relational structure may support navigation, query, derivation, validation, or explanation. Compiler-like [[System Language and Realization|realization]] can lower each interpretation to suitable query languages, databases, graph stores, or runtimes while keeping semantic meaning, evidence, evaluation strategy, and guarantee boundaries explicit.

## Relations and Functions

A binary relation from a set $A$ to a set $B$ can be represented as a subset

$$
R \subseteq A \times B.
$$

The expression $R(a,b)$ says that $a$ and $b$ stand in the relation. An $n$-ary relation similarly identifies admissible tuples in a product of $n$ sets.

A function is a special relation. A relation is the graph of a function precisely when it satisfies two conditions:

- **Totality**: every input is related to an output.
- **Single-valuedness**: every input is related to at most one output.

A general relation may be partial, may relate one value to many values, or may relate many values to one another. This greater generality allows the same relation to be queried in different modes, with different arguments supplied, left unknown, or constrained on each invocation. Given $a$, a query may seek all related $b$ values; given $b$, it may seek compatible $a$ values; given neither, it may enumerate pairs; given both, it may test whether the relation holds.

Relations have a converse: if $R(a,b)$ holds, then $R^{\mathsf{op}}(b,a)$ holds. They compose by existentially hiding an intermediate value:

$$
(S \circ R)(a,c)
\quad\text{when there exists } b \text{ such that } R(a,b) \text{ and } S(b,c).
$$

This does not mean that every relation is cheaply computable in every direction. It describes denotational structure: which tuples satisfy the relation. Executing that description introduces a query mode, indexes, an evaluation order, a search strategy, resource bounds, and termination behavior.

## Relations in Category Theory

The category $\mathbf{Rel}$ has sets as objects and relations as morphisms. The identity relation on a set is equality, and morphisms compose by relational composition. Every function $f : A \to B$ determines a relation consisting of exactly the pairs $(a,f(a))$. This representation preserves identities and composition, so functions form a special class of morphisms within $\mathbf{Rel}$. Reversing a relation gives a converse morphism even when the original relation was not invertible as a function.

Profunctors extend this picture from sets to categories. A Set-valued profunctor has the form

$$
P : \mathcal{C}^{\mathsf{op}} \times \mathcal{D} \to \mathbf{Set}.
$$

Instead of merely recording whether $c$ and $d$ are related, $P(c,d)$ can record a set of witnesses, realizations, paths, explanations, or ways in which they are related. Functoriality says that these witnesses can be transported coherently along morphisms in $\mathcal{C}$ and $\mathcal{D}$.

Bool-valued profunctors recover relation-like feasibility structure: a pair is assigned true or false, and composition combines conjunction over a path with existential choice of the intermediate object. Functors embed into profunctorial structure through representable profunctors, commonly organized as companions and conjoints. This categorifies the statement that functions are special relations while retaining the surrounding structure of the source and target categories.

Profunctor optics build on this mixed variance to represent composable bidirectional data accessors. In a common encoding, an optic from a whole pair $(S,T)$ to a focused pair $(A,B)$ transforms a focused operation into a whole-structure operation:

$$
\forall P.\; \mathsf{OpticConstraint}(P) \Rightarrow P(A,B) \to P(S,T).
$$

For a lens, the two directions are represented by a getter $S \to A$, which extracts the focused value from the source, and an updater $S \times B \to T$, which incorporates a replacement focused value into the source to produce the updated whole. The two directions are complementary but asymmetric: update is not the inverse of observation, and a profunctor does not by itself make an arbitrary relation reversible. The optic's structure and laws specify how observation and update remain coherent; the profunctor representation makes such accessors modular and composable. Profunctor optics thus show how profunctorial structure can support a compositional interpretation of observation and update; see [[Optics and Lenses|optics and lenses]].

## A Family of Relational Traditions

| Tradition                        | Primary description                                                                              | Characteristic evaluation                                             | Cohesive relevance                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | ----------------------------------------------------- |
| Set relations and $\mathbf{Rel}$ | Admissible tuples                                                                                | Composition and converse                                              | [[Relation]] semantics                                |
| Profunctors                      | Structured or evidence-bearing correspondences                                                   | Coherent transport and coend-style composition                        | Composable relations between structured contexts      |
| Profunctor optics                | Bidirectional accessors from a whole to a focus                                                  | Lifting focused transformations and composing optics                  | Structured observation and update                     |
| Relational algebra and SQL       | Relations transformed by selection, projection, join, union, aggregation, and related operations | Query planning over finite database instances                         | [[Query]] and [[Projection Models]]                   |
| LINQ                             | Query expressions embedded in a general-purpose language                                         | Local sequence evaluation or provider-specific expression translation | Typed query representation and compiler-like lowering |
| Datalog                          | Extensional facts and intensional rules                                                          | Least-fixed-point evaluation, often using semi-naive iteration        | Recursive derivation, dependency, and impact analysis |
| Graph and triple systems         | Nodes, edges, or subject-predicate-object facts                                                  | Traversal, graph-pattern matching, and indexes                        | [[Relation Models]] realization                       |
| Ontology languages               | Vocabulary, axioms, individuals, properties, and constraints                                     | Entailment under a declared formal semantics                          | Ontology framework in `Cohesive.AI/Semantics`         |
| Prolog and miniKanren            | Predicates or goals over logical terms                                                           | Unification, constraint solving, and search                           | Multi-mode queries, inverse problems, and synthesis   |

The table describes a family resemblance, not an equivalence. A graph database does not become a logic programming system merely because it stores edges. A SQL query is declarative but is not normally a general multi-directional relation solver. An ontology defines terms and admissible interpretations but need not prescribe a query engine. A logic program may denote a relation while its operational behavior remains highly sensitive to goal order and search control.

## Relational Query Programming

The relational database tradition gives developers the most familiar form of relational programming. Codd's relational model represents database information using $n$-ary relations and separates the logical form of data from its physical organization. Relational algebra and relational calculus provide compositional ways to select, project, join, and combine those relations.

SQL is the practical descendant of that tradition, but SQL should not be identified with mathematical relations without qualification. Practical SQL includes duplicate-preserving behavior, nulls, grouping, aggregation, ordering, updates, and implementation-specific types and functions. Although a SQL query leaves evaluation strategy to the database, it still assigns fixed roles to its terms: source relations are read as available inputs, predicates constrain tuples, and the select expression defines the output shape. The optimizer may choose how to compute that input-to-result specification, but it does not reinterpret result values as constraints and solve backward for compatible source rows. Declarative planning is therefore not the same as mode-independent relational execution.

LINQ carries query structure into C# and other .NET languages. Two cases should be distinguished:

- `IEnumerable<T>` operators form a functional pipeline evaluated over local sequences.
- `IQueryable<T>` represents a query as an expression tree associated with a provider, which may translate that tree into SQL or another source-specific language.

The second case is especially relevant to compiler-like realization. A typed host-language expression can preserve a query's compositional structure so that a provider can interpret, normalize, translate, optimize, and execute it against another substrate. Translation remains limited by the provider's supported language and by semantic differences among data sources.

For Cohesive, a relational query is interpreted as a semantic [[Query|query]] relative to an [[Observer|observer]], [[Boundaries|boundary]], authority, requested [[Shape|shape]], and consistency expectation. Relational algebra describes result construction; it does not by itself determine whose facts are authoritative, whether two identifiers denote the same [[Entity|entity]], or what consistency can be promised across independent sources.

## Deductive Databases and Datalog

Datalog connects relational query languages with logic programming. A Datalog program commonly distinguishes:

- **Extensional facts** supplied as base relations.
- **Intensional relations** defined by rules.
- **Queries** asking which substitutions make a goal derivable.

For example, a direct dependency relation can induce a transitive dependency relation:

```prolog
depends_on(X, Y) :- direct_dependency(X, Y).
depends_on(X, Z) :- direct_dependency(X, Y), depends_on(Y, Z).
```

The declarative semantics of a positive Datalog program over an extensional database is its least Herbrand model. Equivalently, that model is the least fixed point of the program's immediate-consequence operator. In the standard finite Datalog setting, it can be computed by iterating the operator from the extensional facts until no new facts are derived. Operational techniques such as semi-naive evaluation avoid repeatedly deriving the same facts while preserving that meaning.

This makes Datalog a natural language for recursive graph reachability, authorization inheritance, classification, dependency closure, program analysis, and the derivation of read models from facts. It connects [[Recursion|recursive]] rules to [[Fixed Points|fixed-point]] semantics.

Negation and absence require additional care. Positive Datalog is monotone: adding facts cannot invalidate a previously derived positive fact. Closed-world negation, aggregates, retractions, priority, and non-monotone rules require a more specific semantics, such as stratification, well-founded semantics, stable-model semantics, or a deliberately scoped completeness boundary. The distinction matters operationally because non-monotone conclusions often require coordination or evidence that a relevant fact set is complete; see the [[CALM Theorem|CALM theorem]].

## Graphs, Triples, and Ontologies

Graph databases and triple stores represent relationships directly as stored data, making them available for traversal and pattern matching. That representation does not by itself determine the semantic or logical meaning of a relationship.

An RDF graph is a set of subject-predicate-object triples. RDF supplies an abstract graph data model and formal entailment regimes can assign logical consequences to graphs. A property graph or graph database may instead attach properties to nodes and edges and optimize traversal or graph-pattern queries. Either family can realize a [[Relation Models|relation model]], but neither automatically defines the domain meaning of an edge, the authority of a fact, or the rules by which new facts follow.

An ontology adds a formalized vocabulary and axioms describing classes, properties, individuals, and relationships among terms. OWL, for example, separates ontology structure and exchange syntax from formally defined direct and RDF-based semantics. A triple serialization of an ontology is therefore not identical to the ontology's semantics or to the inferences licensed by those semantics.

CycL is another knowledge-representation example. It is the formal representation language used for facts and rules in the Cyc knowledge base, including contextual organization through microtheories. Its role illustrates why ontology modeling, assertion storage, rule expression, context, and inference control should be documented separately even when one system integrates them.

In Cohesive terms:

- A semantic [[Relation|relation]] states what a connection means.
- A [[Relation Models|relation model]] arranges such connections in the system graph.
- An ontology defines vocabulary, constraints, and possible entailments.
- A graph or triple representation is one possible realization of facts and relation instances.
- A query or inference engine is a realization of navigation, matching, derivation, or proof search.

## Logic and Relational Programming

Logic programming expresses a program as logical clauses. Facts assert that particular relations hold, rules describe how further relations follow, and queries ask which values make a goal derivable. A proof procedure and control strategy determine how the system searches for those answers. Kowalski summarized this separation as algorithm = logic + control.

Prolog operationalizes Horn-clause logic through unification and a particular search procedure. Its predicates often support several query modes, but search order and extra-logical features such as cut, instantiation tests, arithmetic evaluation, and stateful effects can make some modes practical and others divergent or semantically different.

miniKanren emphasizes relational programming with a small logical core, unification, fresh variables, constraints, and interleaved search. For example, a relational evaluator can relate expressions to their results. Supplying an expression computes possible results; supplying a desired result can synthesize expressions that produce it; constraining both narrows the possible expression-result pairs. This illustrates the expressive gain from not assigning permanent input and output roles.

Direction-neutral meaning does not imply direction-neutral execution. Every invocation supplies a mode: some terms are known, some are unknown, and some are partially constrained. A useful relational system should therefore distinguish at least:

- Soundness: returned answers satisfy the relation.
- Completeness: all answers in the intended domain can eventually be found.
- Termination: a particular query mode finishes.
- Fairness: one infinite search branch does not permanently hide answers elsewhere.
- Multiplicity: repeated proofs may or may not produce repeated answers.
- Evidence: an answer may carry a proof, derivation, lineage, or merely a truth value.

These guarantees are boundary and language-relative. They must not be inferred merely from the word relational.

## Cohesive Interpretations

### DTO and Shape Mappings

A conventional DTO mapping is usually a function or partial function from one [[Shape|shape]] to another. It becomes usefully relational when the system needs to ask which source values are compatible with a target, retain several possible correspondences, validate a pair without constructing either side, or derive one side from partial constraints on both.

Facts and rules can describe field correspondences, defaults, admissibility conditions, conversions, and derivations. This does not automatically make the mapping invertible. Projection may forget information, several sources may produce the same DTO, and a target update may admit several source updates or none.

[[Optics and Lenses|Lenses]] and relational lenses supply a complementary discipline: they state how a view is read and how permitted view updates are reflected into a source while enforcing round-trip laws or an explicit update policy. Profunctor optics provide a compositional representation of these bidirectional accessors and allow different optic families to compose through ordinary function composition. This is often more precise than saying that a DTO mapper simply runs backward.

### Cross-Source Queries

A generalized cross-source query system can expose one typed relational language while lowering subqueries into SQL, graph queries, APIs, indexes, in-memory collections, or other providers. The LINQ provider model is a useful realization precedent, but cross-source semantics require more than translation.

The model must identify:

- Which source is authoritative for each fact.
- How identities and relation meanings correspond across boundaries.
- Which predicates can be pushed to each provider without changing meaning.
- What information must be joined or filtered locally.
- Which policies constrain visibility and combination.
- Whether the result is snapshot-consistent, stale, monotone, partial, or best-effort.
- How failures, timeouts, duplicates, missing values, and contradictory observations appear.

The semantic request is a [[Query|query]]. Its cross-source dependencies and correspondences belong to [[Relation Models|relation models]]. Result shaping and derivation belong to [[Projection Models|projection models]]. Providers, planners, storage engines, and network calls are realization choices.

### Change Impact, Lineage, and Derivation

Understanding which records are affected by a change is a relational and logical problem, but several questions must be separated:

1. Which records or projections may depend on the changed entity?
2. Which derived facts actually change for this particular transition?
3. Which operational work should be scheduled because of that change?

The first is reachability over a dependency or derivation relation. The second is incremental query evaluation, change propagation, or truth maintenance. The third introduces [[Policy|policy]], [[Process|processes]], [[Effects|effects]], delivery, retry, and recovery; it is not determined by logical consequence alone.

Provenance strengthens this model by recording why a result exists and which facts or derivation paths contributed to it. Provenance can support explanation, invalidation, selective recomputation, trust, and access control. A Boolean relation answers whether a dependency exists; an evidence-bearing or annotated relation can explain how and why it exists.

### Ontology and Semantic Relations

An ontology names relation types and constrains their interpretation. Facts instantiate those relations; rules or axioms may derive more facts; queries select what follows for an observer and purpose. These are distinct responsibilities even when one language or runtime supports all of them.

For Cohesive semantics, ontology integration states:

- Which semantic subjects and relation types are in scope.
- Whether assertions are definitions, facts, defaults, hypotheses, or observations.
- Which observer, authority, source, or context endorses an assertion.
- Which inference regime licenses derived statements.
- Whether reasoning is open-world or closed-world at the relevant boundary.
- Whether contradictions are rejected, isolated by context, tolerated, or surfaced as competing explanations.

This keeps an ontology from being reduced to a graph schema and keeps a stored edge from being mistaken for a universally valid semantic fact.

## Modeling Checks

- Do not equate a semantic relation with a foreign key, join, graph edge, pointer, or network call.
- Do not infer bidirectional execution merely because a definition is relational.
- Do not treat SQL, Datalog, RDF, OWL, CycL, Prolog, and miniKanren as interchangeable languages.
- Distinguish base facts, derived facts, hypotheses, defaults, and observations.
- State the completeness boundary before using absence or negation.
- Separate logical consequence from operational work triggered by a consequence.
- Make query modes, search control, termination limits, and provider translation boundaries explicit.
- Preserve provenance when correctness depends on why, where, or under whose authority a relation holds.

## External References

- Brendan Fong and David I. Spivak, [*An Invitation to Applied Category Theory: Seven Sketches in Compositionality*](https://arxiv.org/abs/1803.05316), Cambridge University Press, 2019, especially Chapter 4 on Bool-valued profunctors and feasibility relations. [DOI](https://doi.org/10.1017/9781108668804)
- Edgar F. Codd, [A Relational Model of Data for Large Shared Data Banks](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks), *Communications of the ACM* 13(6):377-387, 1970. [DOI](https://doi.org/10.1145/362384.362685)
- Serge Abiteboul, Richard Hull, and Victor Vianu, *Foundations of Databases: The Logical Level*, Addison-Wesley, 1995. [Author-hosted edition](https://webdam.di.ens.fr/Alice/)
- James Cheney, Sam Lindley, and Philip Wadler, [A Practical Theory of Language-Integrated Query](https://doi.org/10.1145/2535838.2535843), *ICFP 2013*, pp. 403-416.
- Microsoft, [`IQueryable<T>` Interface](https://learn.microsoft.com/en-us/dotnet/api/system.linq.iqueryable-1), .NET API documentation.
- Todd J. Green, Grigoris Karvounarakis, and Val Tannen, [Provenance Semirings](https://repository.upenn.edu/bitstreams/b598c0a7-0d24-4162-8279-5f51a17d29c2/download), *PODS 2007*, pp. 31-40. [DOI](https://doi.org/10.1145/1265530.1265535)
- Mahmoud Abo Khamis, Hung Q. Ngo, Reinhard Pichler, Dan Suciu, and Yisu Remy Wang, [Convergence of Datalog over (Pre-) Semirings](https://arxiv.org/abs/2105.14435), *PODS 2022*, pp. 105-117. [DOI](https://doi.org/10.1145/3517804.3524150)
- Robert A. Kowalski, [Algorithm = Logic + Control](https://www.doc.ic.ac.uk/~rak/papers/algorithm%20=%20logic%20+%20control.pdf), *Communications of the ACM* 22(7):424-436, 1979. [DOI](https://doi.org/10.1145/359131.359136)
- William E. Byrd, [*Relational Programming in miniKanren: Techniques, Applications, and Implementations*](https://scholarworks.iu.edu/dspace/items/450e1b65-70da-4a38-8e73-c182818de110), PhD dissertation, Indiana University, 2009.
- Dmitry Rozplokhas, Andrey Vyatkin, and Dmitry Boulytchev, [Certified Semantics for Relational Programming](https://arxiv.org/abs/2005.01018), *miniKanren 2020*.
- Matthew Pickering, Jeremy Gibbons, and Nicolas Wu, [Profunctor Optics: Modular Data Accessors](https://ora.ox.ac.uk/objects/uuid%3A9989be57-a045-4504-b9d7-dc93fd508365), *The Art, Science, and Engineering of Programming* 1(2), article 7, 2017. [DOI](https://doi.org/10.22152/programming-journal.org/2017/1/7)
- Bryce Clarke, Derek Elkins, Jeremy Gibbons, Fosco Loregian, Bartosz Milewski, Emily Pillmore, and Mario Román, [Profunctor Optics, a Categorical Update](https://arxiv.org/abs/2001.07488), 2020.
- Aaron Bohannon, Benjamin C. Pierce, and Jeffrey A. Vaughan, [Relational Lenses: A Language for Updatable Views](https://doi.org/10.1145/1142351.1142399), *PODS 2006*, pp. 338-347.
- W3C RDF Working Group, [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/), W3C Recommendation, 2014.
- W3C OWL Working Group, [OWL 2 Web Ontology Language Document Overview, Second Edition](https://www.w3.org/TR/owl2-overview/), W3C Recommendation, 2012.
- R. V. Guha and Douglas B. Lenat, [CYC: A Midterm Report](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/842), *AI Magazine* 11(3):32-59, 1990. [DOI](https://doi.org/10.1609/aimag.v11i3.842)

Related concepts: [[Relation|relation]], [[Relation Models|relation models]], [[Query|query]], [[Projection Models|projection models]], [[Shape|shape]], [[Observer|observer]], [[Boundaries|boundaries]], [[System Language and Realization|system language and realization]], [[Categorical Principles|categorical principles]], [[Functoriality|functoriality]], [[Recursion|recursion]], [[Fixed Points|fixed points]], [[CALM Theorem|CALM theorem]], [[Optics and Lenses|optics and lenses]], [[Database Sheaf Semantics|database sheaf semantics]], [[Policy|policy]], [[Process|process]], [[Effects|effects]], [[Realization|realization]].
