---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-08-02
aliases:
  - Conversation Identity
  - Message Correlation
---

# Correlation and Conversations

Correlation and conversations describe how independently occurring messages, requests, replies, observations, attempts, and process steps are recognized as participating in one interaction or longer-lived protocol.

Correlation groups material under a declared identity. It does not by itself prove [[Causality|causation]], ordering, semantic dependence, or process membership. A causation link makes the stronger claim that one occurrence contributed to producing another. A process identity gives semantic unity to work that may contain several conversations and causal chains.

## Identity Structure

Important identities include:

- Message or emission identity.
- Request identity and the reply that discharges it.
- Conversation or session identity spanning related exchanges.
- Process, subject, entity, and observer identities.
- Attempt, activation, delivery, and retry identities.
- Sequence identity and position for fragmented or ordered material.

These identities should not be collapsed into one correlation identifier. One request may be delivered several times, one process may contain several requests, and one message may contribute to more than one derived observation.

## Request and Reply

An asynchronous request declares a typed terminal-response or terminal-failure obligation. Its protocol should identify how the result is correlated, where it is returned or observed, how long the obligation remains live, which reply wins under duplication or races, and what happens when the result is late, lost, ambiguous, or rejected.

The [[Interaction Bindings|interaction binding]] should identify the exact request and reply [[Interaction Channels|channel]] directions. They may belong to one coupled invocation or session exchange, or to paired one-way channels. Physical coupling does not replace request and reply identity; physical separation does not prevent one protocol from relating them.

A return address is an operational reply path, not the requestor's semantic identity. A smart proxy may preserve the original return and correlation context while routing through another interaction, but it becomes responsible for the correctness, durability, privacy, and failure handling of that correspondence.

Long-lived conversations often require a [[Process|process]] or [[Process Managers|process manager]] when identity, pending obligations, timeouts, results, and completion must survive individual calls or traces.

## External References

- Gregor Hohpe and Bobby Woolf, [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html), [Return Address](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ReturnAddress.html), and [Correlation Identifier](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Interaction|interaction]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Interaction Channels|interaction channels]], [[Messages and Envelopes|messages and envelopes]], [[Identity|identity]], [[Causality|causality]], [[Process|process]], [[Process Graphs|process graphs]], [[Process Managers|process managers]], [[Effect|effect]], [[Event|event]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Ordering|ordering]], [[Time|time]], [[Retry|retry]], [[Recovery|recovery]], [[Observability and Provenance|observability and provenance]].
