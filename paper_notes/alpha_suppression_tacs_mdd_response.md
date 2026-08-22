# Suppression of endogenous alpha power predicts clinical response to 10 Hz tACS in major depressive disorder: A double-blind randomized controlled trial

## Basic info

* Title: Suppression of endogenous alpha power predicts clinical response to 10 Hz tACS in major depressive disorder: A double-blind randomized controlled trial
* Authors: Tobias Schwippel, Francesca Pupillo, Hadden LaGarde, Athena Stein, Mengsen Zhang, David R. Rubinow, Flavio Frohlich
* Year: 2026
* Venue / source: Brain Stimulation
* Link: https://doi.org/10.1016/j.brs.2026.103131
* Date surfaced: 2026-08-22
* Why selected in one sentence: It separates a clinically relevant target-engagement story from a merely decorative fixed-frequency stimulation story by showing that symptom improvement tracks suppression of endogenous alpha power at individual alpha frequency rather than generic 10 Hz power change.

## Quick verdict

* Highly relevant

This is a real keep because it asks a better question than most depression stimulation trials. The useful result is not that fixed 10 Hz transcranial alternating current stimulation obviously beats sham on raw symptoms. It is that the active condition shows a specific link between suppression of endogenous alpha power at each person's individual alpha frequency and later antidepressant improvement, while power at the stimulation frequency itself is less clinically informative. The study is small and clinically underpowered, but it is one of the cleaner recent examples of a neuromodulation paper trying to connect protocol, physiology, and outcome in the same frame.

## One-paragraph overview

The paper reports a double-blind randomized sham-controlled trial in 20 adults with major depressive disorder who received five consecutive days of bifrontal-central 10 Hz transcranial alternating current stimulation or sham, with 128-channel resting EEG recorded before treatment on Day 1, before treatment on Day 5, and again at two-week follow-up. Group-level symptom improvement was not a clean knockout: Hamilton Depression Rating Scale scores improved over time in both groups, with numerically larger reductions in the active arm but no significant time-by-condition interaction, and response or remission rates did not differ. The more interesting result is mechanistic. Within the active condition, greater reductions in alpha power at each participant's individual alpha frequency, both early in the intervention week and by follow-up, predicted larger later HDRS improvement, whereas analogous correlations for power at the applied 10 Hz stimulation frequency did not. A separate whole-head analysis found a delayed posterior cluster of reduced 10 Hz power at follow-up in the active group. The paper therefore matters less as a clinical efficacy win than as a target-engagement note: fixed-frequency stimulation may still work through how well it perturbs the endogenous alpha system, not through the nominal stimulation frequency alone.

## Model definition

This is primarily a randomized stimulation trial with repeated electrophysiology rather than a trainable predictive-model paper.

### Inputs
Adults with major depressive disorder randomized to active or sham stimulation, repeated resting-state 128-channel EEG recordings, and clinical ratings including HDRS-17, BDI-II, IDAS, and rumination measures.

### Outputs
Clinical symptom changes across Day 1, Day 5, and two-week follow-up; alpha power spectral density at 10 Hz and at each participant's individual alpha frequency; topographical EEG change maps; and correlations between electrophysiological change and symptom improvement.

### Training objective (loss)
There is no trainable model with an explicit optimization loss. The core analyses are randomized-group comparisons, nonparametric correlations, repeated-measures clinical models, and topographical cluster tests.

### Architecture / parameterization
Five daily sessions of 10 Hz tACS delivered with two 5 by 5 centimeter electrodes over F3 and F4 and one 5 by 7 centimeter return electrode at Cz, using 2 mA zero-to-peak stimulation with 40-minute sessions in a double-blind sham-controlled parallel design.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve a mechanism problem inside a treatment problem. tACS for depression has been clinically interesting for a while, but it remains unclear whether the relevant physiological target is power change at the applied stimulation frequency or modulation of the brain's own endogenous alpha rhythm. The paper asks whether repeated 10 Hz stimulation in major depressive disorder actually engages depression-relevant alpha dynamics in a way that relates to later clinical improvement.

### 2. What is the method?
The authors ran a randomized, sham-controlled, double-blind parallel trial with 20 adults meeting criteria for unipolar non-psychotic major depressive disorder. Participants received five consecutive daily sessions of active 10 Hz tACS or active sham. Resting-state eyes-open high-density EEG was recorded before stimulation on Day 1, before stimulation on Day 5, and again at two-week follow-up. The authors quantified alpha power spectral density both at the nominal 10 Hz stimulation frequency and at each participant's daily individual alpha frequency, first in prefrontal regions of interest and then across the whole scalp, and related those changes to symptom improvement on the HDRS-17.

### 3. What is the method motivation?
The motivation is that fixed-frequency stimulation is not automatically the right control variable. If depression-relevant brain dynamics depend on a person's endogenous alpha system, then a nominal 10 Hz protocol might only help when it actually perturbs that intrinsic rhythm. The paper therefore tries to separate stimulation-frequency effects from endogenous-alpha engagement and to ask which one better tracks outcome.

### 4. What data does it use?
The main dataset is a 20-person randomized depression trial conducted at UNC between 2021 and 2023. Ten participants were assigned to active tACS and ten to sham, with one active participant lost to follow-up. EEG was recorded with a 128-channel system at 1000 Hz before preprocessing. Clinical outcomes included clinician-rated HDRS-17, BDI-II, IDAS subscales, rumination, and related questionnaires, although some self-report measures had partial data loss for early participants because of a storage failure.

### 5. How is it evaluated?
Evaluation happens at several layers. Clinically, the paper tests time and condition effects on depression ratings and compares response and remission proportions. Electrophysiologically, it tests prefrontal alpha power changes at 10 Hz and at individual alpha frequency over the intervention week and over follow-up. Mechanistically, it asks whether those EEG changes correlate with later symptom improvement, both in predefined prefrontal regions and in whole-head channel-wise analyses with multiple-comparison control.

### 6. What are the main results?
- The cleanest group-level clinical result is modest: both groups improved over time, with no significant time-by-condition interaction for HDRS-17 or BDI-II.
- At follow-up, HDRS-17 reduction was numerically larger in the active group by about 2.2 points, but response and remission rates did not differ from sham.
- In prefrontal ROI analyses, there were no significant between-group differences in alpha power change at either 10 Hz or individual alpha frequency, except for a trend-level right-prefrontal 10 Hz reduction favoring active stimulation.
- In the active group only, greater decreases in prefrontal individual-alpha-frequency power from Day 1 to follow-up were associated with larger HDRS improvement, and early IAF suppression during the intervention week also predicted later follow-up improvement.
- Equivalent correlations using 10 Hz power were not significant, which is the paper's most useful dissociation.
- Whole-head analyses found a significant posterior-occipital and central cluster of reduced 10 Hz power at follow-up in the active group relative to sham, and widespread frontal-central and parietal correlations between IAF suppression and symptom improvement within the active arm.

### 7. What is actually novel?
The useful novelty is not simply that the study combines tACS and EEG. The sharper move is distinguishing stimulation-frequency power change from endogenous-alpha-frequency power change inside the same randomized trial, then showing that the clinically relevant association lives with the endogenous rhythm rather than the nominal 10 Hz label. That is a better mechanistic standard than the usual "10 Hz protocol changed something and symptoms drifted downward" story.

### 8. What are the strengths?
- The study is randomized, sham-controlled, and double-blind rather than open-label stimulation theater.
- It uses repeated high-density EEG rather than a single before-and-after clinical endpoint.
- The analysis separates 10 Hz power from individual alpha frequency power instead of treating them as interchangeable.
- Blinding and tolerability were explicitly checked, and neither obviously collapsed.
- The results are conservative enough to be more trustworthy: the authors do not pretend to have a decisive clinical superiority signal when they mostly have a target-engagement signal.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is very small, which limits clinical power and makes the strong within-group correlations vulnerable to inflation.
- Response and remission rates did not differ from sham, so the paper does not earn a broad efficacy claim.
- Baseline differences in depressive episode duration and psychotherapy exposure could have influenced clinical trajectories.
- EEG inference remains sensor-space and therefore anatomically indirect because of volume conduction.
- The protocol uses a fixed 10 Hz bifrontal-central montage, so the paper cannot tell us whether individualized frequency or different targeting would work better.
- Follow-up only extends two weeks, which is too short to say much about durability.
- Full published journal body text was not cleanly accessible in this environment; this note relies on full-text inspection of the open medRxiv preprint plus cross-check against the final PubMed abstract and citation metadata.

### 10. What challenges or open problems remain?
The biggest open problem is causal specificity. Does IAF suppression mark the useful mechanism, or is it only a correlate of some broader network shift? It also remains unclear which patients are most likely to show this physiology, whether individualized frequency or state-triggered delivery can strengthen it, and whether the delayed posterior 10 Hz effect and the clinically relevant IAF effect are two parts of one process or partially separate phenomena.

### 11. What future work naturally follows?
The obvious next step is a larger adequately powered sham-controlled trial that prospectively stratifies or adapts stimulation by individual alpha features rather than applying fixed 10 Hz to everybody. It would also help to combine EEG with fMRI or another network-level measure to test the paper's DMN and frontoparietal-control interpretation more directly. State-dependent or closed-loop delivery would be a natural follow-on because the paper itself points toward endogenous rhythm engagement rather than blind fixed-frequency dosing.

### 12. Why does this matter for cabbageland?
It matters because it sharpens how we should think about precision neuromodulation. The paper suggests that a protocol parameter such as "10 Hz" may be less important than whether stimulation successfully perturbs a biologically meaningful latent rhythm in a given person. That is exactly the kind of distinction that matters for adaptive stimulation logic, biomarker framing, and skepticism toward simplistic personalization claims.

### 13. What ideas are steal-worthy?
- Treat the endogenous rhythm, not just the applied waveform, as the candidate control variable.
- Use dissociations between stimulation-frequency effects and intrinsic-frequency effects to test target engagement more seriously.
- Accept that clinically useful physiology may appear first as a within-active-condition mechanistic relation before it shows up as a clean between-group symptom difference.
- Pair modest clinical claims with sharper physiological ones instead of inflating the symptom story.

### 14. Final decision
Preserve as a highly relevant mechanistic clinical note. The study is too small to settle antidepressant efficacy, but it does real work on the more interesting question of what kind of alpha modulation actually deserves to count as target engagement in depression tACS.
