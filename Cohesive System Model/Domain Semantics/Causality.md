---
realm: Domain Semantics
kind: semantic-construct
created: 2026-07-15
updated: 2026-07-15
status: draft
aliases:
  - Causal Relation
  - Causal Dependency
---

# Causality

Causality is a dependency [[Relation|relation]] between events, observations, transitions, decisions, or effects in which one occurrence may have influenced, enabled, required, constrained, or carried information into another.

Causality belongs to the meaning of the occurrences being related. [[Ordering]] supplies mathematical structures that can represent causal dependencies, but an order is not causal merely because it compares two positions.

Examples of causal edges include:

- A message transmission enabling its reception.
- An [[Observation|observation]] contributing evidence to a later decision.
- A command interpretation producing an accepted [[Transition|transition]].
- A committed event enabling a projection update or downstream effect.
- One process step creating the precondition for another.
- A version being derived from a predecessor version.

## Causality and Happened-Before

[[Happened-Before|Happened-before]] records potential causal influence through program order, message transmission and reception, and transitive closure. If `A` happened before `B`, information from `A` could have influenced `B`. The relation does not prove that `A` was the semantic reason for `B`.

Actual causal explanation may require additional evidence: which observation was read, which rule fired, which authority endorsed the decision, which transition consumed the input, or which derivation path produced the result. Provenance therefore refines an order edge into an explanation.

Wall-clock precedence is not enough. `A` can occur earlier than `B` without influencing it. A total order imposed by a log, scheduler, or sequencer can also compare independent work while introducing no new semantic dependency between the operations.

## Concurrency and Independence

Two occurrences are concurrent relative to a causal relation when neither causally precedes the other. Causal incomparability does not by itself prove semantic independence. The occurrences may still contend for the same invariant, authority, resource, or effect boundary.

Independence is stronger: the operations can be varied, reordered, or composed without changing the relevant outcome or invalidating a constraint. [[Reduction, Evaluation, and Confluence|Commutativity and confluence]] provide ways to show that causal-order alternatives are observationally harmless.

## Causal Closure

A view is causally closed when it includes the prerequisites of every occurrence it includes. [[Consistent Cuts|Consistent cuts]] use this requirement to define coherent snapshots over distributed histories. Causal consistency similarly prevents an observer from seeing an effect while omitting a cause required by the chosen causal relation.

## Modeling Checks

- What occurrences are related, and what kind of influence does the edge mean?
- Is the relation actual causation, potential influence, dependency, derivation, or merely order?
- Which observer and boundary determine the relation?
- Which edges arise from program order, communication, transition acceptance, or explicit evidence?
- Are incomparable occurrences actually independent, or do they share an invariant or authority boundary?
- Which observations require causal closure?
- What provenance is needed to explain rather than merely order the result?

## External References

- Leslie Lamport, [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf), *Communications of the ACM* 21(7):558-565, 1978.

Related concepts: [[Relation|relation]], [[Event|event]], [[Observation|observation]], [[Transition|transition]], [[Effects|effects]], [[Behavior|behavior]], [[Process|process]], [[Happened-Before|happened-before]], [[Ordering|ordering]], [[Consistent Cuts|consistent cuts]], [[Version Histories|version histories]], [[Consistency Models|consistency models]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Observer|observer]], [[Authority|authority]], [[Boundaries|boundaries]].
