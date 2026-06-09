# A portable closed-loop platform enabling cortical evoked potential operant conditioning: system development and validation of target intensity estimation

## Basic info

* Title: A portable closed-loop platform enabling cortical evoked potential operant conditioning: system development and validation of target intensity estimation
* Authors: Disha Gupta et al.
* Year: 2026
* Venue / source: Biomedical Physics & Engineering Express
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13213180/
* Date surfaced: 2026-06-09
* Why selected in one sentence: It attacks a boring but real closed-loop bottleneck by showing that a portable single-rig EEG-plus-EMG setup can preserve the control-relevant target-intensity estimate even when waveform fidelity drops.

## Quick verdict

* Useful

This is not a glamorous control breakthrough, but it is more honest than a lot of closed-loop rhetoric because it fixes a real deployment bottleneck. The paper shows that if your real control variable is target stimulation intensity, you may not need lab-grade EMG fidelity everywhere in the stack. The limitation is just as important: this is a platform-validation paper for neurorehabilitation-style operant conditioning, not a demonstration of better clinical outcomes or smarter brain-state control.

## One-paragraph overview

The paper adapts the cortical Evoked Potential Operant Conditioning System, or C-EPOCS, into a more portable closed-loop platform that can record EEG and EMG through a single acquisition device while still estimating the stimulation intensity needed to standardize afferent input across sessions. The authors test whether lower-sampling-rate EMG, more typical of portable EEG hardware, is good enough for the recruitment-curve step that determines target intensity. Using retrospective downsampling of high-resolution recordings plus a small real-time feasibility test, they show that reduced sampling degrades waveform detail and curve-fit residuals, especially by 320 hertz, but does not materially shift the stimulation-intensity parameters the platform actually needs most. The useful read is not that portable closed-loop neurostimulation is solved. It is that preserving the control-relevant sufficient statistic may matter more than preserving every bit of analog beauty in the waveform.

## Model definition

### Inputs
Soleus EMG recorded during tibial-nerve stimulation, EEG recorded for cortical evoked responses, stimulation triggers, stimulation-current sweeps used to build H-reflex and M-wave recruitment curves, and background-EMG thresholds used to decide when stimulation can be delivered.

### Outputs
Estimated H-reflex and M-wave recruitment curves, the stimulation intensity at Hmax and Mthreshold used as the target stimulation setting for subsequent cortical-evoked-response conditioning, and real-time visual feedback for closed-loop operant-conditioning sessions.

### Training objective (loss)
There is no learned predictive model in the usual machine-learning sense. The paper uses an automated delineation algorithm plus parametric curve fitting, with the practical objective of recovering stable recruitment-curve parameters and especially stable target-intensity estimates under lower-resolution EMG acquisition.

### Architecture / parameterization
A portable closed-loop acquisition-and-feedback stack built around a single biosignal recording device, synchronized EEG and EMG capture, an automated response-window delineation routine, bell-shaped fitting for the H-reflex recruitment curve, sigmoid fitting for the M-wave recruitment curve, and real-time triggering/feedback through the C-EPOCS software pipeline.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to make cortical evoked-potential operant conditioning less trapped inside a fragile lab-cart setup. More specifically, it asks whether a portable integrated EEG-plus-EMG rig can still recover the stimulation-intensity parameters needed to standardize afferent input across sessions.

### 2. What is the method?
The authors take high-resolution EMG recordings and downsample them to 640 hertz and 320 hertz to mimic portable hardware, compare the resulting recruitment-curve parameters against the original 3200-hertz recordings, test automated versus manual response-window delineation, and then run a small real-time feasibility check using a single integrated system that records EEG and EMG at 600 hertz.

### 3. What is the method motivation?
Closed-loop neurofeedback and neuromodulation systems are easy to oversell when they quietly depend on bulky hardware, subjective calibration, and session-to-session stimulation drift. If a portable system cannot preserve the parameter that keeps afferent drive comparable across visits, the rest of the loop is theater.

### 4. What data does it use?
Retrospective analysis used recordings from 21 healthy participants plus one individual with chronic stroke. Real-time feasibility testing used 4 healthy participants. The platform focused on tibial-nerve stimulation with soleus EMG for H-reflex and M-wave recruitment curves, alongside EEG for cortical-response conditioning.

### 5. How is it evaluated?
By comparing recruitment-curve parameters across 3200-hertz, 640-hertz, and 320-hertz EMG; by checking agreement between manual and automated delineation of response windows; by quantifying curve residuals, Hmax and Mmax magnitudes, and the stimulation intensities at Hmax and Mthreshold; and by verifying that the integrated 600-hertz portable setup works online in real time.

### 6. What are the main results?
- The stimulation intensities at Hmax and Mthreshold stayed broadly stable across sampling rates, which is the main thing the platform needs for session-to-session calibration.
- Waveform quality and curve-fit residuals worsened as sampling rate dropped, with the biggest degradation at 320 hertz.
- Automated and manual delineation agreed extremely well on the target-intensity parameters, with ICC values around 0.97 to 0.99 for Hmax and Mthreshold stimulation intensity.
- The online single-rig setup was operationally feasible at 600 hertz in a small real-time test.

### 7. What is actually novel?
The novelty is not a new brain-state controller. It is the engineering judgment that the portable system should be evaluated against the control-relevant statistic, not against perfect waveform preservation. That is a better translational criterion than a lot of closed-loop platform papers use.

### 8. What are the strengths?
- It tackles a real deployment bottleneck instead of pretending hardware logistics do not matter.
- It separates what degrades under lower-resolution EMG from what remains robust, which is exactly the right question.
- It includes both retrospective analysis and a small real-time feasibility pass.
- It uses objective calibration logic rather than relying on visible twitches or subjective sensation thresholds.

### 9. What are the weaknesses, limitations, or red flags?
- This is a platform-validation paper, not evidence that the portable setup improves cortical conditioning or clinical outcomes.
- The online feasibility sample is tiny.
- The target population is neurorehabilitation-adjacent rather than psychiatric neuromodulation proper.
- Lower sampling still damages waveform fidelity and residual error, so the system preserves only the parameter it cares most about, not the full measurement object.

### 10. What challenges or open problems remain?
The next questions are whether preserving target-intensity estimates actually improves longitudinal cortical-response stability, whether the platform works reliably in more impaired populations and less controlled settings, and whether home or rehab-center use introduces artifact and adherence problems that undo the portability gains.

### 11. What future work naturally follows?
Prospective longitudinal conditioning studies using the portable system, testing in stroke or spinal-injury cohorts, combining the calibration layer with richer brain-state estimators, and asking whether similar sufficient-statistic logic can simplify other closed-loop neuromodulation stacks.

### 12. Why does this matter for cabbageland?
Because closed-loop systems fail on boring layers before they fail on clever ones. This paper is a reminder that if you cannot keep the stimulation input comparable across sessions with practical hardware, your controller and biomarker story are built on sand.

### 13. What ideas are steal-worthy?
- Preserve the control-relevant statistic even if you cannot preserve every measurement detail.
- Separate the calibration layer from the state-estimation and control layers instead of treating “closed loop” as one undifferentiated blob.
- Replace subjective session setup with objective per-session afferent calibration whenever possible.
- Evaluate portability by what it does to the intervention logic, not by how sleek the hardware looks.

### 14. Final decision
Preserve. This is a useful methods bridge because it makes portable closed-loop work slightly less fake, even if it does not yet deliver the harder layers of state estimation or therapeutic control.
