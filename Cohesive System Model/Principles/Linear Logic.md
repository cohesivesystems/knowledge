---
realm: Principles
kind: discipline
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Linear Logics
  - Resource-Sensitive Logic
  - Resource Logic
---

# Linear Logic

Linear logic is a resource-sensitive [[Logic|logic]] in which assumptions cannot ordinarily be duplicated or discarded implicitly. It makes the use of hypotheses part of proof structure, separating connectives that combine independent resources from connectives that offer alternatives and modalities that explicitly permit reuse.

The word *resource* is proof-theoretic. It may model a capability, obligation, protocol endpoint, reference, token, permission, or other single-use assumption, but it does not automatically denote a physical object, conserved quantity, runtime message, or exactly-once external effect.

## Structural Rules

Ordinary intuitionistic and classical proof systems commonly admit structural rules independently of a proposition's content:

- **Exchange** reorders assumptions.
- **Weakening** permits an assumption to go unused.
- **Contraction** permits repeated use of one assumption as though several copies were available.

Linear logic normally retains exchange but does not grant weakening or contraction for linear assumptions. A derivation must account for each such assumption according to the connective and judgement rules. This gives a family of neighboring substructural disciplines:

| Discipline | Exchange | Weakening | Contraction | Informal use discipline |
| --- | --- | --- | --- | --- |
| Ordinary intuitionistic or classical context | yes | yes | yes | assumptions may be reordered, ignored, or reused |
| Linear logic | usually yes | no | no | each linear assumption is accounted for once |
| Affine logic | usually yes | yes | no | an assumption may be used at most once |
| Relevant logic | usually yes | no | yes | an assumption must be relevant but may be reused |
| Ordered or noncommutative logic | restricted or no | varies | varies | assumption order is semantically significant |

These are proof-rule profiles, not complete definitions of every logic bearing those names. Relevant logics also study implication and relevance conditions; ordered and noncommutative logics vary in which context operations they admit. Substructural logic is the broader family obtained by restricting or controlling structural rules.

**Affine** is especially important in programming. A value may be dropped but cannot be duplicated, giving an at-most-once discipline. **Linear** is stricter at the formal term level: a linear assumption cannot simply be abandoned. Languages described informally as linear may implement affine destruction, implicit cleanup, or explicit disposal; their actual typing rules determine the guarantee.

## Multiplicative and Additive Connectives

Linear logic separates conjunction- and disjunction-like operations according to how they use context.

The **multiplicative** connectives combine independently allocated resources:

- Tensor $A \otimes B$ provides both $A$ and $B$, with proof context divided among their constructions.
- Par $A \mathbin{\bindnasrepma} B$ is tensor's classical linear dual.
- Linear implication $A \multimap B$ consumes an $A$-assumption to produce $B$.
- The units $1$ and $\bot$ are the corresponding multiplicative units.

The **additive** connectives express alternatives under a shared surrounding context:

- With $A \mathbin{\&} B$ supports both alternatives, with the consumer or environment selecting which is used.
- Plus $A \oplus B$ selects and provides one alternative.
- The units $\top$ and $0$ are the corresponding additive units.

Linear negation $A^{\perp}$ reverses polarity and relates the connectives through De Morgan dualities. Classical linear logic treats negation involutively and has multiple conclusions; intuitionistic linear logic typically presents a distinguished conclusion and takes $\multimap$ as central. The two presentations are related but not identical.

## Exponentials and Controlled Reuse

The exponential modalities recover ordinary structural use where it is explicitly allowed:

- $!A$, read “of course $A$,” marks an assumption that may support weakening and contraction under the logic's rules.
- $?A$, read “why not $A$,” is the classical dual modality.

Exponentials create a boundary between linear and unrestricted context. A mixed typing [[Judgement|judgement]] may be written schematically as:

$$
\Gamma;\Delta \vdash t:A
$$

where $\Gamma$ contains unrestricted assumptions and $\Delta$ contains linear ones. Function application, tensor introduction, or parallel composition may split $\Delta$ so that no linear capability is silently given to both branches, while $\Gamma$ can remain available under its structural rules.

The symbol $!$ also appears as the replication operator $!P$ in the π-calculus. Logical exponential, process replication, recursive definition, and runtime scaling are related through particular interpretations, not by typography. A propositions-as-sessions calculus may interpret an exponential as access to a shared service realized through replicated process behavior, but its typing and operational semantics establish that relation.

## Affine, Relevant, Ordered, and Bunched Logics

Affine logic admits weakening but not contraction. It is suited to capabilities that may be consumed or safely abandoned but must not be copied. Affine type systems can prevent aliases or repeated use while allowing scope exit, cancellation, or cleanup to dispose of an unused value.

Relevant logic rejects weakening but admits controlled reuse. Every assumption must contribute to the conclusion, while contraction permits more than one use. This captures relevance rather than scarcity.

Ordered and noncommutative logics restrict exchange. They can represent protocols, words, stacks, memory layouts, or effect sequences in which $A$ followed by $B$ differs from $B$ followed by $A$. Removing exchange is distinct from removing contraction or weakening.

Bunched logics combine more than one context-forming operation. Bunched implications, for example, distinguish an additive context that may share assumptions from a multiplicative context whose resources remain separated. Separation logic applies this distinction to disjoint portions of mutable state. “Separate” here is relative to the model of resources and its separating conjunction; it is not automatically physical isolation or distributed ownership.

Graded, quantitative, and coeffect systems refine the binary linear/unrestricted distinction by tracking how many times, with what sensitivity, or under which usage grade an assumption may be used. Modal and effect systems can similarly track phase, location, time, authority, or computational effects. These are related substructural techniques, not synonyms for linear logic.

## Curry–Howard and Linear Types

Under the [[Curry–Howard Correspondence|Curry–Howard correspondence]], linear propositions correspond to linear types and proofs to terms whose use respects the structural rules. A term of type $A \multimap B$ consumes its linear $A$ input according to the calculus, while tensor packages independently accounted-for components.

This supports static disciplines for unique references, file or device handles, memory ownership, capabilities, effect tokens, and protocol endpoints. The type checker establishes a judgement about program terms and contexts. It does not prove that the external resource exists, that a device operation succeeds, that a message is delivered, or that an irreversible effect happens physically once.

Typed [[Functional Programming|functional programming]] can realize these disciplines through linear or affine function arrows, ownership types, uniqueness types, and APIs that consume a value when advancing its state. The source-level use discipline remains distinct from garbage collection, physical deallocation, transaction commit, and external effect execution.

General recursion, exceptions, cancellation, concurrency, and foreign calls require special care. A linear value captured by a continuation, abandoned through an exception, replayed after recovery, or serialized into durable storage needs typing and operational rules that preserve its intended use discipline across those mechanisms.

## Session Types and Process Calculi

[[Session Types|Session types]] provide a prominent computational interpretation of linear logic. In propositions-as-sessions systems, propositions describe communication protocols, proofs are [[Process Calculi|processes]], cut composes dual endpoints along a private channel, and cut elimination corresponds to communication.

Linearity helps ensure that one endpoint has a coherent owner and advances through one protocol state without uncontrolled aliasing. Additive connectives describe selection and branching; multiplicatives describe communication and composition; exponentials can describe shared services. The exact mapping varies between intuitionistic and classical systems and between provider-oriented and endpoint-oriented conventions.

Session fidelity or deadlock-freedom follows only from the theorems of the selected calculus. Linear use alone does not establish eventual delivery, scheduling fairness, crash recovery, or coherent multiparty projection. A process can use each endpoint once and still wait forever because of a cyclic dependency or failed peer.

## Concurrency and Categorical Structure

Linear logic exposes independence because a multiplicative proof divides resources among subproofs. Proof nets reduce some sequencing artifacts of sequent derivations and can make independent cut-elimination steps visible. This provides an important model of concurrency, but it does not by itself choose between interleaving, partial-order, probabilistic, timed, or physically parallel execution.

Categorically, intuitionistic multiplicative linear logic is modeled by symmetric monoidal closed structure, where tensor is the monoidal product and linear implication is an internal hom. Classical multiplicative linear logic is associated with star-autonomous categories. Additives require suitable products and coproducts, while the exponential is commonly modeled by a comonadic structure whose objects carry copying and discarding maps.

This categorical account clarifies why linearity is not merely a compiler restriction. Cartesian products provide diagonal and terminal maps that support copying and discarding; a general monoidal product does not supply them automatically. The exponential identifies the substructure where such operations are available.

## Cohesive Use

Linear and affine disciplines can make Cohesive realization obligations explicit:

- A unique authority or capability may be transferred without creating another authorized owner.
- A session endpoint may advance through one protocol state without aliases using stale types.
- A transition token or effect obligation may be consumed, discharged, delegated, or explicitly abandoned.
- A continuation, emission identity, or recovery right may have controlled multiplicity.

These types describe formal use of representations. Semantic [[Authority|authority]], domain [[Effect|effects]], message identity, [[Delivery Semantics|delivery semantics]], and [[Commit Boundaries|commit boundaries]] remain separate concepts. A linear message value does not make broker delivery exactly once; an affine command reference does not prevent a remote service from repeating its effect; a unique in-memory handle does not prove exclusive distributed ownership after crash or partition.

A compiler-like [[Realization|realization]] should therefore state which semantic role the linear resource represents, where the type judgement holds, how ownership crosses persistence and interaction boundaries, and which runtime evidence preserves the discipline after serialization, retry, replay, recovery, and deployment.

## Modeling Checks

- Which structural rules are admitted for each context or modality?
- Is the intended discipline exactly once in the formal term, at most once, at least once, ordered, graded, or unrestricted?
- What semantic capability, obligation, endpoint, or resource does the proposition or type represent?
- Which connective expresses composition, choice, sequencing, or reuse?
- How do recursion, exceptions, cancellation, persistence, and concurrency preserve resource accounting?
- Does a session or process interpretation establish fidelity, progress, deadlock-freedom, or only linear ownership?
- What categorical structure supplies tensor, implication, additives, and exponentials?
- Which operational properties remain outside the proof or typing boundary?

## External References

- Jean-Yves Girard, [Linear Logic](https://doi.org/10.1016/0304-3975(87)90045-4), *Theoretical Computer Science* 50(1):1-102, 1987.
- Luís Caires and Frank Pfenning, [Session Types as Intuitionistic Linear Propositions](https://doi.org/10.1007/978-3-642-15375-4_16), CONCUR 2010, LNCS 6269:222-236.
- Philip Wadler, [Propositions as Sessions](https://doi.org/10.1145/2364527.2364568), ICFP 2012:273-286.

Related concepts: [[Logic|logic]], [[Type Theory|type theory]], [[Judgement|judgement]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Functional Programming|functional programming]], [[Session Types|session types]], [[Process Calculi|process calculi]], [[Concurrency|concurrency]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Duality and Symmetry|duality and symmetry]], [[Compositionality|compositionality]], [[Categorical Principles|categorical principles]], [[Monads Monoids and Duals|monads monoids and duals]], [[Recursion|recursion]], [[Fixed Points|fixed points]], [[Authority|authority]], [[Effect|effect]], [[Delivery Semantics|delivery semantics]], [[Commit Boundaries|commit boundaries]], [[Realization|realization]].

## Formal relations

- `refines`: [[Logic]] — Makes assumption use explicit by controlling exchange, weakening, contraction, and the modalities that recover structural reuse.
