---
realm: Principles
kind: principle
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Excluded Middle
  - LEM
  - Tertium Non Datur
---

# Law of Excluded Middle

The law of excluded middle is the logical schema:

$$
P \lor \neg P.
$$

It says that for every proposition $P$, either $P$ holds or its negation holds. Classical [[Logic|logic]] accepts this schema. Intuitionistic and constructive logics do not generally derive it without additional evidence, although they may derive excluded middle for particular decidable propositions.

## Classical and Constructive Readings

In classical proof systems, excluded middle can be used without constructing which disjunct holds. It supports proof by contradiction, double-negation elimination, and other classically equivalent principles over an appropriate constructive base.

In constructive logic, a proof of $P\lor\neg P$ must supply either a proof of $P$ or a proof that $P$ leads to contradiction. The absence of a proof of $P$ is not by itself a proof of $\neg P$. Declining the unrestricted law therefore does not assert that some proposition is both true and false; it requires positive evidence for whichever disjunct is claimed.

A proposition is **decidable** when there is a construction or procedure establishing $P\lor\neg P$ for that proposition. Equality on finite values may be decidable even when arbitrary function equality is not. Constructive mathematics can use excluded middle freely for propositions whose decidability has been proved.

## Related but Distinct Principles

Excluded middle should not be collapsed with:

- **Non-contradiction:** $\neg(P\land\neg P)$ rules out jointly proving a proposition and its negation but does not construct either side of $P\lor\neg P$.
- **Double-negation elimination:** $\neg\neg P\to P$ is classically valid and, as a schema over all propositions, is equivalent to excluded middle over intuitionistic logic.
- **Bivalence:** the semantic claim that every proposition has exactly one of the truth values true or false. Excluded middle is a formula or proof principle; bivalence is a claim about a semantics.
- **Decidability:** an effective or proof-relevant method for selecting a side. Classical excluded middle need not supply such a method.
- **Closed-world negation:** a modeling or database policy that treats failure to derive a fact as evidence for its negation. This is not a logical consequence without the completeness and boundary assumptions of the closed world.
- **The axiom of choice:** a separate principle. Relationships between choice and excluded middle depend on the surrounding set or type theory.

These distinctions matter whenever “either yes or no” is treated as though it also supplied knowledge, an algorithm, or an observation telling which answer is correct.

## Curry–Howard Interpretation

Under the [[Curry–Howard Correspondence|Curry–Howard correspondence]], excluded middle has a type such as:

$$
P + (P\to 0).
$$

An inhabitant must contain either evidence for $P$ or a function taking any evidence for $P$ to the empty type. There is no generic constructive lambda term inhabiting this type for every $P$.

Classical calculi give excluded middle computational interpretations through continuations, control operators, continuation-passing translations, or explicit axioms. These choices affect normalization, canonicity, proof extraction, and which terms count as computational evidence. Adding excluded middle as an opaque axiom may establish propositions without yielding a decision procedure that computes a visible left or right injection.

[[Linear Logic|Linear logic]] has its own classical and intuitionistic presentations and dualities. Classical linear negation and multiple-conclusion sequents should not be confused with unrestricted cartesian use of assumptions; excluded-middle-like formulas must be interpreted through the selected linear connectives and structural rules.

## Observation, Knowledge, and Time

For Cohesive, the central boundary is between truth, evidence, and observation. A proposition may be classically true or false while an [[Observer|observer]] lacks enough information to determine which. The observer may instead have an unknown, unavailable, stale, partial, conflicting, or not-yet-observed result.

Distributed systems make this distinction operationally unavoidable. Failure to observe a reply does not prove that the remote action did not happen. Failure to see a record does not prove that no authorized record exists at another replica or later version. A timeout divides behavior according to a [[Policy|policy]] and local clock; it does not derive the negation of the remote proposition.

An open-world model permits facts whose truth is not known locally. A closed-world model may treat non-derivability as negation only inside a declared complete scope. Eventual consistency, delayed delivery, partial observation, retention, and failure can invalidate that completeness assumption.

[[Temporal Logic|Temporal logic]] adds another distinction. “Eventually $P$ or eventually not $P$” is not the same property as deciding $P$ now, and a future observation can refine an earlier unknown result without making the earlier observer irrational. Time, knowledge, and truth occupy different modalities.

## Judgements and Realization

A [[Judgement|judgement]] should report whether a claim is established, refuted, conditional, or unknown under its context and evidence. Forcing every engineering assessment into a Boolean result can silently turn missing evidence into negation.

A compiler or theorem prover may operate in a classical meta-logic while checking a constructive object language, or conversely implement classical reasoning through a constructive kernel plus axioms. A compiler-like [[Realization|realization]] should state which logic governs authored claims, generated proof obligations, runtime decisions, and external observations.

Policies may deliberately totalize a partial situation: reject when evidence is missing, choose a default branch, expire after a deadline, or escalate to a human. Such a decision can be operationally sound, but it is a policy under uncertainty rather than proof that excluded middle supplied the missing evidence.

## Modeling Checks

- Is excluded middle an axiom, a derived theorem, or proved only for a decidable proposition?
- Does the claim require truth, proof evidence, an algorithm, or an observer-visible decision?
- Is failure to prove or observe $P$ being mistaken for proof of $\neg P$?
- Which boundary is complete enough to justify closed-world reasoning?
- How do partial observation, replication, delay, failure, and time affect what is known?
- What computational interpretation does classical reasoning receive?
- Does a policy choose a branch under uncertainty without claiming logical proof?

Related concepts: [[Logic|logic]], [[Judgement|judgement]], [[Type Theory|type theory]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Lambda Calculus|lambda calculus]], [[Linear Logic|linear logic]], [[Temporal Logic|temporal logic]], [[Observer|observer]], [[Observation|observation]], [[Uncertainty|uncertainty]], [[Policy|policy]], [[Boundaries|boundaries]], [[Failure Models|failure models]], [[Consistency Models|consistency models]], [[Realization|realization]].

## Formal relations

- `refines`: [[Logic]] — Identifies the classical schema $P\lor\neg P$ and separates its proof-theoretic use from constructive decidability, semantic bivalence, and boundary-relative evidence.
