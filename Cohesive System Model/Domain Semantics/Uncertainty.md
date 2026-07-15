---
realm: Domain Semantics
kind: semantic-construct
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Epistemic Uncertainty
  - Information State
---

# Uncertainty

Uncertainty is multiplicity in the states, histories, causes, outcomes, or interpretations that an [[Observer|observer]] cannot yet distinguish at a declared [[Boundaries|boundary]].

An observer's information state can be represented as a set of possible worlds or system states:

```txt
knowledge(observer) subset-of PossibleStates
```

An [[Observation|observation]] refines uncertainty when it rules out possibilities. It need not reveal one complete or perfectly current state. Stale, partial, probabilistic, conflicting, or differently authorized observations can leave several possibilities open.

## Forms of Uncertainty

- **State uncertainty**: the current state or version is not known precisely.
- **Outcome uncertainty**: several future results remain possible.
- **Causal uncertainty**: the dependencies or explanation for an occurrence are not known.
- **Measurement uncertainty**: an observation is noisy, approximate, sampled, or interval-valued.
- **Timing and failure uncertainty**: delay cannot be distinguished from pause, loss, partition, overload, or crash within the available evidence.
- **Model uncertainty**: the transition rules, environment, probability model, or relevant boundary are themselves incomplete or disputed.
- **Authority uncertainty**: an observer does not know which source, lease, term, quorum certificate, or decision currently has [[Authority|authority]].

Probability, possibility sets, intervals, belief states, evidence lattices, and provenance graphs preserve different information. A probability distribution can encode belief about hidden state, stochastic behavior in the system, or both. Its interpretation must therefore be stated rather than inferred from the representation alone.

## Relationship to Nondeterminism

[[Nondeterminism and Choice|Nondeterminism]] is multiplicity in the continuation relation: one state admits several possible next outcomes. Uncertainty is multiplicity in an observer's information: several states, histories, or outcomes remain compatible with what has been observed.

For state space `S`:

```txt
nondeterministic transition : S -> Set<S>
observer information        : Set<S>
```

The two interact without being identical:

- An unobserved nondeterministic transition can enlarge uncertainty.
- A deterministic system can still be uncertain to an observer because relevant state or input is hidden.
- A later observation can reduce uncertainty without changing the system's transition relation.
- A scheduler or policy can resolve a choice while an observer remains uncertain about which branch was selected.
- Several internal paths can remain uncertain but irrelevant when they are confluent or observationally equivalent at the boundary.

## Distributed Decisions

Distributed systems make uncertainty operationally important. A participant often cannot determine whether a remote action failed, is delayed, committed but unacknowledged, or will later be retried. [[Consistency Models|Consistency models]], versions, causal metadata, acknowledgments, leases, and consensus certificates constrain which conclusions are justified; they do not remove all uncertainty at every boundary.

Uncertainty should not be converted directly into rejection, retry, or acceptance. A [[Policy|policy]] determines how evidence and risk affect a decision. Authority determines whose assertion can settle a question. [[Safety and Liveness|Safety and liveness]] determine whether waiting, proceeding, compensating, or exposing tentative state is permitted.

## Modeling Checks

- Which observer is uncertain about which subject or occurrence?
- Which possibilities remain compatible with its observations?
- Is the uncertainty epistemic, stochastic, causal, temporal, measurement-based, or structural?
- Which observation, version, evidence, or authority could refine it?
- Must the system decide before the uncertainty is resolved?
- Which mistakes are safe, reversible, compensatable, or forbidden?
- Does a probability describe system behavior or the observer's belief?
- Which differences are intentionally hidden by equivalence or confluence?

## External References

- Joseph Y. Halpern, [Reasoning about Uncertainty](https://mitpress.mit.edu/9780262533805/reasoning-about-uncertainty/), second edition, MIT Press, 2017.

Related concepts: [[Observer|observer]], [[Observation|observation]], [[Observable|observable]], [[State|state]], [[Version|version]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Causality|causality]], [[Authority|authority]], [[Policy|policy]], [[Consistency Models|consistency models]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Consensus|consensus]], [[Safety and Liveness|safety and liveness]], [[Boundaries|boundaries]].
