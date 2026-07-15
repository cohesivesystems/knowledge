---
realm: Principles
kind: reference
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Programming Paradigm
---

# Programming Paradigms

Programming paradigms are recurring ways of interpreting and organizing computation. They select which structures are primary, which composition laws matter, and which operational details are left to a language, compiler, runtime, or other [[Realization|realization]].

Paradigms overlap. A language, program, or system can be functional in its value transformations, relational in its queries, state-machine-based at an entity boundary, actor-oriented in its runtime organization, and process-oriented across a long-running workflow.

## Paradigm Views

| Paradigm view | Primary structure | Characteristic questions |
| --- | --- | --- |
| [[Functional Programming|functional programming]] | values, functions, composition, evaluation, explicit effects | What value does this expression denote, and how do computations compose? |
| [[Relational and Logic Programming|relational and logic programming]] | facts, relations, constraints, proofs, queries, search | Which tuples or substitutions satisfy the relation, and how are answers found? |
| imperative programming | commands, stores, sequencing, mutation | Which command changes which state, and in what order? |
| object-oriented programming | identity-bearing objects, encapsulation, dispatch | Which object interprets the operation, and what state or behavior does it own? |
| [[State Machines|state-machine modeling]] | states, inputs, transitions, outputs, runs | Which transitions are admissible from the current state? |
| dataflow and reactive programming | dependencies, signals, events, time-varying values | How does change propagate through a dependency graph? |
| concurrent and actor-oriented programming | participants, messages, local state, scheduling | Which occurrences are independent, and how is reception or execution ordered? |
| [[Process Theories|process-oriented programming]] | interfaces, interactions, composition, feedback, traces | How does work unfold and compose across participants and time? |

This table names interpretive centers, not exclusive language categories. For example, an actor handler can be a pure function from current state and input to a new state and effects. A relational query engine can use imperative indexes and a functional expression tree. A workflow can be compiled into state machines and executed by an actor runtime.

## Denotation, Control, and Realization

A paradigm can separate what a program means from how it is evaluated:

- Functional denotation can be separated from strict, lazy, parallel, or effectful evaluation.
- Relational denotation can be separated from depth-first, breadth-first, interleaved, indexed, or fixed-point search.
- A state-machine specification can be separated from actor, database, workflow, or replicated-log execution.
- A process theory can be separated from orchestration, choreography, scheduling, and durable execution mechanisms.

[[Nondeterminism and Choice|Nondeterminism]] appears differently in each view: as a multi-valued computation, a relation with several answers, an enabled-transition set, a scheduler choice, a message reception order, or a process branch. [[Reduction, Evaluation, and Confluence|Confluence]] asks when those different execution paths remain coherent.

## Cohesive Use

The Cohesive System Model should use paradigm terminology to expose structure, not to classify systems by branding. A paradigm note should state:

- Which semantic objects are primary.
- Which composition and equivalence laws apply.
- Which forms of state, time, effects, and nondeterminism are represented.
- Which evaluation or search strategy is separate from the denotation.
- Which runtime mechanisms realize the paradigm without defining its meaning.
- How the paradigm maps into domain semantics, system graph, operational concerns, and realization substrate.

## External References

- Peter Van Roy, [Programming Paradigms for Dummies: What Every Programmer Should Know](https://webperso.info.ucl.ac.be/~pvr/VanRoyChapter.pdf), in *New Computational Paradigms for Computer Music*, 2009.

Related concepts: [[Functional Programming|functional programming]], [[Relational and Logic Programming|relational and logic programming]], [[State Machines|state machines]], [[Process Theories|process theories]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Compositionality|compositionality]], [[System Language and Realization|system language and realization]], [[Behavior|behavior]], [[Process|process]], [[Actor Model|actor model]], [[Actor Systems|actor systems]], [[Runtimes|runtimes]], [[Realization|realization]].
