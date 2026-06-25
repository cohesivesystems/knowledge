---
realm: Architecture Practices
---

# Actor Model

The Actor Model addresses the problem of organizing concurrent computation around isolated, addressable participants that communicate by message passing.

## Cohesive Formulation

In Cohesive terms, actors are a realization pattern for addressable [[Observer|observers]]. An actor address gives other observers a delivery path to a receiving observer boundary.

Actors can also realize entities when actor identity aligns with entity identity and the actor hosts that entity's transition boundary.

## Practice Interpretation

The practice is useful when correctness depends on serializing interpretation and commit for a subject. A mailbox turn can align observer, state access, transition interpretation, and commit.

## Failure Modes

Actor serialization only proves transition correctness when the actor owns the transition boundary. A router, cache, shard, or forwarding actor may be addressable without being the semantic owner of the entity transition.

Related concepts: [[Actor Systems]], [[Observer]], [[Entity]], [[Identity]], [[Interaction]], [[Concurrency Control]], [[Delivery Semantics]], [[Realization]].
