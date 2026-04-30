# Effective correction of extreme capacitive artifacts in TMS-EEG via windowed detrending

## Basic info

* Title: Effective correction of extreme capacitive artifacts in TMS-EEG via windowed detrending
* Authors: Alberto Arturo Vergani et al.
* Year: 2026
* Venue / source: Journal of Neural Engineering
* Link: https://pubmed.ncbi.nlm.nih.gov/42055012/
* Date surfaced: 2026-04-30
* Why selected in one sentence: It addresses a real measurement bottleneck in TMS-EEG by showing that standard ICA cleanup can fail badly under severe capacitive artifact conditions and that a windowed detrending approach may hold up better.

## Quick verdict

* Useful

This is a solid infrastructure paper. It matters because TMS-EEG often looks persuasive right up until the artifacts get bad enough to expose how fragile the preprocessing chain is. The useful contribution here is the claim that modeling charging and discharging phases separately makes offline recovery more robust in the ugly regimes where simpler approaches and ICA start collapsing.

## One-paragraph overview

The paper evaluates model-based detrending methods for removing capacitive artifacts from TMS-EEG recordings, especially when online hardware mitigation has not prevented large post-stimulus deflections and drifts. The authors compare non-windowed detrending against windowed approaches that separately fit the rise and decay phases of the artifact, and benchmark these methods against an ICA-based cleaning pipeline across datasets from two centers and multiple hardware configurations. The headline result is that ICA works reasonably for mild artifacts but degrades badly when artifacts become moderate or severe, while windowed detrending, especially windowed polynomial detrending, more robustly preserves physiological signal structure in those harder cases. This is measurement plumbing, but it is important plumbing.

## Model definition

### Inputs
TMS-EEG recordings contaminated by capacitive artifacts under different hardware setups and artifact severities, including the post-stimulus charging and discharging phases of the artifact.

### Outputs
Artifact-corrected EEG signals intended to preserve underlying TMS-evoked physiological components and reduce residual capacitive contamination.

### Training objective (loss)
This is not described as a trainable model in the accessible abstract. The practical objective is accurate artifact removal with preservation of physiological signal structure across mild to extreme artifact conditions.

### Architecture / parameterization
A signal-processing pipeline comparing non-windowed detrending and windowed detrending models, with the windowed versions separately parameterizing artifact rise and decay.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
TMS-EEG can be dominated by capacitive artifacts at the electrode-scalp interface, and standard cleanup methods may fail exactly when the data are most contaminated.

### 2. What is the method?
Fit artifact trends with detrending models, especially windowed models that separately capture charging and discharging phases, and compare them against non-windowed detrending and ICA-based cleanup.

### 3. What is the method motivation?
Capacitive artifacts are nonlinear and phase-structured, so treating the full artifact with one global correction can be too crude, especially in severe cases.

### 4. What data does it use?
Multiple TMS-EEG datasets from two centers using different hardware configurations and spanning mild, moderate, and extreme capacitive artifact conditions.

### 5. How is it evaluated?
By comparing the ability of each method to suppress artifact contamination while preserving physiological components across different severity regimes and hardware configurations.

### 6. What are the main results?
ICA is adequate for mild artifacts but insufficient for moderate and severe cases, sometimes suppressing physiological signal or leaving heavy residual contamination. Windowed detrending performs more robustly, with windowed polynomial detrending showing a slight edge.

### 7. What is actually novel?
The useful novelty is not another generic denoising method. It is the explicit segmentation of charging and discharging phases to improve correction in the extreme-artifact regime where commonly used cleanup approaches break.

### 8. What are the strengths?
- Focuses on the ugly cases that actually break pipelines.
- Multi-center and multi-hardware comparison is better than one-lab benchmarking.
- Compares against a widely used ICA-based reference.
- Keeps physiological preservation in view rather than only visual denoising.

### 9. What are the weaknesses, limitations, or red flags?
- This is still offline correction, not a full end-to-end validation of downstream inference.
- The accessible text does not detail quantitative performance margins.
- Better artifact suppression does not automatically prove better biological interpretation.
- It remains dependent on acquisition quality and does not remove the need for good hardware practice.

### 10. What challenges or open problems remain?
Validation on broader hardware ecosystems, impact on downstream TMS-evoked biomarkers, integration with online monitoring, and uncertainty quantification when preprocessing choices materially change the inferred physiology.

### 11. What future work naturally follows?
Benchmark artifact correction by downstream biomarker stability and reproducibility, combine model-based detrending with acquisition-aware priors, and test whether severe-artifact salvage changes clinical or mechanistic conclusions in real TMS-EEG cohorts.

### 12. Why does this matter for cabbageland?
Because claims about cortical excitability, connectivity, or target engagement from TMS-EEG are only as good as the cleanup stack, and severe artifacts are exactly where bad preprocessing can quietly turn into fake mechanism.

### 13. What ideas are steal-worthy?
- Benchmark preprocessing on hard cases, not only neat ones.
- Model structured artifact phases separately when physics suggests distinct regimes.
- Treat signal-cleaning choices as part of the scientific inference stack.
- Demand downstream robustness, not just prettier traces.

### 14. Final decision
Keep. This is a worthwhile methods note because it addresses a common hidden failure mode in TMS-EEG and appears to improve robustness where standard cleanup pipelines become unreliable.