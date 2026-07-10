# Reward pursuit during a translational reward task correlates with anhedonia reductions following rTMS in patients with major depressive disorder

## Basic info

* Title: Reward pursuit during a translational reward task correlates with anhedonia reductions following rTMS in patients with major depressive disorder
* Authors: Samantha V. Abram, Aaron N. McInnes, Christi R. P. Sullivan, Dawson C. Cooper, Brian M. Sweis, Alik S. Widge
* Year: 2026
* Venue / source: Translational Psychiatry
* Link: https://www.nature.com/articles/s41398-026-04248-3
* Date surfaced: 2026-07-10
* Why selected in one sentence: It is one of the cleaner recent attempts to tie a rodent-to-human reward-foraging phenotype to symptom-specific response heterogeneity during clinical rTMS.

## Quick verdict

* Useful

This is worth keeping because it attacks a real problem that interventional psychiatry usually handles badly: identifying who improves specifically on anhedonia rather than only on generic depression totals. The translational task logic is more interesting than another retrospective symptom correlation, and the repeated weekly sampling gives the paper more shape than a one-shot baseline biomarker story. But the study is still a small observational clinic sample, the clinical anhedonia endpoint is basically a single PHQ-9 item, and the strongest baseline signal weakens after multiple-comparison correction. So this is a promising measurement idea, not a deployable response biomarker.

## One-paragraph overview

The paper studies 32 patients with treatment-resistant major depressive disorder receiving naturalistic daily rTMS and asks whether reward pursuit during a translational foraging task called Web-Surf tracks or predicts improvement in anhedonia. Web-Surf is the human analogue of the rodent Restaurant Row task: participants accept or reject short delays to obtain category-specific primary rewards, here short video clips, under a fixed time budget. The useful result is not that the task produces a clean predictive biomarker for all depression outcomes. It does not. The useful result is narrower. Patients who harvested more of their preferred rewards at baseline reported more pleasure during the task and tended to show larger anhedonia reductions later in treatment, while patients whose anhedonia improved also increased their capture of preferred rewards across the rTMS course. That makes the paper a better archive object for symptom-specific reward-pursuit phenotyping than for broad rTMS outcome prediction.

## Model definition

This is not a trainable stimulation controller or predictive-classifier paper. The core object is a behavioral phenotype plus repeated-measures statistical analysis around reward pursuit during treatment.

### Inputs

Weekly Web-Surf accept or reject decisions, category-specific delay thresholds, counts of rewards earned from more preferred and less preferred video categories, in-task hedonic ratings, treatment week, and weekly PHQ-9 total and anhedonia-item scores collected during clinical rTMS.

### Outputs

The main outputs are a preference-based reward-pursuit metric, its relationship to baseline hedonic experience, its association with later symptom change, and its change trajectory across the treatment course.

### Training objective (loss)

Not applicable. The paper does not train a predictive model. It uses mixed-effects models, correlations, and moderation analyses to test whether the behavioral phenotype relates to symptom change.

### Architecture / parameterization

Naturalistic observational repeated-measures design in treatment-resistant depression, with weekly task sessions during an rTMS course and statistical analyses centered on baseline and longitudinal reward-pursuit measures.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

The paper is trying to find a more behaviorally grounded and translational way to track or predict improvement in anhedonia during rTMS for depression.

### 2. What is the method?

Patients completed the Web-Surf task weekly while receiving clinical rTMS. The authors derived a reward-pursuit metric from how strongly participants concentrated their earned rewards in their preferred categories, then tested whether that metric related to hedonic experience and symptom change.

### 3. What is the method motivation?

Anhedonia is clinically important, mechanistically slippery, and often flattened into crude total-score summaries. A rodent-to-human reward-foraging task could offer a more behaviorally legible phenotype than another generic questionnaire baseline.

### 4. What data does it use?

Thirty-two patients with treatment-resistant major depressive disorder recruited from an academic interventional psychiatry clinic in Minnesota. Participants received dorsolateral prefrontal rTMS five days per week with either a Figure-8 coil or an H1 coil, and completed repeated in-clinic Web-Surf sessions across the treatment course.

### 5. How is it evaluated?

The paper evaluates whether task behavior is stable and interpretable in this patient group, whether baseline reward pursuit correlates with hedonic experience and later symptom change, and whether reward pursuit shifts over treatment differently in patients with and without anhedonia improvement.

### 6. What are the main results?

First, the task behaves sensibly in patients with depression: revealed preferences and hedonic ratings line up, and the reward-pursuit metric is reliable enough to analyze longitudinally. Second, baseline capture of preferred rewards is associated with more pleasurable task experience. Third, the baseline signal is more specific to anhedonia than to overall depression: the cleaner association is with later change in the PHQ-9 anhedonia item rather than total PHQ-9 change, and the stronger effect comes from preferred-reward earnings more than from the composite preferred-minus-less-preferred score. Fourth, over treatment, patients whose anhedonia improves increasingly capture more preferred rewards.

### 7. What is actually novel?

The novelty is not rTMS for depression. It is embedding a rodent-to-human foraging task inside a naturalistic interventional-psychiatry workflow and treating reward pursuit as a symptom-specific translational phenotype rather than a vibes-only clinical metaphor.

### 8. What are the strengths?

The paper uses primary rewards rather than only abstract points or effort proxies.

It has a genuine cross-species task lineage instead of borrowing the word "translational" decoratively.

It samples behavior repeatedly during treatment rather than forcing everything into a single baseline predictor.

And it distinguishes anhedonia from broader depression severity instead of pretending they are interchangeable.

### 9. What are the weaknesses, limitations, or red flags?

The study is observational and not randomized.

There is no non-treatment comparison group, so improved reward pursuit could reflect broader clinical improvement or repeated-task effects rather than rTMS-specific mechanisms.

The sample is small, clinically heterogeneous, and treated with mixed coil and protocol configurations.

The main clinical anhedonia endpoint is a single PHQ-9 item rather than a richer anhedonia instrument.

And the headline baseline association is not clean enough to treat as a ready-made predictive biomarker.

### 10. What challenges or open problems remain?

The big open problem is replication in a larger, more standardized rTMS cohort with stronger symptom phenotyping. It also remains unclear whether reward-pursuit changes are specific to prefrontal stimulation, to general symptom improvement, or to repeated exposure to the task itself.

### 11. What future work naturally follows?

Prospective trials that preregister reward-pursuit hypotheses, use richer anhedonia measures, standardize the rTMS protocol, and combine behavioral phenotyping with imaging or electrophysiology to test whether the phenotype reflects identifiable circuit integrity.

### 12. Why does this matter for cabbageland?

Because it treats interventional psychiatry as a measurement problem instead of a branding problem. If symptom-specific response heterogeneity matters, then cross-species reward-pursuit behavior is a much more interesting thing to archive than another undifferentiated depression total.

### 13. What ideas are steal-worthy?

Use primary-reward foraging tasks, not only abstract reward proxies, when probing motivation in intervention studies.

Track symptom-relevant behavior weekly during treatment instead of relying entirely on pre-post questionnaires.

Separate preferred-reward capture from global symptom totals when studying anhedonia.

And make translational claims earn their keep by using task structures that genuinely map across species.

### 14. Final decision

Keep as a useful note about symptom-specific reward phenotyping in rTMS, but do not overread it as a validated clinical biomarker. The paper is best treated as a promising measurement blueprint that still needs a stronger trial frame.

## Inspection notes / uncertainty

This summary is based on full-text inspection of the open-access article PDF and landing page. Confidence is good on the task design, statistical framing, and stated limitations. Confidence is lower on any strong predictive-biomarker claim, because the study is small, observational, and clinically heterogeneous by design.
