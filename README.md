<p align="center">
  <strong>AIDD-GOV</strong><br>
  <em>Open Governance Standard for AI-Driven Drug Discovery Pipelines</em>
</p>

<p align="center">
  <a href="https://github.com/fxmedus/aidd-gov/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square" alt="License"></a>
  <a href="AIDD-GOV-SPEC-v0.1.yaml"><img src="https://img.shields.io/badge/Spec-v0.1%20Draft-orange.svg?style=flat-square" alt="Version"></a>
  <a href="https://orcid.org/0009-0001-9929-3135"><img src="https://img.shields.io/badge/ORCID-0009--0001--9929--3135-a6ce39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a>
  <img src="https://img.shields.io/badge/Schemas-10-2563eb?style=flat-square" alt="Schemas">
  <img src="https://img.shields.io/badge/Conformance%20Levels-3-2563eb?style=flat-square" alt="Levels">
  <a href="https://www.fda.gov/media/167973/download"><img src="https://img.shields.io/badge/FDA-Docket%20FDA--2024--D--4689-154360?style=flat-square" alt="FDA"></a>
</p>

---

## Why

Every AI drug discovery platform operates as a black box. When regulators ask "how was this molecule nominated?", the answer is a PowerPoint, not an audit trail.

AIDD-GOV changes this by standardizing the governance artifacts that every pipeline should produce. The specification defines **what** must be recorded. It does not prescribe **how** it is computed. Proprietary algorithms, models, and scoring functions remain proprietary. The governance layer becomes transparent.

**Author:** Julian Yin Vieira Borges, MD, MS — Frontier Translational Research Lab (Independent, FxMEDUS LLC)
**Contact:** jyborges@bu.edu · **ORCID:** [0009-0001-9929-3135](https://orcid.org/0009-0001-9929-3135)

---

## Conformance Levels

| Level | Name | Schemas Required | Use Case |
|:---:|------|-----------------|----------|
| **1** | Core | SDR, AuditEvent, StageGatePipeline | Academic research pipelines |
| **2** | Standard | Level 1 + ConstraintPolicy, RewardArchitecture, ConvergenceCriteria | Industry pipelines, regulatory engagement |
| **3** | Full | Level 2 + KillSwitch, ToxicityAlerts, ExclusionZones, ObjectiveDefinitions | FDA pre-submission, CRO partnerships |

---

## The 10 Schemas

| # | Schema | Purpose |
|:---:|--------|---------|
| 1 | **StageDecisionRecord (SDR)** | Immutable, append-only record of every stage gate decision |
| 2 | **AuditEvent** | Timestamped event log with 28 action codes |
| 3 | **StageGatePipeline** | Pipeline topology: stages, entry/exit conditions, kill switches |
| 4 | **ConstraintPolicy** | Hard constraints that cannot be overridden by optimization |
| 5 | **RewardArchitecture** | Multi-objective reward function structure and versioning |
| 6 | **ConvergenceCriteria** | RL loop termination conditions |
| 7 | **KillSwitch** | Binary halt conditions at every stage boundary |
| 8 | **ToxicityAlerts** | Structural alert rules and toxicity flag definitions |
| 9 | **ExclusionZones** | Chemical space regions excluded from generation |
| 10 | **ObjectiveDefinitions** | Formal multi-objective scoring function specifications |

---

## FDA Regulatory Alignment

AIDD-GOV implements the principles of the FDA's January 2025 draft guidance *"Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products"* (Docket FDA-2024-D-4689).

| FDA Step | AIDD-GOV Construct |
|:---:|-------------------|
| 1. Define context of use | Campaign binding + target registry |
| 2. Assess model risk | Kill conditions + constraint policies |
| 3. Credibility assessment plan | Stage gate plan + IVVP selection |
| 4. Execute assessment | Dual-attestation pipeline (SDR) |
| 5. Document results | Immutable audit trail (WAL) |
| 6. Review and communicate | Compliance reports + handoff packages |
| 7. Lifecycle monitoring | Curation policy + reward versioning |

Full guidance: [FDA-2024-D-4689 (PDF)](https://www.fda.gov/media/167973/download)

---

## Repository Structure

```
aidd-gov/
├── AIDD-GOV-SPEC-v0.1.yaml     # Machine-readable spec (10 schemas, 857 lines)
├── AIDD-GOV-OVERVIEW.md         # Human-readable overview with rationale
├── PATENT-NOTICE.md             # Patent notice (open spec vs. patented implementations)
├── POSITIONING-M10.md           # Academic positioning for companion publication
└── LICENSE                      # Apache 2.0
```

---

## Quick Start

1. Read [`AIDD-GOV-OVERVIEW.md`](AIDD-GOV-OVERVIEW.md) for rationale and design principles
2. Review [`AIDD-GOV-SPEC-v0.1.yaml`](AIDD-GOV-SPEC-v0.1.yaml) for schema definitions
3. Implement schemas appropriate to your conformance level
4. Produce a compliance self-assessment mapping your artifacts to AIDD-GOV schemas

---

## Reference Implementation and Downstream Consumers

**DrugSynthAI** ([drugsynth.ai](https://drugsynth.ai)) implements AIDD-GOV Level 3 (Full) across three governed discovery campaigns targeting mitochondrial therapeutics. The platform operates a 67-agent architecture with 536 tests across 5 tiers, producing dual outputs per stage (machine-readable YAML registries and peer-reviewed IMRAD manuscripts). 10 manuscripts completed, 8 under journal review, 5 ChemRxiv preprints, 10 Zenodo data deposits.

**GeneVector Track** ([github.com/fxmedus/genevector-track](https://github.com/fxmedus/genevector-track)) is a four-paper thesis series that consumes AIDD-GOV governed pipeline outputs. The TCDR standard ingests StageDecisionRecords from AIDD-GOV compliant pipelines. The ERI operates downstream of TCDR to optimize experimental investment across evidence gaps.

| Consumer | Relationship to AIDD-GOV |
|----------|--------------------------|
| DrugSynthAI | Reference implementation (Level 3 Full) |
| TCDR Standard (GeneVector P1) | Consumes SDRs as evaluation input |
| TCDR Engine (GeneVector P2) | Scores candidates using governed pipeline data |
| MitoCoreX Case Series (GeneVector P3) | Evaluates 20 candidates from AIDD-GOV compliant campaigns |
| Evidence Readiness Index (GeneVector P4) | Optimizes gap resolution based on governed evaluation |

---

## Validation Evidence

| Venue | Title | DOI |
|:---:|-------|:---:|
| ChemRxiv | ADMET Profiling of a Mitochondria-Focused Compound Library | [`10.26434/chemrxiv.15001519`](https://doi.org/10.26434/chemrxiv.15001519/v1) |
| ChemRxiv | AI-Assisted De Novo Design of Small Molecule Candidates | [`10.26434/chemrxiv.15001592`](https://doi.org/10.26434/chemrxiv.15001592/v1) |
| ChemRxiv | Computational Druggability Assessment of Mitochondrial Targets | [`10.26434/chemrxiv.15001595`](https://doi.org/10.26434/chemrxiv.15001595/v1) |
| ChemRxiv | DrugSynthAI Computational Validation | [`10.26434/chemrxiv.15001670`](https://doi.org/10.26434/chemrxiv.15001670/v1) |
| ChemRxiv | Pan-Mitochondrial Privileged Scaffolds | [`10.26434/chemrxiv.15001671`](https://doi.org/10.26434/chemrxiv.15001671/v1) |
| SSRN | MitoCorex: Validated AI Pipeline for Precision Drug Design | [`10.2139/ssrn.6494079`](https://doi.org/10.2139/ssrn.6494079) |
| SSRN | DrugSynth AI: AI Pipeline for De Novo Molecule Design | [`10.2139/ssrn.6493958`](https://doi.org/10.2139/ssrn.6493958) |
| Harvard | MitoCoreX Compound Library and Validation Data | [`10.7910/DVN/WGHUWM`](https://doi.org/10.7910/DVN/WGHUWM) |

---

## Citation

```bibtex
@misc{borges2026aiddgov,
  author       = {Borges, Julian Yin Vieira},
  title        = {AIDD-GOV: An Open Governance Standard for AI Drug Discovery},
  year         = {2026},
  version      = {0.1},
  publisher    = {GitHub},
  url          = {https://github.com/fxmedus/aidd-gov},
  license      = {Apache-2.0}
}
```

---

## Intellectual Property

Released under Apache 2.0. AIDD-GOV defines an open governance standard. Implementations (including scoring weights, reward functions, and proprietary algorithms) may be separately protected. See [PATENT-NOTICE.md](PATENT-NOTICE.md).

---

<p align="center">
  <a href="https://julian-borges-md.github.io/frontier-lab/"><img src="https://img.shields.io/badge/Lab-Frontier%20Translational%20Research-002244?style=flat-square" alt="Lab"></a>
  <a href="https://www.bu.edu/cs/"><img src="https://img.shields.io/badge/BU-Computer%20Science-cc0000?style=flat-square" alt="BU CS"></a>
  <a href="https://ghsm.hms.harvard.edu/education/global-clinical-scholars-research-training"><img src="https://img.shields.io/badge/HMS-GCSRT%20Alumni-a51c30?style=flat-square" alt="HMS"></a>
  <a href="https://orcid.org/0009-0001-9929-3135"><img src="https://img.shields.io/badge/ORCID-0009--0001--9929--3135-a6ce39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a>
</p>

<p align="center"><em>Julian Yin Vieira Borges, MD, MS · jyborges@bu.edu</em></p>

## Conformance validation (reference tool)

`tools/aidd_gov_validate.py` is the reference validator. It reads the conformance
levels and schema field definitions directly from `AIDD-GOV-SPEC-v0.1.yaml`, so it
never drifts from the standard. No proprietary methods, weights, or scoring logic
are involved; it checks structural conformance only.

```bash
# Validate a bundle against a conformance level (1 Core, 2 Standard, 3 Full)
python3 tools/aidd_gov_validate.py --artifact examples/level1_conformant.json --level 1

# Validate a single record against one schema
python3 tools/aidd_gov_validate.py --artifact sdr.json --schema StageDecisionRecord
```

A bundle is a JSON object mapping schema name to instance. Exit code is `0` when
conformant and `1` otherwise, so the tool drops directly into CI. Worked examples
live in `examples/` (one conformant, one with planted defects); `tests/` exercises
both plus level escalation and type checks.

| Level | Name | Required schemas |
|---|---|---|
| 1 | Core | StageDecisionRecord, AuditEvent, StageGatePipeline |
| 2 | Standard | Level 1 + ConstraintPolicy, RewardArchitecture, ConvergenceCriteria |
| 3 | Full | Level 2 + KillSwitch, ToxicityAlerts, ExclusionZones, ObjectiveDefinitions |
