# Filipino culture KG: candidate concept set (research notes)

Purpose: propose concise, citation-ready candidate concepts for a Filipino culture knowledge graph, with care against Tagalog-centric overgeneralization.

General framing cautions
- Many of the best-known terms in Filipino studies (kapwa, loob, hiya, pakikisama, bahala na) come from Tagalog and Sikolohiyang Pilipino; they are influential analytic terms, but should not be treated as transparent equivalents for all Philippine ethnolinguistic worlds.
- Lowland Christian norms should not be universalized to Bangsamoro, Lumad, and Cordilleran communities, whose kinship, authority, dress, and language ideologies can differ substantially.
- “Filipino hospitality,” “fatalism,” and similar pop-cultural shorthand should stay out of primary nodes unless reframed critically.
- For communication and food, prefer regionally grounded examples (e.g. Cebuano-English code-switching, Ilocano manong/manang, Maranao malong, Visayan/Mindanao kinilaw) over Manila-only defaults.

## 1) Core values and ethics

### kapwa
- Suggested slug: `kapwa`
- One-sentence definition: A Tagalog/Sikolohiyang Pilipino concept of shared personhood in which the other is understood not as a radical outsider but as a fellow self in relationship.
- Why it is canonical: Widely treated as a core organizing concept in Filipino psychology and ethics, and a better anchor than generic “collectivism.”
- Related concepts: `loob`, `pakikipagkapwa`, `pakikisama`, `kagandahang_loob`
- Contrast concepts: Western-style atomized individualism; colonial deficit framings of Filipino conformity
- Caution note: Important but not automatically pan-Philippine; strongest as a Tagalog-derived analytic vocabulary rather than a universal native term across all Philippine languages.
- Sources to cite:
  - Virgilio G. Enriquez, “Kapwa: A Core Concept in Filipino Social Psychology,” in Philippine World View / Sikolohiyang Pilipino tradition
  - Rogelia Pe-Pua and Elizabeth Protacio-Marcelino, “Sikolohiyang Pilipino (Filipino psychology): A legacy of Virgilio G. Enriquez” (Asian Journal of Social Psychology, 2000)
  - Katrin de Guia / later Filipino philosophy discussions of kapwa as relational ethics (use selectively)

### loob
- Suggested slug: `loob`
- One-sentence definition: A Tagalog philosophical-ethical concept often glossed as inner self or interiority, but better understood as relational will, moral interiority, and personhood-in-relation.
- Why it is canonical: It links many moral expressions (`utang na loob`, `kagandahang-loob`, `lakas ng loob`) and supports denser ethical modeling than “inner feelings.”
- Related concepts: `kapwa`, `kagandahang_loob`, `utang_na_loob`, `lakas_ng_loob`
- Contrast concepts: purely private “inner psyche”; Cartesian mind/body split
- Caution note: Easy to mistranslate as only “inside”; the literature stresses its relational and embodied character.
- Sources to cite:
  - Leonardo Mercado, Elements of Filipino Philosophy (1974)
  - Albert E. Alejo and Julia E. Riddle, “Loob as Relational Interiority” (Social Transformations, 2018)
  - Jeremiah Reyes and related Filipino virtue-ethics work on loób

### utang_na_loob
- Suggested slug: `utang_na_loob`
- One-sentence definition: A morally weighted debt of gratitude and reciprocity created by significant help or care, especially when it binds persons and families across unequal resources or status.
- Why it is canonical: Central to Filipino discussions of reciprocity, obligation, patronage, and kin/fictive-kin ties.
- Related concepts: `loob`, `reciprocity`, `compadrazgo`, `hiya`
- Contrast concepts: market debt; purely contractual exchange
- Caution note: Should not be reduced to simple “debt” or romanticized as pure virtue, because it can sustain both solidarity and coercive dependence.
- Sources to cite:
  - Mary R. Hollnsteiner, “Reciprocity in the Lowland Philippines” (Philippine Studies, 1961)
  - Frank Lynch, Four Readings on Philippine Values (for classic lowland-values framing)
  - Recent reassessments of utang na loob in Filipino psychology/virtue ethics (use as supplement, not replacement for Hollnsteiner)

### bahala_na
- Suggested slug: `bahala_na`
- One-sentence definition: A stance of courageous acceptance toward uncertainty in which one proceeds despite incomplete control, rather than simply surrendering to fate.
- Why it is canonical: Frequently misread as fatalism, yet Filipino psychology literature repeatedly treats it as active resolve under uncertainty.
- Related concepts: `lakas_ng_loob`, `diskarte`, `pakikibaka`
- Contrast concepts: fatalism; passivity
- Caution note: Keep explicit note that “bahala na = fatalism” is a colonial and Westernized oversimplification.
- Sources to cite:
  - Alfredo V. Lagmay, “Bahala Na!” (Philippine Journal of Psychology)
  - Pe-Pua and Protacio-Marcelino (2000), summary discussion in Sikolohiyang Pilipino
  - Rolando Gripaldo, philosophical analyses of bahala na (supplementary)

## 2) Family and kinship

### bilateral_extended_kinship
- Suggested slug: `bilateral_extended_kinship`
- One-sentence definition: A common Philippine kinship pattern in which relatives from both maternal and paternal sides remain socially salient, often beyond the nuclear household.
- Why it is canonical: Strong baseline concept for family structure, caregiving, obligation, and neighborhood-level alliance.
- Related concepts: `pamilya`, `angkan`, `fictive_kin`, `seniority`
- Contrast concepts: strictly patrilineal descent; strictly nuclear-family models
- Caution note: Broadly useful for many lowland contexts, but Muslim and Indigenous communities may have more distinct descent, residence, and authority arrangements.
- Sources to cite:
  - Amaryllis T. Torres, “Kinship and Social Relations in Filipino Culture”
  - Belen T.G. Medina, The Filipino Family
  - Felipe Landa Jocano, work on family and social organization

### compadrazgo
- Suggested slug: `compadrazgo`
- One-sentence definition: Ritual co-parenthood through godparent ties (`ninong`/`ninang`, `kumare`/`kumpare`) that extends kin-like obligations and alliance between families.
- Why it is canonical: Crucial bridge between religion, kinship, patronage, and social mobility.
- Related concepts: `fictive_kin`, `utang_na_loob`, `reciprocity`, `baptism`
- Contrast concepts: purely ceremonial godparenthood without ongoing obligations
- Caution note: A colonial-Catholic institution adapted locally; do not treat it as equally central in non-Catholic settings.
- Sources to cite:
  - M. Cristina Blanc-Szanton, “The Uses of Compadrazgo: Views from a Philippine Town” (Philippine Sociological Review, 1979)
  - Frank Lynch / Philippine Studies discussions of compadrinazgo
  - Belen Medina on family and ritual kinship

### fictive_kin
- Suggested slug: `fictive_kin`
- One-sentence definition: Socially recognized kin-like ties formed beyond blood or marriage, often through neighborhood intimacy, migration, caregiving, or respectful address.
- Why it is canonical: Explains why “tita/tito,” `manong/manang`, `ate/kuya`, and kumare/kumpare relations often exceed strict genealogy.
- Related concepts: `compadrazgo`, `bilateral_extended_kinship`, `pakikisama`
- Contrast concepts: biologically strict kin definitions
- Caution note: The term is analytic rather than emic; some scholars now prefer quasi-kin or achieved kinship depending on context.
- Sources to cite:
  - Amaryllis T. Torres on kinship extension and social relations
  - Blanc-Szanton on compadrazgo as achieved/extended kinship
  - Contemporary migration/care scholarship on remade family ties among Filipina domestic workers

### transnational_family_care
- Suggested slug: `transnational_family_care`
- One-sentence definition: A family formation in which care, authority, and obligation are maintained across borders through OFW migration, remittances, communication, and material sending.
- Why it is canonical: Essential for any non-static account of Filipino kinship in the late 20th and 21st centuries.
- Related concepts: `balikbayan_box`, `remittance`, `left_behind_children`, `mothering_from_a_distance`
- Contrast concepts: co-resident household as the only family norm
- Caution note: Avoid flattening this to “sacrifice”; the literature emphasizes ambivalence, gender strain, and unequal emotional labor.
- Sources to cite:
  - Rhacel Salazar Parreñas, Children of Global Migration / work on transnational mothering
  - Mirca Madianou, work on ICTs and Filipino transnational families
  - Recent public-health and family studies on OFW and left-behind households (supplementary)

## 3) Social harmony and conflict dynamics

### pakikisama
- Suggested slug: `pakikisama`
- One-sentence definition: A relational norm of getting along with others through accommodation, tact, and maintenance of workable social rapport.
- Why it is canonical: One of the most cited Filipino social norms, especially in discussions of cooperation, conformity, and group belonging.
- Related concepts: `kapwa`, `smooth_interpersonal_relations`, `pakikiramdam`, `hiya`
- Contrast concepts: open confrontation; whistleblowing against the group; hyper-individual assertiveness
- Caution note: Keep a dual reading: adaptive solidarity on one side, conformity pressure and silence on the other.
- Sources to cite:
  - Frank Lynch, “Social Acceptance Reconsidered” / Four Readings on Philippine Values
  - SAGE Encyclopedia of Filipina/x/o American Studies entry on Pakikisama
  - Enriquez/Pe-Pua on pakikisama as a surface value grounded in kapwa

### pakikiramdam
- Suggested slug: `pakikiramdam`
- One-sentence definition: Social sensing or attunement to others’ feelings, cues, and unspoken meanings, often guiding when to speak, yield, joke, or remain indirect.
- Why it is canonical: Strong explanatory concept for high-context interaction and conflict management beyond simplistic “indirectness.”
- Related concepts: `pakikisama`, `hiya`, `indirect_communication`, `pahiwatig`
- Contrast concepts: blunt explicitness; low-context communication
- Caution note: Best modeled as an interactional skill/norm, not as mystical mind-reading.
- Sources to cite:
  - Pe-Pua and Protacio-Marcelino (2000)
  - Ricardo Mataragnon, “Pakikiramdam in Filipino Social Interaction”
  - Later discourse-analytic work on Filipino politeness and indirectness

### hiya
- Suggested slug: `hiya`
- One-sentence definition: A relational sense of propriety, dignity, and social restraint that helps regulate behavior in the presence of others and their judgments.
- Why it is canonical: High-value concept for face, shame, politeness, deference, and conflict avoidance.
- Related concepts: `amor_propio`, `pakikisama`, `utang_na_loob`, `face_saving`
- Contrast concepts: shamelessness (`walang hiya`); aggressive self-assertion
- Caution note: Do not map hiya directly onto Western shame; many Filipino scholars treat it as dignity/propriety within relationship, not merely internal guilt.
- Sources to cite:
  - Frank Lynch, Four Readings on Philippine Values
  - Enriquez / Pe-Pua discussions in Sikolohiyang Pilipino
  - Supplementary Filipino ethics/philosophy work comparing hiya and shame

### smooth_interpersonal_relations
- Suggested slug: `smooth_interpersonal_relations`
- One-sentence definition: An influential anthropological umbrella term for practices that preserve social ease and minimize overt friction in many lowland Filipino settings.
- Why it is canonical: Historically important in Philippine studies and useful as a bridge node linking `pakikisama`, `hiya`, euphemism, and facework.
- Related concepts: `pakikisama`, `hiya`, `amor_propio`, `social_acceptance`
- Contrast concepts: direct adversarial interaction
- Caution note: Mark as an analytic label coined in mid-century scholarship, not an indigenous emic term, and note its lowland/Tagalog-centric limitations.
- Sources to cite:
  - Frank Lynch, “Social Acceptance Reconsidered”
  - Philippine values literature responding to or critiquing Lynch
  - Pe-Pua and Protacio-Marcelino (for indigenizing critique of older framings)

## 4) Language and communication

### filipino_national_language
- Suggested slug: `filipino_national_language`
- One-sentence definition: The constitutionally recognized national language of the Philippines, formally imagined as evolving from many Philippine languages but in practice structurally rooted in Tagalog.
- Why it is canonical: Necessary node for discussing language politics, schooling, media, and why “Filipino” and “Tagalog” are often conflated.
- Related concepts: `tagalog`, `language_policy`, `ethnolinguistic_identity`
- Contrast concepts: regional first-language identity; English as official language
- Caution note: Explicitly note contested legitimacy among speakers of Cebuano, Ilokano, Hiligaynon, Waray, Kapampangan, Maranao, Tausug, etc.
- Sources to cite:
  - Andrew Gonzalez, “The language provision of the 1987 Constitution of the Republic of the Philippines”
  - Ricardo Ma. Nolasco / language-policy scholarship
  - Community-facing synthesis such as Isaiah Flores, “From Tagalog to Filipino: Deciphering Language and Identity” (use as explainer, not sole authority)

### code_switching
- Suggested slug: `code_switching`
- One-sentence definition: The strategic alternation of languages or varieties in everyday speech, including but not limited to Tagalog-English (Taglish), Cebuano-English, and mixed urban repertoires.
- Why it is canonical: Better umbrella than Taglish alone and more accurate to multilingual Philippine reality.
- Related concepts: `taglish`, `cebuano_english_code_switching`, `bilingualism`, `register`
- Contrast concepts: monolingual purity ideologies
- Caution note: Avoid treating Taglish as the national default; regional code-switching patterns differ significantly, including Cebuano-English variation between Cebu and Mindanao.
- Sources to cite:
  - Maria Lourdes S. Bautista, “Tagalog-English Code Switching as a Mode of Discourse”
  - Kristian J. Abastillas, “Divergence in Cebuano and English Code-Switching Practices in Cebuano Speech Communities in the Central Philippines”
  - Philippine sociolinguistics on multilingual repertoires and language ideology

### honorific_addressing
- Suggested slug: `honorific_addressing`
- One-sentence definition: Respect is commonly communicated through particles, kinship terms, titles, and avoidance strategies, but the forms used vary sharply by language and region.
- Why it is canonical: Strong node connecting language, age hierarchy, kinship, and everyday etiquette.
- Related concepts: `po_opo`, `kuya_ate`, `manong_manang`, `apo`, `title_use`
- Contrast concepts: first-name-only address; egalitarian speech styles
- Caution note: `po/opo` are especially Tagalog-associated and should not be treated as universal Philippine honorifics; Ilocano, Kapampangan, Cebuano, and others use different systems or kinship-based address.
- Sources to cite:
  - Ethnographic and sociolinguistic work on Philippine honorifics and address systems
  - Ilocano/Hiligaynon kinship terminology studies (for `manong/manang` and related forms)
  - Philippine language pedagogy/community materials as supplementary examples only

### ethnolinguistic_identity
- Suggested slug: `ethnolinguistic_identity`
- One-sentence definition: Language in the Philippines often indexes regional belonging and political feeling, as in Bisaya/Cebuano, Ilokano, Kapampangan, or Maranao identities that do not collapse neatly into a single “Filipino” linguistic self.
- Why it is canonical: Helps prevent Manila-centric flattening and anchors region-specific subgraphs.
- Related concepts: `filipino_national_language`, `regional_language`, `code_switching`, `diaspora_identity`
- Contrast concepts: homogenized national-language narratives
- Caution note: Identity labels can be nested and contested (e.g. “Bisaya” as broad identity vs Cebuano as specific language).
- Sources to cite:
  - Abastillas on differentiated Cebuano identity across Cebu, Negros Oriental, Misamis Oriental, and Davao del Sur
  - Gonzalez and Philippine language-policy scholarship
  - Region-specific language-identity studies (Ilokano, Kapampangan, Bangsamoro languages)

## 5) Food and material culture

### fiesta_feasting
- Suggested slug: `fiesta_feasting`
- One-sentence definition: Public feasting tied to patron-saint days, town celebration, and hospitality in which food display, visiting, and reciprocity reinforce social and religious belonging.
- Why it is canonical: A major bridge node for religion, food, class display, and local identity.
- Related concepts: `hospitality`, `compadrazgo`, `kain_na`, `patron_saint_devotion`
- Contrast concepts: private everyday meal; non-feast austerity
- Caution note: Do not reduce fiesta to cheerful excess; scholarship also treats it as status display, obligation, and historically Christian-lowland rather than universally Filipino.
- Sources to cite:
  - Fenella Cannell, Power and Intimacy in the Christian Philippines
  - Doreen G. Fernandez, Tikim / Sarap essays on Philippine food and feast
  - Local ethnographies of town fiestas (regional case studies preferred)

### kinilaw
- Suggested slug: `kinilaw`
- One-sentence definition: A vinegar- or acid-cured raw seafood preparation especially associated with Visayan and Mindanao foodways, often used to foreground freshness and regional coastal identity.
- Why it is canonical: Regionally specific, historically deep, and a good corrective to Luzon-centered dish lists.
- Related concepts: `souring`, `seafood`, `visayan_cuisine`, `mindanao_cuisine`
- Contrast concepts: heavily stewed or braised national-dish stereotypes
- Caution note: Better modeled as a regional food complex than as a single standardized “Filipino dish.”
- Sources to cite:
  - Doreen G. Fernandez and Edilberto Alegre, Kinilaw
  - Doreen G. Fernandez, “Culture Ingested: On the Indigenization of Philippine Food”
  - Palayok / Tikim discussions of regional foodways

### balikbayan_box
- Suggested slug: `balikbayan_box`
- One-sentence definition: A box of goods sent home by overseas Filipinos that materializes care, obligation, aspiration, and diasporic intimacy across distance.
- Why it is canonical: Excellent material-culture node linking diaspora, family care, food, and consumer desire.
- Related concepts: `transnational_family_care`, `gift_giving`, `remittance`, `diaspora_identity`
- Contrast concepts: direct co-presence; purely monetary remittance
- Caution note: Avoid sentimental-only framing; scholarship emphasizes labor, class pressure, and gendered performance of care.
- Sources to cite:
  - Johanna Poethig Alburo, “Boxed In or Out? Balikbayan Boxes as Metaphors for Filipino American Identity”
  - A Hard Look at the Balikbayan Box: The Philippine Diaspora’s Exported Hospitality
  - Studies on feeding, food, and long-distance care in Filipino transnational households

### malong_landap
- Suggested slug: `malong_landap`
- One-sentence definition: A high-status tubular garment associated especially with Maranao and Maguindanao communities in Mindanao, where weaving, color, and langkit/okir design encode rank, region, and artistry.
- Why it is canonical: Strong non-Tagalog material-culture node with clear Bangsamoro specificity.
- Related concepts: `langkit`, `okir`, `bangsamoro_material_culture`, `dress`
- Contrast concepts: generic “traditional Filipino costume” labels
- Caution note: Do not flatten all southern garments into “malong,” and do not detach the object from Maranao/Maguindanao histories and rank symbolism.
- Sources to cite:
  - Mapping Philippine Material Culture, “Malong a Landap (Tubular Garment)”
  - Art Gallery of New South Wales collection note on Maranao malong landap
  - Nicanor Tiongson / National Museum / okir and Maranao art scholarship

## Shortlist recommendation for first implementation

If the plugin should start narrower, my strongest 2-3 per domain are:
- Core values: `kapwa`, `loob`, `utang_na_loob`
- Family/kinship: `bilateral_extended_kinship`, `compadrazgo`, `transnational_family_care`
- Social harmony: `pakikisama`, `pakikiramdam`, `hiya`
- Language/communication: `filipino_national_language`, `code_switching`, `honorific_addressing`
- Food/material culture: `fiesta_feasting`, `kinilaw`, `balikbayan_box`

Why this shortlist
- It preserves famous Filipino studies concepts without making the graph wholly Tagalog-centered.
- It introduces regional specificity through Cebuano code-switching, Visayan/Mindanao kinilaw, and Bangsamoro material culture.
- It keeps diaspora and migration as constitutive, not peripheral, to contemporary Filipino culture.
