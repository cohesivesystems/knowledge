---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-08-20
aliases:
  - Actor System
---

# Actor Model

The actor model addresses the problem of organizing concurrent computation around isolated, addressable participants that communicate by message passing.

## Cohesive Formulation

In Cohesive terms, actors are a realization pattern for addressable [[Observer|observers]]. An actor address gives other observers a delivery path to a receiving observer boundary.

Actors and [[Agent|agents]] answer different modeling questions. An agent is a semantic role that selects or initiates action under purposes, policies, and constraints; an actor is an addressable, message-driven execution role. An actor may realize an agent when its observer context and handler preserve that decision-and-action role. Other actors realize routing, projection, entity hosting, or coordination roles without modeled agency.

That address may remain stable across placement and activation changes, but location transparency is not local-remote equivalence. Latency, serialization, capacity, delivery, partitions, failure domains, and administrative boundaries remain explicit through [[Locality|locality]], [[Failure Models|failure models]], and the [[Infrastructure Graph|infrastructure graph]]. The [[Fallacies of Distributed Computing|fallacies of distributed computing]] are a useful check against letting one actor API conceal those properties.

Actors can also realize entities when actor identity aligns with entity identity and the actor hosts that entity's transition boundary.

Concurrent sends introduce reception-order [[Nondeterminism and Choice|indeterminacy]]: local transport, [[Arbitration|arbitration]], and [[Scheduling|scheduling]] determine which message is interpreted next. The architecture is least sensitive to that order when handlers commute or form [[Reduction, Evaluation, and Confluence|confluent]] paths. [[Fairness]] and delivery guarantees remain explicit runtime and protocol obligations.

## In the Model

The practice is useful when correctness depends on serializing message handling, interpretation, and commit for a subject. An actor mailbox commonly provides this serialization boundary: each turn can align the observer, state access, transition interpretation, and commit.

## Failure Modes

A common failure mode is treating an addressable actor as the authoritative serialization boundary while [[Entity|entity]] transitions can also occur elsewhere. A router, cache, shard, or forwarding actor may serialize its own mailbox turns, but that serialization does not protect transitions that bypass it or commit at another boundary.

## External References

- Carl Hewitt, [Actor Model of Computation: Scalable Robust Information Systems](https://arxiv.org/abs/1008.1459), 2010.

## Formal relations

- `bundles`: [[Actor Systems]] — Adopts actor-system addressing, mailbox, placement, isolation, supervision, and serialized handling as the named realization family for actor roles.
- `bundles`: [[Interaction Modes]] — Selects explicit message passing, one-way tell, correlated ask, mailbox mediation, and actor-boundary serialization as a named interaction profile.
- `distinguished_from`: [[Entity]] — An actor is an addressable execution and observation role; it represents a semantic entity only when identity, authority, transition, and commit boundaries deliberately align.
