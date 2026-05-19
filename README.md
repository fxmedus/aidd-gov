# AIDD-GOV

**AI Drug Discovery Governance Standard**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Version: 0.1](https://img.shields.io/badge/Version-0.1%20(Draft)-orange.svg)](AIDD-GOV-SPEC-v0.1.yaml)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--9929--3135-a6ce39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0001-9929-3135)

AIDD-GOV is an open governance specification for AI-driven drug discovery pipelines. It defines machine-readable schemas for decision records, stage gates, constraint policies, reward architectures, audit trails, convergence criteria, and kill switches.

**Author:** Julian Borges, MD, MS — Frontier Translational Research Lab, Department of Computer Science, Boston University

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

## Reference Implementation and Downstream Consumers

**DrugSynth AI** ([github.com/fxmedus/drugsynth-ai](https://github.com/fxmedus/drugsynth-ai)) implements AIDD-GOV Level 3 (Full) across three governed discovery campaigns targeting mitochondrial therapeutics. The platform operates a 67-agent architecture with 536 tests across 5 tiers, producing dual outputs per stage (machine-readable YAML registries and peer-reviewed IMRAD manuscripts). 10 manuscripts completed, 8 under journal review, 5 ChemRxiv preprints, 10 Zenodo data deposits.

**GeneVector Track** ([github.com/fxmedus/genevector-track](https://github.com/fxmedus/genevector-track)) is a four-paper thesis series that consumes AIDD-GOV governed pipeline outputs. The Therapeutic Candidate Decision Record (TCDR) standard ingests StageDecisionRecords from AIDD-GOV compliant pipelines and transforms them into structured multi-criteria evaluations. The Evidence Readiness Index (ERI) operates downstream of TCDR to optimize experimental investment across evidence gaps identified by the governed pipeline.

| Consumer | Relationship to AIDD-GOV |
|----------|--------------------------|
| DrugSynth AI | Reference implementation (Level 3 Full) |
| TCDR Standard (GeneVector P1) | Consumes SDRs as evaluation input |
| TCDR Engine (GeneVector P2) | Scores candidates using governed pipeline data |
| MitoCoreX Case Series (GeneVector P3) | Evaluates 20 candidates from AIDD-GOV compliant campaigns |
| Evidence Readiness Index (GeneVector P4) | Optimizes gap resolution based on governed evaluation |

## Validation Evidence (Preprints)

| Venue | Title | DOI |
|-------|-------|-----|
| ChemRxiv | ADMET Profiling of a Mitochondria-Focused Compound Library | [10.26434/chemrxiv.15001519/v1](https://doi.org/10.26434/chemrxiv.15001519/v1) |
| ChemRxiv | AI-Assisted De Novo Design of Small Molecule Candidates | [10.26434/chemrxiv.15001592/v1](https://doi.org/10.26434/chemrxiv.15001592/v1) |
| ChemRxiv | Computational Druggability Assessment of Mitochondrial Targets | [10.26434/chemrxiv.15001595/v1](https://doi.org/10.26434/chemrxiv.15001595/v1) |
| ChemRxiv | DrugSynthAI Computational Validation | [10.26434/chemrxiv.15001670/v1](https://doi.org/10.26434/chemrxiv.15001670/v1) |
| ChemRxiv | Pan-Mitochondrial Privileged Scaffolds | [10.26434/chemrxiv.15001671/v1](https://doi.org/10.26434/chemrxiv.15001671/v1) |
| SSRN | MitoCorex: Validated AI Pipeline for Precision Drug Design | [10.2139/ssrn.6494079](https://doi.org/10.2139/ssrn.6494079) |
| SSRN | DrugSynth AI: AI Pipeline for De Novo Molecule Design | [10.2139/ssrn.6493958](https://doi.org/10.2139/ssrn.6493958) |
| Harvard Dataverse | MitoCoreX Compound Library and Validation Data | [10.7910/DVN/WGHUWM](https://doi.org/10.7910/DVN/WGHUWM) |

## Citation

```
Borges J (2026). AIDD-GOV: An Open Governance Standard for AI Drug Discovery.
Version 0.1. https://github.com/fxmedus/aidd-gov

Borges J (2026). DrugSynth AI: An AI Pipeline for De Novo Molecule Design
Targeting Genetically Defined Mitochondrial Defects. SSRN: 10.2139/ssrn.6493958

Borges J (2026). MitoCorex: A Validated AI Pipeline for Precision Drug Design.
SSRN: 10.2139/ssrn.6494079
```

## License

Apache License 2.0. See [LICENSE](LICENSE) and [PATENT-NOTICE.md](PATENT-NOTICE.md).

---

**Contact:** [jyborges@bu.edu](mailto:jyborges@bu.edu) · [Academic CV](https://julian-borges-md.github.io/research-profile/) · [ORCID](https://orcid.org/0009-0001-9929-3135)

---

<div align="center">

**Frontier Translational Research Lab**

Department of Computer Science · Boston University · Harvard Medical School GCSRT Alumni

[![Lab Website](https://img.shields.io/badge/Lab-frontier--lab-002244?style=flat-square)](https://julian-borges-md.github.io/frontier-lab/)
[![BU CS](https://img.shields.io/badge/BU-Computer_Science-cc0000?style=flat-square)](https://www.bu.edu/cs/)
[![HMS](https://img.shields.io/badge/HMS-GCSRT_Alumni-a51c30?style=flat-square)](https://ghsm.hms.harvard.edu/education/global-clinical-scholars-research-training)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--9929--3135-a6ce39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0001-9929-3135)
[![CV](https://img.shields.io/badge/Academic_CV-research--profile-4f46e5?style=flat-square)](https://julian-borges-md.github.io/research-profile/)

*Julian Borges, MD, MS · jyborges@bu.edu*

</div>
