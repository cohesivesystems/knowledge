---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-07-14
---

# Recursion

Recursion defines a value, structure, or behavior in terms of other instances of the same form. The recursive reference may point to a smaller component, a prior step, a nested process, or another derivation of the same relation.

A recursive definition needs a base or boundary condition, a well-founded reduction, or semantics that determines which solutions are admissible. Self-reference alone can be ambiguous, non-terminating, or unproductive.

## What Recursion Can Express

Common uses of recursion include:

- Repeated computation, including many programming-language loops, by defining each iteration from the state produced by the preceding one and stopping at a boundary condition.
- Sequences and recurrence relations, such as factorials, Fibonacci numbers, accumulated totals, and iterative approximations.
- Inductive or nested data, such as lists, trees, syntax trees, directory hierarchies, and documents containing sub-documents.
- Traversals and divide-and-conquer algorithms that solve a problem by applying the same rule to smaller components.
- Recursive grammars and parsers for nested expressions, blocks, and other syntactic forms.
- Graph reachability, dependency closure, hierarchy traversal, and recursive relational derivation.
- Time-varying [[Behavior|behaviors]] and [[State Machines|state machines]] in which each value or state is defined from prior state and new input: $b_{t+1} = F(b_t, i_{t+1})$.
- Nested or repeated [[Process|processes]] in which a process contains, initiates, or advances another process of the same general form.
- Event-history folds that rebuild [[Projection Models|projections]] by applying the same update rule to each successive event.
- Potentially unbounded structures such as lazy streams, where each observation supplies a value and a recursive description of what follows.

These are recursive descriptions. Their realizations may use recursive calls, but they may instead use loops, stacks, queues, folds, schedulers, workflow steps, or other execution mechanisms.

## Recursive Structure and Derivation

Recursion can describe structure without prescribing recursive function calls as its realization:

- A [[Projection Models|projection]] can be rebuilt by folding an ordered source-event history from an initial state with the same update function used for incremental maintenance. This fold is recursive over the history. Agreement between rebuilt and incrementally maintained state is a correctness or equivalence condition, not by itself a [[Fixed Points|fixed point]].
- A [[Process Graphs|process graph]] has recursive structure when a process contains or initiates sub-processes that can themselves contain or initiate further sub-processes. Observer structure recurs similarly when one [[Observer|observer]] routes to another observer that may route onward. This graph composition does not by itself prescribe recursive calls, workflow-engine nesting, or operating-system processes as its realization.
- A recursive Datalog rule derives instances of a relation from prior instances of that relation, as in transitive reachability; see [[Relational and Logic Programming|relational and logic programming]].

## Recursion, Iteration, and Feedback

Recursion is a way of defining a value, structure, or behavior in terms of other instances of the same form. It does not require a particular execution mechanism. A realization may use function calls, loops, folds, queues, workflow steps, or message passing. [[Trace and Feedback|Feedback]] instead describes outputs becoming future inputs, while iteration describes repeated execution. A retry loop may involve all three, but repetition alone does not make it recursive.

Recursion and [[Fixed Points|fixed points]] meet when a recursive equation $X = F(X)$ is interpreted by choosing a fixed point of $F$. Not every recursive definition has a unique fixed point, and not every recursively generated behavior stabilizes: it may terminate, continue indefinitely, oscillate, or diverge.

Related concepts: [[Fixed Points|fixed points]], [[Behavior|behavior]], [[Process|process]], [[Process Graphs|process graphs]], [[Projection Models|projection models]], [[Observer|observer]], [[Relational and Logic Programming|relational and logic programming]], [[Trace and Feedback|trace and feedback]], [[Compositionality|compositionality]].
