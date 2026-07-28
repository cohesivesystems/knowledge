---
realm: Domain Semantics
kind: semantic-construct
created: 2026-07-27
updated: 2026-07-27
aliases:
  - Semantic Effect
---

# Effect

An effect is a modeled consequence or obligation established by a semantic decision.

An effect is not identical to the description that declares it, the record that persists responsibility for it, the mechanism that executes it, or the observation that later reports it. Those stages must remain distinguishable:

```txt
effect declaration
  -> accepted or committed responsibility
  -> local or external execution
  -> acknowledgment, result, observation, or recovery disposition
```

A decision may declare an effect without having performed it. For example, a [[Transition|transition]] decision may contain a sparse patch and emissions, while a storage realization decides whether the patch and the corresponding obligations can be committed. An [[Outbox|outbox]] record may then make an outbound obligation durable, and an adapter may later attempt the external operation.

## Effect Roles

Important semantic roles include:

- A **transition effect** is the accepted evolution of an [[Entity|entity]] from one versioned [[State|state]] to another. Its occurrence is an endogenous [[Event|event]].
- A **domain-event emission** declares a fact to be established or externalized without creating an emitter-side response obligation.
- A **request** establishes a typed terminal-response or terminal-failure obligation and identifies where that response is consumed.
- A **signal** is an addressed one-way input with no response obligation.
- A **reply** discharges one admitted request.

An emission is therefore a boundary-crossing effect declaration. Domain events, requests, signals, and replies have different obligations even when their payloads use similar [[Shape|shapes]] or travel through the same substrate.

When a publication is presented as an event but the emitter's continuation depends on a correlated terminal result, it participates in an [[Interaction|implicit request protocol]]. Its asynchronous transport does not remove its semantic request role or its response obligation.

Persistence events are separate. They record reconstruction, audit, or storage mechanics and are domain events only when the domain independently assigns them that meaning.

## Decision, Commitment, and Handling

A deterministic semantic decision describes which effects would follow from an accepted path. Commitment establishes which local state changes and obligations have been accepted at a declared [[Commit Boundaries|commit boundary]]. Physical execution and downstream consequences occur at later boundaries unless a realization proves that they share the same atomic scope.

An effect handler is an impure adapter interpretation of an accepted request, signal, or event-delivery obligation. It does not become semantic authority merely because a runtime registers it. In particular, an effect handler must not mutate authoritative entity state directly; a resulting state change must be admitted through an authorized transition boundary.

Effects that may be retried, replayed, resumed, or redelivered require stable identity and an explicit [[Idempotency|idempotency]], deduplication, reconciliation, expected-version, or compensation rule. Physical exactly-once execution must not be inferred from one logical effect identity.

## External References

- Gregor Hohpe and Bobby Woolf, [Command Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html), [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html), and [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Effects]], [[Event|event]], [[Transition|transition]], [[Entity|entity]], [[Process|process]], [[State|state]], [[Observation|observation]], [[Messages and Envelopes|messages and envelopes]], [[Correlation and Conversations|correlation and conversations]], [[Boundaries|boundaries]], [[Interaction|interaction]], [[Commit Boundaries|commit boundaries]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Realization|realization]].
