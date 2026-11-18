# Heterogeneous Negative Gray Matter Volume Deviations Converge on a Shared Depression Circuit Associated With Symptoms and rTMS Response

## Basic info

* Title: Heterogeneous Negative Gray Matter Volume Deviations Converge on a Shared Depression Circuit Associated With Symptoms and rTMS Response
* Authors: Shaoqiang Han; Yu Zhang; Keke Fang; Yuzhen Ding; Ya Tian; Ruiping Zheng; Qiyue Zhu; Xueqin Song; Baohong Wen; Liang Liu; Yarui Wei; Yuan Chen; Yong Zhang
* Year: 2026
* Venue / source: Advanced Science; online November 15, 2026; DOI 10.1002/advs.78775
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13771405/
* Date surfaced: 2026-11-18
* Why selected in one sentence: It tests whether heterogeneous individual structural deviations converge on a reproducible depression circuit, while exposing the large gap between network replication and validated rTMS targeting.

## Quick verdict

* Highly relevant

Preserve for normative modeling, spatial-null design, and targeting-hypothesis generation—not as proof of a new optimal stimulation site. The large imaging replication is more persuasive than the retrospective n = 25 open-label rTMS association. Neither cross-sectional negative GMV deviations nor reference-connectome anticorrelations establish lesions, biological inhibition, or causal controllability.

## One-paragraph overview

The authors fit healthy age/sex expectations for voxelwise gray-matter volume, identify each patient's unusually negative deviations, and project their locations through a functional reference connectome. Despite little anatomical overlap, these seeds converge on a subcortical-limbic positive and frontoparietal/default-mode negative connectivity pattern. The map replicates in a multisite depression cohort and alternative connectomes. In a separate, previously published rTMS sample, target connectivity and distance to a circuit-derived left-DLPFC peak correlate with symptom improvement. Crucially, that sample lacks subject-level structural MRI for this analysis: it tests a group-map association with existing targets, not whether an individual's structural deviations identify a better treatment location.

## Model definition

### Inputs

- Normative model: voxelwise modulated T1-derived GMV, age, and sex in healthy controls. REST multisite data undergo ComBat harmonization preserving age, sex, and diagnostic-group effects.
- Network mapping: each participant's clusters with Z < -1.96 and at least 50 voxels, represented by combined 4-mm spheres at cluster peaks; resting-state fMRI from a reference connectome.
- Clinical analyses: HAMD symptom scores; separately, published rTMS coordinates, percentage BDI improvement, and available treatment/demographic variables.
- Auxiliary modalities: depression-risk gene expression and meta-analytic cognitive maps. These are spatial annotations, not jointly trained patient-level multimodal predictors.

### Outputs

Voxelwise normative predictions and uncertainty-adjusted deviation Z-scores; participant-specific normative-connectivity t-maps; a group convergence circuit; positive/negative/total circuit-coupling scores; retrospective target/outcome associations; and candidate group-level DLPFC peaks. No calibrated prospective response probability, stimulation waveform, online state estimate, or feedback policy is produced.

### Training objective (loss)

The learned component is voxelwise Gaussian process regression of GMV on age and sex. The main text reports 10-fold standardized mean-squared prediction error in discovery controls, but delegates kernel specification and hyperparameter estimation to the supplement; that validation metric should not be mislabeled as the fitted training objective. The exact kernel and optimization criterion were not independently inspected. Downstream Pearson correlations, GLMs, one-sample t-tests, permutations, and FDR correction are inference procedures, not an end-to-end treatment-response training loss.

### Architecture / parameterization

A modular normative-GPR → thresholded anatomical seeds → reference-connectome mapping → group statistical-inference pipeline. Reference seed-to-voxel correlations undergo Fisher transformation and age/sex/motion-adjusted combination. Group convergence is tested against 10,000 spatial randomizations, with voxelwise FDR q < 0.05 and >100-voxel extent. For symptom scoring, leave-one-subject-out circuit masks reduce self-inclusion. This is not a dynamical brain model or an individualized TMS E-field model.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Patients with the same depression diagnosis can show negative structural deviations in different locations. The paper asks whether their functional embedding converges more reliably than their anatomical overlap, and whether that circuit has any relationship to symptoms and existing treatment outcomes.

### 2. What is the method?

Train discovery GPR models on 121 healthy controls, using out-of-fold predictions for controls and refitted models for patients. Independently model the multisite cohort using its 1,094 controls. Map patient-specific seed masks through the normative connectome, then test group convergence with the connectome and mapping pipeline fixed while randomizing seed positions, preserving seed number/geometry and cortical-versus-subcortical assignment. Repeat with alternate connectomes, seed radii, and deviation thresholds. Separately correlate target-map values and peak distances with published rTMS outcomes.

### 3. What is the method motivation?

Different abnormal locations might participate in related functional systems. Starting from individual structural deviations offers a route to a candidate circuit without choosing a therapeutic seed first. That is an informative alternative derivation, but a reference connectivity matrix is not evidence that pathology propagates along it or that stimulation can reverse it.

### 4. What data does it use?

- ZZU discovery: 105 medication-naive, first-episode MDD patients and 121 controls; mean patient age 20.30 years. Participants were Han Chinese and right-handed. There were also 98 OCD patients.
- REST replication: 1,265 MDD patients and 1,094 controls across 24 sites; mean patient age 36.22 years, with mixed episode and medication histories and incomplete clinical metadata.
- Independent SLIM connectome: 524 healthy participants after motion exclusions. A disease-specific ZZU MDD connectome provides another sensitivity analysis.
- TRD-TMS: 25 medication-resistant patients, daily left-DLPFC rTMS for 4–7 weeks, structural-neuronavigation placement using the conventional 5.5-cm rule. Coordinates/outcomes are reused from Weigand et al.; individual structural MRI is unavailable here.
- Schizophrenia comparison: 61 patients and 73 controls. Spatial gene-expression analyses use AHBA's six donors.

These are distinct roles and cohorts; the 1,265-patient replication is not a 1,265-patient rTMS trial.

### 5. How is it evaluated?

Discovery-control prediction error, seed-constrained spatial nulls, independent-cohort and connectome map correlations, threshold/radius sensitivity, leave-one-out symptom-score extraction, outcome permutations, and six-primary-test FDR correction for rTMS associations. Treatment analyses include leave-one-out influence checks and separate demographic/baseline and treatment-characteristic adjustments. These checks do not constitute held-out clinical prediction or randomized comparison of targeting strategies.

### 6. What are the main results?

- Qualifying negative-deviation clusters occur in 73/105 discovery patients (69.52%) and 600/1,265 replication patients (47.4%); maximum anatomical overlap is only 15.1% and 5.0%, respectively. The map therefore does not straightforwardly cover every diagnosed patient.
- Circuit spatial correlations are r = 0.87 with the independent SLIM connectome, 0.97 with the disease-specific connectome, and 0.72 with REST replication. These are whole-map similarities, not patient classification accuracies.
- With Z < -2.58, discovery-connectome clusters no longer survive FDR, while SLIM convergence remains detectable. Threshold robustness is qualified, not absolute.
- Discovery positive and total coupling scores correlate with HAMD at r = 0.31 and 0.27; the negative component does not significantly correlate there (r = -0.16, permutation p = 0.095). Episode status moderates the negative-component relationship in the available REST subset.
- In 25 rTMS cases, more negative target connectivity associates with better BDI improvement: r = -0.41, 95% CI [-0.70, -0.03], reported FDR q = 0.018. After separate treatment-characteristic adjustment, this association is not significant (permutation p = 0.065).
- Distance to the discovery peak at MNI (-48, 33, 27) correlates with improvement at r = -0.65, 95% CI [-0.83, -0.34], reported q = 0.004; the separate treatment-adjusted association remains significant (p = 0.024). Alternate-connectome peaks are (-30, 51, 9) and (-36, 51, 9): broad agreement is not coordinate identity.
- Schizophrenia shows partial circuit overlap; no significant OCD convergence is detected. Neither result establishes a depression-specific diagnostic biomarker.

### 7. What is actually novel?

The useful contribution is a structural-deviation-derived route to a shared network hypothesis with explicit seed-constrained nulls and substantial imaging replication. GPR, normative modeling, connectivity mapping, and DLPFC anticorrelation targeting are established ingredients. The candidate peak aligns with prior sgACC-based targets; incremental clinical value remains untested.

### 8. What are the strengths?

Independent multisite replication; alternative healthy and disease-specific connectomes; a null retaining intrinsic connectome structure; separation of cross-sectional deviation from physical lesions; leave-one-out symptom masks; and unusually explicit reporting of treatment-adjustment attenuation and target-coordinate variation. The young discovery cohort and broader-age replication are useful, but do not establish adolescent treatment efficacy.

### 9. What are the weaknesses, limitations, or red flags?

- Cross-sectional statistical deviations are not longitudinal atrophy or causal perturbations. "Network damage" is a coupling score, not observed tissue damage.
- No qualifying seed exists for many patients. Threshold dependence and the handling/generalizability of seed-negative patients deserve explicit prospective accounting.
- The rTMS evidence is small, retrospective, open-label, nonrandomized, and lacks individual structural MRI. Leave-one-out influence stability is not external predictive validation.
- The connectivity association weakens with treatment adjustment. Distance may still reflect target/dose/protocol confounding; no E-field or measured engagement analysis resolves it.
- Global signal regression affects negative connectivity. An anticorrelation is not biological inhibition, and alternative connectomes using similar preprocessing do not replace a direct no-GSR sensitivity test.
- Multisite harmonization preserves diagnostic group and is not demonstrated here as a deployable, fully held-out-site pipeline for a new undiagnosed patient.
- Spatial gene-expression alignment uses six adult donors and is not patient-specific genetic mechanism. A non-significant OCD result does not prove specificity.
- Supplements/code were not audited. Figure 3's caption says all permutation p-values are <0.001, while the main text reports 0.002 for one group contrast; use the specific body-text values rather than treating the caption as uniform confirmation.

### 10. What challenges or open problems remain?

Can the frozen circuit rule add benefit over established sgACC and individual-network targeting? How reproducible is the selected coordinate across acquisition, connectome, preprocessing, and visit? What should the pipeline do for patients without extreme deviations? Does the normative coupling score track meaningful within-person change, rather than only between-person differences?

### 11. What future work naturally follows?

Preregister and freeze the normative/harmonization pipeline before external validation. Include seed-negative patients and report coverage. Compare circuit, sgACC, standard, and individual-network/E-field targets with matched dose and independent outcomes; measure engagement and assess GSR sensitivity. Add repeated imaging to separate premorbid variation, illness effects, and treatment-related change. A feedback application would additionally need perturbation-identified input dynamics and online observability.

### 12. Why does this matter for cabbageland?

It gives a concrete way to test whether anatomical heterogeneity can be compressed into an intervention-relevant network representation without pretending a diagnosis has one damaged voxel. More importantly, it makes the next evidence gap legible: group-map replication, individual physical engagement, and prospective therapeutic benefit must each be demonstrated separately.

### 13. What ideas are steal-worthy?

- Hold the reference connectome fixed in spatial-null tests; otherwise intrinsic map similarity can masquerade as disease convergence.
- Report both circuit-map similarity and selected-coordinate dispersion across reference datasets.
- Treat threshold/seed coverage as part of the model's applicability, not a preprocessing footnote.
- Keep normative-state estimation, physical E-field engagement, and causal stimulation dynamics as distinct modules with distinct validation endpoints.
- Put familiar-target baselines and simple clinical covariates into the prospective design before claiming new precision.

### 14. Final decision

**Preserve as a highly relevant network-methods and targeting-hypothesis paper.** Primary PMC full text inspected across methods, main results, relevant captions, and discussion/limitations; supplementary document, code, and data were not independently audited. It earns the label "replicated network convergence," not "validated personalized rTMS target" or "causal depression-control circuit."
