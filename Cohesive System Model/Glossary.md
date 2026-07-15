---
realm: Principles
kind: glossary
created: 2026-07-04
updated: 2026-07-15
status: draft
aliases:
  - base vocabulary
---

# Glossary

This glossary collects compact vocabulary used across the Cohesive system model. Terms that acquire their own distinctions, relations, and realization obligations are promoted into graph nodes rather than remaining glossary-only definitions.

Promoted concepts:

- [[Authority|authority]]
- [[Causality|causality]]
- [[Happened-Before|happened-before]]
- [[Consistent Cuts|consistent cuts]]
- [[Linearization Points|linearization points]]

## partial order

A partial order relates some positions while allowing others to remain incomparable. It is useful for histories with concurrency, causality, branches, replica divergence, or independent work that should not be forced into one total sequence.

## program order

Program order is the order of operations as issued by one participant, thread, process, observer, or session. [[Consistency Models|Sequential consistency]] preserves program order while allowing the global explanation to differ from wall-clock order between participants.

## real-time order

Real-time order is the external order in which non-overlapping operations occur: if operation `A` completes before operation `B` begins, real-time order places `A` before `B`. [[Consistency Models|Linearizability]] preserves real-time order; sequential consistency does not require it.

## total order

A total order compares every pair of positions in an ordering space. Total orders are useful for logs, replay, consensus decisions, and serial explanations, but they may impose artificial before/after relations on work that was concurrent in the domain.

Related concepts: [[Authority|authority]], [[Causality|causality]], [[Happened-Before|happened-before]], [[Consistent Cuts|consistent cuts]], [[Linearization Points|linearization points]], [[Ordering|ordering]], [[Time|time]], [[Version Histories|version histories]], [[Consistency Models|consistency models]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Sheaves and Gluing|sheaves and gluing]], [[Observation|observation]], [[Event|event]], [[Version|version]], [[Observer|observer]], [[Boundaries|boundaries]].
