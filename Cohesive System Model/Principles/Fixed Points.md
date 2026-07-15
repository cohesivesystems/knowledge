---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-07-14
aliases:
  - Fixed Point
---

# Fixed Points

A fixed point is a value, structure, or behavior that a specified transformation leaves unchanged:

$$
F(x) = x
$$

Fixed-point reasoning asks what remains invariant under a transformation. Both the transformation and the relevant notion of sameness must be explicit: unchanged may mean literal equality or an [[Equivalence vs Equality|equivalence]] appropriate to the model boundary.

## Recursive Definitions

A recursive equation can characterize a whole as a solution to $X = F(X)$. In that setting, a fixed point supplies a possible meaning for the self-referential definition. If the equation has several solutions, additional structure may select a least or greatest fixed point; existence and uniqueness are not automatic.

This is the central relationship with [[Recursion|recursion]]: recursion supplies the self-referential definition, while fixed-point semantics identifies a solution that satisfies it. A recursive computation need not reach that solution, and a fixed point can exist without being computed recursively.

## Stable Behavior

For a transition or update function, a state $s^*$ is a fixed point when another application under the same modeled conditions produces no change:

$$
F(s^*) = s^*
$$

Repeated application may reach or converge toward a fixed point, but it may instead terminate for another reason, oscillate, or diverge. Repetition alone therefore does not establish a fixed point. A retry loop that stops because its budget is exhausted has terminated; it has not necessarily reached a fixed point.

## Idempotence

Algebraic idempotence is not itself a fixed point. It is a property of an operation, while being a fixed point is a property of a value relative to that operation.

For an operation modeled as a function $N : X \to X$, idempotence means:

$$
N(N(x)) = N(x)
$$

Let $y = N(x)$. Then $N(y) = N(N(x)) = N(x) = y$, so every result of an idempotent operation is a fixed point of that operation. The converse does not hold: an operation may have some fixed points without being idempotent for all inputs.

[[Idempotency]] applies a related guarantee operationally to repeated handling of the same semantic input. With that input held fixed, the result is a fixed point of the handling operation at the declared effect boundary. The fixed point may be relative to an equivalence rather than literal equality: domain effects may remain unchanged even when operational logs or audit observations record the duplicate attempt.

Examples:

- In functional programming, the Y combinator is a fixed-point combinator. For a function $F$, it produces a fixed point $Y(F)$ satisfying $F(Y(F)) = Y(F)$, allowing a recursive function to be expressed without referring to itself by name.
- The declarative meaning of a positive Datalog program is the least fixed point of its immediate-consequence operator; see [[Relational and Logic Programming|relational and logic programming]].
- A feedback or control system is at a fixed point when another modeled observation-decision-update cycle leaves its relevant state unchanged. Stability, convergence, and sensitivity remain separate questions; see [[Trace and Feedback|trace and feedback]].

Related concepts: [[Recursion|recursion]], [[Idempotency|idempotency]], [[Behavior|behavior]], [[State Machines|state machines]], [[Relational and Logic Programming|relational and logic programming]], [[Trace and Feedback|trace and feedback]], [[Equivalence vs Equality|equivalence vs equality]], [[Enrichment and Order|enrichment and order]].
