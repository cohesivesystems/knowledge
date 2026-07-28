---
realm: Principles
kind: reference
created: 2026-07-27
updated: 2026-07-27
status: draft
aliases:
  - Execution Kernels
  - Portable Execution Kernel
  - Canonical Execution IR
---

# Execution Kernel

An execution kernel is a shared semantic and interpretation boundary through which portable transition and process descriptions become executable without making one runtime, storage engine, workflow product, actor system, or host-language program the source of meaning.

The kernel is not a new semantic subject, a monolithic runtime, or a requirement that every command be modeled as a [[Process|process]]. It connects the system language to compiler-like [[Realization|realization]]:

```txt
authoring or import
  -> canonical execution definition
  -> validation and requirement extraction
  -> transition decision or finite process activation
  -> capability-checked commit and continuation
  -> substrate effects and observations
```

## Canonical Authority

Persisted, versioned canonical definitions are semantic authority for executable [[Transition Models|transition models]] and [[Process Graphs|process graphs]]. Host-language authoring, source generators, editors, importers, agents, generated code, runtime registrations, checkpoints, backend plans, and deployment artifacts are producers, projections, derived artifacts, or interpretations.

Canonical authority does not replace the broader semantic graph. An [[Entity|entity]], [[State|state]], [[Event|event]], [[Effect|effect]], [[Transition|transition]], or [[Process|process]] is not defined by its serialized representation. The canonical execution definition is the stable system-graph structure chosen to make those meanings portable and independently interpretable.

Persisted definitions should distinguish:

- Definition identity.
- Serialization or schema version.
- Accepted semantic revision.
- Deterministic normalized content identity.
- Producer, source, and transformation provenance.

Names and source positions are descriptive metadata, not sufficient compatibility evidence for long-lived state.

## Finite Decisions and Activations

A transition evaluation and each individual process activation terminate, reach quiescence, or reach an explicit durable cut. Long-lived behavior arises through persisted continuation, timers, observations, signals, feedback, and repeated finite activations rather than unrestricted host-language computation hidden inside the definition.

Deterministic semantic computation uses explicit typed values, expressions, observations, and intrinsic operations. Wall clock, randomness, environment, user input, external state, and infrastructure results enter through explicit observation or interaction boundaries.

## Semantics before Mechanisms

Definitions and system-graph structure declare required behavior and guarantees. Infrastructure graphs and adapters supply capability evidence and candidate realizations. A realization may be native, composed, constrained, overridden with explicit authority, unavailable, or unknown. It must not silently weaken atomicity, isolation, durability, visibility, ordering, response obligation, idempotency, recovery, compatibility, or another declared requirement.

Reference interpreters, concrete interpreters, serializers, validators, requirement extractors, and trace normalizers provide conformance evidence. Equivalent interpretations preserve stable semantic identities, decisions, causal order, effects, terminal outcomes, and declared guarantees even when wall-clock timestamps, workers, storage layouts, or informational diagnostics differ.

Related concepts: [[System Language and Realization|system language and realization]], [[Realization|realization]], [[System Graph|system graph]], [[Infrastructure Graph|infrastructure graph]], [[Transition|transition]], [[Transition Models|transition models]], [[Process|process]], [[Process Graphs|process graphs]], [[Entity|entity]], [[State|state]], [[Event|event]], [[Effect|effect]], [[Observation|observation]], [[Shape|shape]], [[Identity|identity]], [[Version|version]], [[Commit Boundaries|commit boundaries]], [[Durable Execution|durable execution]], [[Recovery|recovery]], [[Runtimes|runtimes]], [[Storage Systems|storage systems]], [[Durable Execution Engines|durable execution engines]].
