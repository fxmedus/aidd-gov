#!/usr/bin/env python3
# Copyright 2026 FxMEDUS LLC. Apache-2.0.
"""AIDD-GOV reference conformance validator.

Spec-driven: the single source of truth is AIDD-GOV-SPEC-v0.1.yaml. This tool
reads the conformance levels and schema field definitions directly from the
spec, so it can never drift from the standard.

Usage:
    python3 tools/aidd_gov_validate.py --artifact bundle.json --level 1
    python3 tools/aidd_gov_validate.py --artifact sdr.json --schema StageDecisionRecord

A "bundle" artifact is a JSON object mapping schema name -> instance, e.g.
    {"StageDecisionRecord": {...}, "AuditEvent": {...}, "StageGatePipeline": {...}}
A single-record artifact is one instance validated with --schema NAME.

Exit code 0 = conformant, 1 = non-conformant, 2 = usage/spec error.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

_TYPE_MAP = {
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "array": list,
    "object": dict,
}


def load_spec(spec_path: Path) -> dict:
    with open(spec_path) as fh:
        return yaml.safe_load(fh)


def required_schemas_for_level(spec: dict, level: int) -> list[str]:
    for lvl in spec["specification"]["conformance_levels"]:
        if int(lvl["level"]) == level:
            return list(lvl["required_schemas"])
    raise ValueError(f"Conformance level {level} not defined in spec")


def _check_type(value, declared: str, enum_values=None) -> str | None:
    """Return an error string, or None if the value's type is acceptable."""
    if declared == "enum":
        if enum_values is not None and value not in enum_values:
            return f"value {value!r} not in allowed {enum_values}"
        return None
    py = _TYPE_MAP.get(declared)
    if py is None:
        return None  # unknown declared type -> do not block (forward-compatible)
    # bool is a subclass of int; guard so a bool is not accepted as integer
    if declared == "integer" and isinstance(value, bool):
        return "expected integer, got boolean"
    if not isinstance(value, py):
        return f"expected {declared}, got {type(value).__name__}"
    return None


def _validate_fieldset(instance: dict, fields: dict, prefix: str = "") -> list[str]:
    issues: list[str] = []
    for fname, fdef in (fields or {}).items():
        if not isinstance(fdef, dict):
            continue
        required = bool(fdef.get("required", False))
        present = fname in instance
        if required and not present:
            issues.append(f"MISSING required field: {prefix}{fname}")
            continue
        if not present:
            continue
        err = _check_type(instance[fname], fdef.get("type", ""), fdef.get("values"))
        if err:
            issues.append(f"FIELD {prefix}{fname}: {err}")
    return issues


def validate_record(instance: dict, schema_name: str, schema_def: dict) -> list[str]:
    issues: list[str] = []
    if not isinstance(instance, dict):
        return [f"{schema_name}: instance must be a JSON object"]
    issues += _validate_fieldset(instance, schema_def.get("fields", {}))
    # integrity block, when defined, is a required nested object
    integ = schema_def.get("integrity")
    if integ:
        if "integrity" not in instance or not isinstance(instance["integrity"], dict):
            issues.append("MISSING required object: integrity")
        else:
            issues += _validate_fieldset(instance["integrity"], integ, prefix="integrity.")
    return [f"{schema_name}: {i}" for i in issues]


def validate_bundle(bundle: dict, level: int, spec: dict) -> dict:
    required = required_schemas_for_level(spec, level)
    schemas = spec.get("schemas", {})
    per_schema: dict[str, list[str]] = {}
    for name in required:
        if name not in schemas:
            per_schema[name] = [f"{name}: schema not defined in spec"]
            continue
        if name not in bundle:
            per_schema[name] = [f"{name}: MISSING required schema for level {level}"]
            continue
        per_schema[name] = validate_record(bundle[name], name, schemas[name])
    conformant = all(len(v) == 0 for v in per_schema.values())
    return {
        "level": level,
        "level_name": next(l["name"] for l in spec["specification"]["conformance_levels"] if int(l["level"]) == level),
        "required_schemas": required,
        "conformant": conformant,
        "issues": {k: v for k, v in per_schema.items() if v},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="AIDD-GOV reference conformance validator")
    ap.add_argument("--artifact", required=True, type=Path, help="JSON artifact (bundle or single record)")
    ap.add_argument("--spec", type=Path, default=Path(__file__).resolve().parents[1] / "AIDD-GOV-SPEC-v0.1.yaml")
    ap.add_argument("--level", type=int, choices=[1, 2, 3], help="Target conformance level (bundle mode)")
    ap.add_argument("--schema", help="Single-schema mode: validate the artifact against this one schema")
    args = ap.parse_args()

    if not args.spec.exists():
        print(f"ERROR: spec not found at {args.spec}", file=sys.stderr)
        return 2
    spec = load_spec(args.spec)
    artifact = json.loads(args.artifact.read_text())

    if args.schema:
        schemas = spec.get("schemas", {})
        if args.schema not in schemas:
            print(f"ERROR: unknown schema {args.schema}", file=sys.stderr)
            return 2
        issues = validate_record(artifact, args.schema, schemas[args.schema])
        ok = len(issues) == 0
        print(json.dumps({"schema": args.schema, "conformant": ok, "issues": issues}, indent=2))
        return 0 if ok else 1

    if args.level is None:
        print("ERROR: provide --level N (bundle) or --schema NAME (single record)", file=sys.stderr)
        return 2
    result = validate_bundle(artifact, args.level, spec)
    print(json.dumps(result, indent=2))
    return 0 if result["conformant"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
