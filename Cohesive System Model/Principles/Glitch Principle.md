---
realm: Principles
kind: principle
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Glitch Phenomenon
  - Principle of the Glitch
---

# Glitch Principle

The glitch principle states that a non-trivial device making a discrete decision among finitely many outcomes from a continuous range of possible inputs cannot guarantee a uniform finite decision time for every input.

The classic example is an electronic arbiter deciding which of two asynchronous input events occurred first. When the inputs arrive sufficiently close together, the device can enter a metastable condition and take arbitrarily long to settle on one digital outcome.

The principle is topological rather than probabilistic. Under the relevant continuity assumptions, continuously varying inputs connect regions that lead to different discrete outcomes. For every finite deadline, some input near the decision boundary has not yet reached either settled outcome by that time.

The conclusion is:

```txt
no uniform finite bound on decision time
```

It does not by itself imply:

```txt
every arbitration eventually settles
the outcome has a declared probability distribution
the device violates its allowed outcomes
the physical dynamics are logically random
```

Eventual settlement is an additional [[Fairness|fairness]] or liveness assumption. Probability can describe practical metastability risk or noise, but adding noise changes which inputs cause long delay rather than removing the absence of a worst-case bound.

## Arbitration and Actors

[[Arbitration]] resolves contention among competing occurrences. In an [[Actor Systems|actor system]], concurrent message transmissions can require runtime or physical arbitration before one reception order is established. This gives a realization path from continuous physical behavior to actor reception-order [[Nondeterminism and Choice|indeterminacy]].

The layers should remain distinct:

```txt
continuous physical inputs
-> arbiter dynamics and possible metastability
-> local reception or scheduling decision
-> actor behavior under the selected order
```

The glitch principle explains why the arbitration step cannot promise bounded response for all physical inputs. It does not alone prove actor-level delivery fairness or guarantee service in the presence of crash, partition, loss, or resource exhaustion.

## Determinacy and Observation

At a continuous physical boundary, the device has an evolving analog state. At a digital boundary, the required result is one of a finite set of decisions. During metastability, the digital result is not yet safely determined even though lower-level physical state continues to evolve.

This illustrates why determinacy and uncertainty are boundary-relative. A detailed physical theory may treat the evolution as deterministic but highly sensitive to hidden conditions. The digital model treats the outcome as unresolved until a stable decision can be observed and committed.

## Modeling Checks

- Is a discrete system decision realized by a continuous physical process?
- Which participants or events require arbitration?
- Is completion bounded, merely eventual, probabilistic, or best effort?
- Which fairness or failure assumptions are separate from the physical result?
- What happens if the arbiter has not settled before a timeout or deadline?
- Does the higher-level protocol preserve safety while waiting an unbounded time?

## External References

- Leslie Lamport and Richard Palais, [On the Glitch Phenomenon](https://lamport.azurewebsites.net/pubs/glitch.pdf), 1976.

Related concepts: [[Nondeterminism and Choice|nondeterminism and choice]], [[Arbitration|arbitration]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Progress Conditions|progress conditions]], [[Safety and Liveness|safety and liveness]], [[Actor Systems|actor systems]], [[Runtimes|runtimes]], [[Realization|realization]], [[Boundaries|boundaries]], [[Observation|observation]].
