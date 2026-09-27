---
realm: Realization Substrate
kind: realization-substrate
created: 2026-09-27
updated: 2026-09-27
status: draft
aliases:
  - Proof Assistant
  - Interactive Theorem Provers
  - Interactive Theorem Prover
---

# Proof Assistants

Proof assistants are languages and checking environments for expressing definitions, propositions, proofs, and machine-checked derivations. Lean, Coq, Agda, Isabelle, and similar systems can realize selected [[Logic|logical]], [[Type Theory|type-theoretic]], algebraic, and refinement accounts of a system model.

A proof assistant is a realization substrate for formal reasoning. It is not the semantic authority for the domain, the running implementation, or empirical evidence about a provider. A checked theorem establishes its conclusion from the encoded definitions, hypotheses, imported results, and trusted checking stack.

## Architecture Mechanization

A bounded Cohesive formalization may use a proof assistant to:

- define parameterized architectural properties over states, operations, traces, histories, and failure models;
- establish implication and refinement relationships among properties;
- prove that a realization strategy's premises entail a required property;
- check consistency or incompatibility of selected assumptions;
- prove preservation laws for composition, abstraction, or lowering; and
- assign stable identities and revisions to reusable theorem artifacts.

The formal projection must remain attributable to canonical graph concepts. It needs a stated adequacy or preservation argument: deterministic translation into a proof language does not by itself establish that the encoding captured the intended meaning.

## Trusted Boundaries

A proof result should identify:

- the exact definitions and theorem statement;
- hypotheses, axioms, imported libraries, and admitted results;
- the proof assistant and checker version;
- generated code, extraction, reflection, solvers, or external certificates involved;
- the source graph identities and revisions represented; and
- the claims not covered by the formalization.

The trusted computing base depends on the proof system and workflow. Kernel checking can reduce trust in tactic implementations, but it does not remove trust in the theorem statement, semantic encoding, compiler, hardware, or evidence used to connect the theorem to a deployed system.

## Realization Boundary

A proof assistant can establish a conditional theorem such as:

```text
linearizable lease
+ monotonic epoch
+ authoritative stale-epoch rejection
=> fenced exclusive mutation
```

It cannot by itself establish that a provider implements a linearizable lease, that the deployed store rejects stale epochs, or that every mutation route passes through the checked construction. Those are [[Implementation Conformance|implementation conformance]] and [[Assurance and Evidence|assurance and evidence]] obligations.

Proof assistants complement rather than replace [[TLA+|TLA+]], model checking, testing, static analysis, and runtime observation. Each mechanism supports different [[Judgement|judgements]] and completeness boundaries.

## Modeling Checks

- Which graph concepts and properties are represented in the formal theory?
- What does the theorem conclude, and from which exact hypotheses?
- How is the projection from canonical concepts justified?
- Which parts of the realization or provider behavior remain assumptions?
- What belongs to the trusted computing base?
- How are theorem identity, revision, provenance, and invalidation tracked?
- Is the result a proof of the model, a conformance result, or evidence about a running deployment?

## Formal relations

- `may_realize`: [[Logic]] — Provides concrete languages and checking kernels for selected logical definitions, propositions, and derivations without defining logic in general.
- `may_realize`: [[Type Theory]] — Implements selected propositions-as-types, dependent typing, equality, induction, and proof-term disciplines under a particular type theory.
- `may_realize`: [[Judgement]] — Checks formal derivability and related judgement forms while leaving semantic adequacy and empirical premises to separate evidence.
