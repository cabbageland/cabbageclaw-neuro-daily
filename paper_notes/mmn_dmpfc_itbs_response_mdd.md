# Auditory mismatch-negativity predicts response to dorsomedial prefrontal intermittent theta-burst stimulation in major depressive disorder

## Basic info

* Title: Auditory mismatch-negativity predicts response to dorsomedial prefrontal intermittent theta-burst stimulation in major depressive disorder
* Authors: Marcus Anderson, Robert Bodén, Caroline E. Wass, Hatice Zora, Johan Bengtsson, Jonas Persson
* Year: 2026
* Venue / source: Journal of Affective Disorders
* Link: https://doi.org/10.1016/j.jad.2026.121908
* Date surfaced: 2026-06-05
* Why selected in one sentence: It is a rare sham-controlled depression-TMS biomarker paper where the signal is modest but legible: baseline MMN may index plasticity capacity better than static targeting folklore.

## Quick verdict

* Useful

This is worth preserving because it asks a real response-prediction question inside a randomized sham-controlled dorsomedial prefrontal cortex intermittent theta-burst stimulation trial instead of mining post-hoc associations from open-label noise. The positive signal is that larger baseline mismatch negativity predicted greater symptom improvement only in the active arm. The limiting fact is that the active-versus-sham difference between those correlations did not itself reach significance, so this is still a candidate biomarker, not a validated one.

## One-paragraph overview

The study tests whether auditory duration-deviant mismatch negativity can function as a biomarker for depression or, more interestingly, as a predictor of antidepressant response to dorsomedial prefrontal cortex intermittent theta-burst stimulation. Forty-six adults with unipolar major depressive disorder entered a double-blind sham-controlled two-week treatment study and sixty-four healthy controls provided baseline comparison data. The main result is not that mismatch negativity diagnoses depression better; it does not. The useful result is narrower: in the active stimulation group, a larger baseline mismatch negativity amplitude correlated with greater reduction in depressive symptoms, while no such relationship appeared in sham. That makes mismatch negativity potentially interesting as a cheap plasticity-capacity marker, but the paper does not yet prove that it beats sham cleanly enough to anchor clinical stratification.

## Model definition

This paper does not present a trainable predictive model. It evaluates a physiological biomarker inside a randomized clinical-trial design.

### Inputs
Baseline auditory mismatch-negativity recordings from a one-channel frontal EEG setup, baseline symptom ratings, treatment assignment to active or sham dorsomedial prefrontal cortex intermittent theta-burst stimulation, and follow-up symptom scores.

### Outputs
Mismatch-negativity amplitude at baseline and follow-up, plus the association between baseline mismatch-negativity amplitude and symptom change on MADRS-S and BPRS-affective after treatment.

### Training objective (loss)
There is no learnable model or explicit optimization loss. The core analytic question is whether baseline mismatch negativity correlates with later symptom change, especially in the active stimulation arm.

### Architecture / parameterization
A randomized double-blind sham-controlled biomarker analysis layered on top of a dorsomedial prefrontal cortex intermittent theta-burst stimulation trial. The biomarker is a duration-deviant event-related potential rather than a multivariate learned predictor.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Depression TMS still lacks credible response biomarkers. The paper asks whether a simple electrophysiological proxy for prediction-error processing and plasticity can help identify who benefits from dorsomedial prefrontal cortex intermittent theta-burst stimulation.

### 2. What is the method?
Record auditory duration-deviant mismatch negativity in patients with major depressive disorder and healthy controls, randomize patients to active or sham dorsomedial prefrontal cortex intermittent theta-burst stimulation, then test whether baseline mismatch negativity relates to subsequent symptom improvement and whether treatment changes mismatch negativity itself.

### 3. What is the method motivation?
The authors frame mismatch negativity as a plausible proxy for prediction-error processing and NMDA-receptor-linked plasticity. Since intermittent theta-burst stimulation is often explained as a plasticity-dependent intervention, baseline mismatch negativity might tag the physiological capacity that the stimulation needs in order to work.

### 4. What data does it use?
Forty-six adults aged eighteen to fifty-four with primary or recurrent unipolar major depressive disorder and sixty-four healthy controls aged eighteen to fifty-eight. Patients were randomized to active or sham treatment, with follow-up analyses using twenty-three active and twenty sham participants after exclusions. The mismatch-negativity task used twelve hundred auditory stimuli, with eighty-five percent twenty-five-millisecond standard tones and fifteen percent fifty-millisecond deviant tones, recorded from a one-channel frontal EEG setup. Treatment ran five days per week for two weeks with two sessions per day, totaling twenty-four hundred pulses per day at ninety percent resting motor threshold.

### 5. How is it evaluated?
The paper evaluates three things: baseline mismatch-negativity differences between patients and controls, change in mismatch negativity after active versus sham stimulation, and correlation between baseline mismatch negativity and later symptom change on MADRS-S and BPRS-affective.

### 6. What are the main results?
- Baseline mismatch-negativity amplitude did not differ significantly between patients and healthy controls.
- Baseline mismatch negativity did not correlate with baseline symptom severity.
- Active stimulation did not significantly change mismatch-negativity amplitude relative to sham.
- In the active group, larger baseline mismatch negativity correlated with greater symptom reduction on MADRS-S and BPRS-affective.
- In the sham group, those predictive correlations were absent.
- The active-versus-sham correlation differences trended but did not reach significance, which is the paper's most important limiting fact.

### 7. What is actually novel?
The novelty is not proving that mismatch negativity is abnormal in depression. The useful novelty is testing mismatch negativity as a response predictor inside a randomized sham-controlled dorsomedial prefrontal cortex intermittent theta-burst stimulation trial, while also showing that the biomarker itself does not simply normalize after treatment.

### 8. What are the strengths?
- The design is randomized, double blind, and sham controlled rather than open label.
- The paper asks a specific mechanistic biomarker question instead of generic correlation mining.
- Outcome is assessed with both self-report and clinician-rated affective symptom measures.
- The result is modest and interpretable rather than dressed up as triumphant precision medicine.
- Full text was accessible, so the note does not rely on abstract theater.

### 9. What are the weaknesses, limitations, or red flags?
- This is a sub-analysis with limited power, especially for the predictor comparisons that matter most.
- The key active-versus-sham difference in predictive correlation did not itself clear significance.
- The biomarker uses a one-channel EEG setup, which is clinically simple but methodologically thin.
- The treatment target was not individualized and even the targeting method changed partway through the cohort.
- Follow-up timing varied, pharmacotherapy was heterogeneous, and patients remained on medication.
- The study does not show that mismatch negativity changes with treatment, only that baseline amplitude may tag who improves.

### 10. What challenges or open problems remain?
The obvious challenge is replication in a larger cohort that is powered to test whether the predictor truly differs between active and sham treatment. Another is determining whether mismatch negativity adds anything beyond clinical covariates, connectivity measures, or more direct plasticity assays. The field also still needs to know whether such a biomarker generalizes beyond this dorsomedial prefrontal cortex protocol.

### 11. What future work naturally follows?
Run a prospectively powered stratification study, compare mismatch negativity against static targeting metrics and multimodal predictors, individualize treatment targets, and test whether combining a cheap physiological biomarker with structural or functional circuit information produces a stronger response model.

### 12. Why does this matter for cabbageland?
Because it shifts the depression-stimulation conversation from site folklore toward state and plasticity capacity, but without pretending the problem is solved. That is exactly the kind of modest but useful paper worth keeping: it points toward a more serious precision stack while exposing how far the field still is from having one.

### 13. What ideas are steal-worthy?
- Treat response prediction as a question about plasticity capacity, not only target location.
- Benchmark candidate biomarkers against sham, not just against symptom change within an active arm.
- Use cheap physiological assays as filters, then ask whether they add value over anatomy, connectivity, and clinical heterogeneity.
- Separate predictor value from mechanistic-change claims: a useful baseline biomarker does not have to be the same thing that changes after treatment.

### 14. Final decision
Preserve as a cautious biomarker note. The paper does not validate mismatch negativity as a deployable clinical predictor, but it is a sharper and more honest step toward that goal than most precision-TMS rhetoric.
