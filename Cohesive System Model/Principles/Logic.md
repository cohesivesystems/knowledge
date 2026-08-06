---
realm: Principles
kind: discipline
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Formal Logic
---

# Logic

Logic studies formal languages, interpretations, and valid inference. It separates the expressions a language permits, the structures in which those expressions have meaning, and the rules by which conclusions follow from assumptions.

For a language $L$, a structure or model $M$, and a formula $\varphi$, the satisfaction [[Judgement|judgement]]

$$
M \models \varphi
$$

says that $\varphi$ is true under the interpretation supplied by $M$. Semantic entailment $\Gamma \models \varphi$ says that every model satisfying the assumptions $\Gamma$ also satisfies $\varphi$. A proof [[Judgement|judgement]] $\Gamma \vdash \varphi$ instead says that $\varphi$ is derivable from $\Gamma$ in a selected proof system. Truth in a model, validity across models, and derivability in a calculus are related but distinct notions.

[[Substitution]] instantiates variables in terms and formulas while preserving binding and well-formedness. A logical system must state which substitutions are admissible and prove a substitution lemma connecting syntax, derivability, and interpretation.

## Propositional, Predicate, and Higher-Order Logic

These names identify different expressive levels:

- **Propositional logic** treats whole propositions as atomic and composes them with connectives such as negation, conjunction, disjunction, and implication. It can express combinations of facts but does not expose the internal subjects or relations within a fact.
- **Predicate logic** adds predicates, terms, variables, and quantifiers so that formulas can describe properties of and relations among objects. The phrase is often used as a synonym for first-order logic, although it can also name the broader family of quantified logics.
- **First-order logic** allows quantification over individuals in the domain of discourse, while predicate and function symbols remain part of the language's interpretation rather than values directly quantified over. For example, $\forall x\, (\mathsf{Order}(x) \Rightarrow \mathsf{HasOwner}(x))$ constrains every modeled order.
- **Higher-order logic** also permits quantification over predicates, relations, functions, or other higher-order objects. Second-order logic is the first such extension; still higher orders continue the hierarchy. This adds expressive power, but its semantics and proof theory differ from first-order logic, and the familiar first-order completeness result does not transfer unchanged under standard higher-order semantics.

The expressive level should be named rather than inferred from notation. A formula containing a predicate is not necessarily higher-order; it becomes higher-order when predicates or functions themselves occupy quantified or value-level positions permitted by the logic.

Propositional, first-order, and higher-order distinguish what formulas can quantify over. [[Linear Logic|Linear logic]] and related substructural logics vary a different axis: whether assumptions may be reordered, discarded, or reused. A logic can therefore be first-order and linear, higher-order and linear, or non-linear at either expressive level.

The [[Law of Excluded Middle|law of excluded middle]] distinguishes classical from constructive proof principles along another axis. Classical logic accepts $P\lor\neg P$ for every proposition; constructive systems require evidence for a selected disjunct and may prove the principle only for decidable propositions.

## Logic in the System Model

Logical formulas can state facts, relations, preconditions, postconditions, refinements, and [[Invariant|invariants]]. A domain invariant has meaning relative to a subject and [[Boundaries|boundary]] before it is encoded as a theorem, validation rule, database constraint, or runtime check. The encoding realizes a logical account of the invariant; it does not replace the domain meaning or widen the guarantee beyond the encoded scope.

[[Temporal Logic|Temporal logic]] extends logical reasoning to [[Behavior|behaviors]], runs, traces, or branching transition structures. It can express claims such as “an invariant always holds” or “a request is eventually answered” while leaving wall-clock bounds, failure assumptions, and runtime enforcement explicit.

[[Relational and Logic Programming|Relational and logic programming]] uses logical or relational descriptions as programs whose answers are found through unification, constraint solving, fixed-point evaluation, or search. The declarative relation remains distinct from the evaluation strategy and its fairness, termination, and cost behavior.

## Functional Programming and Type Theory

[[Functional Programming|Functional programming]] and logic meet through functions, lambda calculi, equational reasoning, and compositional semantics. A functional program may compute logical propositions, proof objects, predicates, relations, or decision procedures, but a function being pure does not by itself prove that it satisfies a specification.

[[Type Theory|Type theory]] connects logic and computation more tightly through the [[Curry–Howard Correspondence|Curry–Howard correspondence]] and related propositions-as-types interpretations. A proposition is represented by a type and a proof by a term inhabiting that type. Function types correspond to implication, product types to conjunction, sum types to alternatives, and dependent types can express quantified propositions. The exact correspondence depends on the selected logic and type theory; classical first-order logic, higher-order logic, and constructive dependent type theories should not be treated as interchangeable.

Typed functional languages commonly realize fragments of type theory through type checking and inference. Their type systems establish only the properties encoded by the available types, effects, refinements, and proof obligations. Domain invariants, temporal progress, distributed failure behavior, and resource bounds remain separate unless the language and verification boundary explicitly represent them.

## Modeling Checks

- What are the formulas, terms, and admissible interpretations?
- Does quantification range over individuals, types, functions, predicates, behaviors, or time positions?
- Is the claim truth in one model, validity across models, or derivability in a proof system?
- Which assumptions and boundaries give the symbols their domain meaning?
- Is a logical statement being used as a specification, a proof obligation, a query, or an executable decision procedure?
- What part of the claim is preserved when it is lowered into types, validation, storage constraints, model checking, or runtime code?

Related concepts: [[Judgement|judgement]], [[Law of Excluded Middle|law of excluded middle]], [[Substitution|substitution]], [[Type Theory|type theory]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Lambda Calculus|lambda calculus]], [[Linear Logic|linear logic]], [[Temporal Logic|temporal logic]], [[Functional Programming|functional programming]], [[Relational and Logic Programming|relational and logic programming]], [[Programming Paradigms|programming paradigms]], [[Invariant|invariants]], [[Relation|relations]], [[Query|queries]], [[Policy|policies]], [[Behavior|behavior]], [[State Machines|state machines]], [[Compositionality|compositionality]], [[System Language and Realization|system language and realization]], [[Realization|realization]].
