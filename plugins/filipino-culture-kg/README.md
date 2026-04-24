# filipino-culture-kg

A Claude skill backed by a curated knowledge graph of Filipino cultural concepts.

Current status: seeded and operational (25 concepts), with high-priority hubs for regional cultures,
religion/spirituality, colonial legacy, diaspora identity, and gender/sexuality.

## Scope and priorities

This KG prioritizes:
- regional specificity over Manila/Tagalog flattening
- Bisaya/Visayan, Ilocano, Kapampangan, and Bangsamoro/Mindanao coverage
- diaspora and transnational family dynamics as first-class, not peripheral
- caution flags for contested/romanticized categories

## Current concept coverage

10 domains are scaffolded; 7 are currently populated.

Populated domains:
- Core Filipino values and ethics
- Social harmony and conflict dynamics
- Regional and ethnic cultures
- Religion and folk spirituality
- Colonial legacy and historical consciousness
- Filipino-American and diaspora identity
- Gender, sexuality, and family roles

Pending domains:
- Family and kinship structures
- Language and communication patterns
- Food, fiesta, and material culture

For an up-to-date slug list, see:
- `skills/filipino-culture-kg/references/concept_index.md`

## High-priority concepts now included

Core/social-harmony hubs now available:
- `hiya`
- `utang_na_loob`
- `kapwa`
- `pakikisama`
- `smooth_interpersonal_relations` (aliases: `sir`, `sip`)

These complement existing hubs such as:
- `transnational_family`
- `bisaya_visayan`
- `bangsamoro`
- `balikbayan`
- `colonial_mentality`

## Usage

Run lookups directly:

```bash
python3 skills/filipino-culture-kg/scripts/lookup.py --index
python3 skills/filipino-culture-kg/scripts/lookup.py hiya
python3 skills/filipino-culture-kg/scripts/lookup.py --fields utang_na_loob definition_dense,related_concepts,citations
python3 skills/filipino-culture-kg/scripts/lookup.py --search "smooth interpersonal relations"
```

## Data quality and interpretation

- Concepts are marked `populated` or `populated_with_caution`.
- `historical_or_contested` and `tagalog_centric` flags are surfaced in lookup output.
- This seed emphasizes usable conceptual coverage first; deeper per-concept fields can be expanded in later enrichment passes.

## Public-repo data hygiene (important)

This plugin lives in a public repo context (`/claude-tools/`).
Do not commit private chat logs, personal identifiers, credentials, or raw sensitive evidence files.

Use only de-identified, scholarly/community-citable concept data in this plugin.
Private/personal analysis artifacts should stay in private workspaces (e.g., `inanna`), not in public plugin files.
