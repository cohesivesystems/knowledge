---
realm: Principles
kind: principle
---

# Equivalence Vs Equality

Equivalence and equality should not be confused.

Equality usually means sameness inside a chosen representation, identity space, or semantic theory. Equivalence means two things can be treated as the same for a declared purpose, boundary, observer, or relation.

The model should ask:

- Equal according to which equality?
- Equivalent for which observer, boundary, operation, or guarantee?
- What information is ignored by the equivalence?
- Is the equivalence stable under the operations that will use it?
- Is the equivalence structural, behavioral, observational, operational, or representational?

Examples:

- Two [[Value|values]] may be equal in logical content while having different physical representations.
- Two event histories may lead to the same state but not be equivalent for audit, causality, or replay.
- Two observers may be behaviorally equivalent at one boundary but differ in latency, failure behavior, or authority.
- Two realizations may be equivalent for command interpretation but not equivalent for ordering, recovery, or locality.
- Two states may be observationally equivalent for a projection while not equal as full entity state.

Equivalence is often the right concept for abstraction. Equality is often too strong. But equivalence must be declared and preserved by the operations that rely on it.

Related concepts: [[Value]], [[State]], [[Event]], [[Observation]], [[Observer]], [[Realization]], [[Projections]], [[Naturality]].
