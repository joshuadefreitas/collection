#!/usr/bin/env python3
"""Validate a collection registry against schema version 1. Needs the `jsonschema` package."""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

SCHEMA = Path(__file__).resolve().parents[1] / "schema" / "1" / "collection.schema.json"


def problems(registry):
    schema = json.loads(SCHEMA.read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}" for e in validator.iter_errors(registry)]


def main(argv):
    if len(argv) != 2:
        print("usage: validate.py <registry.json>", file=sys.stderr)
        return 2
    found = problems(json.loads(Path(argv[1]).read_text()))
    for line in found:
        print(line)
    print("valid" if not found else f"{len(found)} problem(s)")
    return 1 if found else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
