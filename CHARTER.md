# Public work: charter and admission contract (DRAFT v2 for founder ACCEPT/CORRECT)

Status: foundation v1. The registry is empty by design until the first artifact is admitted; nothing in this repository publishes any artifact.

## Approved foundation
- Home: a public `joshuadefreitas/collection` repo (charter, registry + schema, reusable presentation contract; infrastructure, not itself promoted or pinned) and a private inventory and publication record (candidates, exclusions, repair state, disclosure decisions, publication history).
- Taxonomy: Tools, Studies, Notes. `experimental` is a status, never a fourth shelf.
- Registry: the small field set below; `published` means canonical first publication, nothing else.

## Mandate and boundaries
The public workstream is the curation and publication layer for the body of technical work exposed under Joshua de Freitas's name. It decides what is admitted, holds the canonical registry, keeps presentation coherent, and governs disclosure and publication readiness. Projects keep their repositories and ownership; this layer wraps none of them.
- Belongs: admission decisions, the registry and schema, the charter, the presentation kit, the private inventory and publication record, generated surfaces (profile section, site catalog, cards, previews).
- Does not belong: project code or research; private or protected systems; employer or career material; consumer logic; marketing language; destination-specific state in the registry.
- The website is a consumer of the registry, never its source. External consumers (for example a private system that matches public work to outside discussion) read admitted entries through an external `artifact_ref` and never write the registry. Career and employer material is private and not linked from here.
- Standing rule: we only contribute, publicly or in discussion, what we could publish.

## Artifact types
`tool` (installable, used), `study` (reproducible computational work: question, method, result, limits), `note` (short writing grounded in real work).

## Admission contract (smallest useful, by type)
Floor for every artifact, including experimental: a one-sentence claim; summary; status; `published` and `last_verified`; canonical URL; run path where applicable; licence; disclosure-gate pass (private denylist scan of every public surface, history included); a README or page that follows the template.

| Requirement | Tool | Study | Note |
|---|---|---|---|
| Explicit non-claim | if it makes a security/correctness claim | **required** | optional |
| Run path (command or live demo) | **required** | **required** (command, seed, data provenance) | n/a |
| Tests + CI green | **required** | **required** (quoted numbers checked against evidence) | n/a |
| Licence (SPDX) | **required** | **required** | content licence stated |
| Version / release | **required** | tag when complete | n/a |
| One strong visual above the fold | **required** | **required** | optional |
| Independent verification | for security/correctness claims | **required** for the headline result | n/a |
| Corrections visible | n/a | required if any result was corrected | if applicable |

`experimental` is not a bypass. It keeps the whole floor (claim, non-claim for studies, run path, licence, tests present, disclosure pass) and relaxes only the optional rows (visual polish, independent verification of secondary results, release tagging). It requires a `status_note` stating what is unproven and the condition for promotion or removal, and it is re-evaluated at the next verification. If it would not be respectable to publish, it is not experimental, it is not admitted.

## Registry (`collection.json`, schema v1)
Fields: `schema_version`, `updated`, and per artifact `id` (immutable), `type`, `status`, `title`, `claim`, `non_claim`, `summary`, `topics`, `canonical_url`, `repo`, `version`, `license`, `published`, `last_verified`, `visual`, `related`, `supersedes`, typed public `evidence`, plus `status_note` (required for experimental and archived). Topics come from a small controlled vocabulary kept in the collection repo (`topics.json`) and checked by the generator. Renames are expressed with `supersedes`, never by changing an id.
Content hashes: the generator computes (not stored) a canonical-JSON SHA-256 of the whole registry and of each artifact; an external consumer's `artifact_ref` carries the id, canonical URL and artifact hash, so unrelated edits do not invalidate it.
Generator-enforced integrity: schema-valid; related/supersedes ids exist; ids immutable against the previously published registry; URLs resolve; topics in vocabulary. The generator may also warn about entries that are stale under their applicable freshness policy (below); it never invalidates an entry on a countdown.
Explicitly not in the registry: destination-specific state, submission history, venue copy, subreddit lists, social or traffic metrics.

## Publication model (design only; see PUBLICATION-MODEL.md)
One canonical artifact, many legitimate publication surfaces, each with its own eligibility, norms, representation and authorship rules. Readiness and publication state live in a separate private or derived layer that references the registry by `artifact_ref`. Invariant: no surface may receive a stronger substantive claim than the canonical artifact supports; different presentation is allowed, claim inflation is not. Nothing here is automated posting; Joshua decides and performs consequential external publication and authors personally where a platform requires it.

## Freshness and re-verification (policy outside the registry)
`last_verified` records when the admission checks last passed. When re-verification is due is governed by type, status and change events, with the parameters kept in the private record or the generator configuration, never in `collection.json`:
- **Tool:** may need periodic or dependency/API-triggered re-verification, because external change can invalidate its behaviour.
- **Study:** event-driven. A completed result does not become unverified because time passed; re-verify when the claim, evidence, code, data, reproduction environment or a material dependency changes.
- **Note:** no recurring requirement unless it explicitly depends on facts that change.
- **Experimental:** carries its own review or expiry condition in `status_note` or the private inventory state.
- **Archived:** no recurring requirement.

## Publication lifecycle
`candidate` (private inventory) -> `repaired` (meets the contract) -> `verified` (independent check where required, disclosure gate passed) -> `admitted` (registry entry, generated surfaces) -> `current` | `complete` | `archived` / `superseded`. A change event or a due tool re-check flags the entry; retirement keeps the artifact visible with its note.

## README template
1 claim and status line (status, version, last verified); 2 visual; 3 what it establishes; 4 what it does not establish; 5 run or use path; 6 evidence; 7 related; 8 licence. No badge wall.

## Presentation kit (built later, in this order)
A deterministic plate generator (profile and hero generators as base) producing the README visual and the 1280x640 social preview from a registry entry; a catalog generator (profile "Selected work", site index, cards) that only reads the registry.

## Decision rights
Joshua de Freitas admits, retires, publishes and participates. Workers may draft and verify; independent reviewers check the contract; the disclosure gate can only block. Nothing is published without explicit approval.
