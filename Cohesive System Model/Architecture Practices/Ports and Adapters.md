---
realm: Architecture Practices
kind: pattern
created: 2026-06-24
updated: 2026-08-21
aliases:
  - Hexagonal Architecture
  - Ports & Adapters
---

# Ports and Adapters

Ports and Adapters, also known as Hexagonal Architecture, keeps an application's domain and application semantics on the inside independent from user interfaces, databases, message brokers, external services, frameworks, and other technologies on the outside. The inside communicates through purpose-specific ports; adapters translate between those ports and particular outside mechanisms.

The hexagon is only a drawing convention. Its six sides have no architectural significance. The important distinction is inside versus outside, together with the rule that outside mechanisms adapt to the application's boundary rather than define its meaning.

## Familiar Terminology

A **port** names a purposeful conversation at an application boundary and states the protocol or API the application provides or requires for that conversation. It is not a TCP or UDP port, URL, queue name, socket, or other network address. An **adapter** converts between that application-facing conversation and a particular technology, library, device, test fixture, data store, or external system.

Ports and adapters occur in two conversational orientations:

| Orientation | Who initiates the conversation? | Typical adapters |
| --- | --- | --- |
| **primary**, **driving**, or **inbound** | An outside actor drives the application through a port the application provides. | HTTP controller, CLI handler, UI handler, message consumer, batch job, or test harness |
| **secondary**, **driven**, or **outbound** | The application drives an outside actor through a port it requires. | database repository adapter, payment client, message publisher, file store, clock, or notification gateway |

Primary and secondary describe who initiates the conversation, not which side is more important. One port can have several interchangeable adapters. For example, an HTTP controller, CLI handler, and test fixture can all drive the same application use case; a SQL repository adapter, in-memory repository adapter, and remote-store adapter can all satisfy the same persistence port.

## Place Order Example

Consider a `PlaceOrder` use case:

```text
HTTP request
  -> HTTP adapter
  -> PlaceOrder input port
  -> application use case
  -> domain behavior
       -> PaymentGateway output port -> provider adapter -> payment provider
       -> OrderRepository output port -> SQL adapter      -> database
       -> OrderEvents output port     -> broker adapter   -> message broker
```

The `PlaceOrder` port admits a command expressed in application terms. An HTTP controller is one driving adapter: it performs protocol-level checks and maps HTTP- and JSON-specific input into that command, then invokes the port. A CLI command, message consumer, or automated test can be another driving adapter without changing the use case.

During the use case, the application requires secondary ports such as `PaymentGateway`, `OrderRepository`, and `OrderEvents`. Provider-, SQL-, and broker-specific adapters realize those requirements. In a test, in-memory or recording adapters can replace them. The business rule that decides whether an order may be placed remains inside; HTTP status codes, SQL schemas, provider SDK objects, topic names, and retry-library types remain outside.

## Cohesive Formulation

In Cohesive, an [[Interfaces|interface]] is a reusable intentional interaction type projected on a [[Surfaces|surface]]. A port is a particular occurrence on a [[Boundaries|boundary]] through which a component provides or requires that interface. An [[Endpoints|endpoint]] is the bound attachment locus through which that port participates in a particular [[Interaction Channels|channel]] arrangement. An adapter is a [[Realization|realization]] mechanism that translates among interface roles, component behavior, [[Messages and Envelopes|messages]], and substrate mechanisms.

This refines the familiar terminology without replacing it. Cockburn's port identifies the purpose and protocol of a boundary conversation. The Cohesive distinctions additionally keep the reusable interface type, its provided or required occurrence, the endpoint bound into a channel arrangement, any address that selects that endpoint, and the adapter that realizes the translation from becoming synonymous. Consequently, a port may have several adapters and several endpoint bindings, while a network endpoint or address is only one possible realization detail.

The practice asks:

- Which boundary is being crossed?
- Which interface type and provided or required orientation does the port instantiate?
- What semantic object enters or leaves the boundary?
- Which observer interprets the input?
- Which [[Interaction Protocols|interaction protocol]] governs the conversation?
- Which endpoint and channel directions are attached by the [[Interaction Bindings|interaction binding]]?
- What channel realization, protocol binding, storage mechanism, UI, or external system realizes the edge?

## In the Model

A driving adapter admits an external occurrence as an input event relative to an [[Observer|observer]] and supplies the carried value and contract for interpretation as a command, query, event notification, signal, or other role. A driven adapter realizes an endogenous event, request, signal, reply, query, command intent, or observation as a protocol-specific effect. The adapter preserves a correspondence; it does not collapse transport classification into semantic interpretation.

[[Enterprise Integration Patterns|Enterprise integration patterns]] channel adapters, messaging gateways, messaging mappers, and service activators are specialized endpoint and adapter structures. They should remain outside the semantic authority that decides domain transitions.

## Relation to Code Organization

Ports and Adapters governs a boundary and dependency direction; it does not require one universal folder layout. It can be applied within a [[Vertical Slice Architecture|vertical slice]], across a coarser component boundary, or at a service boundary. A slice may colocate a use case with its driving and driven adapters while keeping the application-facing ports explicit.

This makes the practice complementary to [[Cohesion and Coupling|cohesion and coupling]]. Grouping code that changes for one use case can improve feature and change cohesion, while ports reduce coupling to mechanisms outside that cohesive unit. Introducing an interface for every class does not create a useful port: the port should represent a meaningful boundary conversation, substitution point, or independently variable outside dependency.

## Failure Modes

The pattern fails when adapters leak substrate semantics into the domain, when ports are treated as concrete network endpoints, when endpoint addresses become semantic identity, or when interfaces are described without stating their semantic boundary, protocol, binding, and authority. It also fails when nominal ports merely rename framework APIs, or when adapters contain the domain decisions that the inside is meant to own.

## Formal relations

- `corresponds_to`: [[Clean Architecture]] — Shares an inward dependency direction and separation of semantic policy from external mechanisms while retaining distinct interface-role and layering vocabularies.

## External References

- Alistair Cockburn, [Hexagonal Architecture: The Original 2005 Article](https://alistair.cockburn.us/hexagonal-architecture/), HaT Technical Report 2005.02, 2005.
- Gregor Hohpe and Bobby Woolf, [Channel Adapter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html), [Messaging Gateway](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingGateway.html), and [Messaging Mapper](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingMapper.html), *Enterprise Integration Patterns*, 2003.
