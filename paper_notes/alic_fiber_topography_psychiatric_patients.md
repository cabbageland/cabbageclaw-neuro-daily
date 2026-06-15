# Conserved fiber topography of the anterior limb of the internal capsule in treatment-resistant psychiatric patients

## Basic info

* Title: Conserved fiber topography of the anterior limb of the internal capsule in treatment-resistant psychiatric patients
* Authors: Reem El Jammal, Hideo Suzuki, Layth S. Mattar, Thomas Hamre, Sarah Soubra, Melissa A. Ryan, and colleagues
* Year: 2026
* Venue / source: bioRxiv preprint
* Link: https://doi.org/10.64898/2026.05.11.724148
* Date surfaced: 2026-06-15
* Why selected in one sentence: It asks a clean targeting question inside one of psychiatric DBS's most over-assumed white-matter corridors and tries to anchor the answer with both tractography and stimulation-evoked physiology.

## Quick verdict

* Highly relevant

This looks like an important targeting-logic note, even though the accessible evidence here is thinner than I would like. The core claim is that the anterior limb of the internal capsule keeps its ventral-dorsal projection order in treatment-resistant OCD and depression rather than degenerating into a patient-specific mush, which matters if people want to justify contact choice or tract engagement in psychiatric DBS. The catch is that this preserve is abstract-only after 10 full-text access attempts, so confidence is good on the framing, cohort, and headline result, but not on the tractography details or robustness checks.

## One-paragraph overview

The paper studies whether the anterior limb of the internal capsule, or ALIC, preserves the familiar topographic arrangement of prefrontal and subcortical fibers in treatment-resistant psychiatric patients. Using diffusion tractography in eighteen obsessive-compulsive disorder patients and five depression patients, the authors report that the canonical organization is preserved. They then add a smaller stimulation-physiology layer in depression patients by delivering single-pulse electrical stimulation through DBS leads in the ALIC and recording cerebro-cerebral evoked potentials in ventral prefrontal cortex. That physiology reportedly follows the same logic, with ventral ALIC mapping more toward medial ventral prefrontal cortex and dorsal ALIC mapping more toward lateral ventral prefrontal cortex in the left hemisphere. The useful claim is not that ALIC targeting is now solved. It is that psychiatric neuromodulation should stop treating this tract as a generic cable bundle and start taking its internal geometry seriously.

## Model definition

This paper does not present a trainable predictive model. It presents a tract-topography and stimulation-mapping pipeline.

### Inputs
Diffusion tractography data from patients with treatment-resistant obsessive-compulsive disorder and depression, plus single-pulse electrical stimulation delivered through ALIC DBS leads with ventral prefrontal cortex recordings in the depression subgroup.

### Outputs
Estimated topographic arrangement of prefrontal and subcortical fibers through the ALIC, and cerebro-cerebral evoked potential patterns relating ventral versus dorsal ALIC stimulation sites to ventral prefrontal recording locations.

### Training objective (loss)
There is no learnable loss exposed in the accessible text. This is a tractography-plus-evoked-physiology mapping study rather than a trained prediction model.

### Architecture / parameterization
A multimodal targeting-analysis stack combining diffusion tractography with stimulation-evoked response mapping through implanted ALIC DBS leads.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Psychiatric DBS often treats the ALIC as an important intervention corridor, but it is still too easy to assume that tract organization described in healthy or preclinical work carries over unchanged into treatment-resistant psychiatric patients.

### 2. What is the method?
The authors evaluate ALIC fiber topography with diffusion tractography in treatment-resistant obsessive-compulsive disorder and depression cohorts, then test whether stimulation-evoked ventral prefrontal responses follow the same ventral-dorsal organization in depression patients with DBS leads.

### 3. What is the method motivation?
If contact placement and tract engagement are supposed to matter, then the internal geometry of the tract needs to be stable enough to justify those claims in the actual patient populations receiving intervention.

### 4. What data does it use?
According to the accessible abstract-level text, the study uses tractography from eighteen treatment-resistant obsessive-compulsive disorder patients and five depression patients. In the depression subgroup, it also uses cerebro-cerebral evoked potentials elicited by single-pulse stimulation through ALIC DBS leads with recordings in ventral prefrontal cortex.

### 5. How is it evaluated?
By testing whether tractography recovers the expected topographic ordering of prefrontal and subcortical projections through the ALIC, and whether stimulation-evoked ventral prefrontal responses follow a corresponding ventral-medial and dorsal-lateral organization.

### 6. What are the main results?
- The topographic organization of prefrontal and subcortical projections through the ALIC appears preserved in treatment-resistant psychiatric patients.
- The ventral prefrontal evoked-response data reportedly follow a ventral ALIC to medial ventral prefrontal cortex and dorsal ALIC to lateral ventral prefrontal cortex pattern in the left hemisphere.
- The right hemisphere did not show the same clean physiology pattern in the accessible summary.

### 7. What is actually novel?
The novelty is not merely more tractography. It is the attempt to connect canonical ALIC geometry in psychiatric patients to actual stimulation effects, instead of leaving targeting claims at the level of anatomical tradition.

### 8. What are the strengths?
- Directly relevant tract for psychiatric DBS and capsulotomy logic.
- Combines structural mapping with stimulation-evoked physiology instead of relying on one modality alone.
- Useful for individualized targeting, contact selection, and mechanistic interpretation of ALIC interventions.
- The left-right asymmetry in the physiology summary is interesting because it hints that preserved gross topography does not automatically mean perfectly symmetric functional leverage.

### 9. What are the weaknesses, limitations, or red flags?
- This note is abstract-only after 10 full-text acquisition attempts across the PubMed landing page, PubMed DOI route, PubMed Central route, DOI landing page, bioRxiv HTML route, direct bioRxiv PDF route, ResearchGate mirror, Sciety mirror, preprint-index mirror, and search-engine PDF route.
- Without the full article text, I cannot inspect tractography choices, normalization strategy, laterality statistics, or subgroup caveats in enough detail.
- The depression subgroup is small from the accessible summary.
- The physiology result sounds more convincing in the left hemisphere than in the right, which may matter clinically.

### 10. What challenges or open problems remain?
The next hard question is whether preserved ALIC geometry is enough to improve patient-level targeting, or whether clinical benefit still depends more on patient-specific connectivity, symptom phenotype, and how the engaged fibers interact with downstream nodes.

### 11. What future work naturally follows?
Prospective studies that link ALIC tract engagement to response heterogeneity, patient-specific tractography-guided programming, stronger stimulation-evoked validation across both hemispheres, and comparison against simpler atlas-based contact heuristics.

### 12. Why does this matter for cabbageland?
Because this repo keeps circling the same intervention problem: people talk as if white-matter target geometry is obvious, then personalize around it without checking whether the geometry is even preserved in the patients who matter. This paper says that at least some of that geometry survives into treatment-resistant psychiatric cohorts, which makes pathway-aware targeting more defensible.

### 13. What ideas are steal-worthy?
- Treat ALIC targeting as an internal topography problem, not just a coordinate problem.
- Pair tractography claims with stimulation-evoked physiology whenever possible.
- Use preserved tract order as a baseline prior, then ask where patient-specific deviations actually matter.
- Compare tract-engagement logic against symptom-domain and circuit-engagement biomarkers rather than letting any one modality pretend to be sufficient.

### 14. Final decision
Preserve, but as a confidence-limited targeting note rather than a fully trusted methods read. The paper is too relevant to ignore, but not accessible enough in this environment to claim more certainty than the abstract supports.
