---
name: psych-kg
description: >
  Query the consensus psychology knowledge graph — 120 canonical concepts with dense definitions,
  mechanisms, boundary conditions, clinical relevance, citations, and cross-references. Use this
  skill whenever answering questions about psychological constructs, mechanisms, measurement,
  clinical applications, or the evidence base for concepts in: personality, attachment, cognition,
  judgment and decision-making, learning and habit, stress and trauma, emotion regulation,
  mindfulness/metacognition, motivation and self-regulation, or psychotherapy change mechanisms.
  Also use when comparing related concepts (e.g., "rumination vs. worry"), explaining what a
  construct predicts, what it is not, or what the research consensus says. Trigger on any request
  that would benefit from grounded, citation-backed psychological explanation rather than off-the-
  top-of-your-head synthesis.
---

# Psychology Knowledge Graph Skill

## What this database is

A curated knowledge graph of 120 canonical psychology concepts populated from meta-analyses,
systematic reviews, and major handbooks — prioritizing consensus over contested frameworks.
Every concept has: a 150-200 word dense definition, mechanism, functional role, measurement
methods, developmental notes, clinical/applied relevance, boundary conditions, common confusions,
related and contrast concepts (all cross-referenced by slug), and 3-6 citations with source quality notes.

**Quality standard:** Concepts are marked `populated` (high consensus) or `populated_with_caution`
(some contested evidence). Frameworks explicitly excluded or marked contested: polyvagal theory,
window of tolerance, neuroception, somatic marker hypothesis as universal mechanism, memory
reconsolidation as universal mechanism, rigid attachment style categories as types.

**Database location:** Bundled at `skills/psych-kg/psychology_consensus_120_populated.json`. Resolve order:
1. `PSYCH_KG_PATH` environment variable if set
2. Bundled file alongside `SKILL.md` (default — no setup needed)
3. `psychology_consensus_120_populated.json` in the working directory

---

## How to use the lookup script

The script is at `scripts/lookup.py`. Run it from the directory containing the database:

```bash
cd <directory-containing-psychology_consensus_120_populated.json>

# Single concept
python <plugin-path>/skills/psych-kg/scripts/lookup.py cognitive_reappraisal

# Multiple concepts at once
python ... rumination worry repetitive_negative_thinking

# Specific fields only
python ... --fields cognitive_reappraisal definition_dense,mechanism,citations
python ... --fields extinction boundary_conditions,common_confusions

# Available fields: definition_dense, mechanism, functional_role,
#   common_measurement_or_operationalization, developmental_notes,
#   clinical_or_applied_relevance, boundary_conditions, common_confusions,
#   supersedes_or_reframes, keep_outdated_terms_as_aliases_only,
#   related_concepts, contrast_concepts, source_quality_notes,
#   consensus_notes, citations

# Search by keyword
python ... --search "attachment avoidance"
python ... --search "executive function"

# Full index
python ... --index
```

---

## When to run the script vs. answer from context

**Run the script** for:
- Any question needing the exact definition, mechanism, or citations
- Comparing two or more concepts (run both; use `contrast_concepts` and `common_confusions`)
- "What does the research say about..." questions
- Boundary conditions, measurement, developmental notes

**Answer from the index below** (no script needed) for:
- "Is X in the database?" — check the slug list
- "What concepts are in domain Y?"

---

## Response formatting

**Single concept:** definition → mechanism (if how-it-works question) → clinical relevance (if applied context) → boundary conditions (if practically important) → 2-3 key citations as `(Author, Year)`.

**Comparing two concepts:** one-sentence distinction up front → contrast on scope, mechanism, measurement, clinical target → draw from `contrast_concepts` and `common_confusions` fields → one key citation per concept.

**"Is X the same as Y?":** check `contrast_concepts` and `common_confusions` on both. The curation was done specifically for this.

**Concept not in database:** say so, offer closest covered concept. Do not synthesize from memory.

**Contested frameworks (polyvagal theory, window of tolerance, neuroception, memory reconsolidation as universal mechanism):** note contestation, explain what evidence does show, anchor to the covered constructs (e.g., `autonomic_arousal`, `hpa_axis_activation`, `inhibitory_learning`).

---

## Concept index (120 concepts by domain)

Full table in `references/concept_index.md`. Quick slug reference:

**Personality:** `personality_trait` `trait_continuum` `trait_facet` `trait_stability` `trait_change` `honesty_humility` `emotionality` `extraversion` `agreeableness` `conscientiousness` `openness_to_experience` `altruism`

**Attachment:** `attachment_system` `attachment_security` `attachment_anxiety` `attachment_avoidance` `internal_working_model` `secure_base` `safe_haven` `proximity_seeking` `separation_distress` `sensitive_responsiveness` `mentalization` `rupture_repair`

**Cognition/Executive:** `attention` `selective_attention` `working_memory` `cognitive_load` `processing_speed` `inhibitory_control` `cognitive_flexibility` `updating` `goal_maintenance` `episodic_memory` `associative_memory` `retrieval_cue`

**Judgment/Decision-making:** `bounded_rationality` `heuristic` `availability_heuristic` `representativeness_heuristic` `anchoring_adjustment` `framing_effect` `confirmation_bias` `base_rate_neglect` `loss_aversion` `delay_discounting` `automatic_processing` `controlled_processing`

**Learning/Habit:** `classical_conditioning` `operant_conditioning` `positive_reinforcement` `negative_reinforcement` `punishment` `extinction` `stimulus_generalization` `discrimination_learning` `reward_prediction_error` `goal_directed_control` `habit` `cue_response_association`

**Stress/Trauma:** `acute_stress_response` `chronic_stress` `allostasis` `allostatic_load` `autonomic_arousal` `hpa_axis_activation` `hypervigilance` `intrusive_reexperiencing` `trauma_related_avoidance` `posttraumatic_negative_appraisals` `dissociation` `fear_generalization`

**Emotion/Regulation:** `emotion_generation` `emotional_awareness` `emotional_clarity` `emotion_differentiation` `emotional_reactivity` `emotional_recovery` `situation_selection` `situation_modification` `attentional_deployment` `cognitive_reappraisal` `expressive_suppression` `distress_tolerance`

**Mindfulness/Metacognition:** `present_moment_attention` `meta_awareness` `decentering` `nonjudgment` `acceptance` `self_compassion` `metacognitive_knowledge` `metacognitive_monitoring` `metacognitive_control` `rumination` `worry` `repetitive_negative_thinking`

**Motivation/Self-regulation:** `intrinsic_motivation` `extrinsic_motivation` `autonomous_motivation` `controlled_motivation` `autonomy_need` `competence_need` `relatedness_need` `self_efficacy` `goal_setting` `action_planning` `self_monitoring` `feedback_loop`

**Change/Therapy:** `psychological_flexibility` `experiential_avoidance` `cognitive_fusion` `cognitive_defusion` `values_clarification` `committed_action` `behavioral_activation` `exposure` `inhibitory_learning` `therapeutic_alliance` `social_support` `interpersonal_emotion_regulation`
