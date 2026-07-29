---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-07-29
aliases:
  - Message History
  - Execution Provenance
  - Distributed Observability
---

# Observability and Provenance

Observability and provenance describe the evidence by which observers can inspect, explain, correlate, and diagnose system behavior across boundaries and time.

Observability records evidence about executions. It is distinct from the categorical [[Trace and Feedback|trace and feedback]] principle, which models outputs becoming future inputs. Provenance records where a value, decision, route, effect, or observation came from and which definitions, inputs, policies, authorities, and occurrences contributed to it.

## Observation Scopes

- An **operation trace** follows one bounded invocation, activation, attempt, or local commit.
- A **message history** records emission, routing, transformation, delivery, acknowledgment, retry, and disposition evidence.
- A **causal chain** links occurrences through explicit causation rather than correlation alone.
- A **process history** explains durable progress across operations, messages, waits, timers, compensations, and human work.
- A **system health view** aggregates rates, latency, backlog, saturation, errors, expiry, quarantine, and recovery state.

A wire tap or diagnostic subscriber creates another observation path. It must not silently change delivery cardinality, ordering, backpressure, privacy, or failure behavior. A message store used for diagnosis is not automatically authoritative domain history and requires its own retention, access, redaction, and integrity rules.

[[Service Levels|Service-level]] evidence uses declared observables and observations to evaluate consumer-visible outcomes over a defined population and window. A health metric is not automatically a service-level indicator: the definition must say which service boundary, operation, consumer scope, eligibility rule, outcome, unit, and aggregation it represents. Instrumentation supplies evidence; it does not choose the objective or create an agreement between provider and consumer.

Test messages and synthetic transactions should be identifiable, authorized, and scoped. Their effects must be isolated, reversible, or intentionally real; a synthetic marker alone does not prevent a production consumer from performing an irreversible action.

Useful provenance may include definition and semantic revision, node and branch identity, message and request identity, subject and process identity, correlation and causation, route and transformation revisions, source position, handler version, attempt, acknowledgment, commit boundary, authority, and terminal disposition.

## External References

- Gregor Hohpe and Bobby Woolf, [Wire Tap](https://www.enterpriseintegrationpatterns.com/patterns/messaging/WireTap.html), [Message History](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageHistory.html), and [Message Store](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageStore.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Service|service]], [[Service Levels|service levels]], [[Interfaces|interfaces]], [[Observation|observation]], [[Observer|observer]], [[Causality|causality]], [[Identity|identity]], [[Correlation and Conversations|correlation and conversations]], [[Messages and Envelopes|messages and envelopes]], [[Process|process]], [[Process Graphs|process graphs]], [[Trace and Feedback|trace and feedback]], [[Persistence|persistence]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Operational Control|operational control]], [[Infrastructure|infrastructure]].
