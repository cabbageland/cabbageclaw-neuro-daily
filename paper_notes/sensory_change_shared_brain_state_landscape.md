# Sensory Change Detection Unfolds Within a Shared Low-Dimensional Brain-State Landscape

## Basic info

* Title: Sensory Change Detection Unfolds Within a Shared Low-Dimensional Brain-State Landscape
* Authors: Hadi Choubdar Parvin; Kimford J. Meador; Babak Razavi
* Year: 2026
* Venue / source: bioRxiv preprint; version 1 posted November 19, 2026; not peer reviewed
* Link: https://doi.org/10.64898/2026.11.18.767177
* Date surfaced: 2026-11-20
* Why selected in one sentence: It connects cross-modal connectivity geometry to event-associated BOLD trajectories while explicitly distinguishing continuous occupancy from discrete brain states.

## Quick verdict

* Useful

Preserve for representation and evaluation design, not as evidence of causal control or a clinical biomarker. Two dominant connectivity dimensions reproduce across participant splits, and auditory/visual targets share an early projected response before diverging. The important restraint is that mixture components are descriptive regions of a continuous distribution; neither those components nor a fitted autoregression establishes biological attractors, effective connectivity, or a stimulation policy.

## One-paragraph overview

The authors reanalyse matched auditory and visual oddball fMRI from 17 healthy adults. Rather than compare only activation maps, they fit partial least-squares (PLS) decompositions to group-average connectivity profiles, recover shared and modality-biased cortical dimensions, and project each run's BOLD activity onto the resulting loadings. They then describe those trajectories using a ridge-regularized autoregression, Gaussian mixtures, and an overlap-adjusted event-response model. The dominant spatial architecture is shared, but target-associated trajectories differ in how they weight that architecture over time. This is a useful descriptive bridge between connectivity and activity, with substantial limits from a small cohort, group-derived coordinates, exploratory analysis choices, and the confounding of target detection with button presses.

## Model definition

### Inputs

- Preprocessed parcel-wise fMRI time series from auditory and visual oddball runs: 180 symmetric bilateral cortical regions, 170 volumes per run, TR = 2 seconds.
- PLS receives two group-average 180-by-180 Pearson-correlation matrices. Its 180 observations are **parcels**, not independent participants; variables are connectivity profiles. Auditory and visual matrices are also fitted reciprocally.
- Temporal models receive BOLD projected onto the unthresholded modality-specific PLS loadings. VAR models use within-run-standardized latent histories; the input-augmented model adds a binary target indicator shifted by one TR.
- Joint finite impulse response (FIR) models receive actual target/standard onsets and nuisance intercept/trend regressors. The Gaussian mixture receives pooled raw four-dimensional latent observations.

### Outputs

- Four spatial PLS components and their regional loadings; four projected temporal latent variables (tLVs).
- Next-sample predictions of the dominant two-dimensional latent trajectory, fitted autoregressive coefficients, and model-implied fixed points/target-associated displacement.
- Three Gaussian-component membership probabilities and descriptive occupancy/transition summaries, not validated physiological state labels.
- Estimated target-minus-standard BOLD response trajectories and parcel contributions to those responses. No patient response score, treatment target, or stimulation command is produced.

### Training objective (loss)

- **PLS:** maximize covariance between auditory and visual projected connectivity profiles, with sequential component extraction. A symmetric SVD of standardized cross-covariance checks correspondence; the first four squared singular values account for 97.1% of the reported shared cross-modal structure. This is not 97.1% of raw BOLD variance or prospective predictive accuracy.
- **VAR(2):** minimize summed squared next-step prediction error plus an L2 coefficient penalty, using multivariate ridge regression. The input-augmented version adds the target regressor to the same predictive objective.
- **Gaussian mixture:** fit a full-covariance mixture density by likelihood; one-to-five-component solutions were inspected with likelihood/AIC/BIC, but three were retained for an interpretable coarse-graining, not established as the unique biological state count.
- **FIR:** ordinary least squares fits simultaneous target and standard response bases, with knots every 2 seconds through 24 seconds. It estimates overlapping event-associated responses rather than optimizing intervention efficacy.

### Architecture / parameterization

A descriptive analysis stack: linear PLS representation, linear VAR(2) dynamics with or without an external event input, three full-covariance Gaussians, and a linear FIR response model. The VAR is `x[t+1] = A1 x[t] + A2 x[t-1] + b + error`, optionally adding `B u[t]`; each lag matrix is 2-by-2. Empirical kernel density, graph thresholding, and UMAP aid visualization. The displayed density landscape is empirical occupancy; the autoregression supplies a fixed-point estimate, not the density surface or a mechanistic energy function.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Does sensory target detection use separate modality-specific systems, one fixed supramodal network, or common cortical coordinates with context-dependent expression? The paper asks how shared connectivity organization relates to evolving activity, not which region should be stimulated.

### 2. What is the method?

Estimate run-level functional connectivity, average within modality, fit reciprocal four-component PLS, interpret loadings using cortical/network maps, and project BOLD onto the raw loadings. Evaluate participant-level map reproducibility; characterize temporal prediction and occupancy; estimate target/standard responses jointly to account for overlap between closely spaced stimuli. Graphs select parcels using loading thresholds and edges from the original group FC matrices.

### 3. What is the method motivation?

Spatial overlap alone cannot distinguish identical processing from different trajectories through a common representation. Reusing connectivity-derived coordinates makes the spatial-to-temporal relationship explicit. Joint FIR modeling addresses overlapping hemodynamic responses when stimuli arrive every 2–3 seconds.

### 4. What data does it use?

A public simultaneous EEG-fMRI oddball dataset, but **only fMRI is analysed here**. There are 17 healthy adults, six female, mean age 27.7 years; three auditory and three visual runs per person, minus one failed auditory acquisition: 50 auditory and 51 visual runs. Each run has 125 stimuli, 20% targets, with right-index-finger responses to targets. Verified event records support FIR analysis for 91 runs, 48 auditory and 43 visual, still representing all 17 participants. The 17,170 pooled BOLD observations are not 17,170 independent people.

### 5. How is it evaluated?

PLS maps undergo leave-one-participant-out, 1,000 independent participant split-halves, and 1,000 participant bootstraps, plus correspondence to symmetric SVD. Spatial loading thresholds use 1,000 permutations at uncorrected parcel-level P < 0.05. VAR prediction uses five-fold contiguous blocked cross-validation within runs; training can occur on both sides of a test block, so it is not forward-chaining deployment validation. FIR contrasts are averaged within person before participant-level sign-flip tests, with stated Holm corrections. The 4-second and 4–6-second windows were chosen after inspecting trajectories and remain exploratory.

### 6. What are the main results?

- Split-half spatial correlations are stronger for LV1–LV2, median r = 0.930–0.949, than for the more variable LV3–LV4, r = 0.838–0.928. Shared geometry within this small dataset is better supported than a universally fixed four-component decomposition.
- LV1 emphasizes sensory, attention, and action systems; LV2 emphasizes associative/contextual systems. Frontoparietal contributions occur in both, so this is not simply sensory versus executive cortex.
- The dominant two-dimensional VAR has reported cross-validated R² = 0.43 ± 0.16. Adding target timing improves R² by only 0.005 ± 0.015. Most predicted temporal variance is ongoing latent activity, not a strong identified event-input effect.
- The central Gaussian component covers 70.4% of observations; 57.7% of samples have maximum membership probability below 0.8. These figures support soft occupancy descriptions, not sharply separated states.
- At 4 seconds, target-minus-standard tLV1 responses reach +0.418 within-run SD for auditory and +0.528 for visual runs. Between 4 and 6 seconds, the tLV2 contrast changes by −0.283 SD for auditory versus +0.053 for visual. These are exploratory **BOLD** response summaries, not millisecond neural latencies or treatment effects.

All numerical results are author-reported, not independently recomputed.

### 7. What is actually novel?

The useful synthesis links cross-modal FC geometry, projected ongoing activity, and overlap-adjusted event trajectories in one dataset. PLS, VAR, mixtures, and UMAP are established tools. The work offers an interpretable descriptive organization, not a newly identified causal circuit, learned controller, or proven dynamical mechanism.

### 8. What are the strengths?

Closely matched within-person tasks; explicit participant-resampling checks; a symmetric-decomposition cross-check; raw rather than thresholded loadings for temporal projection; participant-level event inference; and unusually clear acknowledgement that Gaussian components need not be discrete states. The weak incremental target-input prediction is informative rather than something to hide behind an attractive landscape plot.

### 9. What are the weaknesses, limitations, or red flags?

- **Causal identification:** undirected FC and PLS do not identify directed interactions. Positive/negative loadings are not excitation/inhibition, and thresholded graph hubs are not causal control nodes.
- **Task confounding:** targets differ in rarity, physical properties, relevance, and motor response. FIR overlap correction cannot separate detection from pressing a button.
- **Representation/evaluation:** group-derived loadings and within-run blocked prediction do not establish a frozen decoder that generalizes to a new subject, site, or future session. Participant map reproducibility is valuable but answers a different question.
- **Exploration/multiplicity:** component count, mixture count, input delay, and response windows involve exploratory choices. Uncorrected spatial thresholds and post-selection regional descriptions warrant caution.
- **Temporal inference:** TR = 2 seconds and hemodynamic convolution limit neural-timing and online-control interpretations. Strong autocorrelation can support prediction without useful perturbation forecasting.
- **Biological coverage/heterogeneity:** symmetric cortical parcellation hides hemispheric differences and excludes subcortex. No patients, developmental trajectory, or treatment-response subgroup is tested; simultaneously recorded EEG is not integrated.
- **State/landscape language:** mixture assignments and empirical density are not evidence of metastability or a physical potential. A smooth descriptive map does not establish controllability.

### 10. What challenges or open problems remain?

Whether these coordinates survive independent acquisition, individual calibration, alternate parcellations, and prospective decoding; whether trajectories predict behavior beyond simple task/motor variables; and whether perturbations move them as predicted. A stimulation input map, safety constraints, and a clinically meaningful target trajectory are all missing.

### 11. What future work naturally follows?

Freeze preprocessing and loadings before testing new participants; use forward-chaining temporal evaluation and simple autocorrelation baselines. Independently manipulate deviance, relevance, and response requirements. Integrate EEG to test the neural timing of the proposed trajectories, retain hemispheric/subcortical structure, and only then test an explicit perturbation model with held-out stimulation responses. Pre-register response windows and test representation stability across sites and symptom strata.

### 12. Why does this matter for cabbageland?

It is a useful antidote to treating every latent cluster as a brain state and every brain-state picture as a control model. A shared coordinate system may help specify what to observe; it does not identify what an actuator changes or what a patient benefits from. Keep representation, system identification, and therapeutic objective as separate claims.

### 13. What ideas are steal-worthy?

- Project activity through independently learned, interpretable network coordinates, then validate those coordinates in a genuinely held-out setting.
- Report posterior ambiguity and continuous occupancy before assigning state labels.
- Separate a model's empirical density display from its dynamical predictions and input response.
- Decompose a trajectory change into regional contributions without claiming those regions are causal drivers.
- Test whether adding an intervention/event input improves prediction beyond intrinsic history; do not equate an attractive displacement plot with useful control authority.

### 14. Final decision

Keep as **useful network-neuroscience/methods inspiration**, with the descriptor-to-controller gap prominently attached. Focused full-text PDF inspection covered the main results, discussion, model definitions, resampling, and event-response methods. Supplementary image panels, source code, and underlying recordings were not independently audited. No clinical or causal-control claim is warranted.
