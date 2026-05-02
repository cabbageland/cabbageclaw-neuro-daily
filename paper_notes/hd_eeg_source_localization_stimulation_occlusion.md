# Spatial Effects of Electrode Configurations and Source Depth in EEG Source Localization: Implications for Concurrent Noninvasive Brain Stimulation with HD-EEG

## Basic info

* Title: Spatial Effects of Electrode Configurations and Source Depth in EEG Source Localization: Implications for Concurrent Noninvasive Brain Stimulation with HD-EEG
* Authors: Authors not fully extracted from accessible abstract metadata
* Year: 2026
* Venue / source: IEEE Transactions on Neural Systems and Rehabilitation Engineering
* Link: https://pubmed.ncbi.nlm.nih.gov/42048205/
* Date surfaced: 2026-05-02
* Why selected in one sentence: It directly tests a hidden but crucial bottleneck for concurrent stimulation-plus-EEG systems, namely what happens when the electrodes closest to the neural source are the ones you lose or distort.

## Quick verdict

* Highly relevant

This is not glamorous, but it is exactly the kind of methods paper that should quietly change how people design stimulation and sensing experiments. The result, that near-source electrode degradation hurts badly while distal loss barely matters, is practical and high leverage. The main limitation is that the evidence comes from a small epilepsy dataset and a single-pulse ground-truth setup, so the exact resilience rankings may shift in noisier real-world protocols.

## One-paragraph overview

The paper evaluates how electrode loss or interpolation affects EEG source localization when high-density EEG is used alongside brain stimulation paradigms that can physically obstruct electrodes near the target. Using simultaneous stereoelectroencephalography and two-hundred-fifty-six-channel EEG from seven epilepsy patients, with single-pulse intracranial stimulation providing ground-truth source locations, the authors compare eight inverse methods across scenarios where electrodes close to or far from the source are removed or interpolated. The central result is simple and useful: damage to proximal electrodes degrades localization and spatial precision substantially, whereas distal electrode manipulation matters much less. Sparse and parametric methods, especially MxNE, dipole fitting, and RAP-MUSIC, appear more resilient than common distributed methods under this kind of localized sensor loss.

## Model definition

### Inputs
High-density EEG recordings, simultaneous stereoelectroencephalography ground truth, known source locations from single-pulse electrical stimulation, and electrode-manipulation scenarios involving proximal or distal removal or interpolation.

### Outputs
Estimated source-localization solutions, especially peak localization error and spatial dispersion under different inverse methods and electrode-degradation conditions.

### Training objective (loss)
This is not presented as a trainable predictive model in the accessible abstract. The practical objective is inverse-solution accuracy and spatial compactness under realistic electrode-loss conditions.

### Architecture / parameterization
A comparative evaluation of eight inverse methods spanning distributed approaches such as weighted minimum norm, dSPM, sLORETA, and eLORETA, sparse methods such as MxNE and Champagne, and parametric methods such as dipole fitting and RAP-MUSIC.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Concurrent noninvasive stimulation and EEG often obstruct or degrade electrodes near the intended neural source, but many studies treat that as a minor implementation detail rather than a core measurement problem.

### 2. What is the method?
Use a dataset with simultaneous implanted and scalp recordings plus known stimulation-ground-truth locations, then systematically remove or interpolate proximal versus distal electrodes and compare how different inverse methods degrade.

### 3. What is the method motivation?
If source localization changes dramatically when target-adjacent electrodes are lost, then stimulation-plus-sensing pipelines can generate overconfident but distorted state estimates and target-engagement claims.

### 4. What data does it use?
The Localize-MI dataset, consisting of simultaneous stereoelectroencephalography and two-hundred-fifty-six-channel EEG from seven epilepsy patients, with single-pulse electrical stimulation through implanted electrodes used as source ground truth.

### 5. How is it evaluated?
By comparing peak localization error and spatial dispersion across eight inverse methods under baseline, proximal removal, proximal interpolation, distal removal, and distal interpolation scenarios, using linear mixed-effects models that incorporate source depth and electrode-to-source distance.

### 6. What are the main results?
Proximal electrode degradation significantly worsens localization error and spatial dispersion, distal degradation has little effect, dipole fitting and RAP-MUSIC show lower localization error than weighted minimum norm, MxNE is also resilient, and dSPM has the most stable spatial dispersion among distributed methods.

### 7. What is actually novel?
The novelty is not a new inverse method. It is the explicit, ground-truth-based quantification of how spatially localized electrode loss interacts with source depth and inverse-method choice in the exact kind of concurrent stimulation context where this problem is usually hand-waved.

### 8. What are the strengths?
- Uses implanted-stimulation ground truth instead of only simulation.
- Tests a practical failure mode that really appears in stimulation experiments.
- Compares multiple inverse-method families rather than defending one favorite algorithm.
- Produces immediately usable design guidance.

### 9. What are the weaknesses, limitations, or red flags?
- Small cohort of seven epilepsy patients.
- Single-pulse stimulation ground truth may not fully represent ongoing or naturalistic brain activity.
- Abstract-level access leaves the exact method margins and robustness details unclear.
- Findings may depend on montage geometry and on the specific forward models used.

### 10. What challenges or open problems remain?
Whether the same degradation pattern holds for ongoing closed-loop settings, different montages, more severe stimulation artifacts, deeper sources, and multimodal pipelines that combine EEG with MRI-informed priors.

### 11. What future work naturally follows?
Benchmark concurrent TMS-EEG or tES-EEG protocols under explicit sensor-occlusion designs, integrate geometry-aware priors with these degradation results, and test whether protocol choices based on these findings improve downstream state estimation or adaptive control.

### 12. Why does this matter for cabbageland?
Because stimulation logic depends on measurement logic. If the sensing layer is systematically warped by hardware occlusion near the target, then targeting, biomarker, and closed-loop claims built on that sensing layer may be much weaker than they look.

### 13. What ideas are steal-worthy?
- Treat near-target sensor occlusion as a first-class experimental variable.
- Prefer inverse methods based on demonstrated resilience under localized electrode loss, not generic popularity.
- Benchmark state-estimation pipelines against realistic hardware-occlusion scenarios before trusting adaptive-control claims.
- Separate distal missing-sensor problems from proximal missing-sensor problems, because they are not equivalent.

### 14. Final decision
Keep. This is a strong methods note because it attacks a real hidden bottleneck in concurrent neuromodulation-plus-sensing systems and gives concrete guidance rather than decorative algorithm branding.
