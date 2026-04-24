# Candidate concept set — Filipino culture KG

Goal: high-signal canonical concepts for initial population, modeled on the psych-kg standard but kept concise. I prioritized concepts that are legible to non-specialists, common in Filipino studies / anthropology / diaspora studies, and useful as graph hubs.

General guidance
- Prefer ethnolinguistic / political formations over essentialized “tribes” or fixed traits.
- Avoid flattening “Filipino culture” into Tagalog/Manila norms; preserve Visayan/Bisayan, Ilocano, Kapampangan, and Bangsamoro distinctions.
- Mark when a term is diasporic, state-produced, contested, or historically transformed.
- Be careful with precolonial gender/spirituality terms: they are analytically useful but often romanticized.

## 1) Regional / ethnic cultures

| Concept | Suggested slug | One-sentence definition | Likely related / contrast concepts | Sources to cite |
|---|---|---|---|---|
| Bisaya / Visayan | `bisaya_visayan` | A meta-ethnolinguistic formation spanning Cebuano, Hiligaynon, Waray, and related groups across the Visayas and much of Mindanao, with identity shaped by multilingualism, migration, and strong regional literary histories. | Related: `cebuano`, `hiligaynon`, `waray`, `bayot`; Contrast: `tagalog_centrality`, `filipino_nationalism` | Resil B. Mojares, “Bisayan studies” (2023); C. Martinez-Juan, “Kaagi: tracing Visayan identities in cultural texts” (2023); David Zorc, The Bisayan Dialects of the Philippines (1977). |
| Ilocano | `ilocano` | An ethnolinguistic identity rooted in the Ilocos region but extended through internal migration and diaspora, especially Hawaiʻi, where language maintenance and narratives of hard work, kin obligation, and heritage education remain salient. | Related: `amianan_north`, `heritage_language`, `transnational_family`; Contrast: `tagalog_centrality`, `regional_language_shift` | Aurelio S. Agcaoili, Paka(sarita)an: On Ilokano Language, Identity, and Heritage Education (2015); ERIC version of “Paka(sarita)an in the Ilokano: Reclaiming a Native Tongue” (2017). |
| Kapampangan | `kapampangan` | A Central Luzon ethnolinguistic formation marked by strong regional self-consciousness, deep entanglement with colonial and national politics, and contemporary concern over language shift and cultural erasure. | Related: `pampanga`, `culinary_prestige`, `language_revival`; Contrast: `filipino_only_schooling`, `regional_marginalization` | Michael Raymon M. Pangilinan, “Kapampangan: A Problem of Identity, Language and Culture” (2013); John A. Larkin, The Pampangans (1972/1993); Cruz, “Preserving Heritage in Diaspora: A Study of Kapampangan Identity in Winnipeg” (2023). |
| Bangsamoro | `bangsamoro` | A modern ethnopolitical identity linking diverse Moro peoples of Mindanao and the Sulu archipelago through shared histories of Islam, anti-colonial resistance, and claims to self-determination without erasing internal ethnic difference. | Related: `moro`, `mindanao`, `bangsamoro_islam`, `settler_colonialism_mindanao`; Contrast: `lumad`, `christian_settler`, `unitary_nationalism` | Thomas M. McKenna, Muslim Rulers and Rebels (1998); BARMM Organic Law preamble; Kimura, “Religious and Ethnopolitical Identities Among Mindanao Muslims” (2019). |

Caution notes
- Do not treat “Bisaya” as a single language or single culture; usage shifts by region and can index Cebuano dominance in Mindanao.
- “Bangsamoro” is politically powerful but not synonymous with all Mindanao peoples; Lumad and Christian settler histories must remain distinct.
- Kapampangan and Ilocano identity are often narrated through stereotypes; prefer historically grounded descriptions over trait lists.

## 2) Religion / spirituality

| Concept | Suggested slug | One-sentence definition | Likely related / contrast concepts | Sources to cite |
|---|---|---|---|---|
| Babaylan | `babaylan` | A category of indigenous ritual specialist, healer, spirit medium, and community leader—especially a Visayan term, though many Philippine societies use other names for related roles. | Related: `asog`, `folk_healing`, `anito`, `decolonial_spirituality`; Contrast: `clerical_catholicism`, `missionization` | Grace Nono, Babaylan Sing Back (2021); Center for Babaylan Studies, “What is Babaylan?”; Carolyn Brewer, Holy Confrontation (2004). |
| Folk Catholicism | `folk_catholicism` | Lived Catholic practice in the Philippines often combines church sacraments and saint devotion with healing, vows, spirit mediation, and other local ritual logics not fully captured by official doctrine. | Related: `anting_anting`, `fiesta`, `panata`, `hilot`; Contrast: `official_catholic_doctrine`, `protestant_iconoclasm` | Charles J.-H. Macdonald, “Folk Catholicism and Pre-Spanish Religions in the Philippines” (2004); Fenella Cannell, Power and Intimacy in the Christian Philippines (1999). |
| Anting-anting | `anting_anting` | A popular amulet complex associated with protection, charisma, healing, power, and sometimes revolutionary or millenarian politics, often mixing Christian symbols with esoteric and vernacular beliefs. | Related: `folk_catholicism`, `orasyon`, `agimat`, `revolutionary_millenarianism`; Contrast: `rationalist_secularism` | Axel Borchgrevink, “The Power of Anting-anting” (Pilipinas, 2000); Reynaldo Ileto, Pasyon and Revolution (1979). |
| Bangsamoro Islam / adat | `bangsamoro_islam_adat` | In Moro societies, Islamic practice is lived through historically layered relations among faith, customary law (adat), kinship, local authority, and reformist currents rather than a single uniform orthodoxy. | Related: `bangsamoro`, `sharia`, `sultanate`, `ulama`; Contrast: `folk_catholicism`, `secular_nationalism` | Thomas M. McKenna, Muslim Rulers and Rebels (1998); Cesar Adib Majul, Muslims in the Philippines (1973); Al Qalam / ADDU, “Islam and Democracy in the Bangsamoro.” |

Caution notes
- “Babaylan” is often used as a pan-Philippine shorthand, but it is regionally specific and should not erase local ritual titles.
- Avoid romanticizing indigenous spirituality as automatically feminist, queer-affirming, or environmentally pure; the scholarship is more complex.
- “Folk Catholicism” is an analytic label, not a self-description for all devotees.

## 3) Colonial legacy / historical consciousness

| Concept | Suggested slug | One-sentence definition | Likely related / contrast concepts | Sources to cite |
|---|---|---|---|---|
| Colonial mentality | `colonial_mentality` | Internalized beliefs and practices that devalue Filipino people or culture and privilege colonizer-associated norms, institutions, aesthetics, or languages. | Related: `mestiza_privilege`, `english_prestige`, `skin_whitening`, `decolonization`; Contrast: `indigenization`, `cultural_reclamation` | E. J. R. David, Brown Skin, White Minds (2013); David, “A Colonial Mentality Model of Depression for Filipino Americans” (2008). |
| Benevolent assimilation | `benevolent_assimilation` | The U.S. colonial doctrine that framed conquest as tutelage and modernization, helping naturalize English schooling, sanitation regimes, and paternalist state power. | Related: `americanization`, `public_schooling`, `pensionado`, `colonial_mentality`; Contrast: `anti_colonial_nationalism` | Stuart Creighton Miller, Benevolent Assimilation (1982); Vicente L. Rafael, White Love and Other Events in Filipino History (2000). |
| Settler colonialism in Mindanao | `settler_colonialism_mindanao` | The long arc of Spanish, American, and especially Philippine-state frontier settlement in Mindanao that dispossessed Moro and Lumad communities while normalizing Christian settler claims to land and nation. | Related: `bangsamoro`, `mindanao_frontier`, `land_dispossession`, `internal_colonialism`; Contrast: `ancestral_domain`, `self_determination` | Patricio N. Abinales, Making Mindanao (2000); Thomas M. McKenna, Muslim Rulers and Rebels (1998); Lara & Schoofs, “Frontier polities and imaginaries” (2016); Adrian De Leon, Balikbayan (2026). |
| Mestiza / mestizo privilege | `mestiza_privilege` | A colonial and postcolonial hierarchy that attaches prestige, beauty, or social mobility to mixed, lighter-skinned, or white-adjacent appearance, though its meanings vary across period and class. | Related: `colorism`, `colonial_mentality`, `beauty_standard`, `class_status`; Contrast: `morena_pride`, `indigenous_identity` | E. J. R. David, Brown Skin, White Minds (2013); Tina Campt et al. / related race-image scholarship on mestiza privilege; Paul A. Kramer and related work on U.S. colonial racialization. |

Caution notes
- `colonial_mentality` is useful but can become a catch-all moral diagnosis; pair it with historical and structural concepts.
- `mestiza_privilege` should not be reduced to “Spanish blood”; it intersects with class, media, Chinese mestizo histories, and U.S. racial formations.
- Mindanao must be treated not as a peripheral footnote but as central to Philippine colonial modernity.

## 4) Diaspora identity

| Concept | Suggested slug | One-sentence definition | Likely related / contrast concepts | Sources to cite |
|---|---|---|---|---|
| Overseas Filipino Worker (OFW) | `overseas_filipino_worker` | A state-recognized and socially powerful category for temporary labor migrants whose remittances are celebrated as national lifelines even as precarity and family separation are normalized. | Related: `bagong_bayani`, `transnational_family`, `labor_brokerage_state`, `remittance`; Contrast: `permanent_settler_migrant` | Rhacel Salazar Parreñas, Children of Global Migration (2005); Robyn Magalit Rodriguez, Migrants for Export (2010); Anna Romina Guevarra, Marketing Dreams, Manufacturing Heroes (2010). |
| Transnational family | `transnational_family` | A family formation stretched across borders through remittances, digital intimacy, serial migration, and redistributed care work rather than a single shared household. | Related: `overseas_filipino_worker`, `care_chain`, `kin_obligation`, `left_behind_children`; Contrast: `co_resident_household` | Rhacel Salazar Parreñas, Children of Global Migration (2005); Yen Le Espiritu, Home Bound (2003). |
| Balikbayan | `balikbayan` | A return-migrant / return-visitor figure through which the Philippine state and diaspora imagine homecoming, roots, obligation, consumption, and the homeland itself. | Related: `balikbayan_box`, `diaspora_tourism`, `homeland`, `transnational_nostalgia`; Contrast: `nonreturn`, `exile` | Adrian De Leon, Balikbayan: A Revenant History of the Filipino Homeland (2026); Cynthia S. Blanc, “Balikbayan: A Filipino Extension of the National Imaginary…” (1996); Gina K. Velasco on queer/hetero balikbayan politics. |
| Filipinx | `filipinx` | A gender-inclusive diasporic label used especially in U.S. activist and academic contexts, embraced by some as queer/trans-inclusive and critiqued by others as linguistically unnecessary or U.S.-centric. | Related: `filipino_american`, `queer_diaspora`, `gender_inclusive_language`; Contrast: `filipino`, `pilipino`, `pinoy_pinay` | Denise Cruz, “On Filipinx: Who Gets to Name Whom?” (Alon, 2023); SAGE Encyclopedia of Filipina/x/o American Studies entries on queer Filipina/x/o Americans. |

Caution notes
- OFW is both a legal-bureaucratic and emotional-national category; avoid turning migrants into remittance abstractions.
- `Filipinx` should be clearly marked as diasporic and contested, not projected as universally accepted in the Philippines.
- `balikbayan` is not politically innocent; scholarship links it to nationalism, class, empire, and settler imaginaries.

## 5) Gender / sexuality

| Concept | Suggested slug | One-sentence definition | Likely related / contrast concepts | Sources to cite |
|---|---|---|---|---|
| Bakla | `bakla` | A Tagalog sexual/gender category that historically bundles effeminacy, same-sex desire, gender variance, and social style in ways that do not map neatly onto Western gay/trans distinctions. | Related: `swardspeak`, `tomboy`, `bayot`, `parlorista`; Contrast: `gay_western_identity`, `cisheteromasculinity` | Martin F. Manalansan IV, “Bakla (Philippines)” (2015); Manalansan, Global Divas (2003); J. Neil C. Garcia, Philippine Gay Culture (2008). |
| Tomboy | `tomboy_philippines` | In the Philippine context, tomboy often names female masculinity and can index lesbian, butch, transmasculine, or gender-nonconforming lives depending on context, generation, and class. | Related: `bakla`, `female_masculinity`, `lesbian`, `transmasculine`; Contrast: `filipina_femininity` | SAGE Encyclopedia of Trans Studies, “Tomboys (Philippines)”; Nadal & Corpus, “Tomboys and Baklas” (2013). |
| Bayot | `bayot` | A Cebuano/Visayan category often used for effeminate queer men or feminine male same-sex subjects, overlapping with but not reducible to Tagalog bakla and important for Visayan-centered analysis. | Related: `bakla`, `bisaya_visayan`, `swardspeak`, `cebuano_literature`; Contrast: `bakla_tagalog`, `straight_masculinity` | Cebuano literary scholarship on bayot; Michael Tan, “Survival through Pluralism”; Torres, “Ang Bayot ug ang Baybayon” (2021). |
| Asog | `asog` | A historical Visayan term for gender-crossing ritual specialists associated with babaylanic practice, useful for tracing precolonial and early colonial gender variance but not directly equivalent to modern LGBT labels. | Related: `babaylan`, `gender_variance`, `ritual_specialist`, `bayog`; Contrast: `modern_lgbt_identity` | Kai Ngu, “Gender Fluidity and Shamanism in the Spanish Philippines” (2022); J. Neil C. Garcia, “Baylan, Asog, Transvestism, and Sodomy…” (1999); Grace Nono, Babaylan Sing Back (2021). |

Caution notes
- Do not translate `bakla`, `bayot`, or `tomboy` straight into U.S. identity categories; retain local semantic range.
- `asog` is historically important but should be flagged as an archival / early colonial term, not a ready-made identity label for the present.
- Visayan queer categories are often erased by Manila-centric vocabularies; `bayot` helps counter that.

## Recommended “best 12” if the first pass must stay small
- `bisaya_visayan`
- `ilocano`
- `kapampangan`
- `bangsamoro`
- `babaylan`
- `folk_catholicism`
- `colonial_mentality`
- `settler_colonialism_mindanao`
- `overseas_filipino_worker`
- `balikbayan`
- `bakla`
- `bayot`

Why these 12
- Strong regional spread with clear non-Manila anchors.
- Good balance of homeland, Mindanao, and diaspora relevance.
- Includes highly reusable graph hubs that can support later concepts such as kapwa, utang na loob, hiya, fiesta, language politics, colorism, or balikbayan box.

Potential next-wave additions
- `kapwa`
- `utang_na_loob`
- `hiya`
- `pakikisama`
- `taglish` / `code_switching`
- `swardspeak`
- `fiesta`
- `balikbayan_box`
- `bagong_bayani`
- `lumad`
- `morena_beauty`
- `english_prestige`
