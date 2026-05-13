# Reliability and signal comparison of OPM-MEG, fMRI & iEEG in a repeated movie viewing paradigm

## Basic info

* Title: Reliability and signal comparison of OPM-MEG, fMRI & iEEG in a repeated movie viewing paradigm
* Authors: Olivia R. Christiano et al.
* Year: 2026
* Venue / source: Imaging Neuroscience
* Link: https://pubmed.ncbi.nlm.nih.gov/42125202/
* Date surfaced: 2026-05-13
* Why selected in one sentence: It is a useful measurement paper because it tests whether optically pumped magnetometer MEG produces reproducible stimulus-driven signals that line up with both fMRI and intracranial EEG rather than asking to be trusted on novelty alone.

## Quick verdict

* Useful

This is a methods paper, not an intervention paper, but it is worth keeping because measurement reliability is part of whether future closed-loop or targeting claims deserve belief. The strongest result is not that OPM-MEG is magical. It is that lower-frequency stimulus-driven patterns are reproducible and show sensible cross-modal alignment with both fMRI and iEEG. The main limitation is that this is a repeated-movie benchmark, which is helpful for signal validation but still far from online control or clinical deployment.

## One-paragraph overview

The authors compare optically pumped magnetometer magnetoencephalography, functional MRI, and intracranial EEG using repeated viewings of a movie segment in separate participant groups. They quantify signal consistency within individuals, across subjects, and across modalities across seven canonical frequency bands plus a broadband measure. The useful finding is that OPM-MEG shows widespread test-retest reliability, especially at lower frequencies, and that its spatial patterns in visual and auditory regions correspond well with both fMRI and iEEG. The paper matters because it treats cross-modal convergence as a measurement test rather than just reporting that a new sensor works in principle.

## Model definition

### Inputs
Movie-driven neural recordings acquired with OPM-MEG, functional MRI, and intracranial EEG, analyzed across canonical frequency bands and broadband activity.

### Outputs
Reliability estimates within participants and across participants, spatial maps of stimulus-driven responses, cross-modal correspondence measures, and signal-to-noise comparisons across modalities.

### Training objective (loss)
There is no central learnable predictive model in the accessible abstract. The work is primarily a comparative signal-analysis and reliability study.

### Architecture / parameterization
A cross-modal analysis framework comparing OPM-MEG, fMRI, and iEEG response reliability and correspondence across frequency-specific and broadband representations.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Whether OPM-MEG produces reliable noninvasive recordings that align with established modalities well enough to be taken seriously as a measurement platform.

### 2. What is the method?
Record repeated movie-viewing responses in separate groups, compute within-person and across-subject reliability, then compare OPM-MEG spatial and spectral response structure against fMRI and iEEG.

### 3. What is the method motivation?
A new sensing modality is only useful for neuroengineering if it is reproducible and if its signals converge with modalities that already have stronger biological trust.

### 4. What data does it use?
Three independent participant groups completing repeated viewings of the same movie segment, one recorded with OPM-MEG, one with functional MRI, and one with intracranial EEG.

### 5. How is it evaluated?
By quantifying signal consistency within individuals, across subjects, and across modalities across seven canonical frequency bands plus broadband activity, then comparing signal-to-noise properties of these alignments.

### 6. What are the main results?
- OPM-MEG shows widespread test-retest reliability, especially in lower frequency bands.
- Its spatial patterns resemble fMRI and iEEG in visual and auditory cortex.
- OPM-fMRI comparisons show inverse low-frequency and positive higher-frequency relationships consistent with known oscillation-to-BOLD patterns.
- In some regions, cross-modal alignment signal-to-noise exceeds within-modality reliability, suggesting shared-noise attenuation through multimodal comparison.

### 7. What is actually novel?
The novelty is not just using OPM-MEG. The useful novelty is putting it through a cross-modal reliability test against both fMRI and iEEG under the same repeated naturalistic stimulus logic.

### 8. What are the strengths?
- Sensible benchmarking target rather than a gadget-first paper.
- Cross-modal comparison against both invasive and noninvasive reference modalities.
- Frequency-resolved analysis rather than one collapsed summary metric.
- Useful for deciding how much trust to place in future OPM-based state-estimation claims.

### 9. What are the weaknesses, limitations, or red flags?
- The accessible text for this run was abstract-level only after repeated full-text attempts.
- Separate participant groups mean cross-modal comparison is indirect rather than truly within-subject.
- Repeated movie viewing is a strong sensory benchmark but not a closed-loop or intervention setting.
- Reliability in sensory cortex does not automatically guarantee utility for harder control targets or psychiatric biomarkers.

### 10. What challenges or open problems remain?
Testing whether OPM-MEG remains this reliable in more mobile, noisy, or clinical settings, whether it can support online state estimation, and whether cross-modal convergence holds for deeper or less stimulus-locked phenomena.

### 11. What future work naturally follows?
Natural next steps are within-subject multimodal comparisons where feasible, online decoding tasks, perturbation experiments, and evaluation on clinically relevant network states rather than only movie-driven sensory responses.

### 12. Why does this matter for cabbageland?
Because better sensing changes what kinds of closed-loop claims are even plausible. If OPM-MEG can become a reliable bridge between noninvasive measurement and network-level state tracking, it could matter for adaptive stimulation and mechanistic validation.

### 13. What ideas are steal-worthy?
- Treat cross-modal convergence as part of validation, not a bonus figure.
- Benchmark new sensing stacks on repeated naturalistic stimuli before making control claims.
- Compare within-modality reliability against cross-modal alignment to detect shared signal versus shared noise.
- Use sensory benchmarks as a gate before scaling a modality into harder psychiatric or neuromodulation problems.

### 14. Final decision
Keep as a methods note. It does not directly improve stimulation logic yet, but it sharpens the measurement side of the loop and is a better use of attention than another decorative neurotechnology launch piece.
