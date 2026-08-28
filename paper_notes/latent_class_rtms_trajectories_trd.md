# Latent class modeling of repetitive transcranial magnetic stimulation response trajectories in treatment-resistant depression

## Basic info

* Title: Latent class modeling of repetitive transcranial magnetic stimulation response trajectories in treatment-resistant depression
* Authors: Cory R. Weissman, Brian Cui, Lindsay Benster, Noah Stapper, Jean-Philippe Miron, Zafiris J. Daskalakis, Lawrence G. Appelbaum, Jordan N. Kohn
* Year: 2026
* Venue / source: Journal of Affective Disorders
* Link: https://doi.org/10.1016/j.jad.2026.122167
* Date surfaced: 2026-07-23
* Why selected in one sentence: It turns vague rTMS heterogeneity talk into explicit response-trajectory classes and makes early pivot logic more legible for the patients most likely to stall.

## Quick verdict

* Highly relevant

This is one of the better clinically useful rTMS heterogeneity papers in the archive now that full text is accessible. The useful move is not just clustering for decoration. It is showing that a high-severity group can split into two genuinely different lanes: one that barely moves and one that improves a lot, while suicidal-ideation history concentrates in the bad lane. The limits are still serious: this is retrospective, single-program, protocol-heterogeneous, and built on weekly PHQ-9 trajectories rather than richer circuit or biomarker state.

## One-paragraph overview

The paper uses latent class mixture modeling on weekly PHQ-9 scores from 308 treatment-resistant depression patients treated with acute rTMS at the UC San Diego Interventional Psychiatry Program. On raw symptom scores, the best clinically interpretable fit is a three-class quadratic solution: High Baseline, Minimal Improvement; Moderate Baseline, Moderate Improvement; and High Baseline, Large Improvement. The key point is that baseline severity alone does not decide outcome. Two groups start high, but one crashes downward and one barely budges. The large-improvement high-baseline group reaches 65.5 percent symptom reduction and an 84 percent response rate, while the minimal-improvement high-baseline group only drops 9 percent and shows a 13 percent response rate. The paper is valuable because it makes nonresponse look like an early triage object rather than an unfortunate surprise discovered after the whole course is over.

## Model definition

### Inputs
Weekly PHQ-9 scores collected during the acute rTMS course, plus baseline demographic and clinical features including pre-treatment PHQ-9, suicidal-ideation and suicide-attempt history, prior ECT, comorbid anxiety, substance-use variables, BMI, education, and medication burden.

### Outputs
Latent response-trajectory classes over treatment, class-specific symptom and suicidal-ideation change profiles, and predicted odds of class membership from baseline clinical variables.

### Training objective (loss)
The paper fits latent class mixed models to longitudinal PHQ-9 trajectories and uses BIC, posterior class-membership probability, and minimum class size for model selection. Baseline predictor analysis uses LASSO-penalized multinomial logistic regression with nested cross-validation. The exact full likelihood and penalty details are not spelled out in the main accessible text beyond those model families.

### Architecture / parameterization
A three-class quadratic latent class mixed model for raw PHQ-9 scores, a two-class quadratic sensitivity model for baseline-adjusted PHQ-9 scores, and a LASSO-penalized multinomial classifier for baseline class prediction.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Average endpoint response rates blur together patients who improve quickly, patients who improve slowly, and patients who probably should have been switched earlier. The paper tries to recover that hidden structure so rTMS nonresponse can be anticipated rather than merely documented.

### 2. What is the method?

The authors fit latent class mixed models to weekly PHQ-9 trajectories during acute rTMS, testing one to five classes and linear through cubic trajectory shapes. They then use multinomial LASSO models with nested cross-validation to ask whether baseline clinical features predict which trajectory class a patient enters.

### 3. What is the method motivation?

If response heterogeneity has stable shape, then clinical decision-making should care about trajectories, not just final totals. The method is motivated by the idea that early divergence could support earlier reassignment to alternatives such as ketamine, ECT, or more intensive stimulation strategies.

### 4. What data does it use?

It uses a retrospective naturalistic cohort of 308 treatment-resistant depression patients treated at UCSD-IPP with acute rTMS. Patients received mixed real-world protocols, with iTBS most common but also bilateral rTMS, deep rTMS, and other variants. Patients completed PHQ-9 assessments about 7.25 times on average over roughly 32 sessions and 7.5 weeks.

### 5. How is it evaluated?

Evaluation is based on trajectory-model fit and interpretability, class-size adequacy, posterior class-membership probabilities, and held-out multi-class discrimination for the baseline-predictor model. The paper also checks a baseline-adjusted sensitivity analysis and reports class differences in symptom reduction, suicidal ideation, and baseline clinical history.

### 6. What are the main results?

The raw-score solution is a three-class quadratic model with classes sized 61, 174, and 73 patients. The moderate-baseline moderate-improvement group starts lower and improves steadily. The two high-baseline groups split sharply: HBLI ends near a post-treatment PHQ-9 of 7.5 with 65.5 percent symptom reduction and 84 percent response, while HBMI ends around 20.4 with only 9 percent reduction and 13 percent response. A baseline-adjusted sensitivity analysis collapses to a two-class moderate-versus-large-improvement solution, which says much of the class structure is driven by baseline severity plus whether substantial improvement actually happens. The predictive model reaches mean multi-class AUC about 0.82, with much stronger discrimination against the moderate-baseline group than between the two high-baseline groups. History of suicidal ideation is the clearest practical warning sign for the bad high-baseline lane.

### 7. What is actually novel?

The novelty is not "rTMS response is heterogeneous." Everyone already knows that. The useful novelty is showing that weekly response curves in a real clinical program can be partitioned into a small number of clinically interpretable classes, and that the clinically annoying group is specifically a severe baseline plus minimal-improvement lane rather than just "high symptoms in general."

### 8. What are the strengths?

The cohort is fairly large for a single interventional-psychiatry service.

The paper uses longitudinal weekly symptom data instead of baseline-endpoint snapshots.

It separates two very different high-baseline groups instead of treating severe depression as one blob.

It reports both descriptive trajectory structure and a baseline-predictor model, so it at least tries to move toward triage rather than stopping at pretty clusters.

The authors are appropriately cautious that the clinically relevant three-class solution did not simply win on the lowest BIC, which makes the modeling judgment more honest.

### 9. What are the weaknesses, limitations, or red flags?

This is still retrospective observational work, so the pivot logic it implies is not experimentally tested.

Everything comes from one UCSD program, so transportability is not earned.

The treatment protocols are heterogeneous, which helps realism but muddies mechanistic interpretation.

The main signal is built from PHQ-9 self-report trajectories, not physiology or circuit measures.

The baseline predictor story is weaker than the headline AUC suggests, because discrimination between the two high-baseline groups is only modest and many predictors look site-structured rather than biologically deep.

The authors also note that predictive performance may be somewhat optimistic and needs external validation.

### 10. What challenges or open problems remain?

The main open problem is turning descriptive trajectories into prospective decision rules. It is still unknown how early a patient can be reliably identified as HBMI, whether switching actually improves outcomes, and what biomarkers can separate HBMI from HBLI before the course is mostly over.

### 11. What future work naturally follows?

Prospective multisite replication, trajectory-guided switching studies, and fusion with EEG, TMS-response, imaging, or cognitive markers would all be obvious next steps. A stronger version of this work would ask not just who belongs to which class, but whether class-aware reassignment changes outcomes.

### 12. Why does this matter for cabbageland?

Because this is the sort of paper that makes interventional psychiatry slightly less mushy. Instead of saying "some patients respond and some do not," it provides a sharper object for biomarker work, adaptive treatment logic, and comparative papers that care about time-to-response rather than only endpoint averages.

### 13. What ideas are steal-worthy?

Treat acute-course symptom change as a latent-trajectory problem instead of a binary response endpoint.

Use the bad high-baseline lane as the thing that biomarkers, protocol tweaks, or sequencing strategies are actually trying to predict or avoid.

Evaluate future interventional-psychiatry papers on whether they can separate fast pivot candidates from slow eventual improvers.

### 14. Final decision

Keep. This is a strong clinical-heterogeneity and triage-framing note even though it is not mechanistic and not causal. The archive value is high because it gives future stimulation, biomarker, and treatment-sequencing papers a more explicit failure mode to beat.
