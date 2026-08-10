# Transcutaneous Spinal Cord Stimulation Disrupts Conscious Ankle Proprioception and Produces a More Constrained Locomotor Pattern in Unimpaired Adults

## Basic info

* Title: Transcutaneous Spinal Cord Stimulation Disrupts Conscious Ankle Proprioception and Produces a More Constrained Locomotor Pattern in Unimpaired Adults
* Authors: Christopher A. Johnson, Andria J. Farrens, Parastoo Ali Pour, Arjan Gillan, Hui Zhong, David J. Reinkensmeyer, Alexandra S. Voloshina
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2608.05635
* Date surfaced: 2026-08-10
* Why selected in one sentence: It makes a useful negative point for neuromodulation design: stronger afferent recruitment can worsen conscious state estimation even while it simplifies gross locomotor output.

## Quick verdict

* Useful

This is worth keeping because it says something sharp about stimulation design rather than selling another generic gait-improvement story. The important dissociation is that acute transcutaneous spinal cord stimulation worsens conscious ankle proprioception while leaving gross dorsiflexion strength unchanged and pushing gait toward a narrower, more constrained pattern. The caution is equally obvious: the sample is tiny, young, and unimpaired, so this is a mechanistic design note, not a clinical efficacy landmark.

## One-paragraph overview

The paper asks what transcutaneous spinal cord stimulation, or tSCS, is actually doing to the sensorimotor loop besides the usual headline about "improving locomotion." Fourteen unimpaired adults completed robotic ankle proprioception testing, dorsiflexion strength testing, and treadmill gait assessment with and without stimulation, then underwent proprioceptive training under stimulation; a separate matched control cohort completed the same proprioceptive training without stimulation. Acute tSCS increased absolute ankle-localization error by about 1.5 degrees on average, did not change dorsiflexion maximum voluntary contraction, and shifted gait toward shorter, narrower, lower-excursion movement, especially in the mediolateral direction. With repeated exposure during training, proprioceptive error dropped back toward or below baseline and several sagittal-plane gait measures recovered, while mediolateral constraint persisted. The useful point is that neuromodulation can degrade explicit sensory accuracy even as it stabilizes gross behavior, which is exactly the kind of tradeoff a serious rehabilitation controller should measure instead of hand-waving away.

## Model definition

This paper does not contain a trainable predictive model. The relevant structure is a stimulation-and-measurement protocol for probing different parts of the sensorimotor control loop under altered afferent drive.

### Inputs
Thoracolumbar transcutaneous spinal cord stimulation state, repeated robotic ankle-localization trials from the Crisscross task, dorsiflexion maximum voluntary contraction measurements, and treadmill gait kinematics during normal and tandem walking.

### Outputs
Absolute ankle-localization error, timing error and timing-error magnitude, dorsiflexion torque, and gait metrics including step width, step length, trunk sway, and mediolateral center-of-mass excursion across baseline, stimulation-on, and post-training conditions.

### Training objective (loss)
There is no learned optimization objective. The paper uses repeated-measures statistical comparisons and mixed-effects models rather than a predictive training loss.

### Architecture / parameterization
A within-subject stimulation experiment in 14 unimpaired adults, with assessments at baseline, stimulation-on before training, stimulation-on after training, and stimulation-off after training, plus a separate 14-person no-stimulation control cohort for the proprioceptive-training comparison.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Most spinal stimulation papers talk as if more afferent recruitment is straightforwardly good for movement. This paper asks the more annoying and more useful question: what happens to conscious proprioception and locomotor control when you perturb the sensory side of the loop at the same time?

### 2. What is the method?
The authors combine thoracolumbar tSCS with three measurement layers. First, they use a robotic bilateral ankle-localization task to quantify conscious proprioceptive accuracy. Second, they test gross motor output with dorsiflexion maximum voluntary contraction. Third, they measure treadmill gait during normal and tandem walking, then examine what changes acutely and what adapts after proprioceptive training under stimulation.

### 3. What is the method motivation?
If stimulation changes afferent traffic, it may change explicit state estimation and not just motor excitability. A rehabilitation paper that only reports gait speed or strength can therefore miss the most interesting part of the intervention logic.

### 4. What data does it use?
Fourteen unimpaired adults completed the stimulation experiment, and a separate matched cohort of fourteen unimpaired adults completed the same proprioceptive training protocol without stimulation. The stimulated cohort had a mean age of about 26 years, and all participants were screened to exclude neurological or musculoskeletal impairment.

### 5. How is it evaluated?
The paper compares baseline, stimulation-on pre-training, stimulation-on post-training, and stimulation-off post-training performance using mixed-effects models and post hoc tests. It evaluates absolute proprioceptive error, timing measures, dorsiflexion torque, and a set of gait kinematic variables for both normal and tandem walking.

### 6. What are the main results?
- Acute stimulation increased ankle-localization absolute error, with stimulation-on conditions about 1.5 degrees worse on average than stimulation-off conditions.
- Dorsiflexion strength did not change significantly, which is useful because it argues against a trivial global motor-impairment explanation.
- Gait shifted toward a modestly more constrained pattern, especially reduced step width and reduced mediolateral center-of-mass excursion.
- After training under stimulation, proprioceptive error improved and persisted after stimulation ended, unlike the no-stimulation control cohort.
- Sagittal-plane gait measures recovered toward or beyond baseline, while mediolateral measures remained constrained, suggesting direction-specific reorganization rather than simple normalization.

### 7. What is actually novel?
The novelty is not just applying tSCS to locomotion. The useful novelty is measuring explicit proprioceptive perception, gross motor output, and gait behavior together, then showing that they can dissociate under stimulation. That turns a generic "neuromodulation helps movement" story into a more precise sensorimotor tradeoff.

### 8. What are the strengths?
- It measures the sensory side of the loop directly instead of inferring it from gross movement alone.
- It separates conscious proprioception from strength, which prevents a lazy "everything improved or worsened together" interpretation.
- It includes both acute effects and short-horizon adaptation effects.
- The gait analysis is richer than a single speed score and shows the effect is direction-specific.
- The paper is willing to report an initially disruptive effect instead of smoothing it into intervention propaganda.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is small.
- The cohort is young and unimpaired, so transfer to stroke, spinal cord injury, or degenerative disease is genuinely unknown.
- The control cohort did not perform the gait protocol, so post-training gait recovery cannot be cleanly separated from practice effects.
- Proprioception was measured with one task, so other proprioceptive dimensions might respond differently.
- Only one stimulation configuration was tested, even though spinal stimulation effects are parameter-sensitive.

### 10. What challenges or open problems remain?
The main open problem is whether the same sensory-motor tradeoff appears in impaired populations where baseline proprioception is already degraded. It also remains unclear which stimulation parameters shift the balance between helpful stabilization, disruptive sensory noise, and learnable adaptation.

### 11. What future work naturally follows?
Replicate the finding in larger neurological cohorts, test multiple stimulation locations and intensities, add more proprioceptive assays, and build rehabilitation protocols that explicitly decide whether the goal is immediate stabilization, sensory retraining, or both.

### 12. Why does this matter for cabbageland?
Because it sharpens a control principle that matters well beyond spinal stimulation: more neural drive is not the same thing as better state estimation. If a neuromodulation protocol changes behavior by degrading one measurement channel while tightening another, we need to know that before pretending we understand the mechanism.

### 13. What ideas are steal-worthy?
- Measure explicit state estimation and overt behavior together when evaluating neuromodulation.
- Treat sensory side effects as part of the intervention mechanism, not as annoying background noise.
- Look for direction-specific adaptation instead of only asking whether performance returned to baseline on average.
- Use short-horizon training under perturbation to test whether an initially disruptive stimulation regime can still become useful after adaptation.

### 14. Final decision
Preserve as a design-logic note for stimulation-based rehabilitation and sensorimotor control. It is not a paper about immediate clinical benefit, but it is a good paper about why neuromodulation evaluation should stop pretending that better movement automatically means better sensing.
