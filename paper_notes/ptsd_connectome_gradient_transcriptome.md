# Connectome gradient dysfunction in earthquake-induced posttraumatic stress disorder and its association with gene expression and neurotransmitter profiles

## Basic info

* Title: Connectome gradient dysfunction in earthquake-induced posttraumatic stress disorder and its association with gene expression and neurotransmitter profiles
* Authors: Xun Zhang, Wenxiong Liu, Li Chen, Chao Zuo, Huan Lan, Lingjiang Li, Graham J. Kemp, Su Lui, Xueling Suo, and Qiyong Gong
* Year: 2026
* Venue / source: Psychological Medicine
* Link: https://doi.org/10.1017/S0033291726105388
* Date surfaced: 2026-09-15
* Why selected in one sentence: It treats PTSD as a disruption of sensory-to-transmodal connectome hierarchy and then tests whether that map lines up with symptom, developmental, transcriptomic, and neurotransmitter structure.

## Quick verdict

* Highly relevant

This is worth preserving because it gives PTSD a sharper network object than another region list: altered position along the principal unimodal-to-transmodal gradient. The paper is not causal and should not be inflated into a biomarker ready for treatment selection. Its value is in the multiscale framing: visual/limbic exaggeration, ventral-attention/frontoparietal reduction, adolescent subcortical vulnerability, and molecular atlas colocalization become one testable hierarchy story.

## One-paragraph overview

The authors analyze resting-state fMRI from 86 adult earthquake-exposed PTSD patients and 86 trauma-exposed non-PTSD controls, with an additional adolescent trauma-exposed dataset for age interaction. For each participant they build a voxelwise functional connectome, use diffusion map embedding to recover the principal gradient from unimodal sensory networks to transmodal association networks, and compare gradient metrics across diagnosis. PTSD shows a globally wider and more variable principal gradient, higher gradient scores in visual and limbic systems, and lower scores in ventral attention and frontoparietal systems. Those maps are then related to CAPS symptoms, Neurosynth cognitive terms, Allen Human Brain Atlas gene-expression maps, and PET/SPECT neurotransmitter maps. The strongest interpretation is not "PTSD equals this gradient," but that persistent post-trauma symptoms may involve a distorted hierarchy between sensory/memory systems and control/salience systems.

## Model definition

### Inputs
Resting-state fMRI time series from trauma-exposed adults with PTSD and matched trauma-exposed non-PTSD controls; covariates including age, sex, education, time since trauma, and mean framewise displacement; an adolescent trauma-exposed comparison sample; Allen Human Brain Atlas regional gene-expression profiles; PET/SPECT neurotransmitter receptor and transporter maps; Neurosynth cognitive term maps.

### Outputs
Individual principal functional-connectome gradients; global metrics including explained ratio, gradient range, and gradient variation; subnetwork and voxelwise PTSD-TENP gradient-difference maps; symptom and age-interaction associations; PLS transcriptomic components and enrichment results; neurotransmitter-system spatial correlations.

### Training objective (loss)
There is no supervised clinical predictor or trainable treatment model. Diffusion map embedding estimates low-dimensional connectome gradients from similarity among thresholded functional-connectivity profiles, and partial least squares regression finds gene-expression components associated with the PTSD-TENP gradient-difference map.

### Architecture / parameterization
A gradient-decomposition and multiscale association pipeline: voxelwise rs-fMRI functional connectivity, cosine similarity over top connections, diffusion map embedding with alpha = 0.5, Procrustes alignment, GLM/permutation testing for group differences, Neurosynth spatial decoding, Allen Human Brain Atlas PLS regression, and JuSpace neurotransmitter-map correlations.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
PTSD neuroimaging often names abnormal regions or networks without saying how sensory, salience, memory, and control systems are reorganized as a hierarchy. The paper asks whether PTSD alters the principal functional gradient that normally separates unimodal sensorimotor systems from transmodal cognitive systems, and whether those alterations connect to symptoms and molecular architecture.

### 2. What is the method?
The authors construct voxelwise resting-state functional connectomes, keep each node's strongest 10% connections, compute similarity among connectivity profiles, and apply diffusion map embedding. They focus on the principal gradient, compare global and local gradient measures between PTSD and trauma-exposed controls, then map those differences onto symptoms, age, cognitive term maps, gene expression, and neurotransmitter maps.

### 3. What is the method motivation?
Gradient mapping can represent continuous transitions in connectome organization better than a hard parcellation of discrete networks. For PTSD, that matters because the disorder plausibly involves distorted interaction between low-level sensory trauma traces, limbic memory/threat systems, attention, and high-level control.

### 4. What data does it use?
The main sample is 86 untreated adult PTSD patients and 86 trauma-exposed non-PTSD controls from the same 2008 Sichuan earthquake survivor cohort, scanned 8-15 months after trauma. The age-interaction analysis also uses a previously reported adolescent sample with 26 PTSD and 25 trauma-exposed non-PTSD participants. Molecular analyses use published healthy-donor gene-expression and neurotransmitter receptor/transporter atlases, not patient tissue.

### 5. How is it evaluated?
Evaluation is statistical and associational. The paper tests group differences in global, subnetwork, and voxelwise gradient measures; correlations with CAPS severity; diagnosis-by-sex and diagnosis-by-age interactions; cognitive-term spatial decoding; PLS association between gradient differences and gene-expression maps; and spatial correlation with neurotransmitter maps with correction for spatial autocorrelation and multiple comparisons.

### 6. What are the main results?
PTSD participants had a principal gradient that explained more connectome variance, spanned a wider range, and showed more spatial variation than trauma-exposed controls. At the network level, PTSD showed higher gradient scores in visual and limbic networks and lower scores in ventral attention and frontoparietal networks. Across the combined trauma-exposed sample, CAPS severity correlated positively with visual and limbic gradient scores and negatively with ventral attention gradient scores, but those correlations did not survive when tested inside the PTSD group alone. The adolescent comparison suggested a stronger PTSD-related subcortical gradient decrease in adolescents than adults. The gradient-difference map aligned with gene-expression patterns enriched for mitochondria and DNA/RNA metabolism and with dopamine D2, kappa opioid, noradrenaline transporter, and cholinergic VAChT distributions.

### 7. What is actually novel?
The novelty is the hierarchy framing. Instead of treating PTSD as isolated amygdala, hippocampal, visual, salience, or prefrontal findings, the paper asks how the sensory-to-transmodal axis itself is warped, then connects that warp to transcriptomic and neurotransmitter atlases.

### 8. What are the strengths?
The trauma-exposed control group is stronger than a generic healthy-control contrast because both groups experienced the same disaster context. The sample is relatively clean, with untreated PTSD and no psychiatric comorbidity. The analysis is multiscale without pretending that one modality is enough: functional hierarchy, symptoms, development, cognitive decoding, gene expression, and neurotransmitter maps are all interrogated. The paper also states several limitations plainly, including cross-sectional design and atlas-based molecular inference.

### 9. What are the weaknesses, limitations, or red flags?
The study is cross-sectional, so it cannot tell whether gradient abnormalities are vulnerability markers, acute state effects, compensatory changes, or illness consequences. Cognitive performance was not directly measured; Neurosynth decoding is indirect. The transcriptomic analysis uses healthy postmortem donor data, not PTSD tissue. There is no nontraumatized healthy control group, so major-trauma exposure itself is not separated from PTSD-specific persistence. The CAPS-gradient associations are mainly between-group effects, since within-PTSD symptom correlations were not significant. The cohort is earthquake-specific and comorbidity-free, which helps internal validity but limits generalization to interpersonal trauma, combat trauma, chronic developmental trauma, and common psychiatric comorbidity.

### 10. What challenges or open problems remain?
The main open problem is temporal direction. Longitudinal data are needed to tell whether the widened gradient predicts PTSD onset, tracks symptom change, or reflects stable post-trauma reorganization. The molecular colocalizations need mechanistic validation rather than atlas overlap. Intervention relevance also remains untested: the paper does not show that gradient measures predict response to psychotherapy, TMS, DBS, pharmacology, MDMA-assisted therapy, or exposure-based treatment.

### 11. What future work naturally follows?
A good next step would combine longitudinal trauma cohorts, symptom-process measures, task data for threat learning and intrusive imagery, structural and functional gradients, and treatment outcomes. For intervention work, the obvious test is whether baseline hierarchy distortion or post-treatment gradient normalization predicts response to exposure therapy, threat-circuit TMS, neuromodulation, or pharmacologic/psychedelic-assisted psychotherapy.

### 12. Why does this matter for cabbageland?
It gives trauma and PTSD work a cleaner state-space object. For cabbageland's purposes, the interesting thing is not just that PTSD has abnormal visual, limbic, attention, and frontoparietal regions. It is that the disorder may distort the hierarchy that governs how sensory evidence, memory, threat, salience, and control separate or collapse. That is useful for thinking about hypnosis, exposure, trauma-memory intrusions, and neuromodulation as state-transition problems.

### 13. What ideas are steal-worthy?
- Treat psychiatric network findings as changes in hierarchy geometry, not only as region-by-region abnormalities.
- Use trauma-exposed controls when the question is persistent PTSD rather than trauma exposure itself.
- Separate categorical markers from dimensional symptom markers; a map can distinguish PTSD from controls without tracking severity inside PTSD.
- Pair visual/limbic trauma-memory hypotheses with control/salience hierarchy measures.
- Use atlas colocalization as hypothesis generation, not mechanism proof.
- Ask whether intervention changes the sensory-to-transmodal gradient in the direction the treatment story implies.

### 14. Final decision
Preserve. This is not ready-made precision psychiatry, and it is definitely not causal treatment logic. But it is a strong network-neuroscience paper for PTSD because it converts a scattered set of trauma findings into a testable hierarchy-disorganization account with clear developmental and molecular hypotheses.
