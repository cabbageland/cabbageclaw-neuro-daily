# A personalized map of where, when, and how to stimulate the brain to elicit controlled responses

## Basic info

* Title: A personalized map of where, when, and how to stimulate the brain to elicit controlled responses
* Authors: Giovanni Rabuffo, Irene Acero-Pousa, Tomas Berjaga-Buisan, Gustavo Deco
* Year: 2026
* Venue / source: bioRxiv preprint
* Link: https://www.biorxiv.org/content/10.64898/2026.07.16.738930v1.full
* Date surfaced: 2026-10-08
* Why selected in one sentence: It turns stimulation variability into a model-search problem over target, timing, and paired-region strategy, with concrete predictions for closed-loop and circuit-level neuromodulation.

## Quick verdict

* Highly relevant

This is worth preserving because it gives a clean computational version of the question every serious stimulation protocol has to answer: not just where to stimulate, but in what brain state and with what circuit partner. The work is entirely in silico, trained on HCP resting-state fMRI rather than empirical stimulation responses, so it should not be treated as a clinical control result. Its value is as a map-making and hypothesis-generation framework for state-dependent neuromodulation.

## One-paragraph overview

The authors train a personalized neural-network surrogate model for each of 100 Human Connectome Project participants, using resting-state fMRI to predict the next whole-brain activity vector from recent activity history. They then virtually stimulate every cortical target at many time points and compare perturbed against unperturbed model trajectories from the same initial state. Three results matter: responses are larger from transmodal than unimodal cortex, lower whole-brain baseline activity produces larger and less variable responses, and bifocal stimulation can often make responses more reproducible than either single site alone. The practical message is not that this exact BOLD-level perturbation is a treatment recipe. It is that stimulation design should search target, state, and circuit pair jointly, then test those predictions empirically.

## Model definition

### Inputs
The model takes each participant's parcellated fMRI activity history: the three most recent whole-brain activity vectors across 450 regions, made from 400 cortical Schaefer parcels and 50 Tian subcortical parcels. Virtual perturbation analyses add a fixed increment to one cortical target, or to two cortical targets for bifocal stimulation, at selected model time points. The validation analyses also use HCP task-fMRI activation maps from motor, working memory, language, relational, social, emotion, and gambling tasks.

### Outputs
The personalized model predicts the next whole-brain activity vector. The perturbation pipeline outputs time-resolved effective-connectivity effects, global effect size, response variability, target-wise responsiveness, closed-loop timing comparisons, and bifocal pair maps showing whether joint stimulation is stronger or more reproducible than single-site stimulation.

### Training objective (loss)
Each participant's feedforward neural network is trained to minimize mean-squared one-step prediction error on resting-state fMRI, using an 80/20 train/test split, Adam, learning rate 5e-4, L2 weight decay 5e-5, batch size 64, and 50 epochs.

### Architecture / parameterization
The surrogate brain is a multilayer perceptron adopted from the Neural Perturbational Inference framework. It concatenates three recent 450-region activity vectors, uses two hidden layers with widths 900 and 360, ReLU nonlinearities, and a linear 450-region output. The perturbation model is not a device-specific TMS, DBS, or tES simulator; it is a generic transient increase in the modeled activity of selected parcels.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Identical stimulation can produce different brain responses across trials, even when target and parameters are fixed. The paper asks whether personalized models can explain and reduce that variability by mapping three controllable design axes: where stimulation is delivered, when it is delivered relative to ongoing brain state, and how two-region stimulation pairs interact.

### 2. What is the method?
Train one ANN surrogate brain per participant from resting-state fMRI, validate the models against resting functional connectivity, dynamic functional connectivity, and task-evoked activation structure, then run exhaustive virtual perturbations across cortical targets and time points. The authors compute response magnitude and variability for single-site stimulation, compare low-energy versus high-energy versus random timing, and search roughly 80,000 cortical region pairs for bifocal strategies.

### 3. What is the method motivation?
The motivating limitation is experimental infeasibility. A real stimulation session cannot probe every region at many brain states, and measured post-stimulation activity is confounded by the pre-stimulation trajectory. A surrogate model lets the authors compare perturbed and unperturbed futures from the same initial state, making state-dependent single-trial effects visible without averaging them away.

### 4. What data does it use?
The study uses resting-state fMRI from 100 healthy adults in the HCP Young Adult release. Each participant contributes four resting runs, for about 56 minutes of usable resting-state activity after preprocessing. The task-validation analysis uses the same participants' HCP task-fMRI data across seven cognitive tasks. The models are trained on resting-state data only.

### 5. How is it evaluated?
The models are checked against empirical resting-state functional connectivity, dynamic functional connectivity, participant-specific held-out prediction, and task-fMRI activation maps. The perturbation claims are evaluated in silico by comparing response magnitude and variability across targets, brain states, and region pairs. A linear autoregressive control model is used to show that the state-gating effect is a nonlinear property of the learned dynamics rather than an artifact of the perturbation pipeline.

### 6. What are the main results?
The subject-averaged empirical and simulated FC matrices correlate at r = 0.97, and participant-level simulated FC matches empirical FC at median r = 0.64. Dynamic FC distributions also match closely, with median KS distance 0.09. Response magnitude increases along the cortical hierarchy from unimodal to transmodal networks, with a median per-participant hierarchy correlation of rho = 0.82 and positive correlations in 97% of participants. Lower baseline whole-brain activity produces larger responses, with the energy-response correlation negative throughout the cohort. Timing stimulation to the lowest-energy 5% of states gives larger and less variable responses than random or high-energy timing. Bifocal stimulation is more reproducible than the better single site for 73% of pairs, stronger than the stronger single site for 31%, and both stronger and more reproducible for 24%.

### 7. What is actually novel?
The useful novelty is the joint map. Prior work already says stimulation is state dependent; this paper builds personalized surrogate brains and searches target, timing, and paired-target effects in the same framework. It also turns effective connectivity from a static matrix into a state-conditioned object, which is exactly the move needed for closed-loop intervention logic.

### 8. What are the strengths?
The paper is disciplined about validation for a model-only study. It checks static FC, dynamic FC, subject specificity, task activation reconstruction, nonlinear state gating, and robustness to perturbation amplitude. It also gives testable predictions rather than vague personalization language: stimulate low-energy states for larger and less variable effects, expect transmodal targets to produce larger whole-brain responses, and search bifocal pairs for reproducibility gains.

### 9. What are the weaknesses, limitations, or red flags?
The central limitation is that no real stimulation data are used to validate the predictions. The perturbation is a fixed synthetic bump in BOLD-state space, not a realistic model of TMS, DBS, tES, focused ultrasound, or intracranial stimulation. The fMRI timescale is slow relative to actual stimulation physiology, and HCP-quality resting scans are longer and cleaner than typical clinical scans. The study also measures variability mainly through response magnitude, leaving topographic variability as an open problem.

### 10. What challenges or open problems remain?
The predictions need empirical tests with concurrent TMS-EEG, TMS-fMRI, intracranial stimulation, or other systems that can measure evoked effective connectivity. The field also needs to know how much subject data is enough to fit a stable personalized model, how model predictions degrade under clinical data quality, and whether the same framework works with faster modalities such as EEG, MEG, sEEG, or ECoG.

### 11. What future work naturally follows?
The most natural next step is a prospective experiment that triggers stimulation during model-defined low-energy states and compares response magnitude, variability, and topography against random timing. A second line is modality-specific perturbation modeling, where the synthetic bump is replaced with TMS-like, DBS-like, or tES-like perturbation kernels. A third line is using bifocal predictions to preselect paired targets for multifocal TMS or multi-electrode stimulation.

### 12. Why does this matter for cabbageland?
Cabbageland cares about intervention logic, not just biomarkers. This paper gives a useful recipe for asking whether an intervention target is controllable under the current brain state and whether a second node can stabilize the response. It also links network neuroscience to device design: target choice, state estimation, and stimulation geometry should be optimized together, not treated as separate folklore layers.

### 13. What ideas are steal-worthy?
Treat baseline state as a gain-control variable, not nuisance variance. Compare perturbed and unperturbed futures from the same initial condition whenever possible. Rank targets by both effect size and reproducibility. Search paired nodes for variance reduction even when single-node targeting looks sufficient. Use task activation maps as an external sanity check for whether a resting-state surrogate model has learned useful effective connectivity.

### 14. Final decision
Preserve. The paper is not a clinical neuromodulation result and should not be oversold, but it is a strong computational scaffold for designing state-aware and circuit-aware stimulation experiments. It belongs next to the existing pre-stimulus-state and dynamic-FC stimulation notes as part of the "stimulation variability is controllable structure" cluster.
