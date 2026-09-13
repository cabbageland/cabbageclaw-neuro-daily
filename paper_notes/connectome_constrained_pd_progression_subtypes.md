# Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model

## Basic info

* Title: Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model
* Authors: Daniel Semchin, Emile d'Angremont, Hao Ding, Alan Antar, Marco Lorenzi, Konstantinos Arfanakis, Ysbrand van der Werf, Paul Thompson, Boris Gutman
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2609.10890
* Date surfaced: 2026-09-13
* Why selected in one sentence: It makes Parkinson's disease progression subtyping a connectome-constrained dynamical-systems problem instead of another cluster-label exercise.

## Quick verdict

* Highly relevant

This is a strong computational-network preserve, with the usual preprint caveat. The paper's useful move is to join subject-specific disease time, subtype discovery, and structural-connectome-constrained nonlinear progression in one model. It does not prove clinical actionability, but it gives a more disciplined representation of heterogeneity than purely descriptive subtyping.

## One-paragraph overview

The paper extends the COMIND disease-progression model so that Parkinson's disease progression is represented as coupled logistic-diffusion dynamics over cortical, subcortical, and clinical biomarkers. Each subject gets a latent disease-time shift and a hard subtype assignment, while each subtype gets its own sparse spatial forcing pattern over biomarkers. Applied to PPMI longitudinal morphometry and clinical scores, the model selects four progression subtypes and shows that those subtypes align with hold-out motor phenotype and full-cohort genetic groupings better than a matched SuStaIn benchmark. The important point is not that these are final Parkinson's biotypes. It is that subtype structure is forced to pay rent through trajectories, connectome constraints, and out-of-sample clinical/genetic association.

## Model definition

### Inputs
Longitudinal PPMI T1-weighted MRI-derived morphometry and clinical measures from Parkinson's disease subjects, expressed as 85 biomarkers: 68 Desikan-Killiany cortical thickness regions, 14 subcortical regions, and MoCA, tremor-dominant, and postural-instability/gait-difficulty clinical scores. The model also uses a group structural connectivity matrix from the IIT Human Brain Atlas v5.0, thresholded to the top 10 percent of streamline-count connections and normalized.

### Outputs
Subject-specific latent disease-time shifts, hard subtype assignments, subtype-specific biomarker trajectories, sparse subtype forcing maps, a shared network-mediated propagation timescale, regional self-propagation rates, and scaled predictions of biomarker abnormality over disease time.

### Training objective (loss)
The objective combines a Gaussian iid biomarker likelihood with priors and penalties: L1 sparsity on subtype forcing terms and self-propagation rates, a log-normal prior on the network timescale, an L2 penalty on scaling parameters, and a Jensen-Shannon divergence penalty discouraging subtype separation that is driven mainly by latent disease-time shifts. The number of subtypes is selected by BIC, and parameter updates are performed with a generalized EM procedure using L-BFGS substeps.

### Architecture / parameterization
A nonlinear connectome-constrained logistic-diffusion dynamical model. The transition matrix is parameterized as a shared network-mediated connectome term plus regional diagonal self-propagation, while subtype-specific forcing terms represent distinct spatial sources of pathology progression.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Parkinson's disease is heterogeneous, but many subtype models are either descriptive clusters or staging models that do not explain how pathology moves through a brain network. The paper tries to recover clinically meaningful progression subtypes while preserving a mechanistic trajectory model.

### 2. What is the method?
The authors extend COMIND with subtype-specific forcing terms. Biomarker abnormality evolves through a logistic differential equation constrained by a structural connectome and regional self-propagation. A generalized EM algorithm alternates among fitting shared dynamics, assigning subjects to subtypes, updating subtype forcing patterns, and estimating each subject's disease-time shift.

### 3. What is the method motivation?
Disease progression models need to infer both where a patient sits along a trajectory and which trajectory family they are following. Purely data-driven subtypes can scale poorly or become hard to interpret, while connectome-constrained models can provide a more biologically legible propagation hypothesis.

### 4. What data does it use?
The Parkinson's analysis uses 313 PPMI subjects and 622 observations. The training set contains 126 subjects with longitudinal follow-up and 435 observations; the hold-out validation set contains 187 subjects with a single cross-sectional scan. MRI data are processed with FreeSurfer 7.0, harmonized with ComBat, mapped to Desikan-Killiany cortical and subcortical regions, converted to normative deviation scores, and combined with MoCA, TD, and PIGD clinical measures.

### 5. How is it evaluated?
First, the method is tested on synthetic data with three ground-truth subtypes to check subtype recovery and disease-time estimation. Then it is fit to PPMI data, with BIC selecting the number of subtypes. The resulting COMIND subtype assignments are compared against TD/PIGD motor phenotype in the hold-out validation cohort and against GBA, LRRK2, PRKN, and sporadic genetic groups in the full cohort. A matched SuStaIn benchmark is fit on aggregated data for comparison.

### 6. What are the main results?
On synthetic data, BIC selects the correct three-subtype solution, subtype forcing terms are recovered accurately, subtype classification reaches an adjusted Rand index of 0.96, and mean absolute disease-time error is 0.345 years on a seven-year simulated axis. On PPMI, BIC selects four subtypes. COMIND subtype assignments significantly associate with hold-out TD/PIGD classification (chi-square = 27.33, df = 6, p < 0.001) and with genetic subgroup in the full cohort (chi-square = 17.80, df = 9, p = 0.038). The matched SuStaIn comparison does not show significant association with either grouping under the reported tests.

### 7. What is actually novel?
The novelty is the combination: nonlinear network-constrained disease dynamics, latent disease-time estimation, sparse subtype-specific pathology sources, and a benchmark against SuStaIn under a matched training and validation protocol. The paper is not just clustering Parkinson's patients. It is making each subtype correspond to a different dynamical forcing pattern over a connectome-constrained progression model.

### 8. What are the strengths?
- Heterogeneity is modeled inside the progression dynamics rather than appended afterward.
- The model gives interpretable subtype forcing maps instead of only cluster labels.
- The synthetic validation directly tests whether forcing patterns and disease time can be recovered.
- The PPMI split keeps the motor-phenotype validation partly out of sample.
- The SuStaIn comparison is useful because it tests against a known disease-subtyping baseline rather than an easy straw baseline.

### 9. What are the weaknesses, limitations, or red flags?
- This is a preprint, and the clinical validation is association with phenotype and genetics, not prospective outcome prediction or intervention selection.
- The structural connectome is group-level, not patient-specific, so the model's mechanistic language is still partly population-averaged.
- Subtype assignments are hard assignments, which can hide borderline or mixed trajectories.
- Clinical measures are included as disconnected model nodes, which is practical but makes the dynamical interpretation of clinical forcing less clean than the morphometry interpretation.
- The validation cohort is cross-sectional, so some claims about progression structure still lean on model assumptions rather than observed long-horizon trajectories.

### 10. What challenges or open problems remain?
The field still needs independent external validation, patient-specific connectomes, longitudinal validation of subtype stability, and proof that the subtype assignments change prediction, monitoring, or treatment decisions. It also needs uncertainty-aware subtype membership rather than only hard labels.

### 11. What future work naturally follows?
Test the model on ENIGMA-PD or another independent multicenter cohort, add patient-specific structural connectivity when available, compare against simpler clinical and imaging baselines, and ask whether subtype-specific trajectories predict medication response, DBS outcome, cognitive decline, gait deterioration, or trial enrichment.

### 12. Why does this matter for cabbageland?
Because cabbageland cares about heterogeneity only when it changes inference or intervention logic. This paper gives a clean scaffold for treating disease subtype as a dynamical object: not a decorative label, but a different source pattern and trajectory through a constrained brain network.

### 13. What ideas are steal-worthy?
- Make subtypes explain trajectories, not just cross-sectional clusters.
- Put sparse subtype-specific forcing terms where a future intervention model might eventually place controllable inputs.
- Penalize subtype solutions that separate mainly by disease-time offset rather than progression pattern.
- Benchmark subtyping against clinically and genetically meaningful external groupings, not only reconstruction error.
- Treat connectome constraints as a way to discipline heterogeneity models, while staying skeptical about group-connectome overinterpretation.

### 14. Final decision
Keep. This is not clinical deployment machinery yet, but it is a sharp computational note for progression modeling, patient stratification, and future intervention-relevant state estimation.
