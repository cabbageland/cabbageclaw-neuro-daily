# An EEG-based digital biomarker for personalizing transcranial magnetic stimulation in major depressive disorder

## Basic info

* Title: An EEG-based digital biomarker for personalizing transcranial magnetic stimulation in major depressive disorder
* Authors: Li Wan, Yaqun Chen, Qinghui Zhang, Shuqi He, Qiong Ye, Enhuan Wang, Tao Yang, Wen Xie
* Year: 2026
* Venue / source: npj Digital Medicine
* Link: https://pubmed.ncbi.nlm.nih.gov/41957270/
* Date surfaced: 2026-04-10
* Why selected in one sentence: It prospectively tests an EEG-derived pretreatment stratifier for repetitive TMS in depression instead of only explaining response variance after stimulation has already happened.

## Quick verdict

* Highly relevant

This is not a solved-personalization paper, but it is more serious than the usual biomarker theater because it makes a prospective stratification claim. The main value is not that it proves a universal antidepressant selector. The value is that it raises the bar for pretreatment response logic in depression TMS.

## One-paragraph overview

The paper introduces a dorsolateral prefrontal cortex sensitivity index, or dSI, computed from EEG functional-connectivity features with an L1-regularized logistic-regression model. In a second study, patients with major depressive disorder were prospectively assigned to sensitive, non-sensitive, and sham groups and all underwent a personalized, neuronavigated bilateral dorsolateral prefrontal cortex repetitive TMS protocol for two weeks. According to the abstract, baseline dSI predicted later clinical and cognitive outcomes, and the prospectively labeled sensitive group showed larger improvements in emotional-attention reaction time plus larger reductions in hostility and paranoia than the non-sensitive and sham groups. The paper is worth preserving because it reframes TMS personalization as pretreatment sensitivity estimation rather than retrospective responder explanation. The caution is that the accessible text emphasizes selected outcome improvements more clearly than it demonstrates a broad antidepressant win.

## Model definition

### Inputs
Baseline EEG functional-connectivity features derived before repetitive TMS treatment in major depressive disorder.

### Outputs
A dorsolateral prefrontal cortex sensitivity index intended to predict whether a patient will respond more favorably to a personalized, neuronavigated bilateral dorsolateral prefrontal cortex repetitive TMS protocol.

### Training objective (loss)
The index was computed using an L1-regularized logistic-regression model. The accessible text does not provide the exact optimization target beyond prediction of treatment sensitivity or response class.

### Architecture / parameterization
A sparse linear classification framework using EEG functional-connectivity features to estimate a pretreatment sensitivity score for dorsolateral prefrontal cortex repetitive TMS.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Repetitive TMS for depression helps some patients much more than others, and the field still lacks robust pretreatment tools for deciding who is likely to benefit from a given stimulation setup.

### 2. What is the method?
The method is an EEG-derived digital biomarker called dSI, built from functional-connectivity features and used prospectively to stratify patients before treatment.

### 3. What is the method motivation?
If pretreatment network state influences whether dorsolateral prefrontal cortex stimulation has leverage, then a pre-stimulation EEG biomarker could improve targeting logic and reduce blind trial-and-error treatment.

### 4. What data does it use?
The accessible abstract describes two studies: one for deriving the dSI from EEG features and a second prospective study in which major depressive disorder patients were stratified into sensitive, non-sensitive, and sham groups before receiving neuronavigated bilateral dorsolateral prefrontal cortex repetitive TMS.

### 5. How is it evaluated?
It is evaluated by whether baseline dSI predicts downstream clinical and cognitive outcomes and whether the prospectively defined sensitive group outperforms non-sensitive and sham groups after treatment.

### 6. What are the main results?
- Baseline dSI significantly predicted post-treatment clinical and cognitive outcomes.
- The prospectively identified sensitive group showed larger improvements in emotional-attention network task reaction times.
- The sensitive group also showed greater reductions in hostility and paranoia than non-sensitive and sham groups.
- Post-treatment EEG reportedly showed network-specific modulation in the sensitive group.

### 7. What is actually novel?
The novelty is not simply using EEG. It is the prospective use of an EEG-derived pretreatment sensitivity index to stratify repetitive-TMS candidates before treatment rather than rationalizing outcome differences afterward.

### 8. What are the strengths?
- Prospective stratification claim instead of purely retrospective biomarker fitting.
- Simple and interpretable sparse modeling approach rather than gratuitous model complexity.
- Uses neuronavigated personalized bilateral dorsolateral prefrontal cortex repetitive TMS rather than a vague stimulation description.
- Includes both behavioral and post-treatment EEG readouts.

### 9. What are the weaknesses, limitations, or red flags?
- From the accessible text, the clearest reported benefits are selective rather than obviously broad-spectrum antidepressant effects.
- I only inspected the abstract and publisher landing-page abstract.
- Sample composition and exact primary endpoint hierarchy are not clear from the accessible text.
- Biomarker papers often look strongest before external replication across sites and protocols.
- The code and full data are not openly available, according to the landing page.

### 10. What challenges or open problems remain?
The central questions are whether dSI replicates across independent datasets, whether it adds decision value over simpler clinical variables, and whether it predicts durable antidepressant benefit rather than narrower short-term task or subscale improvements.

### 11. What future work naturally follows?
Independent prospective replication, comparison against fMRI or combined EEG-fMRI predictors, evaluation across different TMS regimens such as theta-burst versus standard rTMS, and clearer testing of whether dSI can guide individualized protocol selection rather than only stratify one protocol.

### 12. Why does this matter for cabbageland?
Because the field badly needs personalization claims that cash out before treatment starts. Even if this specific biomarker turns out to be limited, the structure of the claim is healthier than generic responder-postmortem papers.

### 13. What ideas are steal-worthy?
- Force biomarker claims into prospective stratification whenever possible.
- Prefer simple sparse models when the scientific claim is about pretreatment sensitivity, not leaderboard performance.
- Treat network-state readouts as intervention priors rather than retrospective decoration.
- Demand clearer endpoint hierarchy before calling a biomarker clinically decisive.

### 14. Final decision
Preserve. This is a worthwhile clinical-translational note because it makes a prospective pretreatment stratification claim for depression TMS, even though the accessible evidence does not yet justify overclaiming broad antidepressant personalization.