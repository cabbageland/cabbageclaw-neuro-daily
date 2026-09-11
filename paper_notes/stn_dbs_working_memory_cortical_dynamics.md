# Subthalamic stimulation modulates working memory-related cortical dynamics in Parkinson's disease

## Basic info

* Title: Subthalamic stimulation modulates working memory-related cortical dynamics in Parkinson's disease
* Authors: Marius Keute, Tianlu Wang, Silvana Miranda Montenegro, Maximilian Scherer, Patrick Bookjans, Bastian Brunnett, Idil Cebi, Luka Milosevic, Daniel Weiss, Alireza Gharabaghi
* Year: 2026
* Venue / source: Brain Communications
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13550774/
* Date surfaced: 2026-09-11
* Why selected in one sentence: It treats STN-DBS cognitive effects as a cortical-state and oscillatory-flexibility problem rather than asking only whether stimulation improves group-average task scores.

## Quick verdict

* Highly relevant

This is not a clean efficacy paper, and that is exactly why it is useful. The group-level working-memory behavior is mostly null, but the full text shows exploratory EEG-behavior relationships that make a better intervention question: which baseline cortical states and task-related desynchronization patterns make cognition more or less vulnerable under STN-DBS? The sample is small and the correlations are not correction-proof, so this should be preserved as a mechanistic signal and biomarker hypothesis, not as proof that one DBS mode improves working memory.

## One-paragraph overview

The study follows nineteen Parkinson's disease patients from preoperative baseline to six months after subthalamic DBS implantation, using verbal and visuospatial working-memory tasks with concurrent EEG. Postoperative testing compared omnidirectional and directional stimulation in a randomized, double-blind crossover design, including chronic three-week stimulation blocks. Average working-memory accuracy and reaction time did not significantly differ between stimulation modes or from preoperative baseline. The useful result sits underneath that null: higher baseline alpha and beta power, especially sensorimotor beta, predicted slower visuospatial reaction time at follow-up, while stronger theta and beta desynchronization during DBS related to better verbal working-memory accuracy. The paper therefore supports a state- and biomarker-centered framing of cognitive DBS effects, while making the caveats visible.

## Model definition

This paper is mainly a clinical electrophysiology and statistical-association study, not a deployed learned control model. The model-like pieces are the mixed-effects and correlation analyses used to relate stimulation condition, EEG spectral features, and working-memory outcomes.

### Inputs
Preoperative and postoperative EEG during verbal and visuospatial delayed-response tasks, stimulation condition (off, omnidirectional DBS, directional DBS depending on visit), task accuracy and reaction time, baseline patient state, and band-limited spectral power features in delta, theta, alpha, and beta ranges.

### Outputs
Estimated stimulation-condition effects on behavior and spectral responses, plus candidate EEG-behavior associations: baseline alpha/beta power predicting follow-up visuospatial reaction time, and task-related theta/beta desynchronization during DBS relating to verbal working-memory accuracy.

### Training objective (loss)
There is no machine-learning training loss. The statistical objective is inference: linear mixed models test stimulation-condition effects with patient-level random intercepts, and exploratory Pearson correlations test relationships between spectral features and behavior. The EEG-behavior correlations were not corrected for multiple comparisons.

### Architecture / parameterization
The analysis uses a clinical crossover design, EEG preprocessing with band-limited time-frequency features, linear mixed-effects models for repeated-measures outcomes, Bayes-factor comparisons against null stimulation effects, and exploratory correlation maps between cortical spectral modulation and working-memory performance.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

STN-DBS can improve motor symptoms in Parkinson's disease while having mixed and sometimes unnoticed cognitive effects. The paper asks whether working-memory outcomes under STN-DBS are better understood through task-related cortical oscillatory dynamics than through group-average behavior alone.

### 2. What is the method?

The authors enrolled Parkinson's disease patients scheduled for STN-DBS, tested verbal and visuospatial working memory before surgery and again at least six months after implantation, and recorded 64-channel EEG during the tasks. Postoperative assessments compared stimulation-off, omnidirectional DBS, and directional DBS acutely, then compared omnidirectional and energy-equivalent directional DBS after randomized three-week chronic stimulation blocks. EEG was analyzed in delta, theta, alpha, and beta bands around task target cues.

### 3. What is the method motivation?

The useful motivation is that cognition may depend on how STN stimulation changes distributed cortical dynamics, not just on whether the stimulated target is "motor" or "cognitive." If excessive synchrony makes the network rigid, then task-related desynchronization could be a candidate marker of more flexible processing during DBS.

### 4. What data does it use?

The parent SANTOP study enrolled twenty-three patients with akinetic-rigid Parkinson's disease scheduled for STN-DBS; nineteen completed the full crossover treatment evaluation periods. After quality control, complete EEG-task datasets were smaller: fourteen patients for acute verbal working memory, twelve for acute visuospatial working memory, and eleven for chronic verbal and visuospatial working-memory analyses. Tasks were verbal delayed response and spatial delayed response paradigms, each with embedded oddball attention streams.

### 5. How is it evaluated?

Behaviorally, the study compares task accuracy and reaction time across stimulation conditions and against preoperative baseline. Physiologically, it tests whether task-related spectral responses differ by stimulation condition, and then explores whether baseline or DBS-period spectral features correlate with follow-up working-memory performance. The chronic analyses are emphasized because acute sessions showed practice effects independent of stimulation condition.

### 6. What are the main results?

Average working-memory performance was stable. In acute testing, accuracy or reaction time improved across sessions in ways consistent with practice rather than stimulation. In chronic testing, there was no significant stimulation-condition effect on spatial or verbal working-memory accuracy or reaction time, and no significant difference from preoperative baseline. Spectral responses also did not differ between omnidirectional and directional DBS. The interesting exploratory results were individual-level: higher baseline alpha and beta power correlated with slower visuospatial reaction time at follow-up, with sensorimotor beta especially visible; more task-related theta desynchronization during DBS correlated with higher verbal working-memory accuracy; and more beta desynchronization correlated with better verbal accuracy relative to baseline.

### 7. What is actually novel?

The novelty is not a new DBS programming recipe. It is the attempt to connect STN-DBS cognitive outcomes to cortical oscillatory state in a delayed, clinically relevant stimulation window, after three-week stimulation blocks rather than only acute toggling. The paper is also useful because it refuses the easy group-average story: the null behavior result does not erase meaningful interindividual cortical dynamics.

### 8. What are the strengths?

It uses a randomized, double-blind crossover design for omnidirectional versus directional stimulation. It records EEG during task performance rather than relying only on clinical scales. It separates acute practice effects from chronic assessments. It explicitly discusses motor improvement, learning, electrode placement, stimulation spread, and individual variability as confounds rather than burying them.

### 9. What are the weaknesses, limitations, or red flags?

The effective EEG sample is small, especially for chronic analyses. The EEG-behavior correlations are exploratory and uncorrected for multiple comparisons. There is no healthy control group and no standardized neuropsychological working-memory score collected in parallel with the experimental tasks. Motor state was not measured concurrently during the cognitive tasks, so reaction time and beta effects may mix cognitive and motor components. The paper cannot determine whether the observed desynchronization patterns are causal, compensatory, or downstream markers of other patient-specific factors.

### 10. What challenges or open problems remain?

The obvious next problem is separating cognitive-network modulation from motor-state improvement during DBS. That requires concurrent kinematics or response-effector controls during cognitive tasks, individualized electrode-location and structural-connectivity modeling, larger samples, longer follow-up, and prospective tests of whether the EEG markers can actually guide programming.

### 11. What future work naturally follows?

Future studies should test whether patient-specific beta/theta desynchronization profiles predict cognitive side effects or benefits under different stimulation settings. A stronger design would combine task EEG, motor readouts, contact-location/connectivity models, and real-time or near-real-time state estimates. The long-term version is an adaptive DBS policy that treats cognitive state as a protected control variable rather than optimizing only motor signs.

### 12. Why does this matter for cabbageland?

It is a useful reminder that stimulation safety and efficacy cannot be reduced to whether the named target is correct. The same STN intervention sits inside a distributed cortical state space, and cognitive effects may depend on baseline synchrony, task demands, and the ability to desynchronize into a flexible regime. That is directly relevant to adaptive neuromodulation, psychiatric stimulation, and any intervention story that wants to protect cognition while changing symptoms.

### 13. What ideas are steal-worthy?

Use null group behavior as a reason to inspect heterogeneity rather than as a reason to stop. Treat baseline oscillatory rigidity as a candidate vulnerability marker. Evaluate cognitive stimulation effects after clinically meaningful blocks, not only acute toggles. Pair stimulation programming with task-state physiology, because the parameter that improves the motor exam may still have invisible cognitive consequences.

### 14. Final decision

Keep. This is a cautious but valuable mechanism note: not definitive, not a programming recipe, but a good scaffold for thinking about cognitive-state biomarkers in DBS.
