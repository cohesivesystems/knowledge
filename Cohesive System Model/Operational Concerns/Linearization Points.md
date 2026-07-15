---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Linearization Point
---

# Linearization Points

A linearization point is the logical instant at which an operation takes effect in the abstract sequential history used to justify [[Consistency Models|linearizability]]. It must lie between that operation's invocation and response.

The linearization point is a proof concept before it is a code location. In simple realizations it may align with one atomic instruction, compare-and-set, lock-protected update, transaction commit, or consensus decision. In more complex algorithms it can depend on another participant's helping step, a successful observation, or a logical point identified only by the correctness proof.

## Physical and Abstract Order

Linearization order need not equal:

- invocation order for overlapping operations;
- [[Scheduling|scheduler-selection]] order;
- physical instruction order across processors;
- message reception order;
- transaction start order;
- visibility order at caches or projections.

Linearizability requires the abstract order to preserve real-time order for non-overlapping operations and to satisfy the object's sequential specification. Overlapping operations may be placed in either order when both placements remain legal.

## Authority and Commitment

A candidate atomic step is not a valid linearization point merely because it is indivisible. The step must occur at the [[Authority|authoritative]] boundary that makes the operation count and must preserve the subject's transition semantics.

For a replicated object, a consensus-decided log position may establish the abstract order. For a database row, a successful expected-version update or transaction commit may establish it. Follower reads, caches, projections, and downstream effects have their own visibility and consistency boundaries and do not automatically share that point.

## Modeling Checks

- What invocation and response delimit the operation?
- Which abstract sequential specification must be preserved?
- Where does the operation logically take effect?
- Does the point lie at the authoritative commit boundary?
- How are overlapping operations ordered?
- Which observers see the result immediately, later, or through another consistency model?
- Is the claimed point a real atomic step, a helping step, a consensus decision, or a proof-derived logical event?

## External References

- Maurice P. Herlihy and Jeannette M. Wing, [Linearizability: A Correctness Condition for Concurrent Objects](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf), *ACM Transactions on Programming Languages and Systems* 12(3):463-492, 1990.

Related concepts: [[Consistency Models|consistency models]], [[Ordering|ordering]], [[Scheduling|scheduling]], [[Authority|authority]], [[Consensus|consensus]], [[Commit Boundaries|commit boundaries]], [[Concurrency Control|concurrency control]], [[Isolation|isolation]], [[Transition|transition]], [[Version|version]], [[Observation|observation]], [[Boundaries|boundaries]], [[Realization|realization]].
