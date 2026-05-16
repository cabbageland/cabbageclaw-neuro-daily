# Distinct Predictive and Recovery EEG Biomarkers of Motor Function after Noninvasive Brain Stimulation in Subacute Stroke Patients

## Basic info

* Title: Distinct Predictive and Recovery EEG Biomarkers of Motor Function after Noninvasive Brain Stimulation in Subacute Stroke Patients
* Authors: Hyejeong Han, Yerim Huh, Sang Wook Lee, Yun-Hee Kim, Minji Lee.
* Year: 2026.
* Venue / source: Research Square preprint.
* Link: https://doi.org/10.21203/rs.3.rs-9648366/v1
* Date surfaced: 2026-05-16.
* Why selected in one sentence: It makes a simple but important distinction that many rehabilitation biomarker papers miss, namely that response prediction and recovery tracking may rely on different neural signatures.

## Quick verdict

* Highly relevant

This is a small study, so it should not be mistaken for a settled biomarker result. But the conceptual distinction it forces is useful: a baseline feature that predicts who benefits from stimulation is not automatically the same thing as a longitudinal marker of recovery-related plasticity. That alone makes it more valuable than many EEG-for-rehab papers with blurrier claims.

## One-paragraph overview

The paper studies 12 subacute stroke patients receiving dual-mode noninvasive brain stimulation and asks two separate questions. First, can baseline EEG features predict who will respond? Second, do the EEG features that change over time track motor recovery? Power spectral density, phase-locking value, and coherence features were fed into several machine-learning models for baseline response prediction, while longitudinal EEG changes were tested against Fugl–Meyer motor improvement. The main finding is that the best predictive feature, ipsilesional temporal beta power, was not the same as the feature associated with recovery over time, which was relative delta power change at ipsilesional occipital cortex.

## Model definition

### Inputs
Baseline EEG-derived power spectral density, phase-locking value, and coherence features from subacute stroke patients receiving repetitive transcranial magnetic stimulation and transcranial direct current stimulation, plus longitudinal EEG measurements across visits.

### Outputs
Binary or categorical responder-status predictions at baseline for the machine-learning models, and statistical associations between longitudinal EEG feature changes and motor recovery scores over time.

### Training objective (loss)
The extracted manuscript text states that multiple machine-learning classifiers were trained and evaluated with 10-fold cross-validation, but it does not specify every exact loss function in the extracted sections. The practical training target was prediction of treatment responsiveness.

### Architecture / parameterization
A small-model comparison across multiple machine-learning classifiers, with LightGBM reported as the best-performing model for PSD-based features. The longitudinal component is not a trainable sequence model but a statistical association analysis across visits.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Stroke rehabilitation papers often talk about EEG biomarkers as if one signature should both identify responders in advance and explain recovery after intervention, which may be conceptually wrong.

### 2. What is the method?

The authors classify 12 subacute stroke patients as responders or non-responders based on two-month change in FMA-UE score after dual-mode noninvasive brain stimulation, train machine-learning models on baseline EEG features, and then separately test whether longitudinal EEG changes correlate with recovery.

### 3. What is the method motivation?

Prediction and recovery tracking are different inferential tasks. The authors want to know whether the field has been conflating them.

### 4. What data does it use?

Twelve subacute stroke patients, seven responders and five non-responders, with baseline and follow-up EEG plus motor assessments. The accessible text indicates a dual-mode noninvasive stimulation program combining repetitive transcranial magnetic stimulation and transcranial direct current stimulation.

### 5. How is it evaluated?

Baseline models are evaluated with 10-fold cross-validation, and feature importance is probed with permutation importance. Recovery tracking is evaluated by testing associations between changes in EEG features across visits and changes in motor scores.

### 6. What are the main results?

PSD features outperformed phase-locking value and coherence features for baseline response prediction, with LightGBM performing best overall. Ipsilesional beta power at T3 was the most influential predictive feature. In contrast, only longitudinal changes in relative spectral power were significantly associated with recovery, especially relative delta power change at ipsilesional O1.

### 7. What is actually novel?

The novelty is the explicit split between predictive biomarkers and recovery biomarkers. That is a more careful intervention-logic move than simply reporting the best classifier.

### 8. What are the strengths?

It asks a cleaner question than most small EEG rehab studies.

It keeps baseline prediction and longitudinal tracking analytically separate.

It prefers interpretable feature families over vague end-to-end performance theater.

### 9. What are the weaknesses, limitations, or red flags?

The sample is tiny, so any specific channel-frequency claim is fragile.

The stimulation protocol is dual-mode, which makes attribution to a single mechanism harder.

Ten-fold cross-validation on 12 patients is easy to overread.

### 10. What challenges or open problems remain?

The next challenge is replication in larger multisite cohorts with explicit prospective use of separate prediction and tracking biomarkers inside an intervention workflow.

### 11. What future work naturally follows?

Prospective stratification trials, biomarker stability studies, and adaptive rehabilitation protocols that use one signal for enrollment and another for ongoing dose adjustment would follow naturally.

### 12. Why does this matter for cabbageland?

Because it reinforces a crucial control-design point: the feature you use to decide who gets an intervention may not be the feature you should monitor during the intervention. That distinction transfers well beyond stroke.

### 13. What ideas are steal-worthy?

One steal-worthy idea is to treat prediction and progress tracking as separate model objects by default.

Another is to report longitudinal recovery markers even when they differ from baseline predictive features instead of forcing a false unification.

A third is to keep biomarker families interpretable enough that a mismatch between predictor and tracker remains legible.

### 14. Final decision

Keep as a highly relevant biomarker-design note. Weak on sample size, strong on conceptual hygiene.
