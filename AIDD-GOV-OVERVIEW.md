# AIDD-GOV: AI Drug Discovery Governance Standard

**Version:** 0.1 (Public Draft)  
**Date:** 2026-03-29  
**Author:** Julian Borges, MD — FxMEDUS LLC / Boston University, Department of Computer Science  
**ORCID:** 0009-0001-9929-3135  
**License:** Apache License 2.0 (specification text)  
**Patent Notice:** Implementation systems may be subject to patent protection. See [PATENT-NOTICE.md](PATENT-NOTICE.md).  
**Companion Paper:** Borges J (2026). *DrugSynthAI: A Governance-First Platform for AI-Governed Drug Discovery.* [DOI pending]

---

## 1. Purpose

AI-driven drug discovery pipelines increasingly generate candidate molecules, binding predictions, ADMET profiles, and optimization trajectories using opaque computational methods. When these candidates advance toward preclinical and clinical evaluation, regulators, institutional review boards, and development partners require answers to fundamental governance questions:

- **Provenance:** How was this molecule nominated? What decisions led to its selection?
- **Auditability:** Can every stage gate decision be reconstructed from the audit trail?
- **Constraint enforcement:** Were safety thresholds defined before the campaign started? Were they enforced?
- **Optimization transparency:** How did the RL reward function converge? What termination criteria were applied?
- **Kill switch documentation:** Were emergency termination mechanisms defined and monitored?

No industry standard currently addresses these questions. AIDD-GOV fills this gap.

## 2. Scope

AIDD-GOV defines **what must be recorded**, not **how it is computed**.

Implementations may use any algorithm, model, or scoring function. The standard requires that governance artifacts conform to specified schemas so that regulators, auditors, and collaborators can evaluate pipeline decisions without access to proprietary methods.

The specification covers:

- **StageDecisionRecords (SDRs):** Immutable records of every stage gate decision
- **Audit Events:** Structured logs of every significant pipeline action
- **Stage Gate Pipelines:** Ordered stage sequences with entry/exit criteria
- **Constraint Policies:** Hard and soft constraints with pre-declared thresholds
- **Reward Architectures:** Multi-objective reward function structure (not values)
- **Convergence Criteria:** RL termination rules
- **Kill Switches:** Emergency campaign termination mechanisms
- **Toxicity Alerts:** Structural alert rule registries
- **Exclusion Zones:** Patent and IP exclusion zone definitions
- **Objective Definitions:** Multi-objective scoring function specifications

The specification does **not** cover:

- Specific molecular representations or file formats (SDF, MOL2, PDB)
- Docking software selection or parameterization
- Machine learning model architectures or training procedures
- Proprietary reward function weight values
- Novel compound structures (SMILES, InChI)

## 3. Conformance Levels

AIDD-GOV defines three conformance levels. Each level builds on the previous one.

### Level 1: Core

Minimum viable governance. Suitable for academic research pipelines and early-stage discovery.

| Schema | Purpose |
|--------|---------|
| StageDecisionRecord | Immutable decision provenance for every gate |
| AuditEvent | Append-only log of pipeline actions |
| StageGatePipeline | Ordered stages with entry/exit criteria |

**What this enables:** A reviewer can trace any candidate molecule back through every decision that advanced it. The audit trail answers "why was this molecule nominated?"

### Level 2: Standard

Production governance. Suitable for industry pipelines and regulatory engagement.

| Schema | Purpose |
|--------|---------|
| All Level 1 schemas | (inherited) |
| ConstraintPolicy | Pre-declared hard/soft thresholds, kill conditions |
| RewardArchitecture | RL reward function structure and component definitions |
| ConvergenceCriteria | Pre-specified RL termination rules |

**What this enables:** A regulator can verify that constraints were declared before the campaign started, that the optimization had defined stopping criteria, and that the reward function structure is documented.

### Level 3: Full

Comprehensive governance. Required for FDA pre-submission engagement and CRO partnerships.

| Schema | Purpose |
|--------|---------|
| All Level 2 schemas | (inherited) |
| KillSwitch | Emergency campaign termination definitions |
| ToxicityAlerts | Structural alert rule registry |
| ExclusionZones | Patent/IP exclusion zone definitions |
| ObjectiveDefinitions | Multi-objective scoring function specification |

**What this enables:** A CRO partner receives a complete governance package with every compound nomination. A regulatory submission can reference AIDD-GOV Level 3 compliance as evidence of algorithmic accountability.

---

## 4. Design Principles

**Immutability.** SDRs and audit events are append-only. Once issued, they cannot be modified or deleted. Corrections require new records that reference the original.

**Pre-declaration.** Constraint policies, convergence criteria, and kill switch definitions must be declared before campaign initialization and locked for the campaign's duration.

**Platform authority.** Only the platform governance layer may issue SDRs. Domain agents and application code cannot create, modify, or override governance decisions.

**Separation of structure and values.** The standard requires that the reward function's component structure, normalization methods, and optimization directions are documented. It does not require disclosure of proprietary weight values.

**Domain neutrality.** The reference pipeline (S00-S10) targets small-molecule discovery. The governance invariants (ordered stages, SDR gating, audit trails, kill switches) apply to any therapeutic modality.

---

## 5. Regulatory Alignment

AIDD-GOV is designed to satisfy emerging regulatory expectations for AI/ML in drug development:

| Regulatory Framework | AIDD-GOV Alignment |
|---------------------|-------------------|
| FDA Draft Guidance on AI/ML in Drug Development (2023) | SDRs provide decision transparency; audit trails satisfy traceability requirements |
| ICH Q8(R2) Quality-by-Design | Pre-declared constraints and objectives align with QbD design space principles |
| 21 CFR Part 11 Electronic Records | Immutable SDRs with checksums satisfy electronic record integrity requirements |
| EMA Reflection Paper on AI (2023) | Kill switches and governance reports address algorithmic accountability |

AIDD-GOV does not guarantee regulatory compliance. It provides a governance framework that facilitates compliance by producing the artifacts regulators require.

---

## 6. Reference Implementation

The first implementation of AIDD-GOV is DrugSynthAI, an AI-governed drug discovery platform developed by FxMEDUS LLC in collaboration with Boston University's Department of Computer Science.

DrugSynthAI implements AIDD-GOV Level 3 (Full) and has been validated across three governed discovery campaigns targeting mitochondrial therapeutics. The platform's governance architecture, stage gate pipeline, and audit trail system are described in the companion publication.

Patent pending: US Provisional Application 64/018,624, filed March 27, 2026.

---

## 7. Contributing

AIDD-GOV is an open specification. Contributions are welcome via GitHub issues and pull requests at [github.com/fxmedus/aidd-gov](https://github.com/fxmedus/aidd-gov).

Areas where community input is specifically sought:

- **Biologics and peptide pipelines:** Stage gate definitions for non-small-molecule modalities
- **Federated governance:** Schemas for multi-site campaign governance without sharing proprietary data
- **Regulatory feedback:** Alignment corrections based on regulatory agency guidance
- **Interoperability:** Mappings to existing standards (CDISC, HL7 FHIR, FAIR data principles)

---

## 8. Versioning

This specification follows [Semantic Versioning](https://semver.org).

- **0.x (current):** Draft releases. May contain breaking changes.
- **1.0 (target):** First stable release. Breaking changes require major version increment.

The path to 1.0 requires: community review feedback, at least one independent implementation, and alignment verification against published FDA/EMA guidance.

---

## 9. License and Patent Notice

The AIDD-GOV specification text is licensed under the [Apache License 2.0](LICENSE).

Systems that implement the AIDD-GOV specification may be subject to patent protection. See [PATENT-NOTICE.md](PATENT-NOTICE.md) for details.

The specification is free to read, cite, and implement. The patent applies to specific implementation methods, not to the governance schema definitions themselves.

