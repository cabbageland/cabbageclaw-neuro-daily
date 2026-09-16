# Sources of the N15 TMS-evoked potential following motor cortex stimulation localize rostrals to TMS-induced electric fields and depend on dose

## Basic info

* Title: Sources of the N15 TMS-evoked potential following motor cortex stimulation localize rostrals to TMS-induced electric fields and depend on dose
* Authors: Sybren Van Hoornweder, Mikkel M. Beck, Jesper D. Nielsen, Leo Tomasevic, Raf L. J. Meesen, Hartwig R. Siebner, Axel Thielscher
* Year: 2026
* Venue / source: Imaging Neuroscience
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13563533/
* Date surfaced: 2026-09-16
* Why selected in one sentence: It tests whether an early TMS-EEG response actually colocalizes with the modeled electric-field peak, which is exactly the sort of assumption target-engagement biomarkers should not get for free.

## Quick verdict

* Highly relevant

This is a methods preserve because it makes TMS-EEG target engagement less hand-wavy. The paper shows that the N15 source after motor-cortex TMS is not simply sitting where the modeled electric field peaks; it is usually more rostral, dose-dependent, and probably reflects early network propagation rather than direct reactivation of the maximally exposed cortex. The result is not a clinical biomarker yet, but it is a good warning label for anyone treating early TEP components as direct readouts of the stimulated patch.

## One-paragraph overview

The authors combine individualized TMS electric-field modeling with source localization of the early N15 TMS-evoked EEG component. Sixteen healthy adults received single-pulse TMS over the left primary motor hand area at six dose levels, during rest and tonic contraction. Using T1/T2 MRI-based head models, EEG source localization with LCMV, dSPM, and eLORETA, linear mixed-effects models, and spatial clustering, the paper asks whether N15 source activity overlaps with the TMS-induced electric field. The main finding is a consistent spatial mismatch: the E-field peaks around the crowns of the pre- and postcentral gyri, while the N15 source field is more rostral, mainly in premotor and motor regions. Higher dose increases N15 magnitude and reduces the mismatch, but does not make the N15 a trivial local field readout.

## Model definition

### Inputs
The analysis takes structural T1 and T2 MRI, TMS coil position/orientation, resting motor threshold, six stimulation intensities from `rMT - 8% MSO` to `rMT + 12% MSO`, rest versus active motor state, TMS-EEG recordings, EEG covariance estimates, individualized head models, and cortical source spaces. Nine participants had corrupt neuronavigation coordinates, so coil positions for those cases were interpolated from the intact participants with supplementary control analyses.

### Outputs
The pipeline outputs modeled cortical electric-field magnitude distributions, N15 EEG source magnitude maps, peak source estimates, whole-cortex source-field maps, spatial clusters where source and electric fields differ, dose and state effects on N15 source magnitude, and inverse-solver comparisons across LCMV, dSPM, and eLORETA.

### Training objective (loss)
There is no trainable clinical predictor or machine-learning loss. The paper uses biophysical field simulation, EEG inverse modeling, linear mixed-effects models, and permutation/TFCE-style spatial clustering to compare electric-field and source-field distributions.

### Architecture / parameterization
The modeling stack has three layers: individualized forward electric-field modeling from MRI and coil geometry; EEG source reconstruction using LCMV, dSPM, and eLORETA; and statistical models that relate N15 source magnitude and location to field type, dose, motor state, participant, and inverse-solver choice.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
TMS-EEG papers often interpret early evoked components as if they directly index the cortex exposed to the stimulation field. For N15 after M1 stimulation, that assumption had not been directly tested against individualized E-field maps. This paper asks whether the N15 source overlaps with the modeled field peak, and whether dose and motor state change that relationship.

### 2. What is the method?
The authors stimulate the left primary motor hand area in healthy participants while recording EEG, model the induced electric field from each subject's anatomy and coil placement, reconstruct the N15 source with three inverse solvers, and compare source-field maps against electric-field maps using mixed-effects and spatial-clustering analyses.

### 3. What is the method motivation?
If early TEP components are going to be used as target-engagement markers, the field needs to know whether they reflect local activation at the field maximum or rapid propagation into a connected circuit. That distinction matters for interpreting dose, state dependence, and clinical TMS biomarkers.

### 4. What data does it use?
The empirical dataset contains 16 healthy younger adults from 28 screened participants after exclusion for muscle-artifact problems. Each participant had structural MRI and TMS-EEG over left M1 across 12 conditions: six stimulation intensities crossed with rest versus active FDI contraction, with 100 pulses per condition when usable.

### 5. How is it evaluated?
Evaluation happens at several levels. The authors compare dose definitions for predicting peak N15 source magnitude; test whole-cortex spatial concordance between normalized E-field and N15 source maps; model peak and nodewise N15 source magnitude as a function of dose and state; and compare whether LCMV, dSPM, and eLORETA give convergent interpretations.

### 6. What are the main results?
The N15 source field is spatially distinct from the modeled TMS electric field. The electric field is strongest around the pre- and postcentral gyral crowns, while N15 source activity localizes more rostrally in left premotor and motor regions. As dose increases, N15 source magnitude rises and the spatial mismatch shrinks, suggesting either better signal-to-noise, recruitment of additional sources closer to M1, or both. N15 source magnitude is larger at rest than during active contraction. LCMV and dSPM behave more similarly and capture dose/state effects better than eLORETA in this parameter range, while all three solvers support the basic rostral-mismatch conclusion.

### 7. What is actually novel?
The useful novelty is the direct spatial comparison between a modeled stimulation field and an early TMS-evoked source component, with dose and state explicitly in the analysis. It is not just another TEP localization paper; it asks whether the measurement object is the stimulated site or a fast network consequence of stimulating that site.

### 8. What are the strengths?
- It tests a specific hidden assumption in TMS-EEG interpretation.
- It uses individualized head models rather than a purely generic field story.
- It compares multiple inverse solvers instead of trusting one localization method.
- It varies dose and motor state, which makes the result more useful for intervention design.
- The paper is appropriately cautious about the E-field not being identical to effective neuronal activation.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is small and healthy, with no clinical target or treatment outcome.
- Nine participants needed interpolated coil coordinates because neuronavigation data were corrupt, even though the authors ran control analyses.
- Peak E-field magnitude is only an approximation to effective stimulation; orientation, cytoarchitecture, axonal geometry, and excitability all matter.
- Source localization lacks intracranial ground truth.
- TMS-EEG is artifact-prone, and early components can still be affected by residual muscle, auditory, or somatosensory contributions.
- The title metadata appears to contain a typo ("rostrals to"), but the scientific claim is clearly that N15 sources are rostral to the field peak.

### 10. What challenges or open problems remain?
The major open problem is ground truth. Future work needs intracranial or otherwise stronger validation of how early TEP sources relate to actual neuronal recruitment. It also needs to test whether this E-field/source mismatch generalizes beyond M1, beyond N15, across clinical cohorts, and under repetitive or patterned stimulation.

### 11. What future work naturally follows?
Run the same framework on prefrontal, parietal, and clinical TMS targets; include orientation-specific field metrics; compare early and late TEP components; pair TMS-EEG with intracranial or high-resolution physiological readouts where possible; and test whether E-field/source coupling predicts treatment response or state-dependent target engagement.

### 12. Why does this matter for cabbageland?
Cabbageland cares about intervention logic, and this paper sharpens a key piece of it: the measurement readout is not automatically the stimulated tissue. If a TMS-EEG biomarker is partly a fast propagated circuit response, then targeting, dose, and state estimation need to model the pathway, not just the local field maximum.

### 13. What ideas are steal-worthy?
- Treat "target engagement" as a field-to-circuit measurement problem, not a local activation slogan.
- Compare modeled stimulation fields directly against physiological source maps before interpreting biomarkers.
- Separate direct exposure, early propagation, dose dependence, and state dependence in stimulation studies.
- Use multiple inverse solvers as a robustness check, while remembering that shared forward-model assumptions can create shared bias.
- Ask whether a biomarker is local, propagated, or mixed before using it to drive adaptive stimulation.

### 14. Final decision

Keep. This is a strong methods note because it catches a fragile interpretive shortcut in TMS-EEG and turns it into a concrete spatial, dose-dependent question. It does not settle TMS biomarkers, but it raises the standard for what future target-engagement claims should prove.
