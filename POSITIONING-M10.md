# AIDD-GOV and the DrugSynthAI Platform Paper: Positioning Statement

**Date:** 2026-03-29  
**Author:** Julian Borges, MD  
**Context:** This document describes the relationship between the AIDD-GOV open specification and the companion academic publication (M10: Platform Architecture).

---

## The Two Artifacts

### 1. AIDD-GOV Specification (this repository)

An open, machine-readable governance standard for AI drug discovery pipelines. Licensed under Apache 2.0. Defines schemas for decision records, stage gates, constraint policies, reward architectures, audit trails, convergence criteria, and kill switches. Does not contain proprietary algorithms, weight values, or compound structures.

### 2. Companion Publication (M10)

**Title:** DrugSynthAI: A Governance-First Platform for AI-Governed Drug Discovery  
**Author:** Julian Borges, MD — FxMEDUS LLC / Boston University, Department of Computer Science  
**Submission targets:** SSRN (first), bioRxiv (preprint), Nature Methods or Bioinformatics (journal)  
**Patent notice:** Patent pending: US Provisional Application 64/018,624, filed March 27, 2026.

The paper describes the reference implementation of AIDD-GOV within the DrugSynthAI platform, including the 49-agent architecture, the S00-S10 stage gate pipeline, the StageDecisionRecord authority system, and validation results across three governed discovery campaigns targeting mitochondrial therapeutics.

---

## Strategic Relationship

The specification and the paper serve complementary purposes:

| Dimension | AIDD-GOV Spec | M10 Paper |
|-----------|--------------|-----------|
| **Audience** | Industry practitioners, regulators, standards bodies | Academic reviewers, researchers, regulators |
| **Content** | Schema definitions (what to record) | Implementation architecture (how it works) |
| **IP exposure** | None — schemas only, no proprietary methods | Controlled — computational framing, no novel SMILES or reward weights in preprint |
| **License** | Apache 2.0 (open) | Academic copyright (publisher) |
| **Longevity** | Versioned standard, community-maintained | Fixed publication record |
| **Citation value** | Establishes governance category | Validates the platform scientifically |

## Why Publish Both Simultaneously

**Category creation.** The paper validates the platform. The specification defines the category. Without the specification, the paper is one more AI drug discovery publication. Without the paper, the specification has no reference implementation. Together, they establish DrugSynthAI as both a validated platform and the origin of an industry governance standard.

**Patent protection.** The patent (US 64/018,624) protects the implementation methods. The open specification protects the ecosystem position. Competitors who adopt the standard validate the category DrugSynthAI created. Competitors who ignore the standard face regulatory disadvantage as governance expectations harden.

**Regulatory positioning.** FDA guidance on AI/ML in drug development (2023 draft) emphasizes transparency and auditability without prescribing formats. AIDD-GOV fills that gap. When the guidance is finalized (expected 2027-2028), organizations that already comply with AIDD-GOV have a structural advantage.

---

## Cross-Referencing Strategy

**In the M10 paper**, include the following in the Methods section:

> The governance architecture described in this paper conforms to AIDD-GOV v0.1, an open governance standard for AI drug discovery pipelines (https://github.com/fxmedus/aidd-gov). The specification defines machine-readable schemas for StageDecisionRecords, audit events, constraint policies, reward architectures, and convergence criteria. DrugSynthAI implements AIDD-GOV Level 3 (Full).

**In the AIDD-GOV repository**, the companion paper is referenced as the first implementation and the source of the reference pipeline definition.

---

## Publication Sequence

1. **Today:** Publish AIDD-GOV repository on GitHub (public, Apache 2.0)
2. **Next:** Submit M10 to SSRN with AIDD-GOV GitHub URL in Methods section
3. **Then:** Deposit M10 on bioRxiv with SSRN DOI reference
4. **Then:** Submit M10 to target journal with both SSRN and bioRxiv DOIs
5. **Ongoing:** Update AIDD-GOV README with DOIs as they become available

---

*Patent pending: US Provisional Application 64/018,624, filed March 27, 2026.*
