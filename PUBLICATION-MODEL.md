# Publication model: readiness outside the registry (DESIGN NOTE, not built)

Purpose: leave clean room in the charter for multiple publication surfaces without putting destination state in `collection.json`.

## Three layers
1. **Registry** (`collection.json`, public): canonical artifact truth. Knows nothing about destinations.
2. **Destination profiles** (policy, one document per destination or community class): eligibility by artifact type, requirements, required representation/package, disclosure checks, authorship rule (human only / assisted allowed / automatable), what "published" means there. Venue norms live here and in application policy, never in the registry or in a general-purpose consumer's core.
3. **Readiness and publication state** (private or derived, per artifact x destination): `artifact_ref` (id + artifact digest), the claim text (or hash) the venue copy was prepared against (optional), eligibility verdict, remaining requirements, prepared package and its hashes, disclosure result, authorship requirement, state (`not_applicable` / `not_ready` / `ready` / `prepared` / `published`), publication URL, outcome pointers. Outcomes are observations recorded by the application that measures them, linked here by reference, not copied.

## Questions every (artifact, destination) pair must answer
Eligible? What remains? What representation is needed? What disclosure/IP checks apply? Must Joshua author or submit by hand? Has it been published? What meaningful outcome followed?

## Type x destination (typical, not automatic)
- Tool: repo -> release/package (npm/PyPI) -> site -> Show HN -> relevant community discussion. Usually not arXiv.
- Study: verified study -> repo -> explorable/site -> technical discussion -> (only if it clears the scholarly bar) manuscript -> arXiv. Most studies never become papers.
- Note: site -> ordinary HN submission -> relevant community or professional discussion. No release or scholarly machinery.

## Destination notes
- **GitHub / releases, package registries:** mechanical; eligibility is the admission contract plus release hygiene.
- **Website / collection:** a generated view of the registry.
- **Hacker News:** two profiles. Ordinary submission (a link people may find interesting; no tag). Show HN (something people can actually try, linked directly, no waitlist). Comments and posts are human-authored when the platform requires it; the workstream prepares facts, evidence, links, context, readiness and likely questions, then hands off. Verify the current guidelines at the primary source before each use.
- **Reddit:** community-specific profiles (rules, self-promotion norms, what the community values). The workstream says whether an artifact is appropriate in principle for a kind of community; an external consumer finds real discussions where the public knowledge intersects. No generic promotion.
- **arXiv:** a research destination, not a social channel. Path: research question -> rigorous study -> evidence and reproducibility -> independent verification -> scholarly manuscript -> references, figures, supplement -> disclosure gate -> Joshua's submission. The bar is a separate checklist (novelty relative to the literature, a defensible method, a complete reproduction package, independent verification, an honest limitations section, endorsement and category requirements). Studies far below it remain valuable collection entries.
- **Professional surfaces (LinkedIn etc.):** summaries traceable to the canonical claim; no new claims.

## Claim-consistency invariant
No publication surface may materially strengthen or extend the canonical artifact's supported claim. Different presentation is allowed; claim inflation is not.
Initial enforcement is deliberately simple: each prepared publication package (title, framing, README or site copy, summary, abstract) receives an independent review against the artifact's `claim`, `non_claim`, public evidence and the disclosure constraints, plus a disclosure-gate scan of the outgoing text. A study's copy must carry or entail its non-claim.
Deferred until it is earned: sentence-level claim provenance, and automatic staleness marking when a registry claim changes (the readiness record may store the claim text it was prepared against; nothing more is built now).

## Roles
Public workstream: what is admitted, what claims are canonical, what representations are prepared, where an artifact is publication-ready. External consumers (outside this repository): what is happening externally, where an admitted artifact intersects a real discussion, whether a contribution is worth recommending, what outcomes followed. Joshua de Freitas: decides and performs consequential publication and participation.
