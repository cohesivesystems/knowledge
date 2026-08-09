---
realm: System Graph
kind: structural-construct
created: 2026-07-27
updated: 2026-08-08
aliases:
  - Transition Model
  - Transition Structure
---

# Transition Models

Transition models describe how the semantic [[Transition|transition]] role is arranged in the system graph.

A transition model belongs to one subject or aggregate authority boundary. It relates typed input, finite [[Observation|observations]], entity state paths, policies, invariants, authority, branching, outcomes, patches, machine movements, and [[Effect|effect]] declarations without choosing the runtime or storage mechanism that will interpret or commit them.

An executable transition model commonly identifies:

- A stable definition identity and accepted semantic revision.
- Typed input and outcome shapes.
- The target [[Entity Models|entity model]] and authority boundary.
- Required sparse observations and their freshness or consistency demands.
- Admission rules, branches, matches, and stable path identities.
- Sparse state patches and machine or lifecycle movements.
- Domain-event, request, signal, or reply emissions.
- Invariants and policies that must hold on accepted paths.
- Derived guarantee demands, diagnostics, and provenance.

Definition identity, schema version, semantic revision, and normalized content identity answer different questions. A display name or source location is not enough to establish compatibility for a persisted definition or a long-lived continuation that references it.

## Decision and Commit Structure

A transition model defines a deterministic decision structure. One evaluation consumes typed input and explicit observations and produces a transition decision. The decision is not a committed entity mutation or a physically executed external effect.

```txt
transition model + input + observations
  -> transition decision
  -> capability-checked commit plan
  -> committed entity effect and durable obligations
  -> later external effect execution or observation
```

This separation lets several substrates interpret the same transition model while preserving the same branch, outcome, patch, emission, and guarantee meanings. A full-state interpreter, sparse-state interpreter, actor-hosted interpreter, database-backed interpreter, or event-sourced interpreter is a [[Realization|realization]] of the model rather than a competing definition of it.

Path-sensitive structure matters. Must, may, and actual observations, writes, and emissions are projections from the conditional transition model; they should not be maintained as unrelated parallel lists. Every observation that influences admission, branch selection, calculation, validation, outcome construction, or emission construction must remain valid through the declared commit boundary.

A transition model may be invoked directly. It becomes a node in a [[Process Graphs|process graph]] when work must coordinate multiple transitions, subjects, interactions, waits, timelines, or recovery boundaries.

Related concepts: [[Transition|transition]], [[Entity|entity]], [[State|state]], [[Observation|observation]], [[Effect|effect]], [[Event|event]], [[Entity Models|entity models]], [[Process Graphs|process graphs]], [[Observer Models|observer models]], [[Policy Scopes|policy scopes]], [[Invariant Scopes|invariant scopes]], [[Boundaries|boundaries]], [[Effect Models|effect models]], [[Commit Boundaries|commit boundaries]], [[Concurrency Control|concurrency control]], [[Realization|realization]], [[Execution Kernel|execution kernel]].

## Formal relations

- `arranges`: [[Transition]] — Places the semantic transition role into model-specific observation, decision, validation, outcome, and commit structure.
