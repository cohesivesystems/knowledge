---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-08-08
aliases:
  - Actor System
---

# Actor Model

The actor model addresses the problem of organizing concurrent computation around isolated, addressable participants that communicate by message passing.

## Cohesive Formulation

In Cohesive terms, actors are a realization pattern for addressable [[Observer|observers]]. An actor address gives other observers a delivery path to a receiving observer boundary.

Actors can also realize entities when actor identity aligns with entity identity and the actor hosts that entity's transition boundary.

Concurrent sends introduce reception-order [[Nondeterminism and Choice|indeterminacy]]: local transport, [[Arbitration|arbitration]], and [[Scheduling|scheduling]] determine which message is interpreted next. The architecture is least sensitive to that order when handlers commute or form [[Reduction, Evaluation, and Confluence|confluent]] paths. [[Fairness]] and delivery guarantees remain explicit runtime and protocol obligations.

## In the Model

The practice is useful when correctness depends on serializing message handling, interpretation, and commit for a subject. An actor mailbox commonly provides this serialization boundary: each turn can align the observer, state access, transition interpretation, and commit.

## Failure Modes

A common failure mode is treating an addressable actor as the authoritative serialization boundary while [[Entity|entity]] transitions can also occur elsewhere. A router, cache, shard, or forwarding actor may serialize its own mailbox turns, but that serialization does not protect transitions that bypass it or commit at another boundary.

## External References

- Carl Hewitt, [Actor Model of Computation: Scalable Robust Information Systems](https://arxiv.org/abs/1008.1459), 2010.

Related concepts: [[Actor Systems|actor systems]], [[Observer|observer]], [[Entity|entity]], [[Identity|identity]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Interaction|interaction]], [[Concurrency Control|concurrency control]], [[Delivery Semantics|delivery semantics]], [[Realization|realization]].

## Formal relations

- `bundles`: [[Actor Systems]] — Adopts actor-system addressing, mailbox, placement, isolation, supervision, and serialized handling as the named realization family for actor roles.
