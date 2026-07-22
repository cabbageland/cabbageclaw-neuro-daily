# Anterior default mode brain state dynamics predict depressive symptom severity before and during TMS treatment

## Basic info

* Title: Anterior default mode brain state dynamics predict depressive symptom severity before and during TMS treatment
* Authors: Carina Forster, Chetan Gohil, Bjorn Burgher, Ilya Kuzovkin, Mats W. J. van Es, Mark Woolrich, Diego Vidaurre, Martijn P. van den Heuvel, Cameron Higgins, Luca Cocchi
* Year: 2026
* Venue / source: bioRxiv preprint
* Link: https://doi.org/10.64898/2026.05.27.728312
* Date surfaced: 2026-07-22
* Why selected in one sentence: It tracks how actual TMS sessions perturb default-mode state dynamics across treatment instead of settling for a single before-versus-after snapshot.

## Quick verdict

* Highly relevant

This is a strong keep with a caution sticker attached. The dataset is larger and more treatment-real than most TMS-EEG mechanism papers, and the longitudinal design is exactly the right instinct. The main catch is that the treatment-response associations are reported with uncorrected p-values and remain correlational, so this is useful state-tracking evidence, not a settled response biomarker.

## One-paragraph overview

The paper follows 70 people with treatment-resistant depression through fMRI-personalized, robotically delivered intermittent theta-burst stimulation to the left dorsolateral prefrontal cortex, with resting EEG collected immediately before and after Sessions 1, 11, and 20. The authors fit a time-delay embedded hidden Markov model to derive ten recurring brain states and then ask how state occupancy, transitions, and longer cycle dynamics relate to symptom severity and later improvement. The core picture is interesting. At baseline, worse depression is associated with less anterior default-mode engagement, more posterior default-mode engagement, fewer transitions into anterior default-mode and attention states, and slower cyclical brain-state dynamics. Then, at mid-treatment, acute post-TMS changes in those state dynamics predict later symptom improvement, especially reduced anterior default-mode occupancy and stronger transitions into anterior default-mode and attention states. The most useful lesson is that the acute response to a treatment session halfway through the course may be more informative than the usual static baseline marker.

## Model definition

### Inputs
Resting-state EEG recorded immediately before and after selected TMS sessions, longitudinal depressive-symptom ratings using the HADS-D, demographic covariates, and the treatment schedule of repeated personalized left-DLPFC intermittent theta-burst stimulation sessions.

### Outputs
Ten recurrent brain states, their fractional occupancies, state-transition probabilities, low-dimensional transition components, cycle-rate estimates, and regression-based predictions of current or later symptom severity.

### Training objective (loss)
The central model is an embedded hidden Markov model fit to EEG time series to infer latent brain states and their transitions. The accessible paper text does not provide a compact machine-learning style loss expression, but the downstream analyses are regression-based rather than predictive deep learning.

### Architecture / parameterization
A time-delay embedded hidden Markov model with ten latent brain states, followed by analyses of fractional occupancy, Markov transition matrices, principal-component summaries of transition structure, and cycle dynamics across treatment.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve a major blind spot in depression TMS studies: we often know symptom scores before and after a course, but not how brain dynamics move during the course or which acute within-session changes actually foreshadow later improvement.

### 2. What is the method?
The method combines repeated pre- and post-session EEG recordings with a hidden-Markov-state model of large-scale brain dynamics, then relates state occupancy, transition structure, and cycle rate to baseline severity and later symptom change across the treatment course.

### 3. What is the method motivation?
If TMS works by gradually reconfiguring large-scale circuits rather than only by producing a fixed immediate effect, then time-resolved brain-state dynamics should carry more signal than a single pre-treatment biomarker snapshot.

### 4. What data does it use?
Seventy participants with treatment-resistant depression underwent 20 to 30 weekday sessions of fMRI-personalized, robotically delivered intermittent theta-burst stimulation to the left DLPFC. Resting EEG was collected immediately before and after Sessions 1, 11, and 20, and depressive symptoms were measured weekly with the HADS-D.

### 5. How is it evaluated?
The authors test whether baseline state properties predict baseline severity, whether acute pre-to-post-TMS changes predict later symptom scores, and whether occupancy, transitions, and cycle-rate summaries explain meaningful variance after adjusting for age, gender, and earlier symptom levels.

### 6. What are the main results?
- Greater baseline severity is associated with more time in a posterior default-mode state and less time in an anterior default-mode state.
- Greater baseline severity is also associated with fewer transitions into the anterior default-mode state and an attention-related state.
- Brain-state activity shows structured cyclical organization, and slower cycle rates are linked to higher baseline severity.
- Acute Session 1 state changes do not significantly predict mid-treatment symptoms.
- Acute Session 11 reductions in anterior default-mode occupancy predict lower symptom severity by Session 20, with model R2 around 0.65 and an uncorrected p-value of 0.010.
- Acute Session 11 changes in a transition component loading on anterior default-mode and attention-state transitions also predict later improvement, again with uncorrected statistics.

### 7. What is actually novel?
The novelty is not that the default mode network matters in depression. The useful novelty is the repeated within-treatment state-dynamics measurement and the claim that mid-course acute TMS reconfiguration may carry response information that static baseline summaries miss.

### 8. What are the strengths?
- The longitudinal repeated-measures design is far better than a simple before-versus-after study.
- Seventy treatment-resistant participants is a decent sample for this kind of TMS-EEG work.
- The stimulation protocol is clinically realistic and personalized rather than toy stimulation in healthy volunteers.
- The paper studies occupancy, transitions, and cycle dynamics instead of collapsing everything into power differences.
- The distinction between baseline severity markers and mid-treatment change markers is conceptually useful.

### 9. What are the weaknesses, limitations, or red flags?
- The response-prediction results are reported with uncorrected p-values, which matters.
- The model remains correlational, so it does not show that these state changes are the mechanism of recovery.
- The interpretation of the anterior default-mode signal is tricky and somewhat counterintuitive: low baseline occupancy tracks worse symptoms, yet further mid-treatment post-TMS reductions predict later improvement.
- Symptoms are measured with self-report rather than richer clinician-rated or multimodal outcome stacks.
- The brain-state labels remain inferential summaries of EEG dynamics rather than directly validated circuit states.

### 10. What challenges or open problems remain?
The field still needs out-of-sample replication, corrected inference, richer outcome targets, and a clearer mapping from these EEG-defined states to stimulation timing, target selection, or dosing decisions. It also remains unclear whether the same effects appear across different protocols, sites, and depression subtypes.

### 11. What future work naturally follows?
Test whether mid-treatment state perturbation profiles can guide adaptive retargeting or dose adjustment, pair this design with TMS-EEG evoked-response modeling, replicate in accelerated or alternative stimulation protocols, and examine whether similar default-mode reconfiguration logic appears in psychotherapy or ketamine courses.

### 12. Why does this matter for cabbageland?
Because it suggests that response-relevant brain dynamics may reveal themselves during treatment rather than only before it. That is exactly the kind of logic you would want if you care about adaptive intervention, state tracking, and not flying blind through a full stimulation course.

### 13. What ideas are steal-worthy?
- Sample the brain repeatedly during treatment instead of only before and after.
- Treat acute mid-course perturbation responses as candidate biomarkers of later response.
- Separate occupancy, transition structure, and cycle rate rather than pretending one summary statistic captures state dynamics.
- Take the baseline-versus-recovery dissociation seriously instead of forcing one network into one psychological label.

### 14. Final decision
Preserve, but keep the caution attached. The paper is more useful than most TMS response-biomarker pieces because the longitudinal state-dynamics design is strong, but the uncorrected statistics and interpretive ambiguity mean this is a promising mechanism clue, not a locked-down biomarker.
