---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-27
---

# Transition

A transition is a semantic decision relation that determines a possible state evolution for one subject boundary from typed input and explicit observations.

For an [[Entity|entity]], a transition definition describes deterministic, terminating, aggregate-local decision structure. Evaluating that definition uses a transition context:

```txt
observer and boundary
+ target entity state
+ typed command/input value
+ finite required observations
+ invariants, policies, authority, and expected version
-> transition decision
```

The transition context should be treated as "the" context only relative to the diagram of required observations, policies, authority, boundary, and version constraints that determine it. Wall clock, randomness, environment, user input, external state, and infrastructure results must appear as explicit observations or inputs rather than ambient semantic dependencies.

## Definition, Decision, and Commitment

The semantic decision law is:

```txt
decide(
  transition definition,
  typed input,
  finite observation,
  deterministic context
) -> transition decision
```

A transition decision may contain:

- A typed applied, no-change, rejected, alternate, or conflict outcome.
- A sparse semantic patch.
- Domain-event, request, signal, or reply emissions.
- Machine or lifecycle movements.
- The actual observation, branch, mutation, and emission trace.
- Derived guarantee demands and structured diagnostics.

The decision does not commit state. A storage or runtime realization interprets its commit demands, checks that the influencing observations remain valid, and either establishes the transition effect or reports an incompatible, conflict, or infrastructure outcome. Only a successful commit advances authoritative entity state and makes the corresponding local obligations durable.

A transition body suitable for portable execution is acyclic and activation-terminating. It does not perform I/O, wait, retry, sleep, resolve runtime services, or embed arbitrary executable callbacks. Those behaviors belong to explicit [[Effect|effects]], [[Process|processes]], and [[Realization|realization]] boundaries.

An applied transition has a transition effect when committed: the entity's state evolves within the entity boundary and advances according to its [[Version|version]] rule. The occurrence of that state evolution is an endogenous [[Event|event]]. Whether it is captured as current-state mutation, a persistence event, or another durable record depends on the realization.

Applied with no changed value is an explicit typed outcome, not a nil event. Domain-specific alternate outcomes and admission rejections should likewise remain explicit. A concurrency conflict is distinct from domain rejection, and an infrastructure or ambiguous-commit failure is distinct from both.

Lower-level value changes are better described as value transforms. The before/after relation between two entity states is a state evolution or state change. The domain transition is the stronger concept because it includes observer-relative interpretation, [[Authority|authority]], policy, invariants, concurrency checks, and realization-specific commitment.

Examples of rejected transitions include:

- Failed validation or precondition.
- Unauthorized request.

An expected-version mismatch is a concurrency conflict rather than a domain rejection. Invalid definitions, invariant violations, infrastructure failures, and ambiguous commit outcomes likewise retain their own failure meanings.

Examples of applied no-change or alternate outcomes include:

- Duplicate input whose domain effect was already committed.
- A valid no-op against the current state.
- Telemetry-only or correlation-only input.

Under the [[Stuff Structure Property|stuff structure property]] lens, a transition is structure: an operation or relation that organizes how entity state, command values, observations, authority, policies, and versions may produce typed outcomes, patches, emissions, movements, or rejection. [[Transition Models|Transition models]] arrange this semantic structure in a system graph; interpreters and commit mechanisms realize it.

Related concepts: [[Value|value]], [[Shape|shape]], [[Command|command]], [[Observer|observer]], [[Observation|observation]], [[Authority|authority]], [[Entity|entity]], [[State|state]], [[Event|event]], [[Version|version]], [[Effect|effect]], [[Effects]], [[Process|process]], [[Transition Models|transition models]], [[Commit Boundaries|commit boundaries]], [[Stuff Structure Property|stuff structure property]], [[Universal Constructions|universal constructions]], [[Algebras and Coalgebras|algebras and coalgebras]], [[Monads Monoids and Duals|monads monoids and duals]], [[Realization|realization]], [[Concurrency Control|concurrency control]].
