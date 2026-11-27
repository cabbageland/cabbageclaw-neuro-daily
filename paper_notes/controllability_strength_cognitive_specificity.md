# Structural and dynamic functional controllability: shared variance between network control metrics limits attribution to distinct domains of intelligence

## Basic info

* Title: Structural and dynamic functional controllability: shared variance between network control metrics limits attribution to distinct domains of intelligence
* Authors: Justin Ng, Jamie D. Feusner, Colin Hawco
* Year: 2026
* Venue / source: Frontiers in Human Neuroscience, volume 20, article 1920417; published October 2, 2026
* Link: https://doi.org/10.3389/fnhum.2026.1920417
* Date surfaced: 2026-11-27
* Why selected in one sentence: It tests whether network-control descriptors earn cognitive specificity beyond node strength, and finds that the choice of connectivity representation matters more clearly than the control-metric label.

Access: accessible full main text via [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13672590/) and Europe PMC XML. Methods, Results, Discussion, main tables, and figure captions were inspected; Figure 7 was also inspected as an image to verify prediction scores. The supplementary DOCX download returned HTML rather than a usable document. Supplementary robustness analyses are therefore author-reported, not independently inspected here; code and raw data were not run. This is an October paper newly preserved today, not a claim of a new November publication. Europe PMC's initial search record gave October 19; the article's own publication metadata gives October 2.

## Quick verdict

* Highly relevant

A useful brake on control-theory storytelling. Dynamic functional connectivity predicts cognition better than structural connectivity in this analysis, but average controllability, modal controllability, and simple node strength have statistically indistinguishable predictive performance. Preserve it for baseline selection and construct validity—not as proof that changing a controllability score improves intelligence or identifies a stimulation target.

## One-paragraph overview

The authors derive structural, static functional, and six recurring dynamic functional connectomes from Human Connectome Project data, then ask whether regional average controllability and modal controllability predict general, fluid, and crystallized intelligence. They use family-aware nested cross-validation and compare those descriptors with regional strength under the same predictive framework. Dynamic connectivity carries the clearer advantage: for general intelligence, dynamic-only prediction explains about 15% of held-out variance with either control metric or strength, versus about 2–3% from structural connectivity. The hoped-for division between modal control/fluid cognition and average control/crystallized cognition does not materialize. The important distinction is between an informative network representation and a uniquely informative control mechanism; this study supports the former much more strongly than the latter.

## Model definition

### Inputs

For each participant: diffusion-MRI structural connectivity and four resting-state fMRI runs, represented using 360 cortical HCP-MMP1.0 parcels. Functional features include static correlations and six phase-coherence states. Each connectivity matrix supplies regional average controllability, modal controllability, or absolute node strength. Age and self-reported binary gender are nuisance covariates. Cognitive targets come from HCP tests; general intelligence is estimated using a separate bifactor confirmatory factor analysis.

### Outputs

Continuous predictions of general intelligence (g), fluid intelligence (gF; Penn Progressive Matrices), and crystallized intelligence (gC; Picture Vocabulary). Additional outputs are modality contributions to explained variance and Haufe-transformed regional importance maps. There is no predicted treatment response, online state-feedback policy, stimulation setting, or experimentally validated transition trajectory.

### Training objective (loss)

Prediction uses kernel ridge regression: conventionally, squared prediction error with ridge regularization in kernel space. The main text names the estimator and cosine kernel, but does not print the complete implemented objective or hyperparameter grid; those details are not reconstructed here. Inner five-fold cross-validation selects regularization hyperparameters. Multiple kernels represent predictor subsets, allowing variance attribution. The state vocabulary is learned by k-medians clustering with Manhattan distance and 500 random initializations; the CFA's exact fitting objective is not specified in the inspected main text.

### Architecture / parameterization

A staged descriptive/predictive stack: Hilbert-transform BOLD phase → instantaneous pairwise phase coherence → leading eigenvectors → pooled k-medians state vocabulary → participant-specific connectivity matrices → graph/control descriptors → cosine-kernel ridge regression. Six dynamic states are used. Methods describe participant state matrices as medians, although the analysis-flowchart caption says averages: an implementation detail worth resolving before replication. Control scores use a time-invariant, discrete-time linear network-control framework, not a learned nonlinear neural dynamics simulator. Average controllability is the Gramian trace; modal controllability weights eigenvector contributions by mode difficulty. The precise matrix stabilization and supplementary equations were not audited because the DOCX was unavailable.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Do control metrics distinguish cognitive constructs, or mostly redescribe shared connectivity variation? The specific hypothesis associates modal controllability with hard-to-reach representations and fluid cognition, and average controllability with easier transitions and crystallized cognition. The study tests prediction and specificity; it explicitly does not test the presumed link between subjective cognitive effort and physical control energy.

### 2. What is the method?

Compute structural, static functional, and dynamic functional connectomes; apply matched graph/control feature extraction; predict cognitive scores with repeated nested cross-validation; compare modalities, control metrics, and strength. Analyze regional importance using Haufe transformations and compare maps with cortical gradients and cognitive-network theories. Strength is the sum of absolute edge weights, avoiding cancellation between positive and negative functional connections.

### 3. What is the method motivation?

Structural connectomes may miss state-dependent coordination relevant to cognition. Dynamic states offer a richer representation, but any resulting predictive gain could belong to that representation rather than to control theory. A same-representation strength comparator is the essential test. LEiDA avoids choosing a sliding-window duration, but it does not eliminate the physiological and statistical limits of BOLD-based state estimation.

### 4. What data does it use?

HCP young-adult data. Methods start with 950 participants with complete fMRI, cognitive scores, and mean relative framewise displacement below 0.2 mm, then remove five without diffusion MRI: an implied analysis sample of 945. CFA uses the larger set of 1,192 participants with complete cognitive testing. Four approximately 15-minute resting runs provide substantial within-person sampling. This is healthy-adult, cortical MRI evidence—not adolescent, patient, intracranial, or stimulation-response validation.

### 5. How is it evaluated?

Five repetitions of outer ten-fold cross-validation, with related participants kept together; inner five-fold tuning. Nuisance-regression and standardization parameters are estimated on training data and applied to test data. Prediction uses held-out coefficient of determination, not squared prediction–outcome correlation. Significance uses 1,000 restricted permutations; model comparisons use corrected resampled t-tests with FDR correction. Regional inference uses permutation/FDR procedures; cortical map comparisons include spatial spin tests. Modality percentages use a demeaned-score decomposition, while headline R² is reported without that test-set demeaning; these quantities should not be casually interchanged.

### 6. What are the main results?

Figure 7 reports the following held-out R² values for dynamic-only models:

| Cognitive target | Average controllability | Modal controllability | Node strength |
| --- | ---: | ---: | ---: |
| General intelligence, g | 0.149 | 0.156 | 0.149 |
| Fluid intelligence, gF | 0.076 | 0.075 | 0.086 |
| Crystallized intelligence, gC | 0.112 | 0.115 | 0.111 |

For g, structural-only R² is 0.030, 0.029, and 0.023, respectively. Combined structural-plus-dynamic models reach 0.161, 0.166, and 0.154, without a significant improvement over dynamic-only models. Dynamic versus structural superiority is significant for all three descriptors for g and gC, but for gF only strength clears the corrected comparison; do not flatten this into universal superiority.

Control metrics do not significantly outperform strength, and average versus modal controllability does not show the predicted gC-versus-gF specificity. All three descriptors predict g most strongly, although measurement reliability differs across targets. Across group-average functional maps, strength and controllability are tightly related; within-region, across-participant relationships are less extreme, so the result is not an identity theorem. Dynamic regional importance broadly follows the transmodal–unimodal gradient, but remains correlational.

### 7. What is actually novel?

The useful increment is the joint comparison of connectivity representation, cognitive construct, and simple-versus-control descriptors under one predictive design. It extends state-based control analysis and directly challenges a particular operationalization of intelligence theory. It is not the discovery that node strength and controllability can correlate, and it does not establish priority over all earlier dynamic-control work.

### 8. What are the strengths?

An informative negative result rather than a rescued positive headline; a serious strength baseline; substantial resting-state sampling; family-aware nested prediction; explicit distinction between R² and squared correlation; and spatial-autocorrelation-aware map testing. Structural and functional modalities are actually compared and combined, rather than merely mentioned. The authors also clearly separate their analysis from a direct test of cognitive effort or intervention efficacy.

### 9. What are the weaknesses, limitations, or red flags?

* **Association, not control validation:** Resting-state prediction does not identify causal input–output dynamics, demonstrate controllability under a real actuator, or measure an intervention's energy cost. BOLD coherence is not an effective-connectivity estimate.
* **Representation learning is not fully cross-fitted as described:** State clustering pools participants, and low-variability edge thresholding is defined across participants. The main text does not say those steps were relearned inside outer folds. These are outcome-free but potentially transductive preprocessing choices; an inductive deployment claim needs a frozen training-only vocabulary and thresholds.
* **State choice has discretion:** k = 6 was chosen partly because it exposed a frontoparietal state, despite a prior elbow around 4–5. The authors report alternative-state robustness in the uninspected supplement.
* **No equivalence test:** Nonsignificant metric differences do not establish that strength is always sufficient, or that control theory has no unique information. Thresholding may change differences; no external cohort tests transportability.
* **Construct reliability:** A broad multi-test g factor is not psychometrically matched to the primary single-test gF and gC measures. Better prediction of g need not mean a uniquely general-control mechanism.
* **Implementation/reporting uncertainty:** Methods imply n = 945, while Table 1's displayed gender counts total 950; the mean-versus-median state-matrix discrepancy also needs clarification. Neither is silently resolved here. Exact supplementary normalization and robustness details remain unaudited.
* **Coverage:** Cortex-only parcellation, a predominantly White healthy-adult sample, long fMRI acquisitions, and no held-out site/device cohort limit clinical, developmental, or real-time generalization. Regional Haufe importance is not a causal target ranking.

### 10. What challenges or open problems remain?

Whether any control descriptor adds reliable out-of-sample information after strength and representation are matched; whether short recordings yield stable state-specific estimates; and whether these scores predict actual perturbation responses. Between-person cognitive prediction also does not establish within-person state tracking. A state-dependent analysis is not automatically a time-varying controller: each state still receives a static control calculation.

### 11. What future work naturally follows?

Repeat the complete pipeline with fold-local state discovery and threshold selection, then freeze it for an independent cohort. Compare matched-strength, static/dynamic, controllability, and finite-horizon target-specific models. Finally test whether model-selected sites and states predict TMS- or intracranial-evoked responses under matched effective dose. Include reliability-matched cognitive factors and evaluate subgroup calibration rather than extrapolating from one adult cohort.

### 12. Why does this matter for cabbageland?

This is directly relevant network/computational neuroscience, and adjacent inspiration for neuromodulation—not clinical treatment evidence. It raises the bar for a personalized-targeting claim: showing that a control score correlates with behavior is insufficient if a simple graph statistic on the same state representation does as well. Hypnosis-state classifiers and psychiatric biomarkers face the analogous problem: state labels, predictive value, causal leverage, and treatment utility are separate achievements.

### 13. What ideas are steal-worthy?

1. Factor the experiment into **representation × descriptor × endpoint**; do not award the descriptor credit for a better representation.
2. Require a node-strength baseline on the identical connectome, preprocessing, and validation splits.
3. Separate trait prediction from within-person state estimation, and both from actuator-response prediction.
4. Test a finite-horizon, target-specific perturbation hypothesis before interpreting an unlimited-state-space control score therapeutically.
5. Report failed specificity hypotheses plainly; a stronger general factor does not rescue a proposed fluid/crystallized dissociation.

### 14. Final decision

Preserve as **Highly relevant** methodological and framing evidence. Use it when designing network-control baselines or reviewing mechanism claims. Do not use it to choose a clinical target, claim causal control of cognition, or dismiss all control methods as interchangeable with strength.
