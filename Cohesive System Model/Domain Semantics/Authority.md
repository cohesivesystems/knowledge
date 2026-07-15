---
realm: Domain Semantics
kind: semantic-construct
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Authorities
  - Authoritative Source
---

# Authority

Authority is the boundary-relative standing by which an [[Observer|observer]], role, protocol outcome, or source is accepted as able to make a claim, decision, [[Transition|transition]], or [[Effects|effect]] count for a modeled subject.

Authority answers:

> Who or what is entitled to settle this question, for which subject, within which boundary, and under what conditions?

Authority is a relation rather than an intrinsic property of a participant:

```txt
holder or source
+ act or claim
+ governed subject
+ boundary and scope
+ policy and validity conditions
+ term, version, or epoch
-> authority to make the act or claim count
```

An [[Identity|identity]] says who a participant is. Authentication supplies evidence for that identity. A capability says what the participant can technically attempt. A permission says what a [[Policy|policy]] allows. Authorization evaluates a request against that policy. Authority says whose accepted act, assertion, or decision establishes the modeled result.

Technical capability does not imply current authority. A worker can retain network access after its lease expires. A former leader can continue sending writes after a new term begins. Fencing tokens, epochs, quorum certificates, signatures, or target-side version checks are realization mechanisms that let a receiving boundary reject stale or invalid exercises of authority.

## Forms of Authority

- **Transition authority**: who may accept and commit state change for a subject.
- **Assertational authority**: whose facts or observations count as endorsed evidence.
- **Decision authority**: who may choose process progress, completion, cancellation, or compensation.
- **Effect authority**: who may commit externally consequential effects.
- **Disclosure authority**: who may expose an observation to a particular observer.
- **Evidentiary authority**: which persisted material controls reconstitution, recovery, or audit.

Authority can be centralized, delegated, partitioned by subject, shared through a protocol, limited to one term or epoch, or derived from [[Consensus|consensus]]. A leader may propose or schedule work while quorum state authorizes the decision. A projection may be authorized to answer a [[Query|query]] while write-side persistence remains authoritative for accepted transitions.

Authority does not imply truth, freshness, or infallibility. An authoritative record can be wrong, and an authoritative observer can act on stale information. The model states which claim controls behavior at a boundary; evidence, consistency, correction, and audit remain separate concerns.

## Authority and Choice

[[Nondeterminism and Choice|Choice]] becomes an authority question when several eligible outcomes exist but only some participant or protocol has standing to resolve them. [[Scheduling]] may select which work runs next without granting the scheduler authority to make a domain decision. [[Arbitration]] may establish a local winner without making that winner's proposal domain-valid. [[Consensus]] may authorize a shared log position without validating the proposed transition against domain invariants and policies.

Split authority is hazardous when two observers can each commit non-commuting transitions for the same subject while believing they are authoritative. It can be intentional when authority is partitioned, operations commute, conflicts remain explicit, or reconciliation is part of the semantic protocol.

## Modeling Checks

- Which subject, claim, transition, decision, or effect is governed?
- Which observer, role, protocol, or source has authority?
- From where is that authority derived?
- Is it delegated, shared, partitioned, revocable, or time-bounded?
- Which term, epoch, version, or evidence establishes that it is current?
- Which boundary accepts or rejects the exercise of authority?
- Does the realization prevent stale capability from being mistaken for authority?
- Which material is authoritative for recovery, reconstitution, and audit?

## External References

- Butler W. Lampson, [Protection](https://dl.acm.org/doi/10.1145/775265.775268), *ACM SIGOPS Operating Systems Review* 8(1):18-24, 1974.
- Jerome H. Saltzer and Michael D. Schroeder, [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939), *Proceedings of the IEEE* 63(9):1278-1308, 1975.

Related concepts: [[Observer|observer]], [[Identity|identity]], [[Policy|policy]], [[Command|command]], [[Query|query]], [[Transition|transition]], [[Invariant|invariant]], [[Boundaries|boundaries]], [[Policy Scopes|policy scopes]], [[Effects|effects]], [[Scheduling|scheduling]], [[Arbitration|arbitration]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Consensus|consensus]], [[Coordination|coordination]], [[Consistency Models|consistency models]], [[Persistence|persistence]], [[Realization|realization]].
