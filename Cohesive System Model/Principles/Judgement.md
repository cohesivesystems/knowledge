---
realm: Principles
kind: principle
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Judgment
  - Formal Judgement
  - Formal Judgment
  - Typing Judgement
  - Typing Judgment
  - Realization Judgement
  - Realization Judgment
---

# Judgement

A judgement is a context-indexed assertion that a specified relation holds. It makes explicit what is being claimed, under which assumptions and rules, at which [[Boundaries|boundary]], and with what evidence or authority the claim is accepted.

Judgements belong to the metalanguage used to reason about expressions, models, proofs, programs, and realizations. A proposition or type may be an object inside a formal language; a judgement asserts something about that object. For example, $\varphi$ is a formula, while $\Gamma \vdash \varphi$ asserts that the formula is derivable under assumptions $\Gamma$.

## Anatomy of a Judgement

A well-scoped judgement identifies:

| Part | Role |
| --- | --- |
| **Subject** | The formula, term, type, model, mapping, mechanism, or other object being judged. |
| **Judgement form** | The relation being asserted, such as satisfaction, derivability, typing, equality, refinement, conformance, or acceptable realization. |
| **Context** | Declarations, assumptions, definitions, requirements, environmental conditions, and prior judgements on which the claim depends. |
| **Boundary** | The semantic, system, operational, substrate, observational, or organizational scope at which the claim is intended to hold. |
| **Rules and evidence** | The derivation, interpretation, capability evidence, validation result, proof, model exploration, test evidence, or review that warrants the claim. |
| **Authority** | The formal calculus, checker, interpreter, compiler, tool, policy owner, or review process authorized to accept the result. |

Leaving one of these implicit can make a correct local judgement look like a stronger global claim. A type check over source code does not judge the state of an external service. A model-checking result over a finite configuration does not judge every parameter size. A substrate capability report does not judge an end-to-end realization unless the mappings and composed boundaries are also covered.

## Judgement in Logic and Type Theory

[[Logic]] uses several related judgement forms:

- A **satisfaction judgement** $M \models \varphi$ says that formula $\varphi$ is true in model $M$ under the selected interpretation.
- An **entailment judgement** $\Gamma \models \varphi$ says that every model satisfying assumptions $\Gamma$ also satisfies $\varphi$.
- A **proof or derivability judgement** $\Gamma \vdash \varphi$ says that $\varphi$ can be derived from $\Gamma$ using a selected proof system.

These are not interchangeable. Soundness relates derivability to semantic consequence; completeness, where it holds, relates semantic consequence back to derivability. Failure to derive a formula is not automatically a derivation of its negation, and missing evidence is not automatically evidence that the claim is false.

[[Type Theory|Type theory]] commonly uses a typing judgement:

$$
\Gamma \vdash t : A
$$

This asserts that term $t$ has type $A$ in context $\Gamma$. Other forms may assert that a type is well formed, that two terms or types are definitionally equal, or that a term computes to another term. A [[Linear Logic|linear or substructural]] judgement can further distinguish unrestricted assumptions from assumptions that may not be duplicated, discarded, or reordered. Under the [[Curry–Howard Correspondence|Curry–Howard correspondence]] and related propositions-as-types interpretations, a type can represent a proposition and an inhabiting term can provide proof evidence, while the typing judgement records that the evidence has the required type.

## Evidence, Checking, and Status

A judgement form defines what would count as a valid assertion. A checking or inference procedure attempts to establish an instance of that form. The checker, proof assistant, model checker, compiler, validator, or human reviewer is a realization of that assessment process, not the meaning of the judgement itself.

Formal systems often treat a judgement as derivable or not derivable. Engineering assessments need a more explicit evidence status because incomplete information is normal. A Cohesive assessment may report that a claim is:

- Established natively by one mechanism.
- Established by a documented composition of mechanisms.
- Conditional on named assumptions, configuration, or boundary restrictions.
- Accepted by an authorized override despite an unmet requirement.
- Rejected or unavailable under the candidate realization.
- Unknown because sufficient evidence is absent.

An override records an authorized [[Policy|policy]] decision; it does not prove that the original requirement holds. Likewise, an unknown result must not be silently converted into success or failure.

## Realization Judgements

In Cohesive, [[Realization|realization]] depends on judgements that a candidate substrate mapping preserves required meaning and properties. For semantic and system graph $G$, requirements $P$, boundary $B$, candidate substrate graph $R$, and realization mapping $\rho$, the compact form

```text
G; P @ B ⊢ ρ : G -> R
```

asserts that $\rho$ is an acceptable mapping from $G$ into $R$ under requirements $P$ at boundary $B$. The judgement is warranted only when capability evidence covers the relevant substrate mechanisms and the composed mapping preserves the identities, relations, authorities, interfaces, behavior, and operational properties required by the source model.

Acceptance of the judgement is distinct from selection and deployment. A candidate may be acceptable but not selected; a selected realization may not yet be deployed; a deployed mechanism may drift from the configuration and assumptions under which it was judged. Conformance and operational evidence are needed to maintain the claim over time.

Realization judgements compose only when their contexts, boundaries, assumptions, and preserved structures align. Independently valid local mappings do not automatically establish a valid end-to-end realization. The composition itself creates obligations for routing, identity, ordering, authority, consistency, recovery, and other cross-boundary properties.

## Judgements, Decisions, and Observations

A judgement is not identical to a domain decision or an [[Observation|observation]]. An observation supplies contextualized evidence about state. A judgement interprets expressions or evidence under declared rules. A decision selects or authorizes an outcome. One activity may involve all three—for example, observing substrate capabilities, judging a realization acceptable, and deciding to deploy it—but their meanings and authorities remain distinct.

## Modeling Checks

- What exactly is the judgement form, and what subject occupies it?
- Which context, assumptions, definitions, and previous judgements are in scope?
- At which boundary does the claim hold, and which boundaries remain outside it?
- What evidence or derivation warrants the judgement, and who or what may accept it?
- Does failure mean false, rejected, not derivable, unsupported, unavailable, or unknown?
- Is the judgement about a candidate, a selected realization, a deployed configuration, or observed runtime behavior?
- Can local judgements compose, and what new obligations arise at their interfaces?

Related concepts: [[Logic|logic]], [[Type Theory|type theory]], [[Linear Logic|linear logic]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Temporal Logic|temporal logic]], [[Functional Programming|functional programming]], [[System Language and Realization|system language and realization]], [[Realization|realization]], [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Boundaries|boundaries]], [[Invariant|invariants]], [[Policy|policy]], [[Observation|observation]], [[Authority|authority]], [[Compositionality|compositionality]], [[Equivalence vs Equality|equivalence vs equality]].

## Formal relations

- `refines`: [[Logic]] — Makes explicit the context, judgement form, rules, and evidence by which satisfaction, entailment, derivability, and related logical assertions are stated.
- `constrains`: [[Realization]] — Requires realization claims to name their source and target, requirements, boundary, evidence, authority, status, and preservation obligations.
