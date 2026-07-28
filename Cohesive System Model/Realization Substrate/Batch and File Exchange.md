---
realm: Realization Substrate
kind: realization-substrate
created: 2026-07-27
updated: 2026-07-27
aliases:
  - File Transfer
  - File Exchange
  - Batch Exchange
---

# Batch and File Exchange

Batch and file exchange is a realization substrate for moving finite collections, documents, snapshots, deltas, manifests, or artifacts across system boundaries through durable named objects.

A file is a carrier and storage representation, not a semantic event, command, observation, or process. Creating, publishing, discovering, transferring, receiving, validating, and admitting a file are distinct occurrences. At a receiving boundary, file arrival or discovery is an exogenous [[Event|event]] whose manifest and contents are interpreted by an [[Observer|observer]].

## Exchange Contract

A robust exchange may require:

- Stable batch, file, contract, source, subject, and attempt identities.
- Manifest, format, schema, semantic revision, checksums, signatures, and encryption context.
- Atomic publication or a completion marker so partial files are not admitted as complete.
- Snapshot, delta, sequence, partition, and consistent-cut meanings.
- Duplicate, replacement, late, missing, corrupt, and out-of-order handling.
- Retention, archival, quarantine, purge, and replay rules.
- Acknowledgment and reconciliation of which records were accepted, rejected, or committed.

File rename, object-store completion, checksum verification, or transfer acknowledgment proves only a local substrate claim. It does not prove that every record was semantically admitted or that downstream transitions committed.

Batch exchange can realize [[Interaction Channels|interaction channels]], document messages, claim checks, projection transfer, backfill, migration, model-artifact movement, or air-gapped integration. [[Storage Systems|Storage systems]], object stores, managed file transfer, shared volumes, email attachments, and removable media provide different durability, identity, ordering, security, and failure boundaries.

## External References

- Gregor Hohpe and Bobby Woolf, [File Transfer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/FileTransferIntegration.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Messages and Envelopes|messages and envelopes]], [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Event|event]], [[Observation|observation]], [[Shape|shape]], [[Compatibility and Evolution|compatibility and evolution]], [[Consistent Cuts|consistent cuts]], [[Delivery Semantics|delivery semantics]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Storage Systems|storage systems]], [[Network|network]].
