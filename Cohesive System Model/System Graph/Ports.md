---
realm: System Graph
kind: structural-construct
created: 2026-11-05
updated: 2026-11-05
---

# Ports

A port is an occurrence of an [[Interfaces|interface]] on a [[Surfaces|surface]]. It states who provides or requires that interface at this boundary, under which policy and assumptions. Two ports can share an interface while exposing different authority or failure conditions.

An [[Endpoints|endpoint]] binds a port into a particular channel arrangement. A port need not select an address, transport, or runtime. The [[Ports and Adapters|ports and adapters]] practice uses this distinction to organize an application and its adapters; a port can be modeled without adopting the practice.

## Formal relations

- `arranges`: [[Interfaces]] — Places an occurrence of a reusable interface on a surface with boundary-specific roles and obligations.
- `distinguished_from`: [[Endpoints]] — The port declares participation; the endpoint identifies its attachment in a channel arrangement.
