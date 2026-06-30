---
realm: Operational Semantics
kind: operational-semantics
---

# Version Histories

Version Histories describe the shape of state evolution for a subject, entity, document, repository, projection, or replicated object.

A history shape determines which versions can succeed which other versions, whether concurrent successors are allowed, and whether later work must reject, branch, merge, commute, or converge.

Common history shapes include:

- **Linear histories**, where each accepted transition has at most one successor from the current version.
- **Branching histories**, where several successors may share the same parent.
- **DAG histories**, where versions may have multiple parents and merges are explicit.
- **Partial-order histories**, where causally related versions are ordered and concurrent versions may be incomparable.
- **Patch histories**, where morphisms between states represent patches, edits, or state actions.
- **Join histories**, where updates converge through a semilattice join or other merge algebra.

Scalar versions, stream offsets, vector clocks, causal contexts, Git commit graphs, event streams, workflow histories, and CRDT metadata are different realizations of version-history shape. The realization must preserve the distinctions the model needs: succession, causality, concurrency, incompatibility, mergeability, replay, audit, or convergence.

A consistent cut selects versions, events, or observations from a history while respecting causal prerequisites. It is useful when a read, checkpoint, projection rebuild, or recovery process must observe several parts of a history coherently.

## Patch Histories and Pushout Merge

A patch model treats states such as files or documents as objects and patches as morphisms between them. Two patches from a common base form a span:

```txt
base -> left
base -> right
```

If the patches can be merged, the merged state and residual patches can be characterized by a pushout square. The pushout gives a universal-property account of "the same effect after the other patch": each side can be applied after accounting for the other, and the resulting merged object is canonical relative to that diagram.

When patches conflict, the ordinary category of states and patches may lack the required pushout. One response is to work in a larger category that freely adds the missing finite colimits, so incompatible or unresolved merge states can be represented rather than hidden.

In this view, patches are [[Event|events]] or state actions with causality and incompatibility structure. Repository import, branch merge, shared-document editing, and patch-based synchronization can be modeled as diagrams whose merge or conflict behavior is determined by the available colimits.

The Cohesive model does not require every version history to be patch-theoretic. The point is that merge, residual, conflict, and equivalence should be specified by the history shape rather than assumed from a scalar version counter.

## Relationship to Concurrency Control

[[Concurrency Control]] depends on history shape.

For a linear entity, an expected-version check can enforce a single successor from the current version. For a branching or DAG history, concurrency control may instead ask whether a proposed successor has acceptable parents, whether a branch head may advance, whether a merge is valid, or whether conflicting successors must be preserved.

For [[CRDTs]], the history shape is often less about selecting one successor and more about preserving enough causal metadata for concurrent updates to commute, merge, or converge.

## Relationship to Consistency Models

[[Consistency Models]] constrain which observations are valid for a history. Some models require that operations admit a single legal total order. Others allow partial orders, causal orders, branching histories, or eventually convergent replica histories.

The history shape determines what kind of consistency claim can be meaningful. A linearizable object needs a legal linearization. A Git-like repository needs parent, branch, and merge semantics. A collaborative document may need patch residuals or operational-transform/CRDT semantics. A replicated cache may only promise eventual convergence within a stated boundary.

## External References

- Samuel Mimram and Cinzia Di Giusto, [A Categorical Theory of Patches](https://arxiv.org/abs/1311.3903), 2013.

Related concepts: [[Version|version]], [[Ordering|ordering]], [[Time|time]], [[Concurrency Control|concurrency control]], [[Consistency Models|consistency models]], [[Event-State Duality|event-state duality]], [[Event|event]], [[State|state]], [[Transition|transition]], [[CRDTs]], [[Universal Constructions|universal constructions]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]].
