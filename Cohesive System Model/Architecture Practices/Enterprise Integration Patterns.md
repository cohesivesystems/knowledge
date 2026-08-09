---
realm: Architecture Practices
kind: reference
created: 2026-07-27
updated: 2026-08-08
aliases:
  - EIP
  - Enterprise Integration Pattern Language
---

# Enterprise Integration Patterns

Enterprise Integration Patterns, or EIP, is a technology-independent pattern language for message-based integration. Cohesive uses the catalog as an important architecture vocabulary while preserving the distinction among domain semantics, system-graph structure, operational concerns, architecture practices, and realization substrate.

An EIP pattern is not automatically a Cohesive semantic primitive. A pattern may instead:

- **Carry** a semantic value or intended interpretation in a message.
- **Arrange** messages, channels, routes, endpoints, or flow operators in the system graph.
- **Require** delivery, ordering, compatibility, correlation, retention, or recovery guarantees.
- **Realize** an interaction through a broker, file exchange, database, application host, or network protocol.
- **Compose** several lower-level structures and guarantees into an architecture practice.

## Foundational Correspondence

Message emission and ingress are occurrences. At a receiving boundary, message ingress is an exogenous [[Event|event]] carrying a [[Value|value]]. A message contract may explicitly express singular command intent, report an occurrence, transfer a document, request a reply, or signal another protocol role. That contract supplies strong evidence for interpretation without replacing the receiving [[Observer|observer]] that admits and interprets the input.

The transport medium remains distinct from the semantic construct while maintaining an explicit correspondence. A channel or broker realizes delivery; a message carries a value and contract; an observer interprets the received occurrence; a transition or process determines the resulting semantic work.

## Later Control-Flow Extension

The original EIP catalog mainly depicts the data flow of messages through endpoints, channels, routers, and transformers. Gregor Hohpe's later control-flow extension adds a second, orthogonal question: which element actively drives each interaction? Cohesive represents this as [[Interaction Control Flow|interaction control flow]].

The extension distinguishes active senders and fetchers from passive sinks and sources. Applying those roles independently to both ports of a stage yields pushers, pullers, queues, and drivers. A queue accepts an active producer on one side and serves an active fetcher on the other, separating arrival cadence from departure cadence. A driver actively fetches and pushes, giving it direct control over polling, batching, and rate.

This is not a sixty-sixth peer pattern or a new semantic primitive. It is a cross-cutting operational facet of the original patterns, especially Pipes and Filters, Message Channel, Polling Consumer, Event-Driven Consumer, Competing Consumers, and broker-backed routing. A pattern diagram should state whether each arrow depicts message or data movement, interaction control, causal order, or process progression because those directions can differ.

## Realm Orientation and Domain Reconciliation

EIP patterns tend to gravitate toward System Graph, Operational Concerns, and Realization Substrate. They are strongest at describing carriers, paths, endpoints, transformations, routing, delivery arrangements, and management structures. [[Domain-Driven Design|DDD]] gravitates toward Domain Semantics and the architecture practices that preserve semantic boundaries, authority, invariants, and ubiquitous language.

The two vocabularies meet through explicit correspondence rather than identification:

| EIP construct | Semantic reconciliation |
| --- | --- |
| Command Message | A carrier whose contract strongly indicates command intent; ingress remains an exogenous event and command interpretation remains relative to the receiving observer. |
| Event Message | A carrier reporting an occurrence; the reported domain event and the message-receipt event are distinct occurrences at different boundaries. |
| Message Channel | An interaction locus that does not decide the semantic role, authority, or business completion meaning of what it carries. |
| Process Manager | A routing and coordination pattern that may realize part of a semantic process but does not define its purpose, state authority, recovery policy, or terminal outcomes. |
| Canonical Data Model | A selected integration representation that does not become canonical domain meaning or one enterprise-wide ubiquitous language. |

[[Pattern Languages and Correspondence|The realm correspondence framework]] starts with the DDD meaning and boundary, places that meaning into messages, channels, observers, effects, and process graphs, assigns EIP structures and operational obligations, and only then selects a broker, runtime, store, protocol, or file exchange.

## Catalog Coverage

### Integration Styles

| EIP pattern | Cohesive correspondence |
| --- | --- |
| File Transfer | [[Batch and File Exchange\|batch and file exchange]], [[Interaction\|interaction]], and [[Storage Systems\|storage systems]] |
| Shared Database | [[Storage Systems\|storage systems]], [[Interaction\|shared-state interaction]], [[Boundaries\|boundaries]], and [[Isolation\|isolation]] |
| Remote Procedure Invocation | [[Interaction\|request/reply]], [[Network\|network]], and [[Application Hosts\|application hosts]] |
| Messaging | [[Interaction\|interaction]], [[Messages and Envelopes\|messages and envelopes]], [[Interaction Channels\|interaction channels]], and [[Brokers\|brokers]] |

### Messaging Systems

| EIP pattern | Cohesive correspondence |
| --- | --- |
| Message Channel | [[Interaction Channels\|interaction channels]] and [[Interaction Control Flow\|interaction control flow]] |
| Message | [[Messages and Envelopes\|messages and envelopes]] |
| Pipes and Filters | [[Flow Operators\|flow operators]], [[Flow Views\|flow views]], and [[Interaction Control Flow\|interaction control flow]] |
| Message Router | [[Routing Models\|routing models]] |
| Message Translator | [[Anti-Corruption Layer\|anti-corruption layer]] and [[Compatibility and Evolution\|compatibility and evolution]] |
| Message Endpoint | [[Endpoints\|endpoints]], [[Observer Models\|observer models]], and [[Ports and Adapters\|ports and adapters]] |

### Messaging Channels

| EIP pattern | Cohesive correspondence |
| --- | --- |
| Point-to-Point Channel | [[Interaction Channels\|interaction channels]] and [[Consumer Coordination\|consumer coordination]] |
| Publish-Subscribe Channel | [[Interaction Channels\|interaction channels]] and [[Brokers\|brokers]] |
| Datatype Channel | [[Interaction Channels\|interaction channels]], [[Shape\|shape]], and [[Compatibility and Evolution\|compatibility and evolution]] |
| Invalid Message Channel | [[Retention Expiration and Quarantine\|retention, expiration, and quarantine]] and [[Recovery\|recovery]] |
| Dead Letter Channel | [[Retention Expiration and Quarantine\|retention, expiration, and quarantine]] and [[Asynchronous Interaction Design\|asynchronous interaction design]] |
| Guaranteed Delivery | [[Delivery Semantics\|delivery semantics]], [[Durability\|durability]], and [[Acknowledgments\|acknowledgments]] |
| Channel Adapter | [[Ports and Adapters\|ports and adapters]] and [[Realization\|realization]] |
| Messaging Bridge | [[Interaction Channels\|interaction channels]], [[Brokers\|brokers]], and [[Network\|network]] |
| Message Bus | [[Interaction Channels\|interaction channels]], [[Brokers\|brokers]], and [[Infrastructure Graph\|infrastructure graph]] |

### Message Construction

| EIP pattern | Cohesive correspondence |
| --- | --- |
| Command Message | [[Messages and Envelopes\|messages and envelopes]] carrying explicit [[Command\|command]] intent as an exogenous [[Event\|event]] at ingress |
| Document Message | [[Messages and Envelopes\|messages and envelopes]] carrying an [[Observation\|observation]], state transfer, artifact, or other shaped value |
| Event Message | [[Messages and Envelopes\|messages and envelopes]] carrying a reported [[Event\|occurrence]]; receipt is also an exogenous messaging event |
| Request-Reply | [[Interaction\|request/reply]], request [[Effect\|effects]], and [[Correlation and Conversations\|correlation and conversations]] |
| Return Address | [[Correlation and Conversations\|correlation and conversations]] and [[Interaction\|interaction]] |
| Correlation Identifier | [[Correlation and Conversations\|correlation and conversations]], [[Identity\|identity]], and [[Causality\|causality]] |
| Message Sequence | [[Correlation and Conversations\|correlation and conversations]] and [[Ordering\|ordering]] |
| Message Expiration | [[Retention Expiration and Quarantine\|retention, expiration, and quarantine]] and [[Time\|time]] |
| Format Indicator | [[Compatibility and Evolution\|compatibility and evolution]], [[Version\|version]], and [[Shape\|shape]] |

### Message Routing

| EIP pattern | Cohesive correspondence |
| --- | --- |
| Content-Based Router | [[Routing Models\|routing models]] and [[Policy Scopes\|policy scopes]] |
| Message Filter | [[Flow Operators\|flow operators]] and [[Policy Scopes\|policy scopes]] |
| Dynamic Router | [[Routing Models\|routing models]], [[Observer Models\|observer models]], and routing observations |
| Recipient List | [[Routing Models\|routing models]] and [[Interaction Channels\|interaction channels]] |
| Splitter | [[Flow Operators\|flow operators]] |
| Aggregator | [[Flow Operators\|flow operators]], [[Correlation and Conversations\|correlation and conversations]], and [[Consistent Cuts\|consistent cuts]] |
| Resequencer | [[Flow Operators\|flow operators]] and [[Ordering\|ordering]] |
| Composed Message Processor | [[Flow Operators\|flow operators]], [[Flow Views\|flow views]], and [[Compositionality\|compositionality]] |
| Scatter-Gather | [[Flow Operators\|flow operators]], [[Interaction\|request/reply]], and [[Correlation and Conversations\|correlation and conversations]] |
| Routing Slip | [[Routing Models\|routing models]] and [[Process Graphs\|process graphs]] |
| Process Manager | [[Process Managers\|process managers]] and [[Process Graphs\|process graphs]] |
| Message Broker | [[Routing Models\|routing models]] and [[Brokers\|brokers]] |

### Message Transformation

| EIP pattern | Cohesive correspondence |
| --- | --- |
| Envelope Wrapper | [[Messages and Envelopes\|messages and envelopes]] |
| Content Enricher | [[Flow Operators\|flow operators]], [[Observation\|observations]], and [[Projection Models\|projection models]] |
| Content Filter | [[Flow Operators\|flow operators]], [[Shape\|shape]], and boundary-relative projection or redaction |
| Claim Check | [[Messages and Envelopes\|messages and envelopes]], [[Identity\|identity]], and [[Storage Systems\|storage systems]] |
| Normalizer | [[Anti-Corruption Layer\|anti-corruption layer]] and [[Compatibility and Evolution\|compatibility and evolution]] |
| Canonical Data Model | [[Anti-Corruption Layer\|anti-corruption layer]], [[Compatibility and Evolution\|compatibility and evolution]], and [[System Language and Realization\|system language and realization]] |

### Messaging Endpoints

| EIP pattern | Cohesive correspondence |
| --- | --- |
| Messaging Gateway | [[Ports and Adapters\|ports and adapters]], [[Observer Models\|observer models]], and [[Application Hosts\|application hosts]] |
| Messaging Mapper | [[Ports and Adapters\|ports and adapters]], [[Shape\|shape]], and [[Realization\|realization]] |
| Transactional Client | [[Commit Boundaries\|commit boundaries]], [[ACID]], [[Transactional Outbox\|transactional outbox]], and [[Transactional Inbox\|transactional inbox]] |
| Polling Consumer | [[Consumer Coordination\|consumer coordination]], [[Interaction Control Flow\|interaction control flow]], [[Scheduling\|scheduling]], and [[Interaction\|interaction]] |
| Event-Driven Consumer | [[Consumer Coordination\|consumer coordination]], [[Interaction Control Flow\|interaction control flow]], [[Observer Models\|observer models]], and [[Runtimes\|runtimes]] |
| Competing Consumers | [[Consumer Coordination\|consumer coordination]], [[Arbitration\|arbitration]], and [[Fairness\|fairness]] |
| Message Dispatcher | [[Consumer Coordination\|consumer coordination]] and [[Routing Models\|routing models]] |
| Selective Consumer | [[Consumer Coordination\|consumer coordination]], [[Routing Models\|routing models]], and [[Policy Scopes\|policy scopes]] |
| Durable Subscriber | [[Consumer Coordination\|consumer coordination]], [[Durability\|durability]], and [[Retention Expiration and Quarantine\|retention, expiration, and quarantine]] |
| Idempotent Receiver | [[Idempotency\|idempotency]] and [[Transactional Inbox\|transactional inbox]] |
| Service Activator | [[Ports and Adapters\|ports and adapters]], [[Observer Models\|observer models]], and [[Application Hosts\|application hosts]] |

### System Management

| EIP pattern | Cohesive correspondence |
| --- | --- |
| Control Bus | [[Operational Control\|operational control]] and [[Infrastructure Graph\|infrastructure graph]] |
| Detour | [[Operational Control\|operational control]], [[Routing Models\|routing models]], and [[Policy Scopes\|policy scopes]] |
| Wire Tap | [[Observability and Provenance\|observability and provenance]] |
| Message History | [[Observability and Provenance\|observability and provenance]] and [[Causality\|causality]] |
| Message Store | [[Observability and Provenance\|observability and provenance]], [[Persistence\|persistence]], and [[Storage Systems\|storage systems]] |
| Smart Proxy | [[Correlation and Conversations\|correlation and conversations]], [[Routing Models\|routing models]], and [[Interaction\|interaction]] |
| Test Message | [[Operational Control\|operational control]] and [[Observability and Provenance\|observability and provenance]] |
| Channel Purger | [[Operational Control\|operational control]] and [[Retention Expiration and Quarantine\|retention, expiration, and quarantine]] |

## Boundary of Adoption

Cohesive adopts EIP with three qualifications: guaranteed delivery is not business completion; a canonical integration model is not canonical domain meaning; and a process manager is not the semantic process it coordinates.

## Formal relations

- `documents`: [[Messages and Envelopes]] — Organizes message construction, translation, correlation, and envelope concerns without identifying carried records with semantic events or commands.
- `documents`: [[Interaction Channels]] — Organizes channel, endpoint, adapter, routing, and mediation patterns for message-based interaction structure.
- `documents`: [[Routing Models]] — Organizes content-, context-, recipient-, process-, and topology-sensitive routing alternatives and their composition.

## External References

- Gregor Hohpe and Bobby Woolf, [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/), Addison-Wesley Professional, 2003.
- Enterprise Integration Patterns, [Messaging Patterns Overview](https://www.enterpriseintegrationpatterns.com/patterns/messaging/index.html) and [Table of Contents](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Domain-Driven Design|domain-driven design]], [[Architecture Practices|architecture practices]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Messages and Envelopes|messages and envelopes]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Flow Operators|flow operators]], [[Observer Models|observer models]], [[Effect|effect]], [[Event|event]], [[Command|command]], [[Process|process]], [[Delivery Semantics|delivery semantics]], [[Realization|realization]].
