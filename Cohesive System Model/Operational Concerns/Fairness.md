---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Fair Scheduling
  - Scheduler Fairness
---

# Fairness

Fairness constrains complete executions so that eligible participants, messages, or actions are not postponed forever under the stated assumptions.

Fairness refines [[Safety and Liveness|liveness]]. It does not state that every action is safe, that completion has a finite time bound, or that resources are allocated equally. It identifies which starvation-like executions are excluded from the model.

## Common Forms

- **Weak fairness** or **justice**: an action that remains continuously enabled from some point onward eventually occurs.
- **Strong fairness** or **compassion**: an action enabled infinitely often eventually occurs.
- **Process fairness**: an eligible participant eventually receives execution opportunity.
- **Message fairness**: a message that remains deliverable is eventually admitted or received.
- **Choice fairness**: an alternative that remains eligible is not ignored forever.
- **Probabilistic fairness**: starvation has probability zero under a declared stochastic model, which is weaker than a per-execution guarantee.

Fairness claims are boundary- and failure-relative. A message cannot remain deliverable across a permanent partition under a model that treats the link as unavailable. A crashed participant is not continuously enabled unless recovery is part of the fairness assumption. Priority, cancellation, expiry, leases, and resource exhaustion can also change eligibility.

## Unbounded Delay

Fairness guarantees eventuality without necessarily giving a finite uniform bound. For every integer `n`, a request may be delayed for more than `n` steps while still being guaranteed eventual service in every admissible execution.

König's lemma explains why this does not fit a naive finitely branching tree in which all branches are admitted. If such a tree contains arbitrarily long finite branches, it contains an infinite branch. Unbounded fair service therefore excludes the infinite starvation branch as inadmissible even though every finite prefix can still be extended to a fair execution.

```txt
work^0 ; service
work^1 ; service
work^2 ; service
...

work^infinity        -- excluded as unfair
```

Fairness is consequently a property of whole paths or their infinite tails, not a safety property witnessed by one finite bad prefix.

## Scheduling and Search

[[Scheduling]] generates a concrete execution by selecting among enabled occurrences. Fairness restricts the allowed scheduler behaviors. Different layers can have different fairness claims: CPU scheduling, runtime tasks, actor activations, message delivery, broker assignments, workflow steps, locks, and retries do not inherit fairness automatically from one another.

Fairness also matters in [[Relational and Logic Programming|relational and logic programming]]. A depth-first search can follow one infinite branch and permanently hide answers elsewhere. Interleaved or breadth-oriented search can improve answer fairness while changing memory, latency, and ordering behavior.

## Fairness, Consensus, and Consistency

[[Consensus]] safety must hold regardless of fair scheduling. Consensus termination usually depends on additional liveness assumptions such as eventual message delivery, quorum availability, partial synchrony, randomized progress, or eventual leadership.

Most [[Consistency Models|consistency models]] constrain history safety rather than scheduling fairness. A history can be linearizable even when an operation starves. Eventual convergence adds liveness assumptions about delivery, reconciliation, and continued execution that should be named separately.

## Modeling Checks

- Which participant, message, action, or choice is protected from starvation?
- What does enabled or eligible mean at this boundary?
- Is fairness weak, strong, probabilistic, or mechanism-specific?
- Which failures, cancellations, priorities, or resource limits suspend the guarantee?
- Is completion merely eventual or bounded by time, steps, turns, or queue positions?
- Is fairness assumed by the semantic model, supplied by a runtime, or only expected operationally?
- Does safety hold even on unfair executions?

## External References

- Nissim Francez, [Fairness](https://doi.org/10.1007/978-1-4612-4886-6), Springer, 1986.
- Daniel Lehmann, Amir Pnueli, and Jonathan Stavi, [Impartiality, Justice and Fairness: The Ethics of Concurrent Termination](https://doi.org/10.1007/3-540-10843-2_22), in *Automata, Languages and Programming*, LNCS 115:264-277, 1981.

Related concepts: [[Nondeterminism and Choice|nondeterminism and choice]], [[Scheduling|scheduling]], [[Arbitration|arbitration]], [[Glitch Principle|glitch principle]], [[Progress Conditions|progress conditions]], [[Safety and Liveness|safety and liveness]], [[Consensus|consensus]], [[Consistency Models|consistency models]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Actor Systems|actor systems]], [[Runtimes|runtimes]], [[Workflow Engines|workflow engines]], [[Relational and Logic Programming|relational and logic programming]].
