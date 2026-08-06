---
realm: Principles
kind: discipline
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Theories of Types
---

# Type Theory

Type theory studies terms together with the types that classify them and the [[Judgement|judgements]] that establish when those terms are well formed. It can serve as a foundation for mathematics, a formal system for proofs, and a semantic basis for programming-language type systems. [[Substitution]] transports terms and types across contexts, while typed [[Lambda Calculus|lambda calculi]] provide foundational term languages for abstraction and application.

A typing [[Judgement|judgement]] is commonly written:

$$
\Gamma \vdash t : A
$$

It says that term $t$ has type $A$ under context $\Gamma$. The context records the variables, assumptions, or declarations on which the judgement depends. Formation, introduction, elimination, and computation rules determine how types and their inhabitants are constructed and used.

## Major Forms

- **Simple type theories** classify values and functions without allowing result types to depend on particular input values.
- **Polymorphic type systems** abstract over types so that one term can operate uniformly across many types.
- **Dependent type theories** allow types to depend on terms, making propositions about values expressible in the type of a program or proof.
- **Refinement types** restrict a base type with predicates whose checking may use logical decision procedures or proof obligations.
- **Linear and substructural type systems**, informed by [[Linear Logic|linear logic]], control how resources or capabilities may be used, duplicated, discarded, or ordered.
- **Effect and modal type systems** classify not only returned values but also computational context such as state, failure, I/O, time, locality, or staged execution.

These systems make different tradeoffs among expressiveness, decidable checking, inference, proof effort, runtime representation, and computational behavior. “Well typed” means well typed in one declared system; it is not a universal correctness claim.

## Logic and Propositions as Types

[[Logic]] and type theory are linked by the [[Curry–Howard Correspondence|Curry–Howard correspondence]] and related propositions-as-types interpretations. A proof of a proposition can be represented by a term inhabiting the corresponding type, and proof normalization can correspond to program evaluation.

Common correspondences include function types with implication, product types with conjunction, sum types with disjunction, and dependent function and pair types with quantified propositions. [[Linear Logic|Linear logic]] yields type systems that control weakening, contraction, exchange, and explicit reuse. The correspondence is structural rather than a claim that every logic is identical to one type system. Classical principles, partiality, general recursion, effects, equality, and higher-order quantification each require explicit treatment.

[[Temporal Logic|Temporal logic]] is often complementary to type theory. Types can constrain individual terms, state transitions, protocols, capabilities, or effects, while temporal formulas constrain whole behaviors and their evolution. A type-and-effect system or [[Session Types|session type]] may encode selected temporal structure, but that does not make all liveness, fairness, or distributed-time properties ordinary type judgements.

## Functional Programming

Typed [[Functional Programming|functional programming]] is one major realization of type-theoretic structure. Function types, algebraic data types, pattern matching, parametric polymorphism, higher-kinded abstractions, and typed effects give program composition a statically checked vocabulary. Typed lambda calculi provide calculational cores for many such languages.

The boundary of the guarantee matters. A compiler can establish that checked source terms satisfy its typing rules, subject to the language's metatheory and trusted implementation. It does not automatically establish that external services honor protocols, persisted data matches current types, a distributed process makes progress, or a domain [[Invariant|invariant]] holds unless those obligations are represented and connected to the relevant system boundary.

## Cohesive Use

Type theory can discipline Cohesive language and compiler-like [[Realization|realization]] by making shapes, interfaces, effects, capabilities, and transformation obligations explicit. It is most useful when the conceptual trace remains visible:

- A type should identify which semantic distinction or graph role it classifies.
- A refinement should state the [[Boundaries|boundary]] and assumptions under which its predicate is meaningful.
- An effect type should distinguish a described domain [[Effect|effect]] from a host-language effect or runtime operation.
- A successful type check should state what was proved and what remains an operational or realization obligation.

Related concepts: [[Logic|logic]], [[Judgement|judgement]], [[Law of Excluded Middle|law of excluded middle]], [[Substitution|substitution]], [[Lambda Calculus|lambda calculus]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Linear Logic|linear logic]], [[Session Types|session types]], [[Process Calculi|process calculi]], [[Temporal Logic|temporal logic]], [[Functional Programming|functional programming]], [[Programming Paradigms|programming paradigms]], [[Shape|shape]], [[Invariant|invariants]], [[Interfaces|interfaces]], [[Effect|effect]], [[Effect Models|effect models]], [[Compositionality|compositionality]], [[System Language and Realization|system language and realization]], [[Realization|realization]].
