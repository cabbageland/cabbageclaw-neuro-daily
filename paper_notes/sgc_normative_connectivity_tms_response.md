# Predictive value of subgenual cingulate normative connectivity to TMS treatment site for antidepressant response in routine clinical practice: a prospective, multisite cohort study

## Basic info

* Title: Predictive value of subgenual cingulate normative connectivity to TMS treatment site for antidepressant response in routine clinical practice: a prospective, multisite cohort study
* Authors: Sanaz Khosravani et al.
* Year: 2026.
* Venue / source: Molecular Psychiatry.
* Link: https://pubmed.ncbi.nlm.nih.gov/40847007/
* Date surfaced: 2026-04-15.
* Why selected in one sentence: It is a valuable real-world pressure test of the anti-subgenual TMS targeting heuristic and finds that normative connectivity alone explains little in a heterogeneous clinic sample.

## Quick verdict

* Highly relevant

This is one of the more useful recent depression-TMS papers precisely because the main result is mostly negative. In a prospective multisite routine-practice cohort, normative connectivity from the delivered left-DLPFC TMS site to subgenual cingulate did not meaningfully predict symptom improvement on its own. That does not invalidate network targeting, but it does weaken the habit of talking as if anti-subgenual targeting is already a robust standalone personalization rule.

## One-paragraph overview

The paper asks whether one of the best-known precision-TMS ideas actually survives contact with routine clinical heterogeneity. Sixty-six patients with major depressive disorder received three to eight weeks of standard-care left-DLPFC repetitive transcranial magnetic stimulation, with actual stimulation sites recorded on multiple days using MRI neuronavigation. The authors then estimated each site’s functional connectivity to subgenual cingulate using a large normative resting-state dataset from healthy individuals and tested whether that connectivity predicted change in Beck Depression Inventory scores. The main answer is no: the primary association was null, while baseline anxiety and psychiatric comorbidity explained more variance once added in post-hoc models. The paper matters because it separates a plausible targeting story from a clinically reliable one.

## Model definition

This paper does not present a trainable predictive model in the accessible abstract text. It combines a normative-connectivity targeting metric with observational outcome analysis.

### Inputs
Actual left-DLPFC TMS site locations recorded with MRI neuronavigation, normative resting-state functional connectivity estimates between each delivered site and subgenual cingulate cortex derived from one thousand healthy individuals, depression outcome scores, and clinical covariates such as baseline anxiety and psychiatric comorbidity.

### Outputs
Primary output is the association between site-to-subgenual connectivity and antidepressant response, indexed as change in Beck Depression Inventory scores. Secondary outputs include post-hoc models that incorporate clinical covariates.

### Training objective (loss)
No trainable model or optimization loss is specified in the accessible abstract. The main analysis is correlational and regression-based outcome modeling.

### Architecture / parameterization
Observational cohort analysis using a normative-connectivity metric plus post-hoc multivariable statistical modeling.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

The paper tests whether a widely cited network-targeting heuristic for depression TMS — stronger negative connectivity between the stimulated left-DLPFC site and subgenual cingulate — actually predicts clinical response in routine practice rather than in smaller, cleaner research cohorts.

### 2. What is the method?

Patients received three to eight weeks of daily left-DLPFC rTMS as part of standard care. Stimulation sites were recorded across multiple days with MRI neuronavigation. The authors estimated normative site-to-subgenual connectivity from a large healthy resting-state dataset and tested its relationship to change in depression symptoms, with secondary post-hoc analyses adding clinical covariates.

### 3. What is the method motivation?

The motivation is straightforward: if antidepressant efficacy depends on stimulating a cortical entry point that is functionally anti-correlated with subgenual cingulate, then delivered sites with stronger negative connectivity should produce better outcomes. This has become one of the field’s most repeated precision-targeting stories, so it is worth stress-testing in a clinically messy setting.

### 4. What data does it use?

Sixty-six treatment-seeking individuals with major depressive disorder treated in routine practice, plus a normative resting-state functional-connectivity reference derived from one thousand healthy individuals. The accessible abstract indicates that actual stimulation locations were captured on multiple treatment days.

### 5. How is it evaluated?

The primary evaluation is the correlation between change in Beck Depression Inventory, second edition, scores and normative connectivity between each individual’s delivered TMS site and subgenual cingulate. Secondary post-hoc analyses add clinical covariates. The abstract also reports that site-location consistency was checked by comparing within- versus between-individual variance.

### 6. What are the main results?

The primary result is a null finding: normative site-to-subgenual connectivity did not predict antidepressant response by itself, with a reported correlation around 0.1 and a non-significant p value of 0.39. Site inconsistency does not appear to explain that null result, because within-individual site variance was smaller than between-individual variance. When clinical covariates were added post hoc, associations became significant, with baseline anxiety and psychiatric comorbidity explaining most of the variance.

### 7. What is actually novel?

The novelty is not the anti-subgenual idea itself. The novel contribution is a prospective multisite routine-practice test that pressures a famous heuristic under more realistic clinical heterogeneity.

### 8. What are the strengths?

The paper asks a real translational question instead of assuming prior single-site findings generalize.

It uses actual delivered stimulation sites rather than idealized target estimates.

And it does not hide the clinically inconvenient answer when the primary heuristic underperforms.

### 9. What are the weaknesses, limitations, or red flags?

The strongest limitation is that the connectivity metric is normative rather than individualized, so a negative result could reflect the weakness of the normative proxy rather than the whole network-targeting idea.

The design is observational rather than randomized, which limits causal interpretation.

Routine-practice protocol heterogeneity may also blur signal.

And because I only inspected the abstract-level text, I do not have a clean read on medication effects, protocol variation, follow-up durability, or exact regression specification.

### 10. What challenges or open problems remain?

The big open problem is whether individualized connectivity, symptom dimensions, or dynamic state measures will outperform static normative connectivity in real clinics. Another challenge is separating genuine circuit-targeting effects from the broader clinical variance introduced by anxiety, comorbidity, and protocol choices.

### 11. What future work naturally follows?

Prospective comparisons between normative and individualized targeting would be the obvious next step. It would also be useful to test whether anti-subgenual logic works better in narrower depression subtypes or when embedded in richer multivariable response models rather than treated as a standalone rule.

### 12. Why does this matter for cabbageland?

Because cabbageland cares about intervention logic, not target folklore. This paper is useful exactly because it shows that a mechanistically plausible network story can still be too weak or too partial to govern clinical personalization on its own.

### 13. What ideas are steal-worthy?

One steal-worthy idea is methodological: treat actual delivered stimulation sites as data rather than assuming intended targets equal real exposure.

Another is conceptual: any serious precision-neuromodulation claim should be tested against heterogeneity variables such as anxiety and comorbidity, not just against prettier connectomic explanations.

A third is strategic: negative translational results can be more informative than another positive small-cohort targeting paper.

### 14. Final decision

Keep. This is not a triumphant precision-targeting paper, and that is exactly why it is valuable.