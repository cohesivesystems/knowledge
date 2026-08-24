---
realm: Operational Concerns
kind: operational-concern
created: 2026-08-23
updated: 2026-08-23
status: draft
aliases:
  - Event Propagation
  - Semantic Event Propagation
---

# Semantic Propagation

Semantic propagation describes when an occurrence or source-state change at one [[Boundaries|boundary]] has satisfied a declared observer-relative postcondition at another boundary. It qualifies semantic movement through a [[Flow Views|flow view]]; it is not the transport of an event object or the successful delivery of a particular message.

For a message $m$, event $e$, [[Observer|observer]] $O$, and required postcondition $\phi$:

$$
\operatorname{Delivered}(m,O)
\not\Rightarrow
\operatorname{Propagated}(e,O,\phi)
$$

Message delivery establishes a channel occurrence. Semantic propagation instead requires $\phi$ to hold at its declared boundary. The postcondition may say that the observer acquired an admissible [[Observation|observation]], a [[Projection Models|projection]] corresponds to a declared source version or cut, a downstream [[Transition|transition]] committed, an [[Invariant|invariant]] was restored, an [[Effect|effect]] became externally effective, or a [[Process|process]] obligation reached its declared disposition.

The converse also need not hold for one particular message:

$$
\neg\operatorname{Delivered}(m,O)
\not\Rightarrow
\neg\operatorname{Propagated}(e,O,\phi)
$$

An observer may satisfy the same postcondition through polling, replay, state comparison, anti-entropy, recomputation, or reconciliation. Such an alternate path establishes progress only when its own delivery, scheduling, retention, authority, and [[Recovery|recovery]] assumptions are explicit.

## Authority and Notification

A publication can carry different relationships to authority:

- **Authoritative history** preserves occurrences whose identity, ordering, and retention are part of the observer's required evidence.
- **State transfer or delta** carries an observation of authoritative or derived state at a declared version, position, or [[Consistent Cuts|consistent cut]].
- **Notification or invalidation hint** indicates that an observer's prior observation may be stale and prompts it to consult another authoritative source.

These roles can use the same [[Messages and Envelopes|message]] and [[Interaction Channels|channel]] mechanisms without acquiring the same guarantees. When retained event history is authoritative, loss or truncation can destroy evidence required by the observer. When authoritative state exists elsewhere, individual notifications may sometimes be coalesced, reordered, or lost if a separate reconciliation path still establishes the required propagation postcondition. A lossy hint without eventual polling, repair, replay, or another progress mechanism does not establish liveness.

## Propagation Requirement

A semantic propagation requirement should state:

- The source occurrence, state, history, or fact and the boundary that authorizes it.
- The target observer, subject, and interpretation boundary.
- The exact postcondition that constitutes propagation.
- The source identity, [[Version|version]], position, or consistent cut to which the postcondition refers.
- Whether every intermediate occurrence matters or only convergence to an admissible state.
- Required freshness, ordering, completeness, consistency, and uncertainty treatment.
- The delivery, retry, fairness, retention, scheduling, and recovery assumptions needed for progress.
- The observation, provenance, commitment, or reconciliation evidence by which satisfaction is established.

For a derived state view, one possible requirement is:

$$
P_O \simeq f(S_c)
$$

where $S_c$ is authoritative source state at a declared cut $c$, $f$ is the declared derivation, and $\simeq$ is the model's accepted equivalence or tolerance rather than unqualified value equality. Another requirement may instead preserve an ordered or causal event history because the intermediate occurrences themselves carry meaning that a final state cannot recover.

## Relation to Delivery

[[Delivery Semantics|Delivery semantics]] states which emitted, admitted, delivered, processed, committed, acknowledged, or discharged occurrence an interaction edge guarantees. Semantic propagation states what must become true for a downstream observer. Delivery can be necessary evidence or a required progress mechanism, but it is not sufficient merely because a provider reports success.

An [[Acknowledgments|acknowledgment]] likewise proves only the occurrence named by its protocol and boundary. Broker admission, consumer delivery, handler return, provider settlement, projection commitment, query visibility, and business completion remain distinct. A model may compose them into a propagation argument, but it must not infer the last from the first without the intermediate semantics and evidence.

## Modeling Checks

- What observer-relative postcondition constitutes semantic propagation?
- Is the publication authoritative history, a state transfer or delta, or a hint to inspect another authority?
- Does every source occurrence matter, or is convergence to an admissible source cut sufficient?
- Which delivery and recovery paths can establish the postcondition?
- What failure, retention, fairness, scheduling, and continued-execution assumptions provide liveness?
- What observation or durable evidence proves propagation, and at which boundary?
- Can a provider report successful delivery while the semantic postcondition remains false?
- Can a missed notification be repaired without losing required semantic information?

## Formal relations

- `qualifies`: [[Flow Views]] — States when semantic movement has satisfied a declared observer-relative postcondition rather than merely producing a channel occurrence.
- `distinguished_from`: [[Delivery Semantics]] — Delivery semantics governs channel occurrences, while semantic propagation governs downstream observations, state, effects, or obligations.
