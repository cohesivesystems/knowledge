---
realm: Realization Substrate
kind: realization-substrate
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - TLA Plus
---

# TLA+

TLA+ is a formal specification language and tool ecosystem for describing and analyzing concurrent and distributed systems. It provides a concrete realization substrate for selected [[Temporal Logic|temporal-logic]] and [[State Machines|state-machine]] models; it is not the semantic notion of temporal logic itself and is not a production execution runtime.

TLA+ combines the Temporal Logic of Actions with mathematical definitions based on set theory and first-order logic. A specification commonly separates:

- An initial-state predicate `Init` over declared variables.
- A next-state relation `Next` composed from actions over current and primed next-state variables.
- A behavior specification such as `Init /\ [][Next]_vars`, including admitted stuttering steps.
- Safety properties such as type-correctness predicates and invariants.
- Liveness properties and weak or strong fairness assumptions where progress depends on eligible actions eventually occurring.

Modules, operators, constants, variables, sets, functions, records, tuples, sequences, and quantification support abstraction over a system's relevant state. PlusCal provides an algorithm-oriented notation that translates into TLA+; the translated TLA+ specification remains the analysis target.

## Tooling and Evidence

The TLA+ ecosystem includes several distinct mechanisms:

- **TLC** explores reachable states for a configured, bounded model and checks invariants, deadlock conditions, action properties, and supported temporal properties. A successful run establishes no counterexample within the explored model and tool assumptions; it is not automatically a proof for all parameter sizes or an implementation.
- **TLAPS** supports deductive proofs of TLA+ obligations. A proof establishes the stated theorem from definitions, assumptions, and the trusted proof stack; it does not establish that deployed code refines the specification.
- **PlusCal** translates imperative- or algorithm-shaped descriptions into TLA+, making control state and atomic actions explicit for analysis.

Simulation, model checking, and proof provide different evidence. Each result supports a [[Judgement|judgement]] scoped to the specification, model configuration, property, tool, and assumptions actually checked; it does not silently judge implementation conformance or a larger parameter space. Each specification must name its abstraction boundary, environmental actions, failure assumptions, fairness assumptions, and the state or history omitted from the model.

## Realization Boundary

TLA+ can realize an analyzable specification of system behavior. It does not by itself:

- Execute the production process, protocol, state machine, or infrastructure.
- Prove that source code, configuration, storage, networks, or operators implement the specification.
- Convert a domain [[Invariant|invariant]] into a system guarantee without a traceable encoding and implementation correspondence.
- Supply the [[Fairness|fairness]], timing, durability, delivery, or failure assumptions used by a liveness claim.
- Turn one bounded TLC result into an unbounded theorem.

Compiler-like [[Realization|realization]] therefore needs an explicit correspondence from Cohesive concepts and system-graph structure into TLA+ variables, actions, behaviors, and properties, followed by a separate correspondence from that specification to the implementation. Refinement mappings, conformance checks, generated specifications, implementation-derived models, and trace validation can strengthen this chain, but their boundaries and trusted assumptions must remain visible.

## Cohesive Mapping

A public mapping may relate:

- [[State|State]] and system-graph projections to TLA+ variables and values.
- [[Transition|Transitions]], commands, events, and environmental moves to TLA+ actions.
- [[State Machines|State-machine]] initial conditions and transition relations to `Init` and `Next`.
- [[Invariant|Invariants]] and [[Safety and Liveness|safety properties]] to state or action predicates over all admitted behaviors.
- Process progress and protocol completion to liveness formulas under explicit [[Fairness|fairness]] and failure assumptions.
- Abstraction boundaries to hidden variables, stuttering steps, and refinement mappings.

These are correspondence choices, not identities. A TLA+ variable may combine several graph roles for analysis, while one semantic role may require several variables or history structures. The mapping should record which distinctions it preserves and which it intentionally abstracts away.

## Formal relations

- `may_realize`: [[Temporal Logic]] — Provides a concrete language and analysis toolchain for action-based temporal specifications, bounded model checking, and deductive proof without defining the broader family of temporal logics.
- `may_realize`: [[State Machines]] — Encodes initial states, next-state actions, stuttering, and behavior properties for analysis without asserting that a production runtime conforms to the encoded machine.

## External References

- Leslie Lamport, [Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers](https://lamport.azurewebsites.net/tla/book.html), Addison-Wesley, 2002.
- [TLA+ project](https://lamport.azurewebsites.net/tla/tla.html).
- [TLA+ tools](https://github.com/tlaplus/tlaplus).

Related concepts: [[Temporal Logic|temporal logic]], [[Logic|logic]], [[Judgement|judgement]], [[State Machines|state machines]], [[State|state]], [[Transition|transition]], [[Behavior|behavior]], [[Invariant|invariants]], [[Safety and Liveness|safety and liveness]], [[Fairness|fairness]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Failure Models|failure models]], [[System Language and Realization|system language and realization]], [[Realization|realization]].
