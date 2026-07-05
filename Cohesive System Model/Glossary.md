---
realm: Principles
kind: glossary
created: 2026-07-04
updated: 2026-07-04
status: draft
aliases:
  - base vocabulary
  - consistent cut
  - happened-before
  - linearization point
---

# Glossary

This glossary collects base vocabulary used across the Cohesive system model. It is for compact definitions of terms that support several notes but do not yet need their own graph node.

## causality

Causality is a dependency relation between events, observations, transitions, or effects where one occurrence may have influenced, enabled, required, or carried information into another. In distributed systems, causality is usually modeled through an explicit [[Ordering|ordering]] relation rather than inferred from wall-clock time.

## consistent cut

A consistent cut is a selected set of events, versions, or observations that is closed under causality: if the cut includes an occurrence, it also includes the causal prerequisites of that occurrence.

A consistent cut is a coherent snapshot relative to a declared partial order. It may include concurrent occurrences in different combinations, but it must not include an effect while omitting a cause that happened before it.

## happened-before

Happened-before is a strict partial order over events or observations that preserves possible causal influence. If `A` happened before `B`, information from `A` could have influenced `B`; the relation does not prove that `A` semantically caused `B`.

## linearization point

A linearization point is the instant at which an operation takes effect in the abstract history used to justify [[Consistency Models|linearizability]]. For a write, it is often an atomic update or transaction commit; for a read, it is the point at which the returned committed version is selected.

## partial order

A partial order relates some positions while allowing others to remain incomparable. It is useful for histories with concurrency, causality, branches, replica divergence, or independent work that should not be forced into one total sequence.

## program order

Program order is the order of operations as issued by one participant, thread, process, observer, or session. [[Consistency Models|Sequential consistency]] preserves program order while allowing the global explanation to differ from wall-clock order between participants.

## real-time order

Real-time order is the external order in which non-overlapping operations occur: if operation `A` completes before operation `B` begins, real-time order places `A` before `B`. [[Consistency Models|Linearizability]] preserves real-time order; sequential consistency does not require it.

## total order

A total order compares every pair of positions in an ordering space. Total orders are useful for logs, replay, consensus decisions, and serial explanations, but they may impose artificial before/after relations on work that was concurrent in the domain.

Related concepts: [[Ordering|ordering]], [[Time|time]], [[Version Histories|version histories]], [[Consistency Models|consistency models]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Sheaves and Gluing|sheaves and gluing]], [[Observation|observation]], [[Event|event]], [[Version|version]], [[Observer|observer]], [[Boundaries|boundaries]].
