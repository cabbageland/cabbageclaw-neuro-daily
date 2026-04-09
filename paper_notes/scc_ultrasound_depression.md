# Noninvasive Modulation of the Subcallosal Cingulate and Depression With Focused Ultrasonic Waves

## Basic info

* Title: Noninvasive Modulation of the Subcallosal Cingulate and Depression With Focused Ultrasonic Waves
* Authors: Thomas S. Riis, Daniel A. Feldman, Sung Soo Kwon, Lauren C. Vonesh, Vincent Koppelmans, Joseph R. Brown, Dale Solzbacher, Jerzy Kubanek, and Brian J. Mickey
* Year: 2025
* Venue / source: Biological Psychiatry
* Link: https://pubmed.ncbi.nlm.nih.gov/39396736/
* Date surfaced: 2026-04-09
* Why selected in one sentence: It is one of the more serious recent attempts to noninvasively engage a depression-relevant deep target with concurrent imaging rather than settling for symptom drift at the scalp.

## Quick verdict

* Highly relevant

This is a good pilot, not a solved depression-treatment story. The paper earns attention because it chooses a deep circuit target that already has real mechanistic and DBS relevance, measures target engagement during stimulation, and keeps sham control in the loop. The main caution is obvious: small sample, only partial single-subject detectability, and the cleaner clinical signal appears in the per-protocol subset rather than the full intent-to-treat sample.

## One-paragraph overview

The paper tests whether low-intensity focused ultrasound can noninvasively modulate the bilateral subcallosal cingulate cortex in people with treatment-resistant depression. Twenty-two participants were randomized in a double-blind sham-controlled design, with stimulation delivered during concurrent functional MRI to quantify whether the intended deep target was actually engaged. The authors report a target-specific decrease in subcallosal cingulate activity during real stimulation, evidence of individually detectable target engagement in seven of sixteen scanned participants, and short-term improvements in sadness and 6-item Hamilton Depression Rating Scale scores that favored real stimulation in the per-protocol sample. The useful read is that focused ultrasound may be able to reach a clinically meaningful depression circuit noninvasively. The non-useful read would be to pretend this already establishes durable antidepressant efficacy.

## Model definition

This paper is not centered on a learnable predictive model.

### Inputs
Treatment-resistant depression participants, focused-ultrasound stimulation delivered to the bilateral subcallosal cingulate, concurrent functional MRI during stimulation, and pre-post mood and depression rating scales.

### Outputs
Target-region functional MRI activity change during stimulation, individual-level detectability of target engagement in some participants, and short-term changes in sadness and 6-item Hamilton Depression Rating Scale scores.

### Training objective (loss)
No trainable model or explicit optimization loss is the scientific core of the paper. The main optimization problem is physical targeting of a deep circuit during stimulation.

### Architecture / parameterization
A circuit-targeted clinical pilot combining low-intensity focused ultrasound, sham control, concurrent functional MRI, and short-horizon symptom assessment.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The problem is that depression neuromodulation still lacks a clean noninvasive method for directly and selectively engaging deep circuit targets that matter mechanistically. The subcallosal cingulate has long been implicated in severe depression and in invasive stimulation work, but ordinary noninvasive tools do not directly reach it with much precision.

### 2. What is the method?
The authors ran a randomized, double-blind, sham-controlled study in twenty-two individuals with treatment-resistant depression. They delivered bilateral focused ultrasound to the subcallosal cingulate during concurrent functional MRI to test target engagement, then measured immediate mood change and short-term depression severity after forty minutes of real or sham stimulation.

### 3. What is the method motivation?
If focused ultrasound is going to matter in psychiatry, it has to do more than produce generic mood changes. It needs to show that it can engage a target with existing circuit relevance. The subcallosal cingulate is a strong choice because it already has a serious mechanistic and interventional history in depression.

### 4. What data does it use?
The accessible abstract describes twenty-two participants with treatment-resistant depression. Functional MRI target-engagement analyses were reported for a subset of sixteen scanned participants, and outcome analyses included both intent-to-treat and per-protocol samples.

### 5. How is it evaluated?
It is evaluated by asking whether real stimulation decreases subcallosal cingulate activity relative to sham during concurrent functional MRI, whether target engagement is detectable at the individual-participant level, and whether short-term sadness and 6-item Hamilton Depression Rating Scale scores improve more under real stimulation.

### 6. What are the main results?
The authors report a target-specific decrease in subcallosal cingulate activity during stimulation with p equals 0.028 in the imaging sample of sixteen participants. In seven of those sixteen participants, target engagement was reportedly detectable at the individual level from a single ten-minute scan. Mood and depression scores favored real over sham stimulation, with significant effects in the per-protocol sample at twenty-four hours for the 6-item Hamilton Depression Rating Scale and for sadness, while the intent-to-treat analysis showed only nonsignificant trends.

### 7. What is actually novel?
The useful novelty is not merely using ultrasound for depression. The real novelty is combining a deep psychiatric target with concurrent imaging-based target verification in a sham-controlled design. That makes the paper more legible than the many noninvasive studies that stimulate something vaguely plausible and only inspect downstream symptoms.

### 8. What are the strengths?
- Picks a target with strong prior depression-circuit relevance.
- Uses concurrent functional MRI rather than hand-waving about target engagement.
- Includes randomized, double-blind, sham-controlled structure.
- Separates imaging evidence from symptom outcomes instead of relying on one alone.
- Makes clear that target engagement is not universal across participants.

### 9. What are the weaknesses, limitations, or red flags?
- It is a small pilot, so effect-size stability is uncertain.
- The stronger clinical signal appears in the per-protocol sample rather than in the intent-to-treat analysis.
- Individual target engagement was only seen in seven of sixteen scanned participants, which is not trivial and not reassuring enough to ignore.
- I only inspected the abstract-level record, not the full article, so confidence should stay bounded on acoustic parameters, detailed statistics, and safety nuance.
- Rapid symptom movement is interesting, but durability is still unclear.

### 10. What challenges or open problems remain?
The field still needs replication, stronger individual-level targeting reliability, dose-parameter mapping, better understanding of which patients show detectable target engagement, and evidence for durable benefit beyond short-horizon symptom change.

### 11. What future work naturally follows?
Larger sham-controlled trials, explicit modeling of who shows measurable subcallosal engagement, imaging-plus-behavior studies that test whether target engagement mediates symptom change, and comparison against other circuit-targeted noninvasive approaches rather than generic depression baselines.

### 12. Why does this matter for cabbageland?
Because it is one of the cleaner recent examples of psychiatric neuromodulation trying to earn its circuit claim. It shifts the standard from mood change after stimulation toward measurable engagement of a target that already matters theoretically and clinically.

### 13. What ideas are steal-worthy?
- Treat concurrent target-engagement measurement as part of the intervention design, not as an optional afterthought.
- Choose deep targets with prior causal or interventional legitimacy instead of novelty-chasing.
- Separate the question of whether a circuit was engaged from the question of whether symptoms improved.
- Pay attention to participant-level detectability rather than hiding behind group averages.

### 14. Final decision
Keep. This is not enough evidence to celebrate focused ultrasound as a depression treatment, but it is enough to preserve as a serious deep-target pilot with better intervention logic than average.
