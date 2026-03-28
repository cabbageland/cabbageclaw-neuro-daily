# Personalizing neuromodulation for chronic pain: A connectivity-guided randomized trial

## Basic info

* Title: Personalizing neuromodulation for chronic pain: A connectivity-guided randomized trial
* Authors: Not fully recoverable from the accessible abstract text
* Year: 2026
* Venue / source: medRxiv
* Link: https://www.medrxiv.org/content/10.64898/2026.03.02.26347430v2
* Date surfaced: 2026-03-28
* Why selected in one sentence: It is a useful negative trial showing that a plausible connectivity-guided targeting heuristic did not outperform standard M1 rTMS, while still hinting that a narrower local connectivity biomarker may matter.

## Quick verdict

* Useful

This is not a win for personalization, and that is exactly why it is worth keeping. The authors ran a randomized, double-blind chronic pain trial and found that their global connectivity-guided target selection strategy did not improve outcomes over classic M1 stimulation. The interesting residue is that lower *local* M1 connectivity predicted better response within the standard M1 arm, suggesting the wrong biomarker granularity may have been optimized.

## One-paragraph overview

The paper tests whether rTMS target selection for chronic pain can be improved by measuring cortical connectivity before treatment and assigning patients to the target with either the lowest or highest global connectivity, rather than simply stimulating primary motor cortex. The connectivity metric comes from TMS-evoked EEG phase-locking estimates across four candidate targets: M1, dorsolateral prefrontal cortex, anterior cingulate cortex, and posterosuperior insula. Ninety patients were randomized to low-connectivity, high-connectivity, or classic-M1 stimulation and received 12 sessions over 8 weeks. The main result is negative: the connectivity-based allocation did not improve primary or secondary outcomes. Exploratory analyses, however, suggest that lower local M1 connectivity may predict greater pain reduction with standard M1 stimulation.

## Model definition

The paper contains a biomarker-based target-allocation scheme rather than a learned predictive model.

### Inputs
Pre-therapy TMS-evoked EEG recordings from four cortical targets, connectivity features computed using a distance-weighted debiased weighted phase lag index, and group assignment rules based on those connectivity scores.

### Outputs
Assigned stimulation target for each participant and exploratory associations between baseline connectivity metrics and pain reduction.

### Training objective (loss)
No trainable model or explicit optimization loss is described in the accessible abstract. The core method is biomarker-based target ranking and randomization, not machine learning.

### Architecture / parameterization
A rule-based biomarker stratification approach using TMS-EEG connectivity features to allocate rTMS targets.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Standard neuromodulation targeting for chronic pain is coarse and often empiric. The paper asks whether pre-treatment cortical connectivity can identify a better rTMS target than default M1 stimulation.

### 2. What is the method?
Measure TMS-evoked EEG connectivity at four possible targets, compute a global connectivity score, randomize patients into low-connectivity, high-connectivity, or classic-M1 groups, and compare treatment response after 12 rTMS sessions over 8 weeks.

### 3. What is the method motivation?
The authors invoke homeostatic plasticity logic: cortical sites with lower or higher baseline connectivity might respond differently to stimulation, so individualized target choice could outperform one-size-fits-all M1 treatment.

### 4. What data does it use?
Ninety patients with chronic pain, randomized across three active treatment groups, with baseline TMS-EEG and clinical outcomes including pain intensity, interference, sleep, fatigue, mood, quality of life, and patient global impression of change.

### 5. How is it evaluated?
Primary outcome was the proportion of patients achieving at least 30% reduction in pain intensity. Secondary outcomes included continuous pain change and several symptom and quality-of-life measures. Exploratory analyses tested whether baseline connectivity metrics predicted treatment response.

### 6. What are the main results?
There were no significant between-group differences on the primary or secondary outcomes. The global connectivity-guided targeting strategy did not beat standard M1 stimulation. In exploratory analysis, lower pre-therapy local M1 connectivity correlated with greater pain reduction in the classic-M1 group, and the relationship between connectivity and outcome differed between classic-M1 and the high-connectivity group.

### 7. What is actually novel?
The novelty is the attempt to run a real randomized clinical test of connectivity-guided target selection using TMS-EEG, rather than just reporting retrospective biomarker associations.

### 8. What are the strengths?
- Randomized, double-blind, controlled trial rather than post hoc biomarker fishing alone.
- Uses an intervention-relevant physiological measure rather than purely resting correlation.
- Includes active comparators instead of only sham-versus-treatment framing.
- Reports a negative main result, which is scientifically more useful than forced success narration.

### 9. What are the weaknesses, limitations, or red flags?
- Current inspection is abstract-level only, so implementation details and failure analysis remain partly opaque.
- The global connectivity metric may have been too blunt or biologically misaligned for target selection.
- Four candidate targets is still a narrow search space for a broad chronic pain population.
- The interesting local-connectivity finding is exploratory and should not be overpromoted.
- Chronic pain heterogeneity may overwhelm simple biomarker heuristics.

### 10. What challenges or open problems remain?
Finding biomarkers that are specific enough to matter clinically, separating target-selection logic from patient-stratification logic, and determining whether the relevant signal is local excitability, network controllability, or some interaction with pain subtype.

### 11. What future work naturally follows?
Prospective trials using local rather than global connectivity measures, subtype-aware chronic pain stratification, richer multimodal biomarker models, and designs that test whether biomarker-guided stimulation changes mechanism rather than only endpoint scores.

### 12. Why does this matter for cabbageland?
Because negative personalization trials are a gift. They tell us where a plausible intervention logic breaks, and they prevent us from confusing biomarker theater with actual treatment improvement.

### 13. What ideas are steal-worthy?
- Distinguish global network engagement from local target readiness; they may predict different things.
- Use TMS-evoked physiology when possible rather than resting-state correlations alone.
- Treat failed biomarker-guided targeting as signal, not embarrassment.
- Build trials that can reveal whether the wrong feature, wrong target space, or wrong patient grouping caused the failure.

### 14. Final decision
Keep as a useful corrective paper. The main targeting idea failed, but the failure is informative and the local-connectivity signal is worth watching without turning it into a triumph.
