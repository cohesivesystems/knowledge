---
realm: Architecture Practices
kind: reference
created: 2026-07-28
updated: 2026-07-28
aliases:
  - POSA
  - POSA Pattern Language
---

# Pattern-Oriented Software Architecture

Pattern-Oriented Software Architecture, or POSA, is a multi-volume system of architectural patterns, design patterns, idioms, concurrency and networking patterns, resource-management patterns, and a composed pattern language for distributed computing.

POSA is especially relevant to Cohesive because it explicitly spans abstraction levels and, in Volume 4, connects patterns from several established catalogs into a larger language.

## Cohesive Correspondence

| POSA emphasis                      | Representative patterns                                                                                                  | Cohesive correspondence                                                                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System organization                | Layers, Pipes and Filters, Blackboard, Broker, Model-View-Controller, Microkernel                                        | [[System Graph\|system graph]] structure, flow views, observer models, interaction channels, and architecture-practice bundles                                         |
| Event demultiplexing and dispatch  | Reactor, Proactor, Acceptor-Connector, Asynchronous Completion Token                                                     | [[Multiplexing and Demultiplexing\|demultiplexing]], [[Interaction Control Flow\|interaction control flow]], correlation, scheduling, network, and runtime realization |
| Concurrency and synchronization    | Active Object, Monitor Object, Half-Sync/Half-Async, Leader/Followers, Guarded Suspension, Future                        | synchrony, scheduling, arbitration, concurrency control, progress conditions, and runtimes                                                                             |
| Distribution infrastructure        | Broker, Client Proxy, Requestor, Invoker, message channels, endpoints, routers, and translators                          | [[Interfaces\|interfaces]], [[Interaction Protocols\|interaction protocols]], interaction channels, routing, ports and adapters, network, and brokers                  |
| Adaptation and resource management | Adapter, Bridge, Interceptor, Strategy, Component Configurator, Object Manager, Pool, Cache, Activator, Evictor, Leasing | architecture practices and replaceable realization mechanisms with lifecycle and capability obligations                                                                |

## Naming Discipline

POSA and object-design catalogs contain names that resemble Cohesive semantic concepts. POSA Observer, Command, State, Message, or Process roles are structural or implementation patterns unless a separate semantic correspondence is established. A Reactor is an event-demultiplexing mechanism, not the semantic [[Observer|observer]] or [[Process|process]] whose work it schedules. Active Object supplies a concurrency arrangement; it does not make the hosted object a domain [[Entity|entity]].

POSA Volume 4 is also an important precedent for this project: it composes patterns from EIP, enterprise application architecture, object design, concurrency, networking, and resource management. Cohesive adds explicit realm separation and preservation conditions to that pattern-language integration.

## External References

- Frank Buschmann, Regine Meunier, Hans Rohnert, Peter Sommerlad, and Michael Stal, [*Pattern-Oriented Software Architecture, Volume 1: A System of Patterns*](https://www.wiley.com/en-us/Pattern-Oriented+Software+Architecture%2C+Volume+1%2C+A+System+of+Patterns-p-9781118725269), Wiley, 1996.
- Douglas C. Schmidt, Michael Stal, Hans Rohnert, and Frank Buschmann, [*Pattern-Oriented Software Architecture, Volume 2: Patterns for Concurrent and Networked Objects*](https://www.wiley.com/en-us/Pattern-Oriented+Software+Architecture%2C+Volume+2%2C+Patterns+for+Concurrent+and+Networked+Objects-p-9781118725177), Wiley, 2000.
- Frank Buschmann, Kevlin Henney, and Douglas C. Schmidt, [*Pattern-Oriented Software Architecture, Volume 4: A Pattern Language for Distributed Computing*](https://www.wiley.com/en-us/Pattern-Oriented+Software+Architecture%2C+Volume+4%2C+A+Pattern+Language+for+Distributed+Computing-p-9780470065303), Wiley, 2007.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[System Graph|system graph]], [[Enterprise Integration Patterns|enterprise integration patterns]], [[Patterns of Enterprise Application Architecture|enterprise application patterns]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Flow Views|flow views]], [[Observer Models|observer models]], [[Scheduling|scheduling]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Concurrency Control|concurrency control]], [[Runtimes|runtimes]], [[Network|network]], [[Brokers|brokers]], [[Realization|realization]].
