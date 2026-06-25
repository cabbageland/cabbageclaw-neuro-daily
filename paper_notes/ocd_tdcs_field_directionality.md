# Linking electric field directionality to treatment outcome in OCD: Insights from patient-specific tDCS modeling

## Basic info

* Title: Linking electric field directionality to treatment outcome in OCD: Insights from patient-specific tDCS modeling
* Authors: Julie Gosez, Arnaud Germaneau, Karim El Houari, Prasanth Bokam, Michel Rochette, Nicolas Langbour, Remy Guillevin, Nemat Jaafari, Ghina Harika-Germaneau
* Year: 2026
* Venue / source: Translational Psychiatry
* Link: https://www.nature.com/articles/s41398-026-04169-1
* Date surfaced: 2026-06-25
* Why selected in one sentence: It asks the right personalization question for OCD tDCS by testing whether patient-specific current direction, not just field magnitude, tracks symptom change.

## Quick verdict

* Highly relevant

This is a real keep because it moves beyond generic “more field is better” tDCS rhetoric and asks whether the direction of current flow relative to cortex matters for outcome. The paper is still retrospective, responder-poor, and statistically fragile enough that nobody should mistake it for a deployable biomarker. But it is much more useful than another montage-comparison paper that never connects modeled dose to actual clinical heterogeneity.

## One-paragraph overview

The paper reanalyzes active-arm MRI data from treatment-resistant obsessive-compulsive disorder patients who received ten sessions of cathodal pre-SMA and anodal right-supraorbital tDCS. The authors build patient-specific SimNIBS finite-element head models, then test whether modeled current directionality and magnitude relate to later symptom change on the Yale-Brown Obsessive-Compulsive Scale. The interesting result is directional rather than scalar: symptom reduction was associated with greater depolarization in left anterior prefrontal cortex and right frontal eye field and with greater hyperpolarization in right pars orbitalis, while electric-field magnitude did not show significant associations. That does not solve OCD targeting, but it does say that anatomy-aware current geometry may matter more than peak-strength fetishism.

## Model definition

This paper does not contain a trainable neural network or classifier at its core. Its main engine is patient-specific finite-element field simulation followed by regression analyses against clinical outcome.

### Inputs
Structural MRI, electrode placement, stimulation current and duration, patient demographics and symptom scales, and the active-treatment tDCS montage used in the OCD trial.

### Outputs
Voxelwise estimates of current directionality and magnitude across cortex, plus statistical associations between those modeled fields and responder status or continuous Y-BOCS change.

### Training objective (loss)
There is no supervised learning loss in the usual sense. The main quantitative step is finite-element field estimation, followed by linear, binomial, and voxelwise regression analyses relating modeled fields to symptom outcome.

### Architecture / parameterization
Patient-specific SimNIBS finite-element head models with current-density projection onto cortical normals to derive depolarization versus hyperpolarization proxies, followed by voxelwise statistics and clinical regression models.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to explain why the same nominal OCD tDCS protocol can produce inconsistent outcomes across patients. The specific hypothesis is that individualized electric-field geometry, especially current direction relative to cortex, may matter more than protocol labels alone.

### 2. What is the method?
The authors retrospectively selected 42 active-treatment OCD patients with usable MRI and clinical follow-up from prior tDCS trials. They simulated each patient’s electric field using finite-element head modeling, projected current onto the cortical surface normal to estimate depolarization versus hyperpolarization, and then related those maps to Y-BOCS evolution and responder status.

### 3. What is the method motivation?
Montage labels like “pre-SMA cathode” hide the fact that anatomy bends current in idiosyncratic ways. If the delivered field differs meaningfully across patients, then outcome variability may partly come from geometry rather than from mysterious clinical noise.

### 4. What data does it use?
Forty-two adults with treatment-resistant OCD retained after MRI segmentation and assessment-completion filters, drawn from two related Poitiers studies. Clinical measures included Y-BOCS, MADRS, and HADS, with once-daily 2 mA stimulation for 30 minutes across ten sessions.

### 5. How is it evaluated?
The paper compares responders and non-responders, fits linear and binomial models with and without finite-element metrics, and performs voxelwise regressions between modeled polarization maps and continuous Y-BOCS change. It separately analyzes current directionality and current magnitude.

### 6. What are the main results?
The main clinical signal is that Y-BOCS scores fell over time, but modeled field magnitude alone did not explain that improvement. Instead, symptom reduction correlated with higher depolarization in left BA10 and right frontal eye field and with higher hyperpolarization in right BA47. A binomial model including finite-element metrics was significant while the model using clinical metrics alone was not, although no single covariate survived as a clear standalone predictor in post hoc testing.

### 7. What is actually novel?
The novelty is not just “we ran SimNIBS on OCD patients.” The real move is testing current directionality rather than only magnitude and relating that directional field estimate to treatment outcome in an OCD clinical-trial context.

### 8. What are the strengths?
It uses real patient MRI rather than toy heads, ties modeling to clinical outcome instead of to anatomy alone, and asks a sharper targeting question than most tDCS papers do. It also makes the useful point that the same montage can likely deliver meaningfully different neuronal polarization patterns across patients.

### 9. What are the weaknesses, limitations, or red flags?
This is a retrospective active-arm analysis with only 42 patients and few responders. None of the key voxelwise findings survived FDR correction, which means the type-I-error risk is real. The parent trial itself showed symptom reduction over time regardless of treatment condition, so this paper is better understood as explanatory targeting work than as proof that the montage truly works.

### 10. What challenges or open problems remain?
The field still needs prospective personalization rather than retrospective explanation. It also needs larger cohorts, better responder balance, symptom-dimension-aware targeting, and comparison of alternative montages such as extracephalic references or HD-tDCS.

### 11. What future work naturally follows?
Prospectively compute directionality maps before treatment, optimize electrode placement per patient, and test whether that actually beats generic scalp heuristics in randomized trials. It would also make sense to stratify by OCD symptom dimensions and to integrate functional-connectivity information alongside anatomy.

### 12. Why does this matter for cabbageland?
Because it sharpens a recurring intervention lesson: the clinically relevant dose is not just “2 mA over pre-SMA.” The relevant object may be the specific directional field pattern that reaches the right cortical territory in a particular head.

### 13. What ideas are steal-worthy?
Use directional field estimates instead of magnitude-only summaries. Treat patient anatomy as part of the actuator, not as nuisance variance. And stop assuming that nominal cathode-over-target placement tells you what neuronal polarization pattern the brain actually received.

### 14. Final decision
Keep. This is one of the better recent targeting papers for psychiatric tDCS, even though the evidence is still too statistically shaky and retrospective to treat as a ready-made clinical biomarker.
