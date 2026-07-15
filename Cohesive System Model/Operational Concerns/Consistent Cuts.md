---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Consistent Cut
---

# Consistent Cuts

A consistent cut is a selected set of events, versions, observations, or process positions that is closed under the declared [[Causality|causal]] prerequisites.

For a happened-before relation, a cut `C` is consistent when:

```txt
e is in C and d happened-before e
implies
d is in C
```

The cut may include concurrent occurrences in different combinations. It must not include an effect while omitting a cause required by the chosen causal relation.

## Observation Semantics

A consistent cut is a coherent snapshot of a partial history, not necessarily a wall-clock snapshot or one atomic read. Different observers can select different consistent cuts while remaining causally valid.

Cross-entity reads, distributed snapshots, checkpoints, workflow recovery, projection rebuilds, debugging, and replicated queries should state whether they observe:

- one consistent cut;
- a stale but causally closed cut;
- a session-relative cut;
- independently selected local observations with no common-cut claim;
- a coordinated atomic snapshot stronger than causal closure.

[[Systems Sheaf Semantics|Systems sheaf semantics]] treats consistent cuts as contexts over which observations, states, versions, histories, and explanations can be restricted, compared, and sometimes glued.

## Construction and Realization

Vector clocks, snapshot algorithms, transaction snapshots, log positions, barriers, checkpoints, dependency tokens, and coordinated reads can help construct or record consistent cuts. These mechanisms provide different boundaries and strengths.

A set of individually fresh reads need not form a consistent cut. A set of stale reads can form one when their versions are mutually causally compatible. Freshness, atomicity, causal closure, and linearizability are therefore separate properties.

## Modeling Checks

- Which occurrences and causal relation define the history?
- Is the cut downward closed under [[Happened-Before|happened-before]]?
- Which concurrent occurrences may be independently included?
- Is the claim causal closure, atomic snapshot, freshness, or all three?
- Which observer and boundary select the cut?
- Which metadata proves that independently obtained observations belong to one coherent cut?

## External References

- K. Mani Chandy and Leslie Lamport, [Distributed Snapshots: Determining Global States of a Distributed System](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Determining-Global-States-of-a-Distributed-System.pdf), *ACM Transactions on Computer Systems* 3(1):63-75, 1985.

Related concepts: [[Causality|causality]], [[Happened-Before|happened-before]], [[Ordering|ordering]], [[Consistency Models|consistency models]], [[Version Histories|version histories]], [[Observation|observation]], [[State|state]], [[Version|version]], [[Observer|observer]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Sheaves and Gluing|sheaves and gluing]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Boundaries|boundaries]].
