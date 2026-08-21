---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-08-21
---

# Clean Architecture

Clean Architecture addresses the problem of dependency direction: keeping high-value semantic rules from depending on volatile delivery, persistence, framework, and infrastructure choices.

## Cohesive Formulation

Clean Architecture can be expressed as a separation between domain semantics, system graph, operational concerns, and realization substrate. Inner policy defines meaning and application behavior; outer mechanisms supply ways to invoke, store, transmit, schedule, and present that behavior.

The domain core defines [[Entity|entities]], [[Value|values]], [[Transition|transitions]], [[Invariant|invariants]], [[Policy|policies]], and [[Event|events]]. Application use cases arrange those semantics for particular interactions. Outer mechanisms realize delivery, [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Interaction Protocols|protocols]], user interfaces, and [[Application Hosts|application hosting]].

The dependency rule requires source dependencies to point from volatile mechanisms toward stable policy. When an inner use case needs an outer capability, the inner boundary owns an abstraction for that requirement and an outer implementation supplies it. Control may cross the boundary in either direction even though source dependency continues to point inward.

## In the Model

The dependency rule says that substrate choices should [[Realization|realize]] semantic roles without defining them. A database, web framework, broker, or UI can realize an [[Observer|observer]] or interaction edge, but it should not determine the meaning of entity state, [[Command|command]] interpretation, or [[Invariant|invariant]] scope.

For example, a `PlaceOrder` use case may interpret a [[Command|command]], apply [[Transition|entity transitions]] and [[Policy|policies]], and require order persistence and payment authorization. An HTTP controller may invoke the use case, while SQL and payment-provider adapters satisfy application-owned requirements. The web framework, schema, and provider SDK remain outside the policy boundary.

Clean Architecture does not prescribe one folder layout. Code may be organized by layer, feature, component, or another declared criterion while retaining the dependency rule. [[Vertical Slice Architecture|Vertical slice architecture]] selects use cases or requests as primary change units; clean architecture constrains which dependencies may cross the boundaries inside or around those slices. The practices can coexist, although imposing the same global layers and abstractions on every slice can defeat the slice's change locality.

[[Ports and Adapters]] describes the inside/outside interaction boundary through ports and technology-specific adapters. Clean Architecture uses a concentric policy-and-mechanism vocabulary. Their structures correspond, but neither practice alone determines whether the code modules have suitable [[Cohesion and Coupling|cohesion and coupling]] for the changes the system must support.

## Failure Modes

The practice fails when layer names replace boundary definitions, when every request is forced through ceremonial layers, when DTOs become the domain model, or when framework lifecycle and storage shape determine semantic behavior. It also fails when interfaces merely mirror concrete mechanisms, dependencies bypass the intended boundary, or inward source dependencies are mistaken for proof that runtime, data, deployment, and failure coupling have been removed.

## External References

- Robert C. Martin, [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), 2012.
