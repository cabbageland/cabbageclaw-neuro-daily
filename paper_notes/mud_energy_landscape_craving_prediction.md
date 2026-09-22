# Longitudinal brain dynamics and prediction of craving changes in individuals with methamphetamine use disorder

## Basic info

* Title: Longitudinal brain dynamics and prediction of craving changes in individuals with methamphetamine use disorder
* Authors: Qing Song, Wenhan Yang, Zhe Du, Dongcheng Wang, Xinwen Wen, Jun Liu, Kai Yuan
* Year: 2026
* Venue / source: Translational Psychiatry
* Link: https://doi.org/10.1038/s41398-026-04401-y
* Date surfaced: 2026-09-22
* Why selected in one sentence: It uses energy-landscape modeling of resting-state fMRI to frame methamphetamine craving as a problem of rigid brain-state dynamics and to test whether baseline dynamics predict later craving change.

## Quick verdict

* Highly relevant

This is a strong computational-psychiatry preserve, with the usual cautions. The paper turns resting-state fMRI into interpretable large-scale brain-state dynamics, tracks partial recovery after prolonged abstinence, and tests an explicit craving-change predictor. The result is not causal and the prediction model is small, but the state-flexibility framing is exactly the kind of mechanism language worth keeping.

## One-paragraph overview

The study compares 41 healthy controls with 40 people with severe methamphetamine use disorder, scanned early in abstinence and again after prolonged abstinence. The authors reduce Power-atlas resting-state fMRI into seven large-scale networks, binarize network activity, fit a pairwise maximum entropy model, and use the resulting energy landscape to identify dominant brain states and transition patterns. Early-abstinence MUD participants spend more time in two major states and less time in minor states, suggesting a more rigid neural landscape; some of that rigidity partially relaxes after longer abstinence. A small RBF support-vector regression model using baseline dynamic indices predicts longitudinal craving change, which makes the paper useful as a biomarker/state-estimation candidate rather than a finished clinical tool.

## Model definition

### Inputs

For the energy-landscape model, inputs are resting-state fMRI time series from 214 Power atlas ROIs averaged into seven functional networks: default mode, frontoparietal, salience, attention, somatosensory/motor, visual, and auditory networks. For the prediction model, inputs are 20 baseline dynamic indices from 38 MUD participants with follow-up craving data, including appearance frequency, duration, and direct or indirect transition metrics for major and minor brain states.

### Outputs

The maximum entropy model outputs an energy landscape over binarized seven-network activity patterns, local minima interpreted as dominant brain states, basin sizes, and simulated transition/dwell metrics. The support-vector regression model outputs predicted longitudinal change in visual-analog craving score after prolonged abstinence.

### Training objective (loss)

The pairwise maximum entropy model is fit by adjusting baseline network terms and pairwise coupling terms so model moments match empirical single-network and pairwise activity moments; goodness of fit is evaluated with KL-divergence-based accuracy and empirical/model probability correlations. The craving predictor is an RBF-kernel support-vector regression model, so the effective objective is epsilon-insensitive regression with regularization; hyperparameters C, gamma, and epsilon are tuned inside nested cross-validation.

### Architecture / parameterization

The mechanistic representation is a pairwise maximum entropy energy landscape over seven binarized brain networks, followed by Metropolis-Hastings random-walk simulations. The predictive component is an RBF-kernel support-vector regression model trained on baseline dynamic metrics with leave-one-out outer cross-validation and 10-fold inner hyperparameter tuning.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

It tries to explain and predict craving change in methamphetamine use disorder using whole-brain dynamics rather than static connectivity snapshots. The clinical problem is relapse risk and heterogeneous recovery during abstinence; the modeling problem is whether brain-state flexibility contains useful information about that recovery.

### 2. What is the method?

The authors preprocess resting-state fMRI, average ROI activity into seven functional networks, binarize each network's activity, and fit a pairwise maximum entropy model. They identify local energy minima as dominant brain states, quantify basin sizes and transitions, simulate random walks across the landscape, correlate dynamic metrics with craving and impulsivity, and train an RBF-SVR model to predict craving change from baseline dynamic features.

### 3. What is the method motivation?

The motivation is that addiction may involve impaired flexibility between large-scale network states, especially between default-mode, salience, control, sensory, and attention systems. Energy-landscape analysis gives a more interpretable state-transition picture than a static connectivity matrix or arbitrary sliding-window connectivity analysis.

### 4. What data does it use?

The study uses resting-state 3T fMRI from 41 healthy controls and 40 people with DSM-5 severe methamphetamine use disorder. MUD participants were scanned at baseline during early abstinence, defined as at most 3.5 months, and again after sustained abstinence of at least 8 months. Thirty-eight had usable longitudinal craving scores for the prediction analysis.

### 5. How is it evaluated?

Model fit is evaluated by how well the pairwise MEM reproduces empirical activity-pattern probabilities; reported model/empirical probability correlations exceed 0.98 and accuracy exceeds 0.97. Group differences in dynamic metrics are tested statistically across healthy controls, early-abstinence MUD, and later-abstinence MUD. The craving predictor is evaluated by the correlation between observed and predicted craving change under nested cross-validation, with permutation testing.

### 6. What are the main results?

The energy landscapes contain six local minima, organized into two major and two minor state groupings. Early-abstinence MUD participants show higher appearance frequency of major states, lower appearance of minor states, longer duration in major state #1, shorter duration in minor states, and more direct transitions between major states. Some of these abnormalities partially recover after prolonged abstinence. Craving correlates positively with indirect transitions and negatively with duration of minor states. The SVR model predicts craving change with r = 0.3718, p = 0.0215, and permutation p < 0.05.

### 7. What is actually novel?

The useful novelty is applying energy-landscape dynamics longitudinally in MUD and connecting baseline dynamic-state features to later craving change. It is not novel because it uses fMRI or SVR; it is novel because it makes rigidity, transition difficulty, and state dwell time explicit enough to become candidate intervention readouts.

### 8. What are the strengths?

The paper gives a concrete state-transition representation instead of another undifferentiated connectivity story.

It includes a longitudinal abstinence scan rather than only cross-sectional patient-control differences.

It connects dynamic features to craving and impulsivity, then tests a prediction model rather than stopping at group contrasts.

It is careful enough to describe the model, local minima, random-walk simulations, hyperparameter grid, and permutation test.

### 9. What are the weaknesses, limitations, or red flags?

The sample is small for predictive modeling, especially the 38-participant craving-change SVR.

The predictor has no independent external validation cohort, so the r = 0.37 result is a candidate signal, not a deployable biomarker.

The analysis uses two time points, which cannot resolve the full trajectory of recovery or relapse risk.

The model depends on binarization, network averaging, and pairwise maximum-entropy assumptions. Those choices make the landscape interpretable, but they also remove within-network detail and may be parameter-sensitive.

The associations with craving and impulsivity are not causal. The paper does not show that changing these dynamics changes craving.

### 10. What challenges or open problems remain?

The main challenge is moving from state description to intervention logic. The field needs denser longitudinal sampling, relapse outcomes, independent validation, and tests of whether therapies, stimulation, exercise, sleep interventions, or pharmacologic treatments actually shift the rigid-state profile in useful ways.

### 11. What future work naturally follows?

A good next study would validate the dynamic predictor in an independent cohort, include relapse or treatment-response endpoints, and compare the energy-landscape features against simpler static connectivity, clinical, and demographic baselines. A stronger intervention study would ask whether changes in the state-transition metrics mediate craving improvement.

### 12. Why does this matter for cabbageland?

Cabbageland keeps needing better language for state flexibility, recovery, and intervention timing. This paper supplies a concrete addiction example: rigid occupation of a few dominant network states, partial recovery with abstinence, and baseline dynamics that predict later craving. That transfers to neuromodulation and psychotherapy as a measurement target, even though the paper itself is not an intervention trial.

### 13. What ideas are steal-worthy?

Use dwell time and transition structure as process variables, not just connectivity strength.

Treat default-mode and salience-network state balance as a craving-regulation readout.

Use baseline dynamic features to stratify follow-up intensity or intervention choice, but demand external validation before clinical use.

Represent recovery as increased access to minor or flexible states rather than only symptom decrease.

### 14. Final decision

Keep as a highly relevant computational-psychiatry and network-dynamics note. The prediction result is preliminary, but the state-flexibility framework is useful and portable.
