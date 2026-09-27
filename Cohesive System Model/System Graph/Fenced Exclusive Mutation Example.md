---
realm: System Graph
kind: example
created: 2026-09-27
updated: 2026-09-27
status: draft
aliases:
  - FencedExclusiveMutation
  - Fenced Serialized Execution Example
  - Lock versus Actor Example
---

# Fenced Exclusive Mutation Example

This bounded example traces one architectural property from an application requirement through candidate infrastructure constructions, conformance evidence, and runtime assurance. It is an ontology driver rather than a universal coordination recipe.

## Required Property

Suppose order transitions require:

```text
FencedExclusiveMutation(
  subject: Order,
  scope: OrderId,
  staleAuthority: Reject,
  failureModel: declared,
  boundary: authoritative commit)
```

The property requires that at most one currently authorized participant can commit a mutation for an order identity and that a participant whose authority has been superseded cannot commit through the authoritative boundary. It is stronger than mutual exclusion in one process and different from delivery ordering, durable admission, effect idempotency, or eventual recovery.

The application expresses a requirement for this property through a [[Contract Models|contract model]]. It does not require a distributed lock, actor runtime, database product, or other named mechanism.

## Lease and Epoch Strategy

A candidate strategy uses:

```text
linearizable lease acquisition
+ monotonically increasing ownership epoch
+ authoritative commit conditioned on the current epoch
+ rejection of stale epochs
=> fenced exclusive mutation
```

Lease expiry alone is insufficient because an old owner can continue after a pause or partition. Correctness depends on the authoritative commit boundary rejecting the old epoch. The lease facility and storage facility therefore participate in a relational construction; neither isolated capability establishes the demanded property.

Residual obligations can include routing each protected mutation through the conditional commit, preserving the epoch across retries, and separately handling external effects that are outside the authoritative transaction.

## Keyed Actor Strategy

Another candidate strategy routes every order mutation through one logical actor identity and serializes admitted turns. This can simplify exclusive execution, but mailbox serialization alone does not prove fenced exclusive mutation.

The construction must additionally establish:

- exclusive or safely transferred activation authority for one `OrderId`;
- complete routing of protected mutations through that authority;
- stale-activation rejection at the authoritative commit boundary;
- declared behavior during partitions, failover, and duplicate activation; and
- persistence and recovery rules for accepted work when those properties are separately required.

Durable admission, FIFO ordering, response completion, and idempotent external effects remain distinct properties unless an explicit strategy derives them.

## Rejected Candidate

A process-local mutex or an expiring distributed lock without storage-enforced fencing is structurally usable and may reduce concurrent work, but it does not satisfy the requirement. A paused holder can resume after replacement and commit stale work. The correct compiler result is a rejected candidate with the missing stale-authority exclusion obligation, not a weaker success classification.

## Evidence Chain

An attributable realization records:

```text
property definition and application requirement
  -> selected strategy theorem
  -> exact facility and configuration premises
  -> application and binding obligations
  -> selected physical realization
  -> implementation conformance evidence
  -> deployment attestation
  -> runtime observations
  -> time-indexed assurance assessment
```

A [[Proof Assistants|proof assistant]] may verify the conditional strategy theorem. Provider documentation or tests may support lease and conditional-write capability claims. Configuration and deployment attestations may show that the selected modes are active. [[Implementation Conformance|Implementation conformance]] must cover mutation routes, epoch propagation, and stale-write rejection. [[Assurance and Evidence|Runtime assurance]] evaluates whether sufficiently fresh evidence still supports the premises.

These forms of evidence do not substitute for one another.

## Counterexample and Incomplete Evidence

The example should exercise two different negative results:

1. A stale owner successfully commits after its epoch was superseded. This is a finite counterexample that **refutes** fenced exclusive mutation for the affected realization and boundary.
2. Telemetry omits epoch values or cannot observe one mutation route. The history cannot establish or refute stale-owner exclusion, so the assessment is **unknown** rather than successful.

The distinction tests whether the assurance model preserves the logical strength and coverage of its evidence.

## Modeling Checks

- Is the protected subject and identity scope explicit?
- Where is current mutation authority decided and enforced?
- Can a stale participant reach any unfenced commit path?
- Which properties come from the facility, strategy, application, and binding?
- Are ordering, admission durability, recovery, and effect idempotency modeled separately?
- What evidence establishes each strategy premise and conformance boundary?
- Which observations can produce a counterexample, and which missing observations leave the result unknown?

## Formal relations

- `corresponds_to`: [[Infrastructure Graph]] — Instantiates the requirement, strategy, facility, physical-realization, and assurance views for one bounded coordination property.
- `corresponds_to`: [[Contract Models]] — Demonstrates how a parameterized requirement remains distinct from its candidate mechanisms, evidence, and residual obligations.
