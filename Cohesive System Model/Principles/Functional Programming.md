---
realm: Principles
kind: discipline
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Functional Paradigm
---

# Functional Programming

Functional programming describes computation primarily through values, functions, composition, and evaluation rather than through a distinguished sequence of commands that mutate shared state.

It is one family within [[Programming Paradigms|programming paradigms]], not a claim that every program is pure, total, terminating, or implemented by direct lambda-calculus reduction.

## Core Structure

Functional models commonly emphasize:

- Functions as values that can be passed, returned, and composed.
- Referential transparency for expressions whose meaning does not depend on hidden mutable context.
- Immutable values and persistent data structures.
- Algebraic data types, pattern matching, and structural decomposition.
- [[Recursion]], folds, unfolds, and [[Fixed Points|fixed-point]] definitions.
- Parametric polymorphism and type-directed composition.
- Explicit representation of context and effects.

Pure functions are deterministic only when their inputs and semantic operations are deterministic. A function can return a relation, list, set, probability distribution, process description, or effectful computation that represents [[Nondeterminism and Choice|nondeterminism and choice]]. Functional programming therefore does not imply single-valued execution at every level.

## Evaluation and Confluence

The lambda calculus supplies a foundational model of function application and substitution. Its pure beta-reduction relation is confluent, but different [[Reduction, Evaluation, and Confluence|evaluation strategies]] can have different termination and cost behavior.

Call-by-value, call-by-name, call-by-need, strict evaluation, lazy evaluation, parallel evaluation, and compiler normalization are realization or language-semantic choices over related functional structure. They should not be treated as interchangeable when effects, divergence, resource usage, or observation timing matter.

## Effects

Functional programs interact with state, errors, asynchronous operations, persistence, nondeterminism, probability, and I/O through several disciplines:

- Explicit state threading.
- [[Monads Monoids and Duals|Monads]] and applicative structures.
- Algebraic effects and handlers.
- Arrows, streams, continuations, and effect systems.
- Process descriptions interpreted by runtimes.

The purpose is not merely syntactic purity. Explicit effect structure lets a model state which operations sequence, commute, retry, fail, branch, or cross a [[Boundaries|boundary]]. A monadic interface gives composition laws, but each effect still needs its own semantic and operational guarantees.

## Functions and Relations

[[Relational and Logic Programming|Relational and logic programming]] generalizes beyond a distinguished input-output direction. A mathematical function is a total, single-valued relation; a general relation may be partial, multi-valued, or queried in several modes.

Functional and relational programming therefore overlap without collapsing:

- A functional program may compute collections of relational answers.
- A relation may be implemented by functions specialized to query modes.
- A logic program may use functional terms and deterministic subcomputations.
- A typed functional language may host relational query expressions and lower them through compiler-like [[Realization|realization]].

## Reactive and Process Interpretation

[[Behavior|Behavior]] as a time-varying value and [[Event|events]] as occurrences provide a functional-reactive interpretation of evolving systems. [[State Machines|State machines]] and [[Process Theories|process theories]] add transition, interaction, concurrency, and recovery structure that a pure value-level account does not supply by itself.

A functional program can describe a process, but the semantic [[Process|process]] remains distinct from the runtime task, thread, actor, workflow activation, or scheduler step that realizes it.

## Modeling Checks

- Which functions are pure, partial, multi-valued, effectful, or non-terminating?
- Which evaluation strategy is semantically observable?
- What equality or equivalence is preserved by refactoring and optimization?
- Which effects sequence, commute, or form confluent paths?
- Does a list denote ordered results, a search trace, or merely an implementation of a set-valued relation?
- Which runtime and scheduling assumptions are outside the functional denotation?

## External References

- John Hughes, [Why Functional Programming Matters](https://doi.org/10.1093/comjnl/32.2.98), *The Computer Journal* 32(2):98-107, 1989.
- Gordon D. Plotkin, [Call-by-Name, Call-by-Value and the Lambda-Calculus](https://doi.org/10.1016/0304-3975(75)90017-1), *Theoretical Computer Science* 1(2):125-159, 1975.

Related concepts: [[Programming Paradigms|programming paradigms]], [[Relational and Logic Programming|relational and logic programming]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Compositionality|compositionality]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Monads Monoids and Duals|monads monoids and duals]], [[Algebras and Coalgebras|algebras and coalgebras]], [[Recursion|recursion]], [[Fixed Points|fixed points]], [[Behavior|behavior]], [[Event|event]], [[State Machines|state machines]], [[Process Theories|process theories]], [[Runtimes|runtimes]], [[Scheduling|scheduling]], [[Realization|realization]].
