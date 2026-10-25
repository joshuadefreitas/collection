# collection

Infrastructure for a body of technical work: the charter, the public registry contract and the publication model. It is not itself something to promote.

- [`CHARTER.md`](CHARTER.md): what the public collection is, what earns admission (by type), freshness policy, lifecycle.
- [`PUBLICATION-MODEL.md`](PUBLICATION-MODEL.md): how readiness for different publication surfaces is kept outside the registry, and the claim-consistency invariant.
- [`schema/1/collection.schema.json`](schema/1/collection.schema.json): JSON Schema for `collection.json` (schema version 1).
- [`examples/collection.example.json`](examples/collection.example.json): a **fictional, illustrative** registry. It lists no real artifact.

The registry is empty by design: no artifact has been admitted yet.

## Validate

```bash
python -m pip install jsonschema
python tools/validate.py examples/collection.example.json
python -m unittest discover -s tests
```

MIT licensed.
