---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Arbiter
  - Arbiters
---

# Arbitration

Arbitration resolves local contention among competing eligible occurrences when the system must select, admit, order, or grant one or more of them.

Examples include choosing which asynchronous signal wins, which actor message is admitted next, which transaction obtains a lock, which request receives a concurrency slot, which worker owns a claim, or which proposal a leader places before a protocol.

Arbitration is an operational concern rather than a claim that the selected action is semantically valid. The receiving [[Boundaries|boundary]] must still interpret the result through current state, [[Authority|authority]], [[Policy|policy]], [[Invariant|invariants]], versions, and commitment rules.

## Adjacent Roles

| Role | Primary responsibility |
| --- | --- |
| arbiter | resolves a local contention or tie |
| [[Scheduling|scheduler]] | allocates execution opportunity across enabled work over time |
| sequencer | assigns positions in an order |
| coordinator | aligns several participants or effects toward a coherent outcome |
| [[Consensus|consensus protocol]] | makes participants agree on one value or ordered position |
| [[Authority|authority]] | determines why the resulting act or decision counts |

One mechanism can perform several roles, but the guarantees should be stated separately. A leader may schedule and sequence proposals, while quorum state authorizes the decided value. A lock manager may arbitrate ownership without deciding whether the protected domain transition is valid.

## Arbitration and Indeterminacy

When concurrent inputs do not determine a total order, arbitration resolves part of the [[Nondeterminism and Choice|nondeterministic]] execution. Actor reception-order indeterminacy is one example: concurrent message transmissions establish causal constraints, while local runtime and physical arbitration determine the order in which one actor receives or processes them.

If the competing operations commute or form [[Reduction, Evaluation, and Confluence|confluent]] paths, the arbitration result may be observationally irrelevant. If they conflict, the selected order can become part of semantic history and may need durable evidence, version advancement, or audit.

## Metastability and the Glitch Principle

Physical arbiters cross from continuously varying input timing into a discrete winner. The [[Glitch Principle|glitch principle]] shows that a non-trivial device making such a decision cannot guarantee one finite response bound for all inputs under the relevant continuity assumptions. Near-simultaneous inputs can leave the device metastable for arbitrarily long.

This result removes a bounded-time guarantee; it does not itself supply eventual settlement. [[Fairness]], failure assumptions, timeout policy, and protocol recovery remain separate.

## Correctness and Progress

Arbitration safety asks whether at most the permitted number of contenders can win and whether stale winners are rejected. Arbitration liveness asks whether an eligible contender eventually wins or learns that it lost. Priority and fairness determine whether repeated contention can starve one participant.

Fencing tokens, epochs, compare-and-set, queue positions, leases, lock ownership, ballots, and grants are realization mechanisms. Their meaning depends on which boundary accepts the evidence and whether later decisions can supersede earlier grants.

## Modeling Checks

- Which contenders and resource or decision are being arbitrated?
- Is the result a winner, an order, a grant, an admission, or a proposal?
- Which safety rule limits simultaneous winners?
- Which fairness or priority rule constrains repeated contention?
- Is decision time bounded, eventual, probabilistic, or best effort?
- Which epoch, token, or evidence proves that the result is current?
- Does winning arbitration confer execution opportunity, authority, or both?
- Are different arbitration outcomes commutative, confluent, or semantically distinct?

## External References

- Leslie Lamport and Richard Palais, [On the Glitch Phenomenon](https://lamport.azurewebsites.net/pubs/glitch.pdf), 1976.

Related concepts: [[Nondeterminism and Choice|nondeterminism and choice]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Glitch Principle|glitch principle]], [[Authority|authority]], [[Ordering|ordering]], [[Causality|causality]], [[Coordination|coordination]], [[Consensus|consensus]], [[Concurrency Control|concurrency control]], [[Progress Conditions|progress conditions]], [[Actor Systems|actor systems]], [[Runtimes|runtimes]], [[Realization|realization]].
