---
realm: Operational Concerns
kind: operational-concern
created: 2026-09-27
updated: 2026-09-27
status: draft
aliases:
  - Conformance
  - Implementation Refinement
  - Architecture Conformance
  - Specification Conformance
---

# Implementation Conformance

Implementation conformance describes whether code, configuration, generated artifacts, adapters, deployment plans, and running resources preserve the semantic and system-graph claims of the canonical model at a declared boundary.

Conformance is a correspondence, not representation equality. A target may introduce lower-level state, control flow, retries, storage layouts, provider resources, or operational mechanisms while remaining conformant when those details refine the source contract and preserve every distinction on which the surrounding system depends.

## Conformance Boundaries

A compiler-like realization can cross several independently accountable boundaries:

```text
authoring surface
  -> canonical semantic and system IR
  -> verified or analyzable projection
  -> realization plan
  -> generated and handwritten implementation
  -> deployment configuration
  -> observed running system
```

Each arrow needs its own preservation claim, assumptions, evidence, and declared trust boundary. Deterministic generation establishes repeatability, not semantic adequacy. A checked theorem about a formal projection does not establish that the projection faithfully represents the canonical model. Generated code does not establish that handwritten adapters or external effects conform. A valid plan does not establish that the deployed estate still matches it.

## Forms of Conformance

- **Authoring conformance** checks that builders, DSLs, importers, and editors produce the intended canonical definitions.
- **Projection conformance** checks that a formal, analytical, documentation, or observation projection preserves the source distinctions and claims required for its purpose.
- **Compiler conformance** checks that lowering and generated artifacts implement the certified source and realization plan.
- **Adapter conformance** checks handwritten translations, external integrations, and provider adapters against their declared contracts.
- **Configuration conformance** checks that an exact configured facility satisfies the premises used by its realization strategy.
- **Deployment conformance** checks that the physical estate matches the accepted realization, ownership, bindings, and configuration.
- **Trace conformance** checks whether observed implementation actions correspond to admitted semantic actions and histories.

Passing one form does not imply the others.

## Evidence and Change

Conformance evidence can include normalized reference traces, differential tests, generated proof obligations, refinement proofs, model-based tests, static analysis, artifact fingerprints, signed attestations, configuration inspection, deployment receipts, and runtime trace validation. [[Assurance and Evidence|Assurance and evidence]] determines which results are accepted for a given claim.

Conformance is revision-relative. Changes to the source model, projection, compiler, adapter, dependency, configuration, target version, or observation mapping can invalidate previous results. [[Compatibility and Evolution|Compatibility and evolution]] asks whether different revisions can continue to correspond; conformance asks whether a particular target or execution preserves its declared source revision.

## Modeling Checks

- Which source and target revisions are being compared?
- Which semantic identities, relationships, protocols, effects, guarantees, and failure meanings must be preserved?
- Which target details may vary without changing the source meaning?
- What proof, test, attestation, or observation supports each correspondence?
- Where are handwritten behavior, external systems, or trusted assumptions outside the checked boundary?
- What invalidates the conformance result?
- Does a runtime discrepancy refute conformance, reveal an incomplete observation mapping, or remain unknown?

## Formal relations

- `qualifies`: [[Realization]] — States whether canonical definitions, projections, plans, implementations, configurations, and deployed mechanisms preserve the required source meaning.
- `constrains`: [[Execution Kernel]] — Requires reference and concrete interpreters to preserve stable semantic identities, decisions, effects, causal order, and terminal outcomes across their differing mechanisms.
- `distinguished_from`: [[Compatibility and Evolution]] — Conformance relates a target to its declared source revision, whereas compatibility relates independently evolving revisions, histories, and participants.
