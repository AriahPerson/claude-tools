---
name: filipino-culture-kg
description: >
  Query the Filipino culture knowledge graph — canonical concepts with dense definitions,
  cultural context, regional variation, diaspora adaptation, boundary conditions, and citations.
  Use this skill whenever answering questions about Filipino cultural values, social dynamics,
  regional subcultures (Bisayan, Ilocano, Kapampangan, Bicolano, Bangsamoro/Mindanao), or
  Filipino-American diaspora identity. Also use when explaining how a concept functions in
  Filipino social life, how it shifts across regions, how it's renegotiated in diaspora contexts,
  or what the scholarly debate looks like. Trigger on any request involving: core Filipino values
  (kapwa, hiya, utang na loob, loob, bahala na, amor propio, pakikisama, SIR), family and kinship
  structures, code-switching and language patterns, colonial legacy, folk Catholicism and folk
  healing, fiesta culture, gender and bakla identity, or Filipino-American identity dynamics.
  Prefer this over off-the-top-of-head synthesis whenever a grounded, citation-backed answer is
  possible.
---

# Filipino Culture Knowledge Graph Skill

## What this database is

A curated knowledge graph of Filipino cultural concepts populated from ethnographic research,
cultural studies scholarship, and community-based sources — prioritizing nuance, regional
specificity, and diaspora experience over Tagalog-centric or romanticized generalizations.
Every concept has: a 150-200 word dense definition, cultural context (historical/sociological
origin), functional role in social life, common expressions or behavioral markers, regional
variation, diaspora adaptation, boundary conditions, common misunderstandings, related and
contrast concepts (all cross-referenced by slug), scholarly notes on contested interpretations,
and 3-6 citations with source quality notes.

**Quality standard:** Concepts are marked `populated` (grounded in scholarship) or
`populated_with_caution` (contested, romanticized, or primarily Tagalog-centric in sourcing).
Explicitly excluded or marked as contested: colonial-era deficit framing of Filipino traits,
untextured pan-Filipino generalizations that erase regional variation, Orientalist or
essentialist characterizations.

**Database location:** Bundled at `skills/filipino-culture-kg/filipino_culture_kg.json`. Resolve order:
1. `FILIPINO_KG_PATH` environment variable if set
2. Bundled file alongside `SKILL.md` (default — no setup needed)
3. `filipino_culture_kg.json` in the working directory

---

## How to use the lookup script

The script is at `scripts/lookup.py`. Run it from the directory containing the database:

```bash
cd <directory-containing-filipino_culture_kg.json>

# Single concept
python <plugin-path>/skills/filipino-culture-kg/scripts/lookup.py kapwa

# Multiple concepts at once
python ... hiya utang_na_loob pakikisama

# Specific fields only
python ... --fields kapwa definition_dense,cultural_context,citations
python ... --fields hiya boundary_conditions,common_misunderstandings

# Available fields: definition_dense, cultural_context, functional_role,
#   common_expressions_or_markers, regional_variation, diaspora_adaptation,
#   boundary_conditions, common_misunderstandings, supersedes_or_reframes,
#   keep_outdated_terms_as_aliases_only, related_concepts, contrast_concepts,
#   source_quality_notes, scholarly_notes, citations

# Search by keyword
python ... --search "shame face"
python ... --search "bisayan family"

# Full index
python ... --index
```

---

## When to run the script vs. answer from context

**Run the script** for:
- Any question needing the exact definition, cultural context, or citations
- Comparing two or more concepts (run both; use `contrast_concepts` and `common_misunderstandings`)
- "What does the scholarship say about..." questions
- Regional variation, diaspora adaptation, boundary conditions

**Answer from the index below** (no script needed) for:
- "Is X in the database?" — check the slug list
- "What concepts are in domain Y?"

---

## Response formatting

**Single concept:** definition → cultural context (if origin/history question) → functional role
(if how-it-works question) → regional variation (if asked about specific region) →
diaspora adaptation (if Fil-Am context) → boundary conditions (if practically important) →
2-3 key citations as `(Author, Year)`.

**Comparing two concepts:** one-sentence distinction up front → contrast on scope, mechanism,
regional expression, diaspora shift → draw from `contrast_concepts` and `common_misunderstandings`
fields → one key citation per concept.

**"Is X the same as Y?":** check `contrast_concepts` and `common_misunderstandings` on both.

**Concept not in database:** say so, offer closest covered concept. Do not synthesize from memory.

**Romanticized or colonial framings (e.g., "Filipinos are naturally hospitable",
"hiya is just shame", "utang na loob is just debt"):** note the flattening, explain what
scholarship shows, anchor to the covered constructs with their full complexity.

**Regional specificity:** always note when a concept is primarily Tagalog-centric vs.
pan-Philippine, and surface the Bisayan/Visayan, Ilocano, or other regional perspective
when available.

---

## Concept index (by domain)

Full table in `references/concept_index.md`. Quick slug reference:

*(Database not yet populated — concepts will appear here as entries are added.)*

**Core Filipino values:** *(pending)*

**Family and kinship:** *(pending)*

**Social harmony and conflict dynamics:** *(pending)*

**Language and communication:** *(pending)*

**Regional and ethnic cultures:** *(pending)*

**Religion and folk spirituality:** *(pending)*

**Colonial legacy and historical consciousness:** *(pending)*

**Filipino-American and diaspora identity:** *(pending)*

**Food, fiesta, and material culture:** *(pending)*

**Gender, sexuality, and family roles:** *(pending)*
