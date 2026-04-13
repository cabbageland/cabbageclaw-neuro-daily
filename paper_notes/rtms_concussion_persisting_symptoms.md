# Treatment of Persisting Symptoms after Concussion with Repetitive Transcranial Magnetic Stimulation: A Double-Blinded, Randomized, Controlled Trial

## Basic info

* Title: Treatment of Persisting Symptoms after Concussion with Repetitive Transcranial Magnetic Stimulation: A Double-Blinded, Randomized, Controlled Trial
* Authors: Christina Campbell, Alexander J. Wilson, Sias du Plessis, Marinus H. Vergeer, Kyla Jobin, Jean-Marc Galarneau, Lisa S. Gan, Chantel T. Debert
* Year: 2026.
* Venue / source: Journal of Neurotrauma.
* Link: https://pubmed.ncbi.nlm.nih.gov/41968688/
* Date surfaced: 2026-04-13.
* Why selected in one sentence: It is a useful negative clinical trial showing that a plausible high-frequency left-dorsolateral-prefrontal rTMS protocol did not beat sham for persistent post-concussion symptoms.

## Quick verdict

* Useful

This is worth preserving because clean negative trials are more informative than endless pilot positivity. Ninety-one participants were randomized, the protocol was substantial, and the primary result was still null: active rTMS did not significantly outperform sham on the main post-concussion symptom outcome at post-treatment, one month, or three months. The paper does not kill neuromodulation for concussion, but it does undercut generic DLPFC recipe transfer and should raise the bar for symptom-specific or state-dependent designs.

## One-paragraph overview

The trial tests whether twenty sessions of high-frequency repetitive transcranial magnetic stimulation over the left dorsolateral prefrontal cortex improve persistent symptoms after mild traumatic brain injury better than sham. Adults with symptoms lasting at least three months and up to five years post-injury were randomized one-to-one to active or sham treatment. The primary outcome was change in Rivermead Postconcussion Symptoms Questionnaire score from baseline to post-treatment and then one- and three-month follow-up. Both groups improved over time, but there was no significant between-group difference at any primary endpoint. Secondary measures including depression, anxiety, quality of life, headache, cognition, and post-traumatic stress showed time effects but not group effects.

## Model definition

This paper does not contain a learnable predictive model or controller.

### Inputs
Adults with persistent post-concussion symptoms, randomized to either active or sham left-dorsolateral-prefrontal repetitive transcranial magnetic stimulation. The active protocol used ten-hertz stimulation, ten trains of sixty pulses, forty-five-second inter-train intervals, and one hundred to one hundred twenty percent resting motor threshold across twenty sessions.

### Outputs
Primary output was change in total Rivermead Postconcussion Symptoms Questionnaire score. Secondary outputs included anxiety, depression, quality of life, headache impact, post-traumatic stress symptoms, and cognition.

### Training objective (loss)
Not applicable. This is a clinical trial, not a trainable model paper.

### Architecture / parameterization
Not applicable in the machine-learning sense. The intervention is an open-loop high-frequency left-dorsolateral-prefrontal rTMS protocol compared against sham.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

A substantial minority of people with mild traumatic brain injury continue to experience persistent symptoms for months or years. The paper asks whether a standard neuromodulation intervention can meaningfully reduce that symptom burden.

### 2. What is the method?

A double-blinded, randomized, sham-controlled trial comparing active versus sham high-frequency rTMS over left dorsolateral prefrontal cortex.

### 3. What is the method motivation?

rTMS has shown promise in smaller studies and has plausible relevance to symptoms such as mood, cognition, and headache. The trial aims to test whether those hopes survive a larger and more controlled design.

### 4. What data does it use?

The paper enrolled ninety-one adults aged eighteen to seventy-five with persistent symptoms after concussion. The abstract does not provide every subgroup detail, but it does specify the overall randomized sample and major outcome measures.

### 5. How is it evaluated?

The main evaluation uses a difference-in-differences framework with linear mixed models, controlling for age, sex, and baseline life stress, and compares symptom-score change between active and sham groups at post-treatment, one month, and three months.

### 6. What are the main results?

There was no significant difference between active and sham rTMS on the primary symptom outcome at any main follow-up point. Both groups improved significantly over time. Secondary outcomes showed time effects but no group effects. Lower baseline life stress was associated with a post-treatment PTSD-symptom benefit in the active group only, but that looks more exploratory than decisive.

### 7. What is actually novel?

The novelty is not a positive effect. The useful contribution is that this is a larger, controlled test that shows a clinically reasonable rTMS recipe may fail to separate from sham in this population.

### 8. What are the strengths?

Randomized, double-blinded, sham-controlled design.

Reasonable sample size by neuromodulation standards.

Multiple follow-up timepoints rather than a single immediate endpoint.

The null result is reported plainly instead of being buried under exploratory optimism.

### 9. What are the weaknesses, limitations, or red flags?

The target is generic left dorsolateral prefrontal cortex rather than symptom-specific or individualized.

Persistent post-concussion symptoms are heterogeneous, so a one-size-fits-all open-loop intervention may wash out subgroup effects.

The abstract does not let me inspect adverse events, protocol adherence, or whether any symptom clusters behaved differently enough to matter.

The exploratory life-stress interaction is interesting but should not be oversold.

### 10. What challenges or open problems remain?

The major challenge is heterogeneity. Persistent post-concussion symptoms likely require better stratification by symptom cluster, network dysfunction, or physiological state. Another is whether timing, target, or personalized biomarkers matter more than simply giving more sessions of a standard recipe.

### 11. What future work naturally follows?

Future work should test individualized targeting, symptom-cluster stratification, or state-dependent stimulation rather than generic DLPFC carryover. It would also be useful to pair intervention with mechanistic readouts such as EEG, TMS-EEG, or symptom-dynamics modeling.

### 12. Why does this matter for cabbageland?

Because negative intervention evidence is part of good mechanism. If a plausible protocol fails, that is a clue that the disorder or syndrome is not well matched to the chosen target and timing logic. This paper is a decent antidote to neuromodulation theater.

### 13. What ideas are steal-worthy?

One steal-worthy idea is evaluative rather than technical: keep good null trials in the repository because they prune bad intervention habits.

Another is to treat life-stress or broader context variables as potential moderators rather than afterthought covariates.

A third is that concussion neuromodulation probably needs stronger state or symptom models before large efficacy claims are believable.

### 14. Final decision

Keep as a useful negative clinical note. The result is not exciting, but it is exactly the kind of evidence that keeps future intervention framing honest.
