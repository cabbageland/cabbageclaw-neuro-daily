# Intrinsic neural dynamics reveal a body-part-specific topography in mouse secondary motor cortex

## Basic info

* Title: Intrinsic neural dynamics reveal a body-part-specific topography in mouse secondary motor cortex
* Authors: Weihao Xu; Alexis J. Yagielski; David N. Thibodeaux; Lina Marcela Carmona; Kosisochukwu Ugorji; Somayeh Shahsavarani; Sharon H. Kim; Fatema Lodgher; Hanzhi T. Zhao; Elizabeth A. Malan; Lu Xu; Caitlin Freeman; Anupam Bisht; Kaitlyn Swayze; Morgan Cambareri; Wenze Li; Elizabeth M. C. Hillman
* Year: 2026
* Venue / source: Nature Communications, volume 17; published November 13, 2026
* Link: https://doi.org/10.1038/s41467-026-78900-3
* Date surfaced: 2026-11-14
* Why selected in one sentence: It separates state-dependent cortical organization from descending motor output through convergent optical, anatomical, and projection-population measurements, offering a useful constraint on neural decoding and intervention targeting.

## Quick verdict

* Highly relevant

Preserve for network-mapping and measurement logic, not as a causal account of movement orchestration. Resting activity reveals an orderly S1–M2 correspondence supported by anatomical projections and behavior-dependent engagement; simultaneous corticospinal imaging importantly limits a motor-output interpretation. Small animal counts in key analyses, imposed component decorrelation, and the absence of selective M2 perturbation constrain the mechanistic claim.

## One-paragraph overview

The authors use wide-field optical mapping (WFOM) of calcium fluorescence with reflectance-based hemodynamic correction in mice. Sensory stimulation localizes S1 body representations; quiet-rest correlations then identify homologous subregions in secondary motor cortex, M2. Independent Allen atlas projection datasets support the spatial organization. Dual-color recording contrasts broadly expressed Thy1 activity with retrogradely labeled corticospinal neurons (CSNs), showing that the prominent resting fluctuations are weak in the output population. Finally, a constrained spatial/temporal decomposition and spontaneous movement analyses relate M2 subregions to particular effectors and coordinated actions. The study identifies organization and state dependence; it does not identify an intervention-response model.

## Model definition

### Inputs

- **Mapping:** Hemodynamically corrected fluorescence time series, sensory-localized S1 seed signals, and behavior-defined quiet-rest epochs. Functional parcels are obtained using k-means; resting Pearson correlations are Fisher-transformed for mapping.
- **Constrained least squares (CLS):** Resting images and seed time courses from S1, M1, M2, and additional regions; at least 300 seconds of concatenated rest define temporal bases. New movement recordings are projected onto the fitted spatial templates.
- **Decoders:** Activity time courses from 500 cortical parcels. Per mouse, more than sixteen nine-minute recordings are concatenated; the first 60% train and the final 40% test. CNN inputs contain 40-frame windows.

### Outputs

- Body-part-associated S1–M2 correlation peaks/maps, not directed effective connectivity.
- CLS spatial weights and extracted regional time courses, including shared/global and region-specific M2 components.
- Predicted whisking, wheel speed, oromanual movement, and forepaw speed. Rest/locomotion labels are also derived by thresholding actual and predicted wheel speed after excluding oromanual-motion frames.

### Training objective (loss)

- Forward CLS minimizes squared image-reconstruction error, `||Y_rest − W H||²`, with nonnegative spatial weights `W` and fixed seed-derived temporal bases. Region selection is adjusted to reach at least 90% forward reconstruction FVE.
- A global M2 component is separated by subtracting a fraction `k` of the median M2 time course. Four continuous temporal folds assess values minimizing mean absolute pairwise intra-M2 correlation. Optimal values span 0.45–0.58; the authors apply `k = 0.5` to held-out data.
- Backward CLS fits regional activations to new images with fixed spatial templates and constraints linking global and seed-specific M2 signals; optimization uses SciPy SLSQP. Reconstruction FVE is not a behavioral or causal objective.
- The linear comparator is MultiTaskLassoCV: squared prediction error plus an L1/L2 mixed-norm penalty, with five-fold selection over stated alpha values. The inspected text does not establish that these internal folds are grouped by recording session.
- **The exact CNN training loss is not specified in the inspected methods.** L1/L2 kernel regularization is reported, but it is not the full data-fitting objective; no loss is inferred from the linear output activation.

### Architecture / parameterization

The main mapping is seed-based correlation, supported by a structured linear image decomposition—not a recurrent dynamical model. The nonlinear decoder uses a Conv1D layer with 1,024 filters, kernel size 20, ReLU, and L1/L2 kernel regularization of 0.0001; dense layers have 128, 64, and four units. A bidirectional LSTM with 100 units per direction is optional and improves oromanual decoding; it is excluded from the linear/nonlinear wheel-speed comparison and rest/locomotion analysis. The ablation replaces nonlinear activations with linear ones while retaining the convolutional architecture. No learned stimulation policy, state-transition equation, or input-response model is supplied.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Mouse motor-cortex maps are coarse, and spontaneous movements recruit multiple body parts together. The authors ask whether intrinsic activity can reveal finer M2 organization and clarify which signals reflect outgoing movement versus other cortical processes.

### 2. What is the method?

Localize sensory seeds, correlate their quiet-rest activity with cortex-wide signals, compare the resulting M2 arrangement with anatomical projections, contrast Thy1 and corticospinal populations, and examine region-specific responses across spontaneous movements. Hemodynamic correction, video tracking, raw-ROI comparisons, and constrained unmixing address distinct measurement problems.

### 3. What is the method motivation?

Movement introduces shared kinematic variance while quenching resting fluctuations. Mapping during quiet rest can expose selective interregional synchrony that is obscured during movement; projection-defined output recordings then test whether that synchrony resembles descending motor activity.

### 4. What data does it use?

Repeated imaging from 11 male and female Thy1-jRGECO1a mice, starting around three months of age, with behavioral videos and wheel measurements; selected mice also have retrogradely labeled CSN GCaMP recordings. Important denominators differ: the M2 correlation maps show six mice; the paired dual-color correlation analysis uses **42 sessions from two mice**; movement-type aggregates use **three qualifying mice per type** from a six-animal pool, requiring at least seven spontaneous bouts per included behavior. Atlas tracing is a separate source, with one forelimb example from an Rbp4-Cre line rather than wild type. Sex-disaggregated analysis was not supported by the design.

### 5. How is it evaluated?

Across-mouse mapping consistency, circular-time-shift correlation nulls, anatomical projection correspondence, rest-versus-movement comparisons, projection-population contrasts, and behavior-linked selectivity. CLS is evaluated by reconstruction FVE, held-out resting folds, and movement-bout reconstruction. Decoder comparisons use the same chronological train/test split, wheel-speed R², and normalized rest/locomotion confusion matrices. Session-level correlation tests use Fisher transforms and paired Wilcoxon tests with FDR correction; they do not turn repeated sessions into independent animals.

### 6. What are the main results?

- Quiet-rest S1 signals identify a reproducible body-part-related arrangement in M2, supported by S1-to-M2 axonal projection patterns.
- Thy1 resting fluctuations are much smaller in simultaneously recorded CSNs, arguing against their being a simple descending motor-output signal. For the highlighted session-averaged comparisons, CSN-M1/Thy1-M2 correlation rises from about 0.08 at rest to 0.40 during locomotion.
- M2 responses are more pronounced during coordinated paw-raising/licking than simple locomotion. The reported forepaw-M2 amplitude ratio is 3.28 for Thy1 versus 1.12 for CSNs; this is a specific within-paradigm contrast, not a general efficacy effect.
- Nonlinear decoding better distinguishes quiet periods from movement despite resting cortical fluctuations. Exact decoder performance values were not independently extracted from supplementary assets, so none is invented here.

### 7. What is actually novel?

The useful contribution is the convergence of resting functional topography, anatomical projections, output-population contrast, and spontaneous behavior to sharpen M2 organization. It is not the invention of resting functional connectivity, proof of directed communication, or demonstration of an M2 control mechanism.

### 8. What are the strengths?

The evidence is genuinely multimodal: imaging, reflectance correction, behavior, anatomical projections, and projection-defined fluorescence constrain different alternatives. Quiet-state mapping reduces movement confounding; chronological decoder testing is preferable to random frame splitting. Raw-ROI comparisons help prevent the entire behavioral story from resting on one decomposition. Processed data and versioned code are publicly linked.

### 9. What are the weaknesses, limitations, or red flags?

- **Causality:** No selective perturbation tests whether the mapped M2 subregions are necessary or sufficient for the proposed coordination function. Common input and subcortical loops remain alternatives to direct functional communication.
- **Independent replication:** Forty-two sessions from two mice provide within-animal precision, not broad population replication. Very small session-level p-values should not hide that denominator; some behavior analyses contain three mice.
- **Representation:** Global subtraction explicitly minimizes intra-M2 correlations. Decorrelation afterward is partly an optimization target, not independent evidence of physiological modularity; reconstruction FVE cannot establish that each component is biologically correct.
- **Mapping discretion:** Sensory seeds for two mapping mice were inferred from behavior/comparison rather than direct sensory mapping. Contours depend on local percentile thresholds, including lower thresholds for diffuse regions; peak correspondence is more defensible than hard atlas boundaries.
- **Online realism:** Fluorescence is filtered with zero-phase `filtfilt`; an optional decoder is bidirectional. Offline performance does not establish causal, low-latency prediction. Preprocessing and feature-fitting boundaries would need auditing before a leakage-free deployment claim.
- **Measurement/cohort:** Wide-field fluorescence does not resolve individual cells or every output pathway; weaker CSN fluorescence is not proof that all motor output is absent. Orofacial M1 is not localized with corticobulbar tracing. Experiments were not randomized or blinded, and sample size was not predetermined.

### 10. What challenges or open problems remain?

What drives the resting fluctuations, how do arousal and common inputs gate them, and which mapped regions causally affect coordination? Do the maps generalize to trained behaviors, different animals, broader effector coverage, and measurement modalities without these fluorescent labels? There is no demonstrated controllability or clinically validated biomarker here.

### 11. What future work naturally follows?

Perturb individually mapped M2 regions while measuring full-body kinematics, EMG, output populations, and subcortical activity. Compare effects on matched simple versus coordinated movements across rest/arousal states. Preregister animal-level analyses; test held-out animals and sessions; vary global subtraction, seeds, and contour thresholds. Rebuild decoding with causal filters and windows, then test actual latency and false activations during quiet rest.

### 12. Why does this matter for cabbageland?

It sharpens a recurring targeting mistake: an accessible or highly structured network signal is not necessarily the state a controller should regulate. The transferable idea is to condition observation models on state and cell population, then separately identify causal intervention responses. It is network/methods evidence, not a depression treatment result or a clinical targeting recipe.

### 13. What ideas are steal-worthy?

1. Discover organization in a quiet state and validate it against anatomy and behavior rather than making the same signal validate itself.
2. Include a projection-defined output comparator to distinguish network fluctuations from outgoing commands.
3. Report decoder errors separately during rest and movement; aggregate accuracy can conceal dangerous false activations.
4. Keep raw-ROI, global-component, and unmixed-component analyses side by side; make the constraints visible.
5. Before using the map for stimulation, add selective perturbation and input-response identification, then compare controllers at matched sensing, stimulation, and energy budgets.

### 14. Final decision

**Preserve — highly relevant network/methods work with bounded intervention relevance.** Primary publisher full text was inspected for selected results/captions, discussion, cohort definitions, preprocessing, mapping, model equations, decoding, and statistics. Supplementary files, source datasets, public code, and numerical reproduction were not independently audited. Data: https://doi.org/10.25452/figshare.plus.28633379. Code: https://github.com/hillmanlab/M2-topography; paper-linked version: https://doi.org/10.5281/zenodo.23605411. Treat the proposed coordination mechanism as a hypothesis awaiting perturbation, not as the study's established causal result.
