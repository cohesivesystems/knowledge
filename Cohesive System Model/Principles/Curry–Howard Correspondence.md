---
realm: Principles
kind: principle
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Curry-Howard Correspondence
  - Curry Howard Correspondence
  - Propositions as Types
  - Proofs as Programs
  - Formulae as Types
---

# Curry–Howard Correspondence

The Curry–Howard correspondence relates formal proofs to typed programs: propositions correspond to types, proofs correspond to terms inhabiting those types, and proof normalization corresponds to program evaluation.

It is a family of structural correspondences among particular [[Logic|logics]], proof calculi, and [[Type Theory|type theories]], not one unrestricted identity between every proposition, type, proof, and program. The selected logical rules, type constructors, equality, evaluation discipline, effects, and termination properties determine which correspondence holds.

## Core Correspondence

The logical [[Judgement|judgement]]

$$
\Gamma \vdash A
$$

says that proposition $A$ is derivable from assumptions $\Gamma$. Its proof-relevant type-theoretic form is:

$$
\Gamma \vdash t : A
$$

Here the assumptions become typed variables, proposition $A$ becomes a type, and proof term $t$ records evidence that $A$ is inhabited. Constructing a term constructs a proof; eliminating or applying the term uses that proof according to the corresponding logical rule.

Common constructive correspondences include:

| Logic | Type theory and programming |
| --- | --- |
| Implication $A \Rightarrow B$ | Function type $A \to B$ |
| Conjunction $A \land B$ | Product or pair type $A \times B$ |
| Disjunction $A \lor B$ | Sum or tagged-union type $A + B$ |
| Truth $\top$ | Unit type with a canonical inhabitant |
| Falsehood $\bot$ | Empty or uninhabited type |
| Universal quantification $\forall x:A.\,B(x)$ | Dependent function type $\prod_{x:A} B(x)$ |
| Existential quantification $\exists x:A.\,B(x)$ | Dependent pair type $\sum_{x:A} B(x)$ |

For implication, a proof of $A \Rightarrow B$ is a construction that transforms any proof of $A$ into a proof of $B$. This is represented by a function accepting an inhabitant of $A$ and producing an inhabitant of $B$. Beta reduction corresponds to eliminating a detour in the proof, while eta principles express an appropriate extensional form of proof or program equivalence.

## Correspondence Families

Different systems support different instances of the correspondence:

- Intuitionistic propositional logic corresponds to the simply typed [[Lambda Calculus|lambda calculus]] with suitable product, sum, unit, and empty types.
- Polymorphic calculi such as System F correspond to forms of second-order constructive logic.
- Dependent type theories internalize predicate-level propositions through types that depend on terms.
- [[Linear Logic|Linear logic]] corresponds to linear type systems in which assumptions and resources cannot be duplicated or discarded without explicit permission.
- Classical logic and the [[Law of Excluded Middle|law of excluded middle]] can receive computational interpretations through continuations, control operators, double-negation translations, or related calculi, but they do not share the ordinary direct constructive reading unchanged.

[[Session Types|Session types]] and typed [[Process Calculi|process calculi]] extend the correspondence from propositions-as-types and proofs-as-programs to propositions-as-sessions and proofs-as-processes. [[Linear Logic|Linear propositions]] describe communication protocols, logical duality relates compatible endpoints, cut composes processes along a private channel, and cut elimination corresponds to communication. These results belong to particular logical process calculi rather than to every distributed interaction.

The correspondence can extend categorically. Cartesian closed categories provide semantics for simply typed [[Lambda Calculus|lambda calculus]] and intuitionistic propositional logic: types or propositions appear as objects, programs or proofs as morphisms, and composition represents [[Substitution|substitution]] or cut. This broader view is often called the Curry–Howard–Lambek correspondence and connects the principle to [[Categorical Principles|categorical principles]] and [[Compositionality|compositionality]].

## Normalization, Totality, and Effects

The propositions-as-types reading depends on the computational rules of the type theory. In a normalizing, logically consistent calculus, evaluation transforms proof evidence without manufacturing an inhabitant of falsehood.

Unrestricted general recursion, nontermination, exceptions, unsafe casts, unchecked axioms, foreign code, and other effects require an explicit boundary. If every nonterminating program can be assigned an arbitrary proposition-as-type, program typing no longer supplies constructive evidence that the proposition is true. Systems preserve useful logical readings by separating total from partial computation, tracking effects, restricting recursion, using guarded or coinductive disciplines, or making trusted assumptions explicit.

Proof irrelevance and program extraction introduce another boundary. Two proofs may establish the same proposition while containing different computational content. A proof assistant may erase logically relevant annotations or proof-irrelevant terms when extracting executable code, but the extraction mapping must preserve the theorem and the computational behavior actually claimed.

## Functional Programming

The correspondence explains why typed [[Functional Programming|functional programming]] and constructive proof share so much structure: lambda abstraction, application, algebraic data types, pattern matching, parametric polymorphism, and normalization can each have both computational and logical interpretations.

The slogan “programs are proofs” needs qualification. An ordinary application program is a proof only relative to a proposition represented by its type and a sound typing and evaluation discipline. Most application types express shape, composition, or effect constraints rather than complete domain specifications. A type-safe function may still be partial, perform incorrect external effects, violate a temporal property, or rely on a service that does not honor its assumed interface.

Likewise, higher-order functions do not automatically imply higher-order logic. A language has the logical strength justified by its type formation, quantification, equality, proof, and computation rules—not merely by allowing functions as values.

## Cohesive Use

The Curry–Howard correspondence offers a disciplined path from Cohesive descriptions to proof-carrying or type-checked realizations:

- Semantic and system-graph constraints can generate propositions, types, refinements, or proof obligations.
- A derivation or proof term can provide evidence for a scoped judgement.
- A compiler can preserve typing and proof judgements while lowering definitions into executable representations.
- Proof extraction or certified compilation can carry selected evidence into a realization toolchain.

This does not collapse meaning into types. A domain [[Invariant|invariant]] remains defined at its semantic boundary; its type-theoretic encoding must state which subjects, states, transitions, and assumptions it represents. A successful type or proof judgement establishes only that encoding within its trusted formal boundary. A separate [[Realization|realization]] judgement is still needed to show that generated code, runtimes, storage, networks, external systems, and deployed configuration preserve the claimed meaning and operational properties.

## Modeling Checks

- Which logic and type theory participate in the claimed correspondence?
- Which propositions are represented as types, and which terms count as proof evidence?
- Does the calculus normalize, and how are recursion, partiality, effects, and trusted axioms handled?
- Which equality relates proofs or programs: definitional, propositional, extensional, or observational?
- Is the type merely structural, or does it encode the intended domain proposition?
- Which proof and typing judgements survive compilation, extraction, and execution?
- What realization evidence connects the formal judgement to the deployed system boundary?

## External References

- Philip Wadler, [Propositions as Types](https://doi.org/10.1145/2699407), *Communications of the ACM* 58(12):75–84, 2015.

Related concepts: [[Logic|logic]], [[Type Theory|type theory]], [[Judgement|judgement]], [[Law of Excluded Middle|law of excluded middle]], [[Substitution|substitution]], [[Lambda Calculus|lambda calculus]], [[Functional Programming|functional programming]], [[Linear Logic|linear logic]], [[Session Types|session types]], [[Process Calculi|process calculi]], [[Categorical Principles|categorical principles]], [[Compositionality|compositionality]], [[Invariant|invariants]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[System Language and Realization|system language and realization]], [[Realization|realization]].

## Formal relations

- `refines`: [[Logic]] — Gives constructive propositions and derivations a proof-relevant computational interpretation without claiming that every logical system has the same program correspondence.
- `refines`: [[Type Theory]] — Explains how selected types, inhabitants, and computation rules correspond to propositions, proofs, and proof normalization.
