---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Service Level
  - Service Level Indicator
  - Service Level Indicators
  - SLI
  - Service Level Objective
  - Service Level Objectives
  - SLO
  - Service Level Agreement
  - Service Level Agreements
  - SLA
  - Error Budget
  - Error Budgets
---

# Service Levels

Service levels state how the outcomes of a [[Service|service]] are measured, targeted, and, when applicable, made accountable commitments between a provider and consumer.

They qualify a capability at a declared [[Boundaries|boundary]]. They are not properties of a code module, deployment, runtime process, host, or provider organization in isolation. One service may be realized by many such units, and one unit may contribute to several service-level commitments.

The slogan that a service is a program with an SLA usefully distinguishes offered service from executable behavior, but it is not an identity. A service need not be one program, and useful internal or public services can have service-level objectives without a formal agreement carrying remedies or penalties.

## Indicators, Objectives, Agreements, and Budgets

| Term | Meaning |
| --- | --- |
| **Service-level indicator (SLI)** | A precisely defined quantitative observation of some aspect of delivered service, such as successful completion, availability, latency, freshness, durability, correctness, or throughput. |
| **Service-level objective (SLO)** | A target or acceptable range for an SLI over a declared population, scope, and time window. |
| **Service-level agreement (SLA)** | An agreement between provider and consumer that makes selected objectives accountable commitments and states the consequences, remedies, or escalation associated with meeting or missing them. |
| **Error budget** | The permitted shortfall implied by an SLO over its evaluation window, together with any policy governing how that margin affects change, risk, or intervention. |

An indicator says what is measured; an objective says which measured result is expected; an agreement says who commits to what and what follows from the result. These should not be collapsed into the overloaded term *SLA*.

An error budget is straightforward for a ratio objective: a 99.9% good-outcome objective permits 0.1% non-good outcomes within the same eligible population and window. Other objectives, such as several latency percentiles, freshness bounds, or maximum consecutive outage, need their own budget interpretation. Separate budgets are not automatically interchangeable.

## Measurement Contract

An SLI is an [[Observable|observable]] definition, not merely the name of a metric. Its resulting [[Observation|observations]] need enough context to establish:

- The capability, operation, interface, consumer population, and [[Policy Scopes|policy scope]] being measured.
- The observation boundary and whose experience it represents.
- The eligible population or denominator and the classification of good, degraded, failed, excluded, missing, and indeterminate outcomes.
- The unit, threshold, aggregation, percentile, or other evaluation rule.
- The event-time or processing-time basis, evaluation window, lateness policy, and treatment of partial periods.
- The evidence source, provenance, retention, consistency, and authority for resolving disagreement.

Provider-side process uptime is not automatically consumer-visible availability. Admission is not useful completion; a transport acknowledgment is not necessarily application completion; and a fast error may satisfy a latency threshold while failing the requested capability. The indicator should observe the outcome promised at the service boundary as directly as practical.

Measurement can itself be incomplete or delayed. Missing telemetry must not silently become either success or failure, and changes to instrumentation, sampling, traffic mix, eligibility, or aggregation can change the indicator without changing the underlying service. [[Observability and Provenance|Observability and provenance]] supplies the evidence; the service-level definition supplies its contractual interpretation.

## Objective and Agreement Scope

An SLO should state:

- The SLI definition and target or range.
- The operation, workload class, tenant, geography, version, priority, or other scope to which it applies.
- The rolling, calendar, release, or event-defined evaluation window.
- The expected behavior during low or absent traffic.
- The owner, approver, effective revision, review cadence, and error-budget policy.

An SLA additionally identifies the provider and consumer roles, governed [[Interfaces|interfaces]] and [[Interaction Protocols|interaction protocols]], exclusions and maintenance treatment, measurement authority, reporting and dispute rules, escalation, remedies or consequences, and the interval during which the commitment is effective.

An agreement can cover semantic as well as operational obligations. Correctness, accepted responsibility, terminal outcomes, privacy, durability, and recovery may matter as much as availability or latency. A service-level target does not weaken those meanings unless the service contract explicitly permits a degraded outcome or narrower guarantee.

## Composition and Operation

Service levels are not automatically [[Compositionality|compositional]]. End-to-end behavior depends on fanout, retries, shared dependencies, correlated failures, caching, routing, fallback, and which paths each request actually uses. Multiplying dependency availability percentages or adding latency targets is valid only under assumptions that match the service graph and workload.

Internal objectives can be stricter than an external commitment to leave room for dependencies, uncertainty, detection, repair, and recovery. A downstream SLA is evidence for planning an upstream objective, not proof that the upstream objective will be met.

[[Capacity Planning|Capacity planning]] turns service objectives, workload, failure assumptions, and lead times into required effective capacity and reserve. [[Control Models|Control models]], [[Scaling Mechanisms|autoscaling]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Rate Limiting|rate limiting]], and [[Flow Control|flow control]] may protect objectives, but their local metrics are not substitutes for observing the promised outcome.

Error-budget policy can inform release pacing, risk acceptance, escalation, or recovery work. It is an operational decision policy, not permission to manufacture failures or ignore errors until the budget is exhausted. High-priority, safety-critical, contractual, and semantic obligations may impose additional constraints regardless of remaining budget.

## Modeling Checks

- Which service capability and boundary does the service level qualify?
- Which consumers, operations, workload classes, and policy scopes are included?
- What is the SLI's eligible population, good-outcome rule, unit, and observation source?
- Does the measurement represent consumer-visible service or only an internal proxy?
- What target and evaluation window define the SLO?
- How are missing evidence, sparse traffic, delayed data, exclusions, and definition changes handled?
- Which provider and consumer roles are parties to an SLA, and what consequences make it an agreement rather than only an objective?
- Which semantic guarantees remain absolute or separately governed?
- How is the error budget derived, attributed, and used operationally?
- How do dependency objectives and correlated failures affect the end-to-end claim?
- Which capacity, recovery, degradation, and control policies protect the objective?

## Formal relations

- `qualifies`: [[Service]] — States measurable objectives and, where applicable, accountable commitments for outcomes at a declared service boundary.

## External References

- Google, [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), in *Site Reliability Engineering*, 2016.
- Google, [Implementing SLOs](https://sre.google/workbook/implementing-slos/), in *The Site Reliability Workbook*, 2018.

Related concepts: [[Service|service]], [[Service Models|service models]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Boundaries|boundaries]], [[Policy|policy]], [[Policy Scopes|policy scopes]], [[Observable|observable]], [[Observation|observation]], [[Observability and Provenance|observability and provenance]], [[Authority|authority]], [[Compositionality|compositionality]], [[Compatibility and Evolution|compatibility and evolution]], [[Scalability|scalability]], [[Capacity Planning|capacity planning]], [[Control Models|control models]], [[Scaling Mechanisms|scaling mechanisms]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Rate Limiting|rate limiting]], [[Flow Control|flow control]], [[Fairness|fairness]], [[Recovery|recovery]].
