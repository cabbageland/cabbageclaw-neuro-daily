# A reproducible event-driven analytical framework for ECG-derived skin sympathetic nerve activity analysis: towards afferent signal processing for closed-loop neuromodulation

## Basic info

* Title: A reproducible event-driven analytical framework for ECG-derived skin sympathetic nerve activity analysis: towards afferent signal processing for closed-loop neuromodulation
* Authors: Shahrokh Rahmani; Julie Norup Hertel; Benedikt Linz; Dominik Linz; Amir P Divanbeighi Zand; Victoria S Marks; Thomas Jespersen; Stefan Sattler; Sarah Dalgas Nissen; Tim Denison; Alexander L Green; Pier D Lambiase
* Year: 2026
* Venue / source: Frontiers in Bioengineering and Biotechnology; published November 4, 2026
* Link: https://doi.org/10.3389/fbioe.2026.1980881
* Date surfaced: 2026-11-24
* Why selected in one sentence: It specifies and evaluates a personalized physiological-event detector while exposing the gap between sequential offline replay, causal real-time sensing, and an actual closed-loop intervention.

## Quick verdict

* Useful

Preserve as a sensing/evaluation reference, not evidence of an effective autonomic or psychiatric controller. The useful contribution is an explicit threshold-and-persistence pipeline with recording-level detection denominators, latency, and limited independent replay tests. The authors acknowledge the decisive boundaries: offline preprocessing, retrospective calibration, surrogate physiology, no specificity estimate, and no trigger-driven treatment experiment.

## One-paragraph overview

The paper takes high-frequency activity from surface ECG recordings during experimentally imposed respiratory obstruction in anesthetized pigs, converts it into a skin-sympathetic-activity surrogate, and asks whether sustained bursts can generate reproducible event-associated triggers. It combines channel-median fusion, recording-specific baseline thresholding, event-centered summaries, and sequential offline replay. The principal dataset contains one respiratory event from each of 50 pigs; two additional pigs provide a three-event held-out recording and a four-event intervention illustration. The trigger processes past samples of a previously computed envelope, not a live raw-signal stream. That distinction—and the absence of independently labeled sympathetic ground truth—limits what its apparent detection performance establishes.

## Model definition

### Inputs

- Surface ECG, acquired at 4 kHz in 47 development recordings and 10 kHz in three; up to three channels, with some channels unavailable.
- A baseline calibration interval: the 60 seconds before an annotated intermittent negative upper-airway pressure (INAP) onset, or the available pre-event segment when shorter. Its retrospective selection uses event timing unavailable to an unannounced-event detector.
- ECG preprocessing: fourth-order Butterworth high-pass filtering at 500 Hz, rectification, a 1-second moving-average envelope, channel-median fusion, and downsampling to 100 Hz. Forward-backward zero-phase filtering is applied offline.
- Upper-airway pressure supplies event onset/termination annotations for calibration and evaluation. Oxygen saturation, heart rate, and hemodynamics provide context, not additional learned inputs or independent sympathetic labels.

### Outputs

- A continuous ECG-derived SKNA envelope: a sympathetic-activity surrogate, not direct nerve firing or an identified neural-network state.
- Binary burst-active samples and burst occupancy, the percentage of above-threshold samples in a window.
- An ON/OFF replay trigger: occupancy must exceed 5% in two consecutive 30-second trailing windows updated every 10 seconds.
- Detection latency and event-associated activation summaries. No stimulation amplitude, anatomical target, clinical response prediction, or therapeutic action policy is learned.

### Training objective (loss)

The learned component is a two-component Gaussian mixture fitted to each baseline envelope distribution. The main text does not explicitly specify its numerical fitting objective, initialization, convergence settings, or implementation-level handling of mixture crossings; do not invent a supervised loss or claim a particular optimizer was audited. The weighted Gaussian-density intersection supplies one candidate threshold. The final threshold is the maximum of that candidate, the baseline 95th percentile, and baseline median plus six median absolute deviations. The authors state that this maximum rule was not optimized against detection performance. Replay thresholds/persistence are prescribed rules, not a reward-trained controller.

### Architecture / parameterization

A modular signal-processing and unsupervised-calibration pipeline followed by a deterministic persistence-gated state machine. Recording-specific mixture parameters and amplitude thresholds handle baseline heterogeneity; the trigger configuration is shared. Calibration is fixed during the main single-event replay, with event-specific recalibration in the multi-event examples. This is neither an end-to-end classifier nor a mechanistic latent-state model, and it does not close an actuator feedback loop.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

ECG-derived sympathetic surrogates are bursty, noisy, and sensitive to preprocessing and baseline amplitude. Mean activity or hand-picked bursts do not specify a reproducible detector, let alone one with quantified timing. The paper tries to standardize extraction, calibration, event comparisons, and a deployment-oriented replay test.

### 2. What is the method?

Extract and median-fuse high-frequency ECG envelopes; fit the baseline-informed threshold; mark above-threshold samples; then require sustained occupancy before issuing a replay trigger. Keep event presence, a new OFF-to-ON transition, pre-event activation, and post-event persistence separate. A second recording tests the same prescribed configuration on repeated events, and another illustrates replay before and during dorsal root ganglion (DRG) stimulation.

### 3. What is the method motivation?

A personal amplitude threshold is more plausible than one absolute threshold across animals with different signal scales. Channel-median fusion can reduce channel-specific contamination, while occupancy and persistence emphasize sustained activation rather than isolated high-amplitude samples. Those choices create a latency/missed-event trade-off; conservatism is not automatically optimal for the eventual therapeutic objective.

### 4. What data does it use?

- Development/evaluation cohort: 50 INAP recordings from 50 individual anesthetized pigs, each contributing one imposed respiratory event. The protocol targeted roughly 75 seconds of obstruction, but actual durations varied.
- Held-out proof of principle: one additional pig with three INAP events. This is one independent preparation, not three independent animals or an external cohort.
- Intervention illustration: one further pig, four 75-second events—two before and two during DRG stimulation at 4 Hz and 0.3 mA. Stimulation testing/transition periods were excluded from replay evaluation.
- No human, psychiatric, longitudinal treatment-response, or direct sympathetic nerve-recording dataset is supplied.

### 5. How is it evaluated?

Event-aligned envelopes and burst occupancy are compared across baseline, INAP, and recovery using paired Wilcoxon tests. Replay reports in-event trigger presence separately from new post-onset activation among recordings OFF at onset; latency is summarized only among detected new activations. Threshold and one-at-a-time replay-parameter sensitivity analyses test operating-point dependence. The held-out and intervention recordings are illustrative applications, not a large test set or a randomized controller comparison. Respiratory annotations establish perturbation timing, not independent sympathetic-state labels; conventional specificity and precision are not estimated.

### 6. What are the main results?

- Burst occupancy increases from baseline to INAP (`p < 0.001`). INAP versus recovery is not detectably different (`p = 0.886`); this is not evidence that recovery equals baseline or that state reversal is immediate.
- A trigger is present during INAP in **43/50 recordings (86%)**. One is already ON at event onset; among the **49 OFF-at-onset recordings, 42 generate a new activation (85.7%)**.
- Among those 42 detections, median latency is **24.0 seconds**, IQR **18.9–54.3 seconds**. This excludes missed detections and is not an all-event end-to-end hardware latency.
- **7/50 recordings** show some pre-INAP trigger activity. This is not a measured false-positive rate, because genuine sympathetic activity can occur outside respiratory events and no independent sympathetic absence label was available.
- The three-event held-out recording generates reported activation latencies of **28.4, 30.0, and 20.0 seconds**, with event-specific calibration. One event also has pre-event activation, underscoring why event-associated detection and specificity differ.
- All four intervention-illustration events generate triggers. The authors explicitly decline to interpret before/during-stimulation differences as treatment effects; pulse-synchronized artifact assessment and blanking were not performed.

These numbers come from the main Results and figure descriptions. Separately linked supplementary tables/figures were not independently checked.

### 7. What is actually novel?

The advance is the integration and explicit evaluation contract: personalized conservative calibration, event-centered physiological summaries, sequential replay, interpretable trigger rules, and reproducibility artifacts. High-pass ECG-derived SKNA, Gaussian mixtures, median fusion, and persistence rules are not individually new. It is not a new physiological mechanism, verified afferent-nerve measurement, or demonstrated adaptive therapy.

### 8. What are the strengths?

- Fifty independent development animals provide more useful heterogeneity than a single selected trace.
- Reports the distinction between trigger presence and newly generated activation rather than laundering both into one accuracy number.
- Exposes its calibration, temporal windows, persistence, and parameter trade-offs.
- Keeps the physiological surrogate, respiratory-event reference, and treatment interpretation separate.
- Acknowledges noncausal preprocessing, retrospective calibration, and the limited external sample. Code and processed-data archives are linked, although they were not independently audited for this note.

### 9. What are the weaknesses, limitations, or red flags?

- **End-to-end causality:** replay uses preprocessed envelopes; forward-backward filtering uses future raw samples. Calibration is selected relative to a retrospectively known event. Past-only trigger windows do not repair either upstream dependency.
- **Physiological identification:** high-frequency ECG activity is not direct sympathetic discharge. Airway pressure labels obstruction timing, not sympathetic state; no specificity, precision, or continuous false-alarm burden is established.
- **Intervention logic:** the trigger never determines actual stimulation in this study. There is no closed-loop-versus-fixed/yoked intervention comparison, safety evaluation, or evidence of therapeutic benefit.
- **Artifact vulnerability:** stimulation may add broadband high-frequency activity to the very signal being detected. The one-animal DRG illustration lacks pulse-by-pulse artifact characterization or blanking and omits transition/testing periods.
- **Generalization:** anesthetized pigs undergoing imposed obstruction are not awake humans, natural sleep apnea, or psychiatric patients. One extra multi-event animal is not cross-site/device validation.
- **Operating-point uncertainty:** the 24-second median conditions on detection; missed events and long-tail delays still matter. Parameters receive sensitivity analysis, not an independently validated task-optimal selection rule.
- **Mechanism and representation:** the pipeline combines channels of one surrogate modality; contextual physiological signals are not integrated into a validated multimodal state estimator. It identifies neither a brain network nor a controllable disease state.

### 10. What challenges or open problems remain?

Can a causal raw-signal implementation retain the replay performance after prospective baseline selection, filter delays, missing channels, motion, drift, and hardware communication are included? Can independent nerve measurements or validated multimodal labels establish what triggers mean? Which event delays, false alarms, and missed states are clinically tolerable? Can stimulation artifacts be prevented from creating a self-triggering loop?

### 11. What future work naturally follows?

1. Prospectively stream raw ECG with causal filtering and event-independent calibration; compare with the offline envelope using the same recordings and report the latency difference.
2. Validate sympathetic-state labels and report false alarms per hour, missed events, time-to-detection including failures, recovery behavior, and artifact sensitivity on held-out animals/sites/devices.
3. Prespecify a control objective and compare matched-dose closed loop, fixed stimulation, and time-shuffled/yoked triggers, with stimulation-aware sensing and safety limits.
4. Test awake human physiology and repeated sessions before translating the surrogate to psychiatric symptom tracking or treatment selection.

### 12. Why does this matter for cabbageland?

It adds a concrete observation-layer gate to adaptive intervention reasoning. A sophisticated planner cannot rescue a readout that requires future data or has not been tied to the relevant physiological state. This matters for autonomic bioelectronics, stimulation-compatible sensing, wearables, and state-conditioned psychiatry designs, but the paper itself provides no depression, hypnosis, CBT-combination, or brain-network-control evidence.

### 13. What ideas are steal-worthy?

- Specify each module's contract: raw signal → causal representation → calibrated event detector → action rule → independent outcome.
- Report in-event presence, new activation, baseline activation, persistence, and misses separately; do not collapse them into accuracy.
- Treat calibration timing and preprocessing look-ahead as model assumptions, not software footnotes.
- Distinguish changing an observation from changing the latent physiology; explicitly test actuator contamination of the observation channel.
- Keep cohort variation and repeated-event variation visible, and evaluate control separately from reconstruction or detection.

### 14. Final decision

Keep as a **useful methods and evaluation reference**. It earns reproducible offline physiological analysis and sequential replay, not causal live sensing, anatomical targeting, afferent-specific measurement, or therapeutic closed-loop efficacy. The next confidence upgrade is a prospectively calibrated, artifact-aware raw-signal implementation with independent physiological validation and a controlled intervention test.

Access record: full PMC XML acquired from https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13777941/fullTextXML . Main Methods, Results, Discussion/limitations, and figure captions were inspected. Supplementary files, raw/processed datasets, public code, archived software versions, and hardware timing were not independently audited. Artifact links: [framework](https://github.com/Shahrokh-Imperial/skna-event-driven-framework), [processed data](https://zenodo.org/records/22080173). Availability is reported by the article, not independently verified here.
