# Accelerated TMS is associated with changes of subgenual cingulate-default mode network coupling in depression: an observational 7 Tesla fMRI study

## Basic info

* Title: Accelerated TMS is associated with changes of subgenual cingulate-default mode network coupling in depression: an observational 7 Tesla fMRI study
* Authors: Tobias Bracht, Pascal Borel, Stefan Dendorfer, Leila M. Soravia, Kristina Adorjan, Sebastian Walther, Andrea Federspiel, Roland Wiest, Gianluca A. Florineth, and Niklaus Denier
* Year: 2026
* Venue / source: European Archives of Psychiatry and Clinical Neuroscience
* Link: https://link.springer.com/article/10.1007/s00406-026-02355-2
* Date surfaced: 2026-09-20
* Why selected in one sentence: It uses 7-Tesla resting-state fMRI to ask whether accelerated left-DLPFC iTBS changes sgACC-default-mode coupling in depression, which is exactly the right mechanistic neighborhood even though the design is observational.

## Quick verdict

* Useful

This is worth keeping as a clinical-mechanistic signal, not as proof that accelerated TMS caused the reported network change. The useful part is the pre/post 7-Tesla sgACC seed analysis showing reduced coupling with posterior DMN and left frontal cortex after a two-week accelerated iTBS course. The weak part is severe: no sham, no randomization, stable but heterogeneous medications and psychotherapy exposure, small N, and exploratory uncorrected correlations. Treat it as a target-engagement clue, not as a causal efficacy paper.

## One-paragraph overview

The study enrolled patients with current depression who were already planned for accelerated TMS and scanned them with 7-Tesla MRI before and after a two-week left-DLPFC accelerated iTBS course. The authors used the sgACC as a seed region and asked whether resting-state functional connectivity to DMN-related regions changed after treatment, with healthy controls scanned twice to provide a test-retest comparison. Patients improved clinically and showed reduced sgACC connectivity with bilateral precunei and left frontal cortex; the sgACC-precuneus change was also associated with mindfulness improvement in an exploratory analysis. The paper is useful because it keeps the intervention mechanism at the network level, but the design cannot tell whether aTMS specifically caused the imaging or clinical changes.

## Model definition

This paper does not contain a trainable predictive model. Its main computational component is seed-based resting-state functional-connectivity analysis.

### Inputs

Pre/post 7-Tesla structural and resting-state fMRI, a bilateral sgACC atlas seed, motion and nuisance regressors, depression and mindfulness/affect scales, medication-equivalent covariates, and group/time labels for patients and healthy controls.

### Outputs

Whole-brain sgACC resting-state functional-connectivity maps, longitudinal difference maps, significant FWE-corrected clusters, group-by-time effects, clinical symptom changes, remission/response counts, and exploratory correlations between connectivity change and clinical or mindfulness change.

### Training objective (loss)

There is no training loss. The analysis computes Pearson-correlation-based rs-FC maps and uses voxelwise statistics, cluster-level FWE correction, linear mixed-effects models, paired tests, and exploratory Spearman correlations.

### Architecture / parameterization

Observational pre/post clinical imaging study with a left-DLPFC accelerated iTBS intervention, a healthy repeated-scan control group, CONN/SPM seed-based rs-FC analysis, and clinical scale follow-up.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

It asks whether accelerated TMS for depression is accompanied by measurable changes in sgACC-DMN coupling, a network relationship often invoked in depression TMS targeting but not always measured directly after treatment.

### 2. What is the method?

Twenty-two patients with current depression received a two-week accelerated iTBS course targeting left DLPFC by Beam-F3. Four iTBS sessions were delivered per treatment day, five days per week, for ten treatment days and 24,000 total pulses. Patients underwent 7-Tesla MRI before and after treatment. Fourteen healthy controls were scanned twice without intervention. The authors computed sgACC seed-based resting-state connectivity maps, tested longitudinal changes, compared patients and controls, and correlated imaging changes with clinical scales.

### 3. What is the method motivation?

The sgACC is a depression-relevant hub, and DLPFC TMS is often justified partly through its anticorrelated relationship with sgACC. If accelerated DLPFC stimulation works through a distributed network rather than a local cortical patch, sgACC-DMN connectivity should be one plausible target-engagement readout.

### 4. What data does it use?

The final longitudinal sample included 22 patients and 14 healthy controls. Patients had MDD except for one bipolar depression type 2 case, with substantial clinical heterogeneity and mostly ongoing antidepressant medication. Imaging included high-resolution 7-Tesla structural MRI and six-minute resting-state fMRI at baseline and follow-up. Clinical measures included MADRS, BDI-II, CHIME mindfulness, and EMO-Check positive/negative affect.

### 5. How is it evaluated?

Evaluation is pre/post imaging and clinical change, not randomized clinical efficacy. The authors test within-patient sgACC rs-FC change, repeated-scan change in controls, group-by-time interactions for significant clusters, baseline/follow-up patient-control differences, and exploratory associations between imaging change and symptom or mindfulness change.

### 6. What are the main results?

Patients improved on depression severity, mindfulness, and positive affect. MADRS dropped from 26.2 +/- 9.2 to 13.7 +/- 8.7, with 13 responders and 7 remitters reported. Imaging showed reduced sgACC connectivity with bilateral precunei and left frontal cortex after aTMS. At baseline, patients had higher sgACC connectivity with a cluster including left precuneus/lateral occipital cortex and right superior frontal gyrus. The sgACC-precuneus connectivity reduction correlated with CHIME mindfulness improvement at p = 0.008, but this was uncorrected and exploratory; the MADRS association was not significant.

### 7. What is actually novel?

The strongest novelty is not "aTMS changes depression networks" in general. It is the combination of accelerated TMS with ultra-high-field 7-Tesla repeated rs-fMRI focused on sgACC-DMN coupling. That gives a sharper target-engagement measurement than a routine symptom-only accelerated TMS report.

### 8. What are the strengths?

The paper measures a plausible network mechanism instead of only reporting symptom change.

The 7-Tesla acquisition gives better spatial and signal detail than ordinary 3T resting-state studies.

The sgACC seed choice is mechanistically motivated by depression TMS targeting literature.

The authors are explicit that the mindfulness correlation is exploratory and needs replication.

### 9. What are the weaknesses, limitations, or red flags?

The design is observational, unblinded, non-randomized, and has no sham stimulation. That means clinical and connectivity changes could reflect placebo effects, regression, concurrent care, medication context, spontaneous remission, or generic time effects.

The sample is small and clinically heterogeneous. Most patients were medicated, and several had comorbidities.

The target was Beam-F3 left DLPFC rather than individualized DLPFC-sgACC anticorrelation targeting, which weakens the precision-targeting story.

The exploratory correlations were uncorrected for multiple comparisons and the MADRS-connectivity association did not reach significance.

### 10. What challenges or open problems remain?

The main open problem is causal identification. A proper sham-controlled, randomized, larger study is needed to determine whether accelerated iTBS specifically changes sgACC-DMN coupling and whether that change mediates symptom improvement. Another open problem is whether individualized connectivity-guided targeting would produce stronger or more specific sgACC effects than Beam-F3.

### 11. What future work naturally follows?

Run a sham-controlled aTMS imaging trial with individualized targeting, preregistered sgACC-DMN endpoints, objective monitoring of rest-state vigilance/eyes, and mediation tests linking target engagement to symptom and rumination/mindfulness change. It would also be useful to compare 7T-derived target-engagement markers against cheaper clinical readouts.

### 12. Why does this matter for cabbageland?

Cabbageland cares about interventions as state and network perturbations, not just treatment labels. This paper is a useful example of measuring the hypothesized downstream circuit of DLPFC stimulation, while also showing how quickly an attractive mechanism becomes soft if the design cannot separate stimulation effects from context and time.

### 13. What ideas are steal-worthy?

Use sgACC-DMN coupling as a target-engagement endpoint when the intervention rationale depends on DLPFC-sgACC network modulation.

Pair symptom scales with process measures like rumination, mindfulness, or emotion regulation, because those may sit closer to the network being changed than a global depression score.

Treat ultra-high-field imaging as a mechanistic probe, not a magic causal instrument: better measurement does not rescue an uncontrolled design.

### 14. Final decision

Keep as a useful clinical-mechanistic note. It is not causal evidence for aTMS efficacy, but it is a good reminder that depression neuromodulation should be judged by whether the intended network moves in a plausible direction and whether the study design can actually support that claim.
