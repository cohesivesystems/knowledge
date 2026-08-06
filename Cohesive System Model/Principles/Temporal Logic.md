---
realm: Principles
kind: discipline
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Temporal Logics
---

# Temporal Logic

Temporal logic is a family of [[Logic|logics]] for stating how propositions hold across [[Behavior|behaviors]], runs, traces, or branching transition structures. It adds modalities for time and succession without requiring every temporal claim to use wall-clock timestamps or metric durations.

A model first determines the behaviors under consideration: often sequences or paths of [[State|states]] related by admissible [[Transition|transitions]]. A temporal formula is then interpreted over positions, suffixes, or branches of those behaviors. The formula constrains the allowed behavior set; it does not by itself select a runtime, scheduler, clock, or enforcement mechanism.

## Common Operators

In linear-time notation, common operators include:

- $\mathbf{X}\,P$: $P$ holds at the next position.
- $\mathbf{F}\,P$: $P$ eventually holds at the current or some future position.
- $\mathbf{G}\,P$: $P$ always holds at every relevant future position.
- $P\,\mathbf{U}\,Q$: $P$ holds until $Q$ holds, with $Q$ eventually occurring.

Past-time, metric, interval, probabilistic, real-time, and epistemic extensions add other distinctions when the model requires them. “Eventually” ordinarily means at the current or some later position in every behavior covered by the formula. It does not establish a deadline or even a uniform finite bound unless the selected logic and model say so.

## Linear and Branching Views

Linear temporal logic evaluates formulas along individual linear paths. Branching-time logics distinguish alternative futures from a state and add path quantification, such as “on every path” or “on some path.” CTL constrains how path quantifiers and temporal operators combine, while CTL* permits more general nesting.

The choice is semantic. A linear trace may be appropriate after [[Scheduling|scheduling]] or [[Arbitration|arbitration]] selects one execution. A branching structure preserves the alternatives that were possible before that choice. Neither view should silently erase [[Nondeterminism and Choice|nondeterminism]], concurrency, or observer-relative information that matters to the claim.

## State, Actions, and Behaviors

State predicates describe one state. Action predicates relate a current state to a possible next state. Temporal formulas constrain complete behaviors built from those steps. This separation is central to the Temporal Logic of Actions used by [[TLA+]]: an initial-state predicate and a next-state action describe possible behaviors, while temporal formulas state invariance, progress, and fairness conditions over them.

Stuttering steps, in which the modeled variables do not change, matter when one specification step may correspond to zero or more steps at another abstraction level. A stuttering-invariant specification can hide internal steps or refine an abstract action into several concrete actions without changing the visible temporal meaning. Specifications using a distinguished next operator need extra care because that operator can make individual step counts observable.

## Safety, Liveness, and Fairness

[[Safety and Liveness|Safety and liveness]] give two central temporal property classes:

- A safety violation has a finite bad prefix: something forbidden has already happened.
- A liveness property requires that desired progress eventually occurs and cannot generally be refuted by one finite prefix.

An [[Invariant|invariant]] is a common safety property, often written $\mathbf{G}\,I$ for a state predicate $I$. Not every safety property is a state invariant; some constrain transitions or finite history patterns.

[[Fairness|Fairness]] excludes executions that indefinitely postpone eligible actions. Weak fairness requires progress for an action that remains continuously enabled; strong fairness addresses an action enabled infinitely often. Fairness is an assumption or constraint on the admitted behaviors, not a proof that the production scheduler supplies it.

## Cohesive Use

Temporal logic can qualify [[State Machines|state machines]], [[Process Theories|process descriptions]], interaction protocols, and distributed algorithms with explicit behavioral claims. It is especially useful for separating:

- Domain invariants from temporal progress requirements.
- Possible behavior from selected execution.
- Logical succession from wall-clock [[Time|time]].
- Safety that must hold on every admitted execution from liveness that depends on timing, failure, scheduling, or fairness assumptions.
- A verified specification from the implementation correspondence needed to transfer the result to a running system.

Model checking can explore a finite or finitely represented behavior space for violations. Deductive proof can establish claims symbolically from definitions and assumptions. Testing samples executions. Runtime monitoring observes a live trace. These are distinct realization and evidence mechanisms with different completeness boundaries.

## Formal relations

- `refines`: [[Logic]] — Adds modalities interpreted over behaviors, paths, or branching transition structures while retaining the distinction among syntax, models, satisfaction, and proof.
- `constrains`: [[State Machines]] — States safety, liveness, fairness, and other behavioral conditions over machine runs without selecting the mechanism that executes the transitions.

## External References

- Amir Pnueli, [The Temporal Logic of Programs](https://doi.org/10.1109/SFCS.1977.32), *18th Annual Symposium on Foundations of Computer Science*, 1977.
- Leslie Lamport, [The Temporal Logic of Actions](https://doi.org/10.1145/177492.177726), *ACM Transactions on Programming Languages and Systems* 16(3):872–923, 1994.

Related concepts: [[Logic|logic]], [[TLA+]], [[State Machines|state machines]], [[Behavior|behavior]], [[State|state]], [[Transition|transition]], [[Time|time]], [[Invariant|invariants]], [[Safety and Liveness|safety and liveness]], [[Fairness|fairness]], [[Scheduling|scheduling]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Process Theories|process theories]], [[Trace and Feedback|trace and feedback]], [[System Language and Realization|system language and realization]], [[Realization|realization]].
