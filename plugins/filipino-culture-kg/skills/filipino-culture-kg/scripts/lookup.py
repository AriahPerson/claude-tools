#!/usr/bin/env python3
"""
Lookup one or more concepts from the Filipino culture knowledge graph.

Usage:
  python lookup.py <slug> [<slug2> ...]          # exact slug lookup
  python lookup.py --search <keyword>            # search by name/keyword
  python lookup.py --index                       # list all slugs + labels
  python lookup.py --fields <slug> <field,...>   # extract specific fields only

Examples:
  python lookup.py kapwa
  python lookup.py hiya utang_na_loob
  python lookup.py --search "bisayan family honor"
  python lookup.py --fields kapwa definition_dense,cultural_context,citations
  python lookup.py --index
"""

import json
import sys
import os
from pathlib import Path

# Resolve database path
SCRIPT_DIR = Path(__file__).parent.parent  # skills/filipino-culture-kg/
DB_CANDIDATES = [
    Path(os.environ.get("FILIPINO_KG_PATH", "/nonexistent")),
    SCRIPT_DIR / "filipino_culture_kg.json",  # bundled
    Path.cwd() / "filipino_culture_kg.json",
    SCRIPT_DIR.parent.parent.parent / "filipino_culture_kg.json",
    SCRIPT_DIR.parent / "filipino_culture_kg.json",
]

def find_db():
    for p in DB_CANDIDATES:
        if p.exists():
            return p
    here = Path.cwd()
    for _ in range(6):
        candidate = here / "filipino_culture_kg.json"
        if candidate.exists():
            return candidate
        here = here.parent
    raise FileNotFoundError(
        "Cannot find filipino_culture_kg.json. "
        "Set FILIPINO_KG_PATH env var or place the file in the working directory."
    )

def load_db():
    with open(find_db()) as f:
        return json.load(f)

def format_citations(citations):
    if not citations:
        return "  (none)"
    lines = []
    for c in citations:
        authors = c.get("authors", "")
        year = c.get("year", "")
        title = c.get("title", "")
        source = c.get("source_type", "")
        why = c.get("why_it_was_used", "")
        lines.append(f"  - {authors} ({year}). {title}. [{source}]")
        if why:
            lines.append(f"    Why: {why}")
    return "\n".join(lines)

def format_concept(c, fields=None):
    pf = c["populate_fields"]
    kg = c["kg_fields"]

    ALL_FIELDS = {
        "definition_dense":                  ("Definition",                    pf.get("definition_dense", "")),
        "cultural_context":                  ("Cultural context",              pf.get("cultural_context", "")),
        "functional_role":                   ("Functional role",               pf.get("functional_role", "")),
        "common_expressions_or_markers":     ("Common expressions/markers",    pf.get("common_expressions_or_markers", "")),
        "regional_variation":                ("Regional variation",            pf.get("regional_variation", "")),
        "diaspora_adaptation":               ("Diaspora adaptation",           pf.get("diaspora_adaptation", "")),
        "boundary_conditions":               ("Boundary conditions",           pf.get("boundary_conditions", "")),
        "common_misunderstandings":          ("Common misunderstandings",      pf.get("common_misunderstandings", [])),
        "supersedes_or_reframes":            ("Supersedes/reframes",           pf.get("supersedes_or_reframes", [])),
        "keep_outdated_terms_as_aliases_only": ("Aliases (outdated/colonial)", pf.get("keep_outdated_terms_as_aliases_only", [])),
        "related_concepts":                  ("Related",                       pf.get("related_concepts", [])),
        "contrast_concepts":                 ("Contrast",                      pf.get("contrast_concepts", [])),
        "source_quality_notes":              ("Source quality",                pf.get("source_quality_notes", "")),
        "scholarly_notes":                   ("Scholarly notes",               pf.get("scholarly_notes", "")),
        "citations":                         ("Citations",                     pf.get("citations", [])),
    }

    header = f"{'='*60}\n{c['canonical_name'].upper()} [{c['slug']}]\n"
    header += f"Domain: {c['parent_domain_label']}\n"
    header += f"Status: {c['status']}"
    if kg.get("historical_or_contested"):
        header += " | HISTORICAL/CONTESTED"
    if kg.get("tagalog_centric"):
        header += " | TAGALOG-CENTRIC SOURCE"
    header += "\n" + "="*60

    lines = [header]
    for key in (fields if fields else list(ALL_FIELDS.keys())):
        if key not in ALL_FIELDS:
            lines.append(f"\n[Unknown field: {key}]")
            continue
        label, val = ALL_FIELDS[key]
        if not val:
            continue
        if key == "citations":
            lines.append(f"\n{label}:\n{format_citations(val)}")
        elif isinstance(val, list):
            if val:
                lines.append(f"\n{label}: {', '.join(val)}")
        else:
            lines.append(f"\n{label}:\n{val}")

    return "\n".join(lines)

def search_concepts(data, keyword):
    words = keyword.lower().split()
    matches = []
    for c in data["concepts"]:
        score = 0
        slug = c["slug"]
        label = c["label"].lower()
        canonical = c["canonical_name"].lower()
        aliases = " ".join(c.get("aliases", [])).lower()
        defn = (c["populate_fields"].get("definition_dense") or "").lower()
        for w in words:
            if w in slug:      score += 3
            if w in label:     score += 3
            if w in canonical: score += 2
            if w in aliases:   score += 2
            if w in defn:      score += 1
        if score > 0:
            matches.append((score, c))
    matches.sort(key=lambda x: -x[0])
    return matches

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    data = load_db()

    if not data.get("concepts"):
        print("Database is not yet populated. No concepts to look up.")
        sys.exit(0)

    concept_map = {c["slug"]: c for c in data["concepts"]}

    if args[0] == "--index":
        from collections import defaultdict
        by_domain = defaultdict(list)
        for c in data["concepts"]:
            by_domain[c["parent_domain_label"]].append(c)
        for domain in sorted(by_domain.keys()):
            print(f"\n{domain}")
            print("-" * len(domain))
            for c in sorted(by_domain[domain], key=lambda x: x["slug"]):
                print(f"  {c['slug']:<45} {c['label']}")
        return

    if args[0] == "--search":
        keyword = " ".join(args[1:])
        matches = search_concepts(data, keyword)
        if not matches:
            print(f"No matches for: {keyword}")
        else:
            print(f"Matches for '{keyword}':")
            for score, c in matches[:10]:
                print(f"  [{score}] {c['slug']:<45} {c['label']}")
        return

    if args[0] == "--fields":
        slug = args[1]
        fields = args[2].split(",") if len(args) > 2 else None
        if slug not in concept_map:
            print(f"Unknown slug: {slug}")
            sys.exit(1)
        print(format_concept(concept_map[slug], fields=fields))
        return

    for slug in args:
        if slug not in concept_map:
            matches = search_concepts(data, slug.replace("_", " "))
            if matches:
                best = matches[0][1]
                print(f"['{slug}' not found — closest: '{best['slug']}']\n")
                print(format_concept(best))
            else:
                print(f"Unknown slug: {slug}")
        else:
            print(format_concept(concept_map[slug]))
        print()

if __name__ == "__main__":
    main()
