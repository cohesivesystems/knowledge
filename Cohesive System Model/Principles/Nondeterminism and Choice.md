---
realm: Principles
kind: principle
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Non-determinism and Choice
  - Computational Nondeterminism
  - Unbounded Nondeterminism
---

# Nondeterminism and Choice

Nondeterminism describes a model in which one context admits more than one possible continuation. Choice describes how, where, or by whom that multiplicity is resolved.

A deterministic step is a function:

```txt
step : Context -> Outcome
```

A nondeterministic step is more generally a relation or set-valued function:

```txt
step : Context -> Set<Outcome>
```

This distinction is model-relative. A lower-level deterministic system can appear nondeterministic when hidden state, scheduling, physical detail, or environmental input is abstracted away. Conversely, a specification can intentionally leave several implementations or outcomes admissible even when a realization eventually selects one deterministically.

## Sources of Nondeterminism

- **Semantic nondeterminism**: the domain permits several valid outcomes.
- **Underspecification**: an abstract model leaves a decision to later refinement or [[Realization|realization]].
- **External nondeterminism**: an environment or exogenous [[Event|event]] determines which continuation is available.
- **Internal choice**: a component, [[Policy|policy]], or authorized [[Observer|observer]] selects among alternatives.
- **Concurrency and scheduling nondeterminism**: independent occurrences can be selected, ordered, observed, or committed differently.
- **Failure nondeterminism**: delay, loss, duplication, crash, partition, retry, and recovery admit alternative executions.
- **Probabilistic nondeterminism**: outcomes are assigned a probability measure rather than represented only as an unweighted set.
- **Accidental realization nondeterminism**: a race, unstable iteration order, hidden shared state, or other substrate detail introduces behavior not licensed by the semantic model.

Not every operational difference is semantically nondeterministic. If two schedules commute, converge, or remain observationally equivalent at the declared [[Boundaries|boundary]], their internal difference may be intentionally hidden.

## Computational Representations

In programming-language semantics, a nondeterministic computation can be represented by a type constructor or monad `M`:

```txt
pure : A -> M A
bind : M A -> (A -> M B) -> M B
```

Different choices of `M` preserve different distinctions:

| Structure | Interpretation |
| --- | --- |
| `Maybe<A>` | zero or one result; partiality or failure rather than general nondeterminism |
| `List<A>` | an ordered enumeration of zero or more results, preserving duplicate answers |
| `Set<A>` or a powerset | extensional possibilities with order and multiplicity forgotten |
| `Multiset<A>` | alternatives with multiplicity but without presentation order |
| a distribution monad | discrete probabilistic branching |
| the Giry monad | probability measures over measurable spaces; Kleisli arrows act as probability kernels |
| a lazy stream or logic monad | potentially infinite search with an explicit enumeration and fairness strategy |
| a free choice effect | unresolved choice syntax interpreted later by a handler |

For a list, `[]` represents no answer, `[a]` one answer, and `[a,b]` two enumerated answers. List bind uses concatenation and therefore exposes search order and multiplicity. A list is not an extensional set: `[a,b]` differs from `[b,a]`, and `[a,a]` differs from `[a]`.

This matters for [[Relational and Logic Programming|relational and logic programming]]. A relation or set of satisfying substitutions can provide the denotation, while a list or stream provides an operational enumeration of answers. The enumeration additionally carries search order, duplicate proofs, fairness, and termination behavior.

Probability and ordinary nondeterminism should also remain distinct. A set states which outcomes are possible. A probability measure assigns quantitative mass. Systems such as Markov decision processes combine policy- or environment-resolved nondeterminism with probabilistic state transitions; their semantics must state how those two forms of branching interact.

## Choice Algebra

A computation with choice often provides:

```txt
failure : M A
choice  : M A x M A -> M A
```

The laws of `choice` determine what the model remembers:

- **Associativity** says grouping alternatives does not matter.
- **Commutativity** says presentation order does not matter.
- **Idempotence** says offering the same alternative twice adds nothing.
- **Identity** says choosing against failure changes nothing.

List append is associative with an identity, but it is not commutative or idempotent. Set union satisfies all four laws. Multiset union is associative and commutative but not idempotent. Monad associativity says that sequencing can be rebracketed coherently; it does not imply that independent computations commute or that divergent evaluation paths are confluent.

## Choice Ownership

A choice point should state who or what resolves it:

- **External choice** is resolved by an input or interaction with the environment.
- **Internal choice** is resolved by the process or component.
- **Policy choice** is resolved by a declared decision rule.
- **Authority choice** is resolved by a role whose decision is accepted as counting.
- **Joint choice** is resolved through negotiation, voting, [[Consensus|consensus]], or another protocol.
- **Randomized choice** is resolved by a probability mechanism.
- **Scheduler choice** selects among enabled occurrences in an execution.
- **Unresolved choice** remains abstract for a later refinement.

Angelic and demonic nondeterminism describe reasoning interpretations rather than physical sources of choice. Angelic reasoning asks whether some permitted branch succeeds. Demonic reasoning requires a guarantee to hold across every permitted branch. [[Safety and Liveness|Safety]] properties normally quantify over all admissible branches; progress properties additionally depend on [[Fairness|fairness]].

## Uncertainty

Nondeterminism and [[Uncertainty|uncertainty]] both use sets of possibilities but describe different multiplicities:

- Nondeterminism is multiplicity in what may happen next.
- Uncertainty is multiplicity in which current or prior state an observer considers possible.

For state space `S`, a nondeterministic transition has the form `S -> Set<S>`, while an observer's information state is a subset of `S`. An unobserved nondeterministic transition can enlarge uncertainty. A later [[Observation|observation]] can restrict the possible-state set without changing the transition relation itself.

A probability distribution can likewise represent either stochastic behavior in the system or an observer's degree of belief about hidden state. The representation alone does not determine whether the probability is aleatory or epistemic; the model must state its interpretation and boundary.

## Actor Reception-Order Indeterminacy

The [[Actor Model|actor model]] literature uses **reception-order indeterminacy** for the fact that concurrently sent messages do not determine one global next state or one universal arrival order. Local transport, runtime [[Arbitration|arbitration]], and [[Scheduling|scheduling]] establish the order in which a receiving actor interprets messages, and different reception orders can affect future behavior.

This is still representable as a family of possible behaviors, but its source is distributed order formation rather than an explicit choice expression in one global state machine. [[Actor Systems|Actor systems]] can reduce the observable impact of this indeterminacy when handlers commute, are quasi-commutative, or form confluent paths. When order remains semantically visible, the model needs explicit ordering, concurrency control, consensus, conflict representation, or domain-level acceptance of several outcomes.

## Fairness and Unbounded Nondeterminism

[[Scheduling]] resolves enabled work one occurrence at a time. [[Fairness]] constrains complete schedules by excluding indefinite postponement under stated assumptions. A fair service may guarantee eventual response without supplying a finite response bound.

König's lemma exposes the semantic issue. A finitely branching tree with arbitrarily long finite branches has an infinite branch. Therefore, if an ordinary finitely branching computation tree contains every execution prefix and every branch terminates, the whole tree is finite and has a uniform depth bound.

Unbounded nondeterminism permits every finite delay while excluding the infinite starvation path as unfair:

```txt
go^0 ; stop
go^1 ; stop
go^2 ; stop
...
go^n ; stop

go^infinity      -- excluded by the fairness condition
```

Fairness is therefore a property of admissible complete executions, not something determined by a finite prefix alone. Claims about unbounded nondeterminism concern interactive or relational behavior under fairness assumptions; they should not be silently restated as claims about computing a new ordinary single-valued function.

## Confluence and Consistency

[[Reduction, Evaluation, and Confluence|Confluence]] asks whether different permitted paths can later join. [[Consistency Models|Consistency models]] ask whether the histories exposed to observers are legal. These are related but distinct:

- A confluent computation may hide schedule differences by reaching one normal form or observational equivalence class.
- A non-confluent computation can still be correct when the specification admits several outcomes.
- A consistency model may allow several histories while constraining real-time, program-order, causal, session, or convergence relationships among them.
- [[Consensus]] can reduce distributed multiplicity to one agreed value or log position, while [[Authority|authority]] explains why that decision counts for the governed boundary.

A realization may narrow permitted nondeterminism through refinement, but it must not introduce outcomes forbidden by the abstract model or rely on a fairness, probability, or ordering assumption that the model did not declare.

## Modeling Checks

- What are the possible continuations from this context?
- Is the multiplicity semantic, environmental, epistemic, probabilistic, scheduled, or accidental?
- Who or what resolves the choice?
- Which algebraic distinctions among alternatives matter?
- Which observers can distinguish the resulting paths?
- Does correctness quantify over every branch, some branch, or fair branches?
- Must the decision be recorded for replay, audit, or recovery?
- Do different paths commute, converge, or remain observably different?
- Which choices may a realization remove, and which new choices would violate refinement?

## External References

- Eugenio Moggi, [Notions of Computation and Monads](https://doi.org/10.1016/0890-5401(91)90052-4), *Information and Computation* 93(1):55-92, 1991.
- Michèle Giry, [A Categorical Approach to Probability Theory](https://doi.org/10.1007/BFb0079007), in *Categorical Aspects of Topology and Analysis*, 1982.
- Carl Hewitt, [Actor Model of Computation: Scalable Robust Information Systems](https://arxiv.org/abs/1008.1459), 2010.
- Nissim Francez, [Fairness](https://doi.org/10.1007/978-1-4612-4886-6), Springer, 1986.

Related concepts: [[Programming Paradigms|programming paradigms]], [[Functional Programming|functional programming]], [[Relational and Logic Programming|relational and logic programming]], [[Monads Monoids and Duals|monads monoids and duals]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[State Machines|state machines]], [[Process Theories|process theories]], [[Uncertainty|uncertainty]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Glitch Principle|glitch principle]], [[Authority|authority]], [[Causality|causality]], [[Ordering|ordering]], [[Consistency Models|consistency models]], [[Consensus|consensus]], [[Actor Systems|actor systems]], [[Observer|observer]], [[Observation|observation]], [[Boundaries|boundaries]], [[Realization|realization]].
