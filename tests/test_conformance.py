# Copyright 2026 FxMEDUS LLC. Apache-2.0.
"""Tests for the AIDD-GOV reference conformance validator."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import aidd_gov_validate as v  # noqa: E402

SPEC = v.load_spec(ROOT / "AIDD-GOV-SPEC-v0.1.yaml")


def _bundle(name):
    return json.loads((ROOT / "examples" / name).read_text())


def test_conformant_bundle_passes_level1():
    r = v.validate_bundle(_bundle("level1_conformant.json"), 1, SPEC)
    assert r["conformant"] is True
    assert r["issues"] == {}


def test_nonconformant_bundle_fails_level1():
    r = v.validate_bundle(_bundle("level1_nonconformant.json"), 1, SPEC)
    assert r["conformant"] is False
    # invalid enum on decision is detected
    assert any("decision" in i for i in r["issues"]["StageDecisionRecord"])
    # missing nested integrity field is detected
    assert any("integrity.ledger_index" in i for i in r["issues"]["StageDecisionRecord"])
    # missing required field detected
    assert any("actor" in i for i in r["issues"]["AuditEvent"])
    # wrong type detected
    assert any("expected array" in i for i in r["issues"]["StageGatePipeline"])


def test_missing_required_schema_fails():
    b = _bundle("level1_conformant.json")
    del b["StageGatePipeline"]
    r = v.validate_bundle(b, 1, SPEC)
    assert r["conformant"] is False
    assert "StageGatePipeline" in r["issues"]


def test_level1_bundle_is_insufficient_for_level2():
    # A valid Level-1 bundle must fail Level 2 (missing ConstraintPolicy etc.)
    r = v.validate_bundle(_bundle("level1_conformant.json"), 2, SPEC)
    assert r["conformant"] is False
    for s in ("ConstraintPolicy", "RewardArchitecture", "ConvergenceCriteria"):
        assert s in r["issues"]


def test_single_schema_mode():
    sdr = _bundle("level1_conformant.json")["StageDecisionRecord"]
    issues = v.validate_record(sdr, "StageDecisionRecord", SPEC["schemas"]["StageDecisionRecord"])
    assert issues == []


def test_bool_not_accepted_as_integer():
    err = v._check_type(True, "integer")
    assert err is not None


def test_all_three_levels_defined():
    for lvl in (1, 2, 3):
        assert v.required_schemas_for_level(SPEC, lvl)
