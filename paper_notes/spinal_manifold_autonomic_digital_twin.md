# Recurrent latent dynamics in spinal circuits enable a digital twin of autonomic state transitions

## Basic info

* Title: Recurrent latent dynamics in spinal circuits enable a digital twin of autonomic state transitions
* Authors: Minhye Choo; Mingeun Cho; Jiho Lee; Changhwa Oh; Sungjun Hong; Chaewon Heo; Young-Min Shon; Sungmin Park
* Year: 2026
* Venue / source: iScience; first published October 26, 2026
* Link: https://doi.org/10.1016/j.isci.2026.117971
* Date surfaced: 2026-11-13
* Why selected in one sentence: It links invasive spinal population recordings to autonomic state trajectories, while exposing a concrete gap between a useful latent representation and a claimed recurrent digital twin.

## Quick verdict

* Useful

Preserve the population-phase representation and the model-audit lesson, not an established closed-loop controller. Primary full text supports stimulation-locked neural/BP organization, but the inspected implementation disables recurrent coupling and evaluates same-trial reconstruction. “Recurrent digital twin” is therefore a stronger claim than the inspected example earns; a numerical reproduction would be needed to resolve the complete implementation, not merely its wording.

## One-paragraph overview

The authors electrically stimulate the spinal intermediolateral nucleus (IML), simultaneously record sorted neuronal activity and arterial blood pressure, and use Isomap to organize heterogeneous neural responses into a low-dimensional loop associated with pressure decline and recovery. They align individual manifolds using geometry and a measured BP reference, then fit a FORCE-style model to reconstruct BP and discuss neural-response similarity. This is a potentially useful autonomic-state representation. It does not establish that the embedding identifies biological recurrent connectivity, that the model runs autonomously from a stimulation command, or that it generalizes to an unseen intervention or animal.

## Model definition

### Inputs

Extracellular spike trains are converted to firing rates with animal-specific 0.2–0.6-second windows and Gaussian smoothing. Isomap uses a nearest-neighbor graph (`k = 5`, six embedding dimensions reported); the model consumes the first two latent coordinates. The inspected FORCE example interpolates a recorded trial to 240 samples and standardizes latent inputs and BP using that trial. Although Figure 6 describes binary stimulation input and feedback, the methods/example instead specify measured latent features as the driving input.

### Outputs

The paper specifies a BP readout and a separate neural-response readout. The inspected example trains readout weights against BP-derived targets and computes a flattened BP prediction; it is not a demonstrated stimulation-setting policy. There is no safety constraint, set-point controller, or validated counterfactual response interface.

### Training objective (loss)

Isomap aims to preserve shortest-path distances on the firing-rate neighbor graph in a low-dimensional embedding. The FORCE-style stage updates readout weights by recursive least squares to reduce output error; the paper defines error as predicted minus observed output and keeps reservoir/input weights fixed. Comparator regressions include BP reconstruction and sliding-window ridge regression. The CNN code uses Adam with mean-squared error and validation-based early stopping. These objectives fit observations; none directly optimizes physiological control or establishes causal identification.

### Architecture / parameterization

A 200-unit tanh reservoir with fixed random recurrent matrix `J`, fixed latent-input projection `Wz`, and learned linear readouts. The stated state equation contains a leak, `g J tanh(x)`, and `Wz X(t)`.

**The consequential implementation detail:** Methods reports `g = 0`, `dt = tau = 0.1`; the inspected FORCE code agrees. Its Euler update therefore simplifies to `x_next = Wz X_current`: the recurrent matrix contributes nothing, and the old state cancels. Evaluation explicitly computes `tanh(Wz @ X)`, then applies the learned readout. In this example, that is fixed nonlinear-feature regression, not evidence that recurrent neural interactions were learned. This is a static code/algebra audit, not a claim that every unpublished or uninspected implementation behaves identically.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

How can heterogeneous spinal neural responses be turned into a useful representation of an autonomic physiological transition, rather than averaging away neurons with opposite response signs?

### 2. What is the method?

Record IML units and arterial BP during focal spinal stimulation; embed population firing rates with Isomap; examine loop topology and phase-dependent BP relationships; align individual manifolds; compare BP reconstruction using latent features, individual neurons, linear regression, and a CNN. Fit a FORCE-style readout and compare real/model response-feature clusters.

### 3. What is the method motivation?

The same BP can occur on its falling or recovering limb. A population trajectory may distinguish these histories better than a scalar firing-rate average. That motivates phase-aware state estimation; it does not require assuming that a circular plot proves biological recurrence.

### 4. What data does it use?

Acute recordings from male Sprague-Dawley rats, 8–10 weeks old, under urethane anesthesia after isoflurane induction. A 16-channel probe yielded roughly 30–50 sorted units per animal; stimulation targeted spinal segments T13–L1 at 40 Hz. Sessions included a five-minute baseline and 60-second stimulation. Arterial BP came from a femoral catheter.

Results refers to eight rats in places, while major figure captions/statistical comparisons and alignment analyses use seven; an exclusion explanation was not established from the inspected text. Do not silently treat neurons or time bins as independent animal replications.

### 5. How is it evaluated?

Spike correlations versus time-shuffled controls; embedding comparisons with PCA, LLE, and an autoencoder; persistent homology; BP association/reconstruction; cross-animal alignment; and real/model response-feature clustering. Most statistical comparisons use seven animals. Persistent-homology significance is described as a representative-trial descriptive analysis.

The alternative-embedding BP regression is explicitly in-sample. The inspected FORCE example trains and scores on the same recorded trial, with no held-out animal/trial split. The CNN comparator splits each trial temporally 80/20 for training/validation, but later reports a full-trial score. Thus the inspected scripts do not establish a clean, common held-out benchmark. RidgeCV choosing a local regularization strength is not an external test of the full pipeline.

### 6. What are the main results?

- Stimulation evokes a reproducible BP decrease alongside heterogeneous unit responses; population activity contains structured coactivation and an approximately circular latent trajectory.
- Manifold-phase BP reconstruction outperforms the paper's neuron-based comparators; the relevant figure reports R-squared, MAE, and mutual information across seven animals, with paired-test `p < 0.001`.
- Geometric alignment produces similarly oriented BP-referenced trajectories, but reservoirs remain animal-specific.
- Figure 6 reports mean “prediction accuracy” of 0.82 for the neural dynamic model, 0.75 for linear regression, and 0.65 for CNN, with paired comparisons `p < 0.05`. These are reported reconstruction results, not independently reproduced prospective forecasts.
- The inspected implementation provides a direct counterweight to the mechanistic interpretation: its recurrent coupling is inactive, and evaluation does not require recurrent state evolution.

### 7. What is actually novel?

The application of population-manifold analysis to spinal autonomic transitions and the explicit phase/physiology alignment are the useful domain contributions. Isomap, reservoir computing, and recursive least squares are not new. Neither a causal recurrent circuit model nor an intervention-validating digital twin is established by the inspected evidence.

### 8. What are the strengths?

Simultaneous invasive neural and physiological recordings during a perturbation; analysis of response heterogeneity rather than only a mean; explicit embedding comparators; and public code that makes important implementation checks possible. Falling/recovering phase is a concrete, testable state-estimation idea.

### 9. What are the weaknesses, limitations, or red flags?

- **Recurrence mismatch:** Figure 6 emphasizes feedback and recurrent generation; methods/code set `g = 0`, and the inspected evaluation is a direct feature-map calculation. Architecture naming cannot settle that contradiction.
- **Reconstruction versus prediction:** Same-trial fitting, whole-trial preprocessing, and mismatched comparator protocols leave generalization and architecture superiority unresolved.
- **Calibration versus transfer:** Alignment uses a measured BP extremum to orient the axes. That is not evidence that an unseen subject can be aligned without physiological labels.
- **Geometry versus mechanism:** A stimulus-locked excursion can form a loop without being a stable autonomous oscillator. Common input and a stimulus clock remain alternatives to circuit-specific recurrent dynamics. Isomap is also evaluated on geodesic preservation, closely aligned with its fitting goal.
- **Causality:** Electrical stimulation perturbs the system, but latent/neuron correlations and UMAP cluster overlap do not identify cell types, synaptic signs, causal pathways, or biological connectivity.
- **Data realism:** Small acute anesthetized male-only cohort, variable smoothing, inconsistent seven/eight reporting, and no demonstrated chronic stability, disease cohort, or independently validated human transfer.

### 10. What challenges or open problems remain?

Can phase predict future BP beyond elapsed time and recent BP history? Is it stable under a different stimulation frequency, intensity, anesthesia state, electrode sample, or day? What is the exact executable specification behind the recurrence/feedback narrative? Can calibration be separated from testing?

### 11. What future work naturally follows?

Use held-out trials/animals with training-only preprocessing and an explicit out-of-sample embedding. Compare stimulus-clock kernels, BP autoregression, matched-capacity random features, and genuinely active recurrent models under identical splits. Test prospective responses to unseen stimulation settings, then a safety-constrained BP controller in awake longitudinal recordings. Include female animals and uncertainty under electrode/unit drift.

### 12. Why does this matter for cabbageland?

It connects invasive state estimation, latent dynamics, and intervention design without needing a psychiatric endpoint to be useful. More importantly, it makes a reusable control-paper audit concrete: inspect what drives the model, which weights actually influence state evolution, and whether evaluation uses information unavailable at deployment.

### 13. What ideas are steal-worthy?

Represent physiological direction/history rather than only amplitude; explicitly compare different phases at matched BP; benchmark neural phase against a stimulus clock; and audit the implemented state equation before crediting a recurrence mechanism. Treat latent geometry, transition prediction, stimulation-response identification, and closed-loop benefit as four separate gates.

### 14. Final decision

Keep as a useful representation-and-audit note, not as a validated recurrent digital twin or treatment result. Reading basis: primary [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13734804/) plus targeted static inspection of the public README, FORCE example, CNN comparator, and BP-regression code at commit `cc9509260caad6b5032c5d11225ef6618fa621e9`. The decisive [FORCE example](https://github.com/Choo-Minhye/spinal-manifold-digital-twin/blob/cc9509260caad6b5032c5d11225ef6618fa621e9/spinal-manifold-digital-twin/revi_forceregression.py#L72) and [evaluation](https://github.com/Choo-Minhye/spinal-manifold-digital-twin/blob/cc9509260caad6b5032c5d11225ef6618fa621e9/spinal-manifold-digital-twin/revi_forceregression.py#L143) make the limitation inspectable. No raw-data audit, supplementary-asset audit, code execution, or numerical reproduction was performed.
