# Connectivity-guided accelerated theta burst stimulation as augmentation for inpatient treatment-resistant depression: a randomized, double-blind, sham-controlled trial

## Basic info

* Title: Connectivity-guided accelerated theta burst stimulation as augmentation for inpatient treatment-resistant depression: a randomized, double-blind, sham-controlled trial
* Authors: Christina Muller, Marc Onken, Andrea Hildebrandt, Maximilian Kiebs, Andrew Zalesky, Robin F. H. Cash, Dirk Scheele, Rene Hurlemann
* Year: 2026
* Venue / source: medRxiv preprint
* Link: https://doi.org/10.64898/2026.06.25.26356553
* Date surfaced: 2026-08-09
* Why selected in one sentence: It is one of the more useful recent depression TMS papers because it tests individualized connectivity-guided accelerated iTBS under sham control inside messy real inpatient TRD care rather than in a cleaner demonstration setting.

## Quick verdict

* Highly relevant

This is a real keep because it asks the right translational question. Instead of treating precision targeting as a geometry exercise in a curated outpatient sample, the paper asks whether a connectivity-guided accelerated protocol still adds antidepressant signal once it is embedded in multimodal inpatient care for clinically ugly treatment-resistant depression. The main caution is that the protocol is bundled and the durability story is modest, so it does not prove that connectivity-guided targeting itself was the decisive ingredient.

## One-paragraph overview

The paper reports a randomized, double-blind, sham-controlled trial of accelerated intermittent theta-burst stimulation as an inpatient augmentation treatment for unipolar treatment-resistant depression. Participants underwent structural and resting-state MRI, and the active or sham target was individualized as the left dorsolateral prefrontal cluster showing strongest functional anticorrelation with the subgenual anterior cingulate cortex. Treatment was delivered at 90 percent of resting motor threshold as three daily sessions across ten weekdays, for thirty sessions and 54,000 total pulses, on top of routine multidisciplinary inpatient care. Of 57 randomized patients, 51 completed treatment and 44 contributed six-week follow-up data. Active treatment produced steeper clinician-rated MADRS improvement than sham, with a model-estimated 12.06-point versus 4.98-point reduction during the acute window and higher MADRS response rates, while self-report BDI-II trajectories also favored active treatment but with a smaller effect. The paper matters because it turns precision TMS into a deployment question rather than a branding exercise.

## Model definition

This paper does not train a predictive response model. The relevant model-like machinery is the rule-based connectivity-guided target-selection procedure plus the longitudinal statistical models used to estimate treatment effects over time.

### Inputs
Structural MRI, resting-state fMRI used to identify the left dorsolateral prefrontal cortex cluster with strongest functional anticorrelation to the subgenual anterior cingulate cortex, active versus sham treatment assignment, repeated MADRS and BDI-II symptom measurements, and baseline clinical covariates including chronicity and treatment-resistance severity.

### Outputs
Individualized stimulation targets, clinician-rated and self-reported depression trajectories across the acute treatment phase, exploratory response and remission rates, and follow-up symptom trajectories.

### Training objective (loss)
There is no trainable machine-learning loss in the paper itself. The targeting rule selects the site with strongest negative functional connectivity to the subgenual anterior cingulate cortex, while the outcome analyses use latent growth and mixed-effects models to estimate group-by-time treatment effects.

### Architecture / parameterization
A rule-based individualized targeting pipeline followed by a randomized, double-blind, sham-controlled accelerated iTBS trial. The main inferential stack uses latent growth modeling for weekly MADRS change and random-intercept linear mixed models for daily BDI-II change.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Standard repetitive transcranial magnetic stimulation protocols are awkward fits for inpatient psychiatry because they usually require daily treatment over several weeks, while the cleaner sham-controlled evidence base is dominated by outpatient samples. The paper tries to solve a more practical problem: can a connectivity-guided accelerated iTBS protocol produce real add-on antidepressant benefit inside routine inpatient care for hard treatment-resistant depression?

### 2. What is the method?
Run a randomized, double-blind, sham-controlled inpatient trial in adults with unipolar treatment-resistant depression. Use resting-state fMRI to select an individualized left dorsolateral prefrontal target showing maximal anticorrelation with the subgenual anterior cingulate cortex. Deliver active or sham iTBS at 90 percent of resting motor threshold as three daily sessions over ten weekdays, then compare clinician-rated and self-reported symptom trajectories.

### 3. What is the method motivation?
There are two motivations. First, accelerated schedules may fit inpatient workflows better than classic four-to-six-week protocols. Second, if connectivity-guided targeting really improves antidepressant efficacy, it should be tested in a clinically realistic environment rather than only in cleaner demonstration settings.

### 4. What data does it use?
The trial randomized 57 adults with unipolar treatment-resistant depression and analyzed 51 treatment completers, with 44 participants available at six-week follow-up. This was a clinically complex cohort: average illness duration 12.5 years, average current episode duration 4.2 years, more than six failed antidepressant trials on average, Maudsley Staging Method scores around 10.9, and psychiatric comorbidity in 82 percent of participants. The data include MRI-based targets, weekly MADRS ratings, daily BDI-II scores during the stimulation phase, medication and ward-treatment context, and follow-up assessments.

### 5. How is it evaluated?
The primary outcome is change in MADRS across the acute treatment window, modeled with latent growth models. The secondary outcome is change in BDI-II across daily assessments, modeled with linear mixed effects after the preregistered latent growth approach fit poorly. The paper also reports exploratory response and remission rates, follow-up trajectory analyses, blinding checks, and safety/tolerability comparisons.

### 6. What are the main results?
- Active treatment produced steeper clinician-rated improvement than sham, with a time-by-group effect of minus 3.54 MADRS points per week and a model-estimated acute reduction of 12.06 points versus 4.98 points.
- The acute MADRS between-group effect was large, reported as `d = -0.89`.
- Daily self-report trajectories also favored active treatment, but the effect was smaller for BDI-II than for MADRS.
- MADRS response rates were higher with active treatment, 42.3 percent versus 13.0 percent, while remission was numerically higher but not clearly significant without baseline adjustment.
- No serious adverse events occurred, and blinding integrity looked acceptable.
- Six-week follow-up did not show a clear between-group separation in post-treatment symptom trajectories.

### 7. What is actually novel?
The novelty is not just that the target is connectivity-guided. The more useful novelty is that the paper tests a personalized accelerated protocol in a naturalistic inpatient setting under sham control, using a schedule that is aggressive enough to matter but still plausibly deployable inside ordinary hospital care.

### 8. What are the strengths?
- Randomized, double-blind, sham-controlled design rather than an open-label inpatient anecdote.
- Clinically difficult cohort, which makes positive signal more interesting than the same result in a milder outpatient sample.
- Individualized resting-state-fMRI targeting instead of crude scalp heuristics.
- Pragmatic middle-ground acceleration schedule that is more deployable than all-day five-day protocols.
- Daily self-report and repeated clinician ratings provide slope information rather than relying only on a single endpoint.
- Blinding and tolerability checks were reported rather than waved away.

### 9. What are the weaknesses, limitations, or red flags?
- Single-site study with modest sample size, especially for categorical endpoints and moderator analyses.
- Baseline MADRS severity was higher in the active arm, which makes sensitivity analyses necessary and leaves regression-to-the-mean as an obvious attack line.
- The protocol is bundled, so it cannot isolate the independent value of connectivity-guided targeting, the accelerated schedule, the total pulse dose, or the intersession interval.
- The treatment occurs inside ongoing multimodal inpatient care with medication changes, so attribution is additive rather than cleanly mechanistic.
- The follow-up story is weaker than the acute treatment story.

### 10. What challenges or open problems remain?
The field still needs to know whether the benefit is durable, whether individualized connectivity-guided targeting beats simpler localization methods in direct comparison, which stimulation-parameter components actually matter, and whether similar results survive multicenter deployment under more heterogeneous routine-care conditions.

### 11. What future work naturally follows?
Run a larger multicenter inpatient trial, ideally with a design that helps separate targeting from acceleration and total dose. Test pretreatment moderators of response using the MRI and clinical data. Compare this pragmatic three-sessions-per-day schedule against more compressed or simpler alternatives, and ask whether ward-compatible precision TMS can be integrated into adaptive care pathways rather than fixed protocols.

### 12. Why does this matter for cabbageland?
Because it is exactly the sort of paper that makes precision neuromodulation more real and less decorative. The question is not only whether a target can be personalized in principle. The question is whether personalized stimulation still helps once it enters the messy ecology of real psychiatric care.

### 13. What ideas are steal-worthy?
- Test precision-targeted neuromodulation inside realistic care environments instead of only inside purified protocol showcases.
- Use a cluster-based connectivity target rather than a single-voxel peak to reduce target fragility.
- Treat acute symptom slope as a key outcome, not just endpoint dichotomies.
- Use a middle-ground accelerated schedule that balances intensity with operational feasibility.
- Ask explicitly which part of a bundled precision protocol is doing the work instead of letting the entire package borrow credit from one elegant targeting idea.

### 14. Final decision
Preserve. This is one of the more decision-relevant recent depression TMS papers because it shows that a sham-controlled, connectivity-guided accelerated protocol can add signal in a clinically difficult inpatient cohort, even if the paper still leaves open which part of the bundle deserves most of the credit.
