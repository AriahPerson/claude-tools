# claude-tools

A public collection of Claude Code plugins.

## Plugins

### [psych-kg](plugins/psych-kg/)

A self-contained psychology knowledge graph skill for Claude. Covers 120 canonical concepts drawn from meta-analyses, systematic reviews, and major handbooks — consensus-first, with contested frameworks explicitly excluded or flagged.

**Domains:** personality, attachment, cognitive architecture, judgment and decision-making, learning and habit, stress and trauma, emotion regulation, mindfulness and metacognition, motivation and self-regulation, psychotherapy change mechanisms.

**Each concept includes:** dense definition, mechanism, functional role, measurement methods, developmental notes, clinical relevance, boundary conditions, common confusions, related and contrast concepts (cross-referenced by slug), and 3–6 citations.

**Fully self-contained** — the knowledge graph database is bundled with the plugin, no external setup required.

Claude uses this skill automatically when answering questions about psychological constructs, or you can trigger it explicitly:

- *"What is the mechanism behind cognitive reappraisal?"*
- *"Compare rumination and worry"*
- *"What are the boundary conditions for habit formation?"*
- *"What does the research consensus say about expressive suppression?"*
