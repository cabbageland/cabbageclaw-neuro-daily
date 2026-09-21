# Cathodal tDCS in obsessive-compulsive disorder: cognitive and neurophysiological outcomes in a double-blind sham-controlled trial

## Basic info

* Title: Cathodal tDCS in obsessive-compulsive disorder: cognitive and neurophysiological outcomes in a double-blind sham-controlled trial
* Authors: Rut Zaks-Ohayon, Talia Beit-On Hakmon, Hagit Cohen, Itay Besser, Zippi Frenkel, Jonathan Guez, Doron Todder.
* Year: 2026.
* Venue / source: Clinical Neurophysiology Practice.
* Link: https://doi.org/10.1016/j.cnp.2026.08.009
* Date surfaced: 2026-09-21
* Why selected in one sentence: It is a small but directly relevant sham-controlled OCD neuromodulation trial that measures symptoms, cognitive flexibility, salivary BDNF, and frontal EEG rather than reporting only a symptom score.

## Quick verdict

* Useful

Useful, but very preliminary. The active cathodal mPFC-tDCS group improved more over time on Y-BOCS and task-switching reaction time, while salivary BDNF increased within the treatment group at follow-up. The design is stronger than an uncontrolled case series, but the final sample is only 15 completers, qEEG data were partly lost, blinding success was not formally assessed, and the BDNF group interaction was not significant.

## One-paragraph overview

The study randomized 20 adults with DSM-V OCD to cathodal medial prefrontal tDCS or sham; 15 completed treatment and entered the final analysis. Active stimulation used 2 mA for 20 minutes across 10 sessions, with the cathode at FPz and the anode on the wrist; sham used the same montage with only 30 seconds of current. The authors measured OCD severity with Y-BOCS, cognitive flexibility with a task-switching paradigm, salivary BDNF, and resting frontal alpha at Fz. The active group showed a larger within-group drop in Y-BOCS and faster task-switching over time, but the mechanistic readouts are still soft: frontal alpha did not give a clean significant corrected effect, and BDNF is a peripheral marker with a non-significant time-by-group interaction.

## Model definition

### Inputs

The intervention inputs are stimulation group, montage, current intensity, session schedule, baseline OCD severity, medication-stable clinical status, task-switching behavior, salivary BDNF, and qEEG frontal alpha power at Fz.

### Outputs

The outputs are Y-BOCS symptom severity across baseline, post-treatment, and follow-up; task-switching reaction-time and accuracy measures; salivary BDNF concentrations; and frontal alpha power changes.

### Training objective (loss)

There is no trainable model and no loss function. The analysis uses repeated-measures ANOVA and post hoc tests to estimate time, group, and time-by-group effects.

### Architecture / parameterization

This is a double-blind randomized sham-controlled stimulation protocol, not a computational architecture. The active parameterization is cathodal mPFC-tDCS at FPz, 2 mA, 20 minutes, 10 sessions, with an anodal wrist electrode.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

OCD has a substantial treatment-resistant subgroup, and cognitive inflexibility is part of the clinical problem. The paper asks whether reducing medial prefrontal hyperactivity with cathodal tDCS can improve symptoms and cognitive flexibility while moving plausible plasticity and EEG markers.

### 2. What is the method?

The authors ran a small double-blind randomized sham-controlled trial. Participants received either active cathodal mPFC-tDCS or sham stimulation over 10 sessions, then were assessed at baseline, after treatment, and 30 to 40 days later.

### 3. What is the method motivation?

The motivation is that medial prefrontal cortex hyperactivity is implicated in OCD conflict monitoring and intrusive thought dynamics. Cathodal stimulation is expected to down-modulate cortical excitability, and cognitive flexibility plus BDNF are intended to make the trial more mechanistic than a symptom-only stimulation report.

### 4. What data does it use?

The final analytic sample contains 15 adult OCD patients: 8 in the active tDCS group and 7 in the sham group. Measures include Y-BOCS, a Hebrew word task-switching paradigm, salivary BDNF ELISA, and resting-state qEEG focused on absolute alpha power at Fz. Participants were on stable pharmacological treatment.

### 5. How is it evaluated?

The main evaluation is repeated-measures ANOVA over time and group. Y-BOCS is the clinical outcome. Task-switching reaction time, salivary BDNF, and frontal alpha power are secondary cognitive and neurophysiological outcomes.

### 6. What are the main results?

The active group dropped from a mean Y-BOCS of 31.0 at baseline to 23.78 after treatment and 22.89 at follow-up, while the sham group stayed around 30. The time-by-group effect for Y-BOCS was significant. Task-switching reaction time also showed a significant time-by-group interaction. Frontal alpha showed an uncorrected time-by-group interaction that weakened under Greenhouse-Geisser correction and did not survive custom contrasts. BDNF increased from baseline to follow-up within the active group, but the time-by-group interaction was not significant.

### 7. What is actually novel?

The novelty is not the existence of tDCS for OCD. The useful addition is the attempt to link symptom change to cognitive flexibility, peripheral neurotrophic signaling, and a frontal EEG readout in a sham-controlled design.

### 8. What are the strengths?

It uses sham control and blinding across participants, operators, clinical assessors, and lab technicians.

It measures cognition and biology, not just Y-BOCS.

The montage and dose are clearly described, which makes the protocol easier to compare with other OCD tDCS studies.

### 9. What are the weaknesses, limitations, or red flags?

The final sample is tiny: 8 active and 7 sham completers.

Five participants dropped out, and all discontinuations happened in a difficult real-world context of security instability.

The qEEG amplifier broke during the study, creating missing neurophysiology data.

Blinding effectiveness was not formally assessed.

The BDNF interpretation is easy to overstate because the key group interaction was not significant.

The active group had numerically worse baseline task performance, so apparent improvement needs caution.

### 10. What challenges or open problems remain?

The field still needs larger OCD tDCS trials with formal blinding checks, preregistered primary outcomes, stronger montage comparisons, longer follow-up, better mechanistic readouts, and subgroup analysis. It also needs to know whether cognitive-flexibility gains mediate symptom change or merely travel alongside it.

### 11. What future work naturally follows?

A good next study would compare cathodal mPFC-tDCS against a stronger active montage, include ERP or source-localized EEG measures tied to conflict monitoring, test exposure-and-response-prevention augmentation, and stratify by symptom dimension or baseline cognitive inflexibility.

### 12. Why does this matter for cabbageland?

It is exactly the kind of clinical neuromodulation paper that should be kept but not worshipped. It tries to connect stimulation, symptoms, cognition, and biology, which is the right direction. The evidence is still too small and messy to support confident treatment logic.

### 13. What ideas are steal-worthy?

One steal-worthy idea is to treat cognitive flexibility as a candidate process variable in OCD neuromodulation instead of only measuring symptom severity.

Another is to pair clinical tDCS trials with a simple biology marker and an EEG marker, while being honest that peripheral BDNF and single-electrode alpha are weak mechanistic proxies.

A third is to test whether stimulation makes patients more able to benefit from behavioral interventions that demand set shifting and inhibitory control.

### 14. Final decision

Keep as a useful preliminary clinical note. It is promising enough to track, but the correct language is "small sham-controlled signal requiring replication," not "mechanism established."
