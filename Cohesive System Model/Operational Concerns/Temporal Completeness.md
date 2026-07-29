---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Event-Time Completeness
  - Stream-Time Completeness
  - Window Completeness
  - Watermarks and Late Data
---

# Temporal Completeness

Temporal completeness describes when an observer or flow operator may treat the input relevant to a time-bounded result as sufficiently complete to emit, finalize, correct, or retract that result.

For an unbounded or asynchronously delivered history, silence does not prove that no earlier event will arrive. Completeness is therefore a boundary-relative operational claim based on source knowledge, progress evidence, retention, delivery assumptions, deadlines, and policy. It is not an intrinsic property of a timestamp or window.

## Time Axes

Streaming and asynchronous systems commonly distinguish several non-identical times:

- **Occurrence or event time:** when the modeled occurrence happened according to its semantic or source context.
- **Observation or ingestion time:** when a receiving observer admitted evidence of the occurrence.
- **Processing time:** when an operator evaluated the record.
- **Commit time:** when selected effects became accepted at a commit boundary.
- **Visibility time:** when a result became observable through a query, projection, cache, or external interface.

These times can be ordered differently. A record may be processed after later-occurring records, committed in another partition order, and become visible after a projection delay. A source-supplied timestamp is itself evidence requiring identity, interpretation, trust, and clock assumptions; it does not prove causal order.

## Windows, Watermarks, and Triggers

A **window** selects a finite context from an otherwise unbounded history by time, count, session, key, or another boundary. The selection rule does not determine when the window is complete enough to emit.

A **watermark** is evidence or a policy claim that future input earlier than a selected event-time position is no longer expected beyond an admitted lateness model. It is not proof that no earlier record can arrive. Its validity depends on the participating sources, idle-source rules, partitions, clock assumptions, delivery paths, and recovery behavior included in its scope.

A **trigger** chooses when an operator emits a result. It may emit early speculative results, periodic updates, a result when a watermark passes, a result after processing-time delay, or repeated corrections. Triggering and completeness are distinct: a useful early result may be intentionally provisional.

## Late Input and Correction

The model should state how input that arrives after an emitted or finalized result is treated:

- Ignore or quarantine it under an explicit loss policy.
- Update the result in place.
- Emit a correction, retraction, or compensating value.
- Reopen the window or derived state.
- Route it to reconciliation or manual review.

Correction requires stable result and derivation identity. Downstream consumers must know whether updates replace prior results, accumulate deltas, retract prior facts, or represent new semantic events. A transport-level duplicate and a legitimate correction are not the same occurrence.

State retention must cover the admitted lateness and correction horizon. Expiring window state, source history, schema interpretations, deduplication material, or provenance can make a nominally supported correction impossible.

## Completeness and Non-Monotone Decisions

Aggregation, joins, absence tests, uniqueness, top-k results, and closed-window decisions often depend on evidence that relevant input is complete enough. These are non-monotone when later facts can invalidate an earlier conclusion. The [[CALM Theorem|CALM theorem]] explains why such decisions need coordination, a declared completeness boundary, or explicit provisional and correction semantics.

A complete result for one [[Shape|shape]], source set, key, window, and policy may remain incomplete for another. Completeness claims should therefore identify the observer, sources, partitions, event-time interval, allowed lateness, missing-source behavior, and result revision policy.

## Modeling Checks

- Which occurrence, observation, processing, commit, and visibility times are present?
- Which sources, partitions, keys, and intervals define the completeness scope?
- What evidence advances a watermark, and what happens when a source is idle or unavailable?
- Is an emitted result provisional, final for a policy horizon, or permanently revisable?
- How are late, duplicate, corrected, missing, and contradictory inputs distinguished?
- Which output identity and revision let downstream observers replace or retract prior results?
- How long must input, operator state, schemas, provenance, and deduplication material be retained?
- Which decisions depend on absence or completeness and therefore require coordination or explicit uncertainty?

## Formal relations

- `qualifies`: [[Flow Operators]] — States when windows, joins, aggregates, and other time-bounded operators may emit, finalize, or revise results from incomplete asynchronous input.

## External References

- Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly Media, 2017, chapter 11.

Related concepts: [[Time|time]], [[Uncertainty|uncertainty]], [[Observation|observation]], [[Event|event]], [[Flow Operators|flow operators]], [[Flow Views|flow views]], [[Projection Models|projection models]], [[Interaction Channels|interaction channels]], [[Consistent Cuts|consistent cuts]], [[Ordering|ordering]], [[Delivery Semantics|delivery semantics]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Compatibility and Evolution|compatibility and evolution]], [[Observability and Provenance|observability and provenance]], [[CALM Theorem|CALM theorem]], [[Asynchronous Interaction Design|asynchronous interaction design]].
