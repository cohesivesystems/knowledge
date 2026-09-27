---
realm: Operational Concerns
kind: operational-concern
created: 2026-09-27
updated: 2026-09-27
status: draft
aliases:
  - Assurance
  - Evidence
  - Runtime Assurance
  - Assurance Assessment
  - Evidence Policy
---

# Assurance and Evidence

Assurance and evidence describe why a semantic, structural, operational, realization, or conformance claim is accepted, rejected, conditional, or unknown at a declared boundary and time.

Evidence is attributable material offered in support of a claim. Assurance is the [[Judgement|judgement]] that interprets available evidence under an explicit policy. Evidence does not determine its own meaning, and an accepted judgement does not make the evidence stronger than the method, scope, assumptions, and coverage actually warrant.

## Evidence Records

An evidence record should identify:

- the exact claim and subject it supports or refutes;
- the subject revision, configuration, realization, and boundary;
- the assumptions and operating envelope under which it applies;
- the producer, method, authority, and collection time;
- its coverage, completeness, uncertainty, and known loss modes;
- its validity interval, freshness rule, and invalidation dependencies; and
- provenance to definitions, tools, inputs, artifacts, observations, and prior evidence.

Proofs, type checks, static analyses, model checks, provider declarations, certifications, configuration facts, conformance tests, deployment attestations, traces, measurements, benchmarks, operational histories, and human review are different evidence methods. They may concern the same property while remaining logically incomparable.

## Assurance Status

An assurance assessment should distinguish at least:

- **Established** — accepted evidence supports the claim within its declared scope.
- **Conditional** — the claim follows only while named assumptions, configurations, or boundaries hold.
- **Refuted** — valid evidence supplies a counterexample or contradiction within the claim scope.
- **Unknown** — available evidence is absent, stale, incomplete, inapplicable, or insufficient.
- **Overridden** — an authorized policy permits action despite an unmet assurance requirement without asserting that the original claim holds.

These statuses must not be collapsed into a Boolean result. Failure to derive is not derivation of failure, missing telemetry is not success, and an override is not proof.

## Safety, Liveness, and Observation Strength

A valid finite counterexample can refute a [[Safety and Liveness|safety]] property. A finite history with no observed violation generally cannot establish that the property holds for every admitted execution. Liveness claims additionally depend on progress, fairness, failure, timing, or bounded-deadline assumptions that finite observation alone rarely establishes.

An observation contract should identify the semantic actions or outcomes to be observed, correlation and causation identities, required ordering or clock information, collection coverage, sampling and loss behavior, retention, and the consequence of missing evidence. [[Observability and Provenance|Observability and provenance]] supplies observations and their lineage; assurance policy determines which conclusions those observations support.

## Compile-Time and Runtime Assurance

Compile-time assurance concerns definitions, derivations, candidate realizations, and generated artifacts. Runtime assurance concerns an exact deployed realization and the current evidence that its premises, configuration, environment, and behavior remain within accepted boundaries.

Runtime observations may strengthen confidence, detect drift, refute a claim, or make an assessment unknown when evidence expires. They do not retroactively turn a provider declaration into a formal theorem. A change to a property definition, strategy theorem, provider claim, configuration, realization, instrumentation path, or evidence policy invalidates dependent assessments unless a declared preservation rule says otherwise.

## Modeling Checks

- What exact claim, subject, boundary, and revision is being assessed?
- Which evidence method produced each record, and what can that method establish?
- Are the evidence scope, assumptions, and configuration aligned with the claim?
- Is the evidence sufficiently complete and fresh under the active policy?
- Does the result mean established, conditional, refuted, unknown, or overridden?
- Which dependencies would invalidate or require recomputation of the assessment?
- What response follows when assurance becomes violated or unknown?

## Formal relations

- `qualifies`: [[Realization]] — States which evidence supports a candidate, selected, deployed, or observed realization and which conclusions remain conditional or unknown.
- `qualifies`: [[Surfaces]] — Requires externally exposed claims to retain their evidence method, scope, assumptions, validity, and accepted assurance status.
- `qualifies`: [[Infrastructure Graph]] — Qualifies capability claims, physical mappings, attestations, observations, and time-indexed assessments in the substrate-facing projection.
- `distinguished_from`: [[Observability and Provenance]] — Observability supplies attributable observations, whereas assurance interprets evidence under rules and policy to reach a scoped judgement.
