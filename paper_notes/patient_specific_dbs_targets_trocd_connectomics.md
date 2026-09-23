# Patient-specific structural connectomic differences of deep brain stimulation targets in treatment-resistant obsessive-compulsive disorder patients

## Basic info

* Title: Patient-specific structural connectomic differences of deep brain stimulation targets in treatment-resistant obsessive-compulsive disorder patients
* Authors: Rene Marquez-Franco, Luis Ruelas, Ricardo Loucao, Rabea Schmahl, Fatima Ximena Cid Rodriguez, Petra Heiden, Jens Kuhn, Anne Koy, Veerle Visser-Vandewalle, Pablo Andrade
* Year: 2026
* Venue / source: Translational Psychiatry
* Link: https://www.nature.com/articles/s41398-026-04441-4
* Date surfaced: 2026-09-23
* Why selected in one sentence: It is a clinically direct DBS targeting paper that compares patient-space tractography profiles for NAc/ALIC, MFB, and amSTN targets in treatment-resistant OCD instead of flattening them into one generic CSTC story.

## Quick verdict

* Highly relevant

This is worth preserving as targeting infrastructure, not as outcome proof. The paper shows that three clinically used DBS target regions for treatment-resistant OCD engage different patient-specific tractography profiles, with NAc/ALIC more fronto-limbic, MFB more reward/pallidal, and amSTN more motor-control weighted. The major caveat is also the important one: all patients actually received NAc/ALIC DBS, while MFB and amSTN were standardized virtual ROIs, so the paper does not prove target-specific clinical superiority.

## One-paragraph overview

The study takes structural and diffusion MRI from 22 treatment-resistant OCD patients who underwent NAc/ALIC DBS and reconstructs whole-brain probabilistic tractography in each patient's native space. The authors then place standardized 2 mm spherical ROIs at three DBS-relevant target regions, NAc/ALIC, medial forebrain bundle, and anteromedial subthalamic nucleus, and compare the streamline, FA, and MD profiles linking those ROIs to OCD-relevant cortical, subcortical, and white-matter regions. NAc/ALIC shows the strongest fronto-limbic connectivity to medial/lateral orbitofrontal cortex, rostral anterior cingulate, insula, amygdala, and accumbens; MFB emphasizes reward-related pallidal and rostral middle frontal connections; and amSTN emphasizes precentral/paracentral and superior frontal motor-control circuitry. The useful contribution is a more differentiated target-language for OCD DBS, but the paper remains exploratory because it does not link these profiles to implanted electrodes, stimulation fields, symptom dimensions, or longitudinal outcome.

## Model definition

### Inputs
Patient-specific T1, T2, and diffusion MRI from 22 treatment-resistant OCD patients; standardized stereotactic 2 mm spherical ROIs for NAc/ALIC, MFB, and amSTN transformed into native space; atlas-defined OCD-relevant cortical, subcortical, and white-matter ROIs; and meta-analytic functional-network maps for affect, salience, default-mode, reward/motivation, and cognitive/motor-control networks.

### Outputs
Target-specific tractography-derived structural connectivity profiles, including streamline counts, FA, and MD sampled along target-specific tract selections; qualitative mappings between structural ROIs and functional-network interpretations; and hypotheses about which symptom-relevant networks each DBS target region may engage.

### Training objective (loss)
There is no trainable predictive model and no optimization loss. The workflow computes probabilistic tractography and group-level statistical comparisons of target-specific streamline and diffusion-metric profiles.

### Architecture / parameterization
A patient-space diffusion-connectomics pipeline using FSL, FreeSurfer, ANTs, MRtrix3, lead-DBS, and DSI-Studio; single-shell 3-tissue constrained spherical deconvolution; anatomically constrained tractography; SIFT-reduced whole-brain tractograms; ROI-based streamline selection; and nonparametric group comparisons across target regions.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
DBS can help treatment-resistant OCD, but clinical response varies and the field still argues about targets as if NAc/ALIC, MFB, and amSTN were interchangeable handles on one cortico-striato-thalamo-cortical circuit. The paper tries to make target choice more mechanistic by asking which patient-specific structural networks each target region actually samples.

### 2. What is the method?
The authors reconstruct whole-brain probabilistic tractography from each patient's diffusion MRI, transform standardized DBS target ROIs into native space, select target-specific streamline subsets, and compare streamline counts plus FA/MD across OCD-relevant regions. They then align the anatomical pattern qualitatively with meta-analytic functional networks implicated in OCD.

### 3. What is the method motivation?
Group-average connectomes and standard stereotactic coordinates can hide interindividual anatomy. If OCD symptom dimensions map partly onto different affective, salience, reward, and motor-control networks, then DBS planning should eventually care about which network a patient-specific target actually engages.

### 4. What data does it use?
The dataset includes structural and diffusion MRI from 22 treatment-resistant OCD patients treated with NAc/ALIC DBS at the University Hospital Cologne between 2016 and 2025. The diffusion acquisition used 40 directions at b = 1000 s/mm2, 2 mm isotropic DWI, and 0.5 x 0.5 x 1 mm structural imaging. The analysis covers 44 hemispheres.

### 5. How is it evaluated?
The paper evaluates whether the three target ROIs differ in tractography-derived connectivity to a priori OCD-relevant regions and in diffusion metrics sampled along target-specific tracts. It uses Kruskal-Wallis and Dunn post-hoc tests for cross-target differences, plus qualitative anatomical and functional-network interpretation.

### 6. What are the main results?
NAc/ALIC has higher streamline counts to fronto-limbic regions, including medial and lateral orbitofrontal cortex, rostral anterior cingulate, insula, amygdala, and accumbens, with several target differences reported at p < 0.001. MFB preferentially connects with reward-related pallidum and rostral middle frontal cortex. amSTN shows stronger connectivity to precentral, paracentral, and superior frontal regions, consistent with cognitive/motor-control network engagement. FA differs across target-specific frontopontine-corticothalamic tract selections, with NAc/ALIC lower than amSTN and MFB bilaterally.

### 7. What is actually novel?
The novelty is not "OCD is a CSTC disorder" or "tractography can help DBS." The useful move is comparing three DBS-relevant target regions in the same treatment-resistant OCD patients using patient-space tractography, then spelling out how each target samples partially distinct functional-network hypotheses.

### 8. What are the strengths?
- Directly targets a live clinical planning problem in psychiatric DBS.
- Uses patient-specific diffusion and structural MRI rather than only normative connectomes.
- Compares multiple target regions inside the same subjects, which makes the target differences cleaner.
- Interprets FA and MD cautiously rather than treating them as direct microstructural truth.
- Explicitly warns that tractography profiles are hypothesis-generating until outcome-linked validation exists.

### 9. What are the weaknesses, limitations, or red flags?
- All patients received NAc/ALIC DBS; the MFB and amSTN analyses are virtual standardized ROIs, not implanted target cohorts.
- There is no direct linkage to electrode localization, volume of tissue activated, stimulation settings, symptom dimensions, or longitudinal clinical response.
- The sample is small, single-center, and hemisphere observations from the same patient are not fully independent.
- Probabilistic tractography can create false-positive or anatomically implausible streamlines, especially around crossing fibers in the internal capsule.
- Streamline count is not axon count and should not be overread as physiological modulation strength.

### 10. What challenges or open problems remain?
The obvious next problem is to connect patient-specific tractography to actual stimulation fields and clinical outcomes. The field also needs dimensional symptom phenotyping, multicenter cohorts, prospective target selection, and tests of whether network-matched target choice beats standard anatomical planning.

### 11. What future work naturally follows?
Prospective DBS studies that combine electrode localization, e-field or pathway activation modeling, dimensional OCD symptom measures, and longitudinal outcomes. A stronger version would compare patients implanted in NAc/ALIC, MFB, and amSTN, then ask whether specific symptom clusters or side-effect profiles match the predicted target-network profiles.

### 12. Why does this matter for cabbageland?
Because it sharpens the target-selection question. Instead of saying "stimulate the OCD circuit," it asks whether this patient needs more fronto-limbic affect regulation, reward/motivation modulation, or motor-control/inhibitory-loop engagement, and whether anatomy supports that choice.

### 13. What ideas are steal-worthy?
- Treat psychiatric DBS targets as network-sampling hypotheses, not anatomical brands.
- Compare candidate targets inside the same patient-specific connectome before making target claims.
- Keep symptom dimensions, stimulation fields, and tractography in the same causal sentence.
- Use existing target disagreements as a way to separate affective, reward, salience, and motor-control intervention logic.

### 14. Final decision
Preserve. This is not clinical proof, but it is a useful target-comparison paper for OCD DBS and a good reminder that patient-specific connectomics only becomes intervention science once it is tied to stimulation fields and outcomes.
