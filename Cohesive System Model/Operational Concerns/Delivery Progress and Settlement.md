---
realm: Operational Concerns
kind: operational-concern
created: 2026-08-02
updated: 2026-08-02
status: draft
aliases:
  - Channel Progress
  - Delivery Progress
  - Consumer Progress
  - Provider Settlement
  - Message Settlement
---

# Delivery Progress and Settlement

Delivery progress and settlement describe what input an application has durably accounted for and how that durable fact authorizes a later change to provider-managed delivery state.

The safe causal order for a consuming block is:

```text
apply covered effects
  -> durably record exact application progress
  -> settle the corresponding provider delivery state
```

This order does not require one distributed transaction. It makes the crash cuts explicit. If failure occurs before durable progress, the application must not claim the input was applied. If failure occurs after durable progress but before settlement, redelivery or reconciliation must recover the durable fact and avoid repeating incompatible effects.

## Distinct Evidence

| Evidence | Meaning |
| --- | --- |
| logical emission identity | Stable identity of the carried publication, request, reply, or other emission across attempts. |
| provider delivery identity | Provider-scoped identity that may remain stable across redelivery when the provider proves it. |
| delivery-attempt identity | Identity of one physical delivery attempt; it changes on redelivery. |
| settlement authority | Current receipt, lock, lease, acknowledgment subject, or token authorizing a provider-state change. It may expire and must not become durable logical identity. |
| replay cursor | Opaque position used to select retained input. It does not prove application processing. |
| application progress | Durable application-owned evidence of what input and effects have been accounted for. |
| settlement receipt | Attributable evidence that provider delivery state was changed after a cited durable progress boundary. |

These forms may refer to one another but must not be collapsed. A replay cursor can be retained inside application progress, yet the cursor alone does not prove that the selected input was applied. A provider can manage an acknowledgment floor, yet that floor is not automatically the application's authoritative checkpoint. A settlement token can authorize a current attempt without surviving long enough to identify the logical work.

## Progress Shapes

Durable progress is not always one scalar offset. It can contain orthogonal components:

- a cumulative floor through an ordered position or stable provider delivery identity;
- exact pending deliveries above that floor;
- unresolved gaps that prevent a later position from implying complete prefix processing;
- an attributable provider-managed floor or pending snapshot; and
- a replay position used to resume retained input.

The model must state whether a floor is exact, cumulative, provider-managed, or merely a read position. Persisting only the latest observed cursor can lose the distinction between applied input and gaps still in flight.

## Settlement Operations

Settlement changes provider delivery state. Different operations have different scopes and consequences:

- **invocation-coupled completion** completes one request or session operation;
- **individual settlement** completes one stable delivery;
- **cumulative settlement** advances an ordered prefix;
- **batch settlement** couples several explicitly identified deliveries or ordering scopes;
- **negative settlement or release** makes delivery eligible again;
- **defer** postpones completion without discharging the delivery;
- **quarantine** moves material to an exceptional path without proving business completion.

The settlement coupling scope must match the application's durable proof. A cumulative acknowledgment cannot safely advance past an unresolved gap merely because a later item completed. A provider callback that settles a whole batch requires durable coverage for every delivery coupled to that callback.

## Acknowledgment and Settlement

An [[Acknowledgments|acknowledgment]] is any boundary-relative claim that something happened. Settlement is narrower: it is an operation that changes provider delivery state. A protocol response can acknowledge receipt without settling a durable queue item; settlement can occur through a cursor commit without sending a semantic reply; and neither proves business completion unless the relevant contract says so.

The model should therefore state:

- which durable progress record authorizes settlement;
- which provider scope and deliveries the operation changes;
- whether authority is current, leased, fenced, or invocation-scoped;
- whether an ambiguous failure requires provider reconciliation;
- how redelivery consults prior progress;
- which settlement receipt or observation records the result; and
- which effects remain outside the covered commit boundary.

## Replay, Redelivery, and Resume

- **Replay** intentionally selects retained history, often from a cursor, for the same or a new interpretation.
- **Redelivery** repeats provider delivery because prior completion was absent, expired, released, or ambiguous.
- **Resume** continues bounded session or stream state after interruption.

These operations can compose but are not equivalent. Transport session resume may preserve frames without preserving application progress. Replay can intentionally revisit already applied history. Redelivery can reuse provider delivery identity while creating a new attempt and settlement authority.

## Atomicity and Recovery

When state mutation, produced output, application progress, and provider settlement cannot share one atomic boundary, the realization needs an explicit recovery structure such as an [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], idempotent transition, fenced checkpoint, durable operation record, reconciliation protocol, or broker transaction whose exact participants are named.

Claims of atomicity must enumerate the coupled operations and resource boundary. Atomic publication and offset advancement inside a broker does not automatically include an application's database, an external effect, or a downstream semantic obligation.

Related concepts: [[Interaction Channels|interaction channels]], [[Interaction Protocols|interaction protocols]], [[Messages and Envelopes|messages and envelopes]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Commit Boundaries|commit boundaries]], [[Durability|durability]], [[Ordering|ordering]], [[Correlation and Conversations|correlation and conversations]], [[Consumer Coordination|consumer coordination]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Network Channels|network channels]], [[Brokers|brokers]].

## Formal relations

- `qualifies`: [[Interaction Channels]] — Delivery progress and settlement state which channel inputs are durably accounted for and how that evidence authorizes provider delivery-state changes.
