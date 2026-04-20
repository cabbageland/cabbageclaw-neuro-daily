# Non-invasive Neuromodulation Targeting Approach by Mapping Stimulations and Lesions That Modify Visual Memory

## Basic info

* Title: Non-invasive Neuromodulation Targeting Approach by Mapping Stimulations and Lesions That Modify Visual Memory
* Authors: Simon Kwon, Soyoung Lee, Joshua S. Siegel, Nicole Chiulli, Michael Freedberg, Melissa Hebscher, Joshua Hendrikse, Molly S. Hermiller, Gong-Jun Ji, Arielle Tambini, Eyre Ye, Shira Cohen-Zimerman, Maurizio Corbetta, Jordan Grafman, Joel L. Voss, Shan H. Siddiqi
* Year: 2026
* Venue / source: bioRxiv
* Link: https://www.biorxiv.org/content/10.64898/2026.04.10.717784v1
* Date surfaced: 2026-04-19
* Why selected in one sentence: It uses convergent lesion and stimulation network mapping to derive candidate noninvasive targets for visual memory, with an explicit age interaction instead of a fake one-size-fits-all target story.

## Quick verdict

* Highly relevant

This is not clinical proof, but it is exactly the kind of target-discovery logic that is more interesting than another shallow stimulation trial. The best part is the convergence across perturbation modalities and the explicit age-dependent inversion of effect direction. The main caveat is that normative-connectivity target maps can look more definitive than they really are.

## One-paragraph overview

The paper asks whether symptom-specific network-mapping logic, already used for other neuromodulation targets, can be applied to visual memory rather than only to broad "memory" phenotypes. It combines data from TMS, penetrating head trauma, and ischemic stroke to identify a network linked to visual-memory change, then tests the age dependence of that relationship in an independent preclinical Alzheimer's-related dataset. The authors then compute electric-field overlaps for candidate TMS sites and report convergence with several known memory-related targets, including the precuneus, cortical-hippocampal network, and dorsolateral prefrontal cortex, with peaks in medial posterior parietal, angular gyrus, and left anterior middle frontal regions. The paper is strongest as a targeting framework, not as evidence that any one site already works best in treatment.

## Model definition

The paper is mostly a mapping and target-discovery study rather than a standard learnable prediction model.

### Inputs
Connectivity profiles of stimulation sites, lesion locations, and atrophy patterns associated with visual-memory change across multiple datasets, plus electric-field models for candidate TMS sites.

### Outputs
A putative network associated with visual-memory modulation, age-dependent directionality of effects, and candidate noninvasive stimulation targets that overlap that network.

### Training objective (loss)
The accessible abstract does not specify an optimization loss. The work appears to rely on connectivity mapping and overlap analyses rather than a clearly described trainable loss-based model.

### Architecture / parameterization
A multimodal lesion-network and stimulation-network mapping pipeline with electric-field overlap analysis for candidate targets.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Memory-targeting approaches in neuromodulation are still diffuse and often underspecified. The paper tries to localize more precise visual-memory targets using perturbation-informed network mapping.

### 2. What is the method?
Map connectivity of lesions and stimulation sites associated with visual-memory change across multiple datasets, test for convergence, evaluate age-dependent inversion, and derive candidate TMS targets by overlapping electric-field models with those inferred networks.

### 3. What is the method motivation?
If lesions and stimulation sites that alter the same function converge onto a shared network, that network may provide a more principled target-discovery route than anatomy-first guesswork.

### 4. What data does it use?
Three main datasets totaling 544 individuals: TMS with 262 participants, penetrating head trauma with 169 participants, and ischemic stroke with 113 participants, plus an independent replication analysis in 1,240 people with preclinical Alzheimer's disease.

### 5. How is it evaluated?
By convergence of lesion and stimulation network maps for visual-memory effects, replication of the age-direction interaction, and overlap of derived networks with candidate TMS target electric fields.

### 6. What are the main results?
The authors report a network specifically associated with changes in visual memory, not just generic memory function. They also report that the direction of effect flips depending on whether injury or stimulation occurred at younger versus older age, and that this age effect replicates in an Alzheimer's-related dataset. Candidate TMS targets overlap established memory-related targets but peak differently across medial posterior parietal, angular gyrus, and left anterior middle frontal regions.

### 7. What is actually novel?
Symptom-specific memory targeting through convergent lesion and stimulation mapping, plus the explicit age-dependent inversion claim, is the main novelty.

### 8. What are the strengths?
- Good perturbation logic across lesions and stimulation rather than one-modality correlation.
- Avoids pretending that all memory phenotypes share one network.
- Explicitly surfaces age dependence.
- Translates network results into concrete candidate target maps.
- Includes independent replication of the age effect.

### 9. What are the weaknesses, limitations, or red flags?
- This is still target nomination, not therapeutic validation.
- Normative connectivity mapping can overstate precision.
- Dataset heterogeneity may blur mechanism even while helping convergence.
- The abstract does not reveal how robust the maps are to preprocessing, atlas choice, or alternative connectomes.
- Age-dependent sign inversion is interesting but also a place where confounding can hide.

### 10. What challenges or open problems remain?
Prospective head-to-head trials of the nominated targets, stronger mechanistic explanation for the age interaction, and tests of whether symptom-specific maps generalize beyond visual memory.

### 11. What future work naturally follows?
Direct stimulation comparisons across nominated targets, age-stratified trials, personalized rather than purely normative connectivity mapping, and integration with structural degeneration or electrophysiology.

### 12. Why does this matter for cabbageland?
Because it is a strong example of network-informed targeting that begins from perturbation evidence rather than from decorative connectome rhetoric. It is useful for thinking about how symptom-specific targets should be derived and how heterogeneity should be handled.

### 13. What ideas are steal-worthy?
- Use convergent lesion-plus-stimulation evidence to derive target networks.
- Treat age as a possible effect-direction variable, not just a nuisance covariate.
- Translate network maps into actionable electric-field target proposals instead of leaving them as abstract blobs.
- Separate target discovery from target validation very clearly.

### 14. Final decision
Keep as an important network-targeting reference. Strong for framing and target generation, not yet strong for clinical claims.
