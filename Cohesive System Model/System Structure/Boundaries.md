---
realm: System Structure
kind: structural-construct
---

# Boundaries

Boundaries define the scope and context in which observation, interpretation, authority, failure, persistence, delivery, and coordination apply.

At the structure level, boundaries describe semantic and operational scoping in the system graph, not a specific process, network, storage, or deployment mechanism.

Scope answers what is included, excluded, owned, visible, controlled, or guaranteed. Context answers which meanings, policies, identities, versions, capabilities, assumptions, and authorities apply inside that scope.

As a modeling discipline, a boundary should be treated as a kind of [[Universal Constructions|universal construction]] only when its scope and context are determined by the relevant inclusions, exclusions, authorities, guarantees, and interaction edges.

Interpretation is performed by an [[Observer]] relative to a boundary. An observer interprets [[Value|values]], [[Observation|observations]], [[Event|events]], [[Command|commands]], and [[Query|queries]] within the scope and context defined by that boundary.

An observer boundary determines whether an event is exogenous, input, endogenous, or output relative to that [[Observer|observer]]. It also frames which state is visible, which policies apply, which authority is available, which effects can be committed, and what command or query interpretation can mean.

Boundary types include:

- **Observer boundaries**: define what an [[Observer]] can see, interpret, authorize, and commit.
- **Entity or aggregate boundaries**: define the subject whose state, invariants, transitions, and version history are controlled together.
- **Transaction boundaries**: define which reads and writes commit or roll back atomically.
- **Process or workflow boundaries**: define the scope of a long-running behavior, its durable progress, retries, compensations, and recovery.
- **Service boundaries**: define an independently deployed or operated capability with its own API, policies, dependencies, and failure modes.
- **Protocol and broker boundaries**: define delivery, ordering, acknowledgment, retries, and message ownership for an interaction substrate.
- **Failure boundaries**: define what can fail, restart, partition, or recover independently.
- **Persistence boundaries**: define what is durably recorded and treated as recoverable truth.

Guarantees are meaningful only when their boundary is explicit. At-most-once delivery, ordering, acknowledgment, durability, and commitment can all refer to different boundaries.

## Example

Consider a Kafka consumer that updates an entity in a database and writes an outbox record:

```txt
Kafka topic -> consumer service -> database transaction -> outbox -> downstream broker
```

Different guarantees apply at different boundaries:

- At-most-once delivery may describe the broker/consumer boundary: once the consumer acknowledges or advances its offset, the broker may not redeliver the message even if processing later fails.
- Ordering may be described with respect to the Kafka partition boundary. It does not imply global ordering or ordering across unrelated entity IDs.
- Acknowledgment takes place at the broker protocol boundary. Committing an offset means the consumer accepted responsibility for the message, not necessarily that the domain transition committed.
- Durability may describe Kafka log retention, database state durability, or outbox durability. These are separate persistence boundaries with different replication, retention, compaction, backup, and recovery policies.
- Commitment may correspond to the entity or aggregate boundary. The business transition commits only when the entity accepts the command, records the new state or event, and advances the version.

So a system can acknowledge a message and preserve broker ordering while still failing to commit the domain transition. It can also receive the same message more than once while committing the domain transition only once through idempotency and concurrency control.

Related concepts: [[Observer]], [[Value]], [[Observation]], [[State]], [[Event]], [[Command]], [[Query]], [[Universal Constructions]], [[Interaction]], [[Delivery Semantics]], [[Coordination]], [[Recovery]].
