# Gamma and beta power and the 1/f slope vary across a spectrum of depression severity

## Basic info

* Title: Gamma and beta power and the 1/f slope vary across a spectrum of depression severity
* Authors: Juliet Hosler, James Coxon, Joshua Hendrikse
* Year: 2026
* Venue / source: Translational Psychiatry
* Link: https://doi.org/10.1038/s41398-026-04268-z
* Date surfaced: 2026-07-17
* Why selected in one sentence: It asks a better biomarker question than most depression EEG papers by testing whether periodic and aperiodic features scale with symptom severity instead of hiding inside a simple case-versus-control contrast.

## Quick verdict

* Useful

This is a calibration paper, not a turnkey precision-psychiatry tool. It matters because it forces depression EEG biomarker logic to pass a severity-continuum test across two open datasets, which is more informative than another binary diagnosis contrast. The main caveat is that the replication signal is not cleanly one-to-one: gamma and 1/f offset are strongest in the larger heterogeneous cohort, while beta is the sturdier effect in the cleaner young-adult cohort.

## One-paragraph overview

The paper analyzes resting-state EEG from two open datasets to ask whether high-frequency spectral power and aperiodic structure vary systematically with depression symptom burden. In the larger TDBRAIN cohort, the authors report higher gamma power and higher 1/f offset with more severe depression symptoms, especially when severe cases are compared with moderate cases. In the second Cavanagh cohort, the stronger replicated effect shifts toward beta power rather than gamma, while 1/f findings weaken. The useful takeaway is not that the field now has a settled EEG biomarker for depression severity. The useful takeaway is that severity-graded analysis exposes which candidate signals survive heterogeneity and which ones start wobbling when the cohort changes.

## Model definition

### Inputs
Resting-state EEG recordings from two open datasets, plus Beck Depression Inventory II scores. Dataset 1 used 26-channel eyes-open resting EEG from the TDBRAIN archive, with 181 eligible participants and 173 retained after preprocessing exclusions. Dataset 2 used higher-density 60-channel resting EEG from the Cavanagh open dataset, with 116 eligible participants and 113 retained after preprocessing exclusions.

### Outputs
Band-limited spectral power estimates for low beta, high beta, low gamma, and high gamma, plus aperiodic 1/f exponent and offset estimates. The paper also outputs cluster-based permutation statistics for correlations with BDI scores and group differences across depression-severity strata.

### Training objective (loss)
There is no trainable predictive model here. The inferential objective is statistical association testing: cluster-based permutation Spearman correlations between EEG features and BDI scores, plus cluster-based permutation independent-samples t-tests between severity groups.

### Architecture / parameterization
This is a signal-processing and statistical-analysis pipeline rather than a learned model. EEG was preprocessed with RELAX, spectral power was estimated with Welch power spectral density, aperiodic parameters were fit with specparam, and topographic effects were tested with FieldTrip cluster-based permutation analyses.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Most depression EEG biomarker papers ask a lazy question: do depressed people differ from healthy controls? That design says little about whether the signal scales with actual symptom burden or is useful for stratification. This paper tries to test whether periodic and aperiodic EEG features vary across a severity continuum instead.

### 2. What is the method?
The authors preprocess resting-state EEG from two open datasets, estimate beta and gamma power plus 1/f exponent and offset, and run topographic cluster-based permutation tests against BDI symptom scores and severity-group contrasts. They then check whether the main patterns hold in a second independent dataset with cleaner sampling and denser EEG.

### 3. What is the method motivation?
If EEG is going to matter for precision psychiatry, it should not only separate broad diagnostic bins. It should track clinically relevant variation inside depression severity and remain at least partly stable when the cohort, recording density, and sampling strategy change.

### 4. What data does it use?
Dataset 1 is the TDBRAIN archive, an open Brainclinics resting-state EEG dataset collected from 2001 to 2021. The current analysis used eyes-open resting EEG and BDI-II scores from 181 eligible participants, with 173 retained after noise exclusions. The cohort is heterogeneous, includes multiple mental-health diagnoses, and includes recent medication use in some participants. Dataset 2 is the Cavanagh open dataset from OpenNeuro, with 60-channel resting EEG and BDI-II scores from 116 eligible young adults, 113 after exclusions, split more cleanly between very low and moderate-to-severe symptom groups.

### 5. How is it evaluated?
Evaluation is statistical rather than predictive. The paper tests whether EEG features differ between severity groups and whether they correlate with BDI scores across the sample. It also runs control analyses excluding recent drug and alcohol use and removing the aperiodic component from the spectral signal to see whether the main relationships survive.

### 6. What are the main results?
In TDBRAIN, severe symptoms relative to moderate symptoms are associated with higher low gamma and high gamma power, and low gamma also shows a positive correlation with BDI scores. The 1/f offset is higher in severe relative to moderate depression and correlates positively with BDI. Beta trends upward with severity in TDBRAIN but does not survive correction. In the Cavanagh dataset, gamma does not replicate cleanly, but low beta is higher in depression versus controls and both low and high beta show corrected positive correlations with BDI. The 1/f exponent and offset do not show strong corrected replication effects there. The net result is that high-frequency EEG markers do vary with symptom burden, but the specific winning feature depends on cohort.

### 7. What is actually novel?
The novelty is not a fancy model. The useful novelty is forcing depression EEG biomarkers through a severity-continuum design and combining periodic with aperiodic features in that frame. That is a better question than another diagnosis-versus-control paper, even though the answer is messier than the field would like.

### 8. What are the strengths?
The paper uses two independent open datasets instead of one convenience sample. It explicitly separates periodic power from aperiodic structure rather than treating high-frequency EEG as one undifferentiated object. It uses cluster-based permutation testing rather than noisy electrode-by-electrode fishing. And it includes control analyses for recent substance use and for the aperiodic component.

### 9. What are the weaknesses, limitations, or red flags?
The main dataset is diagnostically messy, includes recent medication exposure, and uses a relatively low-density 26-channel montage. The second dataset is cleaner but much younger and sampled differently, so replication becomes partly a cohort-shift problem. The study is cross-sectional and uses self-reported symptom severity rather than treatment response or longitudinal change. The gamma and 1/f offset signals may partly reflect the same underlying broadband process rather than two cleanly separable biomarkers. Most importantly, nothing here shows that these markers improve targeting, treatment selection, or prognosis in a real intervention workflow.

### 10. What challenges or open problems remain?
The field still needs to determine which EEG component is actually stable enough to carry across age, medication history, comorbidity, chronicity, and recording setup. It also needs to show whether severity-related signals are distinct from signals of arousal, chronicity, or treatment exposure, and whether they help with prediction instead of just description.

### 11. What future work naturally follows?
The obvious next step is to test these periodic and aperiodic features in longitudinal treatment datasets, ideally alongside rTMS, medication, psychotherapy, or hybrid-care interventions. Another useful next step would be to model symptom dimensions and treatment sensitivity directly rather than relying only on total BDI score buckets. A third step is to ask whether gamma, beta, and 1/f terms each contribute unique predictive value or mostly collapse onto one shared excitability-related signal.

### 12. Why does this matter for cabbageland?
Because cabbageland cares about biomarkers that might eventually matter for intervention logic, not just for decorative diagnosis papers. This study does not solve that problem, but it does sharpen the screening criterion: any serious depression EEG biomarker should be tested across heterogeneous severity, should survive cohort shifts, and should explain what part of the signal is actually unique versus redundant.

### 13. What ideas are steal-worthy?
One steal-worthy move is to force candidate biomarkers through a severity-continuum design before treating them as intervention tools. Another is to evaluate periodic and aperiodic EEG components together, then explicitly test whether they provide unique information or just rephrase the same physiology. A third is to use a large messy archive for discovery and a cleaner higher-density cohort for stress-testing, instead of pretending one dataset is enough.

### 14. Final decision
Keep as a useful biomarker-calibration note. It is not strong enough to anchor a treatment pipeline by itself, but it improves how future depression EEG markers should be judged.
