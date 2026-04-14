# AIDD-GOV

**AI Drug Discovery Governance Standard**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Version: 0.1](https://img.shields.io/badge/Version-0.1%20(Draft)-orange.svg)](AIDD-GOV-SPEC-v0.1.yaml)

AIDD-GOV is an open governance specification for AI-driven drug discovery pipelines. It defines machine-readable schemas for decision records, stage gates, constraint policies, reward architectures, audit trails, convergence criteria, and kill switches.

## Why

Every AI drug discovery platform operates as a black box. When regulators ask "how was this molecule nominated?", the answer is a PowerPoint, not an audit trail. AIDD-GOV changes this by standardizing the governance artifacts that every pipeline should produce.

The specification defines **what** must be recorded. It does not prescribe **how** it is computed. Proprietary algorithms, models, and scoring functions remain proprietary. The governance layer becomes transparent.

## Files

| File | Description |
|------|-------------|
| [AIDD-GOV-SPEC-v0.1.yaml](AIDD-GOV-SPEC-v0.1.yaml) | Machine-readable specification (10 schemas, 3 conformance levels) |
| [AIDD-GOV-OVERVIEW.md](AIDD-GOV-OVERVIEW.md) | Human-readable overview with rationale and conformance guidance |
| [PATENT-NOTICE.md](PATENT-NOTICE.md) | Patent notice distinguishing open spec from patented implementations |
| [POSITIONING-M10.md](POSITIONING-M10.md) | Academic positioning linking AIDD-GOV to the companion publication |
| [LICENSE](LICENSE) | Apache License 2.0 |

## Conformance Levels

| Level | Name | Schemas Required | Use Case |
|-------|------|-----------------|----------|
| 1 | Core | SDR, AuditEvent, StageGatePipeline | Academic research pipelines |
| 2 | Standard | Level 1 + ConstraintPolicy, RewardArchitecture, ConvergenceCriteria | Industry pipelines, regulatory engagement |
| 3 | Full | Level 2 + KillSwitch, ToxicityAlerts, ExclusionZones, ObjectiveDefinitions | FDA pre-submission, CRO partnerships |

## Quick Start

1. Read [AIDD-GOV-OVERVIEW.md](AIDD-GOV-OVERVIEW.md) for rationale and design principles
2. Review [AIDD-GOV-SPEC-v0.1.yaml](AIDD-GOV-SPEC-v0.1.yaml) for schema definitions
3. Implement schemas appropriate to your conformance level
4. Produce a compliance self-assessment mapping your artifacts to AIDD-GOV schemas

## FDA Regulatory Alignment

AIDD-GOV implements the principles of the FDA's January 2025 draft guidance *"Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products"* (Docket FDA-2024-D-4689). The FDA's 7-step credibility assessment framework maps to AIDD-GOV constructs:

| FDA Step | AIDD-GOV Construct |
|----------|-------------------|
| 1. Define context of use | Campaign binding + target registry |
| 2. Assess model risk | Kill conditions + constraint policies |
| 3. Credibility assessment plan | Stage gate plan + IVVP selection |
| 4. Execute assessment | Dual-attestation pipeline (SDR) |
| 5. Document results | Immutable audit trail (WAL) |
| 6. Review and communicate | Compliance reports + handoff packages |
| 7. Lifecycle monitoring | Curation policy + reward versioning |

Full guidance PDF: https://www.fda.gov/media/167973/download

## Reference Implementation

[DrugSynthAI](https://github.com/fxmedus/drugsynth-ai) implements AIDD-GOV Level 3 (Full) across three governed discovery campaigns. See the companion publication for details.

## Citation

If you use AIDD-GOV in academic work, please cite:

```
Borges J (2026). AIDD-GOV: An Open Governance Standard for AI Drug Discovery.
Version 0.1. https://github.com/fxmedus/aidd-gov

Borges J (2026). DrugSynthAI: A Governance-First Platform for AI-Governed
Drug Discovery. [DOI pending]
```

## License

Apache License 2.0. See [LICENSE](LICENSE) and [PATENT-NOTICE.md](PATENT-NOTICE.md).

