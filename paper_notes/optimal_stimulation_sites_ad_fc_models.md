# Optimal stimulation sites are not the most affected: personalised models of resting-state fMRI in Alzheimer's disease

## Basic info

* Title: Optimal stimulation sites are not the most affected: personalised models of resting-state fMRI in Alzheimer's disease
* Authors: Cristiano Capone, Enza Cece, Andrea Ciardiello, Guido Gigante, Evaristo Cisbani, Maurizio Mattia
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2607.24356
* Date surfaced: 2026-07-30
* Why selected in one sentence: It makes a sharp targeting claim that a lot of neuromodulation papers dodge, namely that the site which looks most diseased in a network model is not necessarily the site where focal stimulation has the most therapeutic leverage.

## Quick verdict

* Highly relevant

This is worth preserving because it asks a real control question instead of stopping at classification. The paper builds a subject-specific reservoir model of resting-state fMRI in Alzheimer's disease, shows that the disease signal behaves as a distributed connectivity alteration rather than a focal lesion surrogate, and then uses the same fitted model to ask where a single-site intervention should actually land. The answer is the useful part: pathology magnitude and stimulation leverage dissociate cleanly. The main caution is that everything therapeutic here is still in silico, with only modest case-control discrimination and no real intervention outcome yet.

## One-paragraph overview

The paper fits individualized reservoir-computing models to resting-state fMRI from controls and Alzheimer's disease patients, using 121 cortical and subcortical parcels and a linear read-out trained on each subject's dynamics. The fitted models reconstruct subject-specific lagged functional connectivity well enough to be identifiable across people and to classify Alzheimer's disease versus controls at modest above-chance accuracy. The paper then makes the move that matters for neuromodulation: it perturbs each fitted model in silico and compares two targeting logics. If you correct or stimulate the sites whose read-out deviates most from controls, you mostly hit subcortical and limbic nodes and fail to normalize the disease discriminant with plausible focal stimulation. If you instead select each patient's site by how much a resonant drive improves the disease discriminant, single-site personalized targets, usually cortical and heterogeneous across patients, can nearly completely reclassify the model state toward control. That is not clinical proof, but it is a useful demonstration that disease salience and intervention salience are not the same object.

## Model definition

### Inputs
Resting-state fMRI BOLD time series from cognitively unimpaired controls and Alzheimer's disease patients, parcellated into 121 cortical and subcortical regions; PCA-projected subject signals; and stimulation-site and amplitude choices for the in-silico perturbation analyses.

### Outputs
Subject-specific read-out weight matrices, synthetic closed-loop reconstructions of each subject's lagged functional connectivity, Alzheimer's-versus-control discriminant scores, rankings of pathology-like versus discriminant-aligned stimulation targets, and simulated responses to open-loop or adaptive stimulation.

### Training objective (loss)
The paper does not use an end-to-end clinical prediction loss. It fits a linear read-out on top of a fixed recurrent reservoir so the closed-loop model reproduces each subject's dynamics and lagged functional connectivity, then evaluates downstream classification and stimulation effects in separate analyses.

### Architecture / parameterization
A fixed recurrent reservoir-computing model with per-subject linear read-out weights, plus downstream low-dimensional embeddings and discriminants built from either the geometry of the fitted read-out matrices or the lagged functional connectivity of the model reconstructions.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to answer a targeting question that observational network papers usually leave vague. If Alzheimer's disease is a distributed connectivity disorder, can that alteration be reduced to a few focal sites for stimulation, or is the useful target something else entirely? The paper wants a causal, counterfactual answer rather than another group-average disease map.

### 2. What is the method?
The authors fit a subject-specific reservoir model to resting-state fMRI so that each person's closed-loop reconstruction reproduces their lagged functional connectivity. They then derive two disease read-outs from the fitted model, use them for Alzheimer's-versus-control discrimination, and finally perturb the fitted models in silico with either distributed corrections or focal resonant drives. The key comparison is between choosing targets by pathology magnitude versus choosing them by improvement in the disease discriminant.

### 3. What is the method motivation?
Targeting logic gets sloppy when the field assumes the most abnormal node is automatically the best stimulation site. That intuition might be wrong in a distributed dynamical system where leverage depends on controllability and propagation, not only on local abnormality. The paper is motivated by that gap.

### 4. What data does it use?
The cohort contains 557 control resting-state fMRI sessions and 145 Alzheimer's disease sessions, with analyses focused on 143 control patients and 40 Alzheimer's patients for some classification steps. The data are parcellated into 121 regions spanning cortical and subcortical territory. No real stimulation data are used; the intervention results come from perturbing the fitted models.

### 5. How is it evaluated?
Evaluation happens at three levels. First, the authors test whether the fitted models reconstruct subject-specific functional connectivity and remain identifiable across individuals. Second, they test whether model-derived read-outs can classify Alzheimer's disease versus controls with cross-validation. Third, they test whether different in-silico stimulation strategies move the disease discriminant toward the control distribution.

### 6. What are the main results?
- The reservoir models reconstruct individual lagged functional connectivity well enough to be subject-identifiable rather than generic.
- Model-derived read-outs classify Alzheimer's disease versus controls at modest but above-chance accuracy, roughly 0.66 to 0.70 AUROC, below structural atrophy benchmarks but in the same general range as leakage-free functional-connectivity baselines.
- Distributed correction of the full read-out toward the control template can revert the disease discriminant, but focal correction of the most-deviant sites fails within plausible amplitudes.
- The anatomically most-deviant sites cluster in subcortical and limbic regions, especially pallidum, nucleus accumbens, brainstem, and amygdala, but these are not the best focal intervention sites.
- Choosing a single site by its discriminant effect under resonant drive works far better, with highly personalized mostly cortical targets and near-complete model reclassification.
- A simple causal online controller reaches nearly the same in-silico reversal while reducing mean stimulation amplitude by about 44 percent.

### 7. What is actually novel?
The useful novelty is not the Alzheimer's classifier. That part is only modest. The real novelty is the explicit dissociation between pathology-ranked sites and therapeutically effective sites inside the same generative model, plus the demonstration that a discriminant-aligned focal target can outperform the obviously affected nodes.

### 8. What are the strengths?
- It asks a real intervention question instead of dressing up classification as targeting.
- The fitted models are individual and identifiable, which matters if the targeting claim is going to be personalized.
- The paper includes a strong negative control: focal correction of the most-deviant sites fails.
- It separates distributed correction from physically realizable focal drive instead of pretending they are the same thing.
- The adaptive-controller analysis is a good touch because it moves the work closer to closed-loop reasoning rather than one-shot oracle stimulation.

### 9. What are the weaknesses, limitations, or red flags?
- The clinical signal is still entirely in silico. No human stimulation experiment validates these targets.
- The disease classifier is only modest, so the whole control story depends on a representation that is informative but not especially strong diagnostically.
- Resting-state BOLD is slow and indirect, which limits what "resonant" control means biologically.
- The paper openly admits that the dissociation between pathological sites and effective sites could reflect model geometry as much as disease biology.
- Reclassification across a model decision boundary is not the same thing as improving cognition or symptoms.

### 10. What challenges or open problems remain?
The big open problem is whether model-prescribed targets survive contact with real stimulation physics and real patient outcomes. The field also still needs better biomarkers than slow fMRI alone, more external validation across cohorts and scanners, and a clearer bridge from in-silico discriminant reversal to clinically meaningful change.

### 11. What future work naturally follows?
The next obvious step is prospective testing of model-informed targets in actual noninvasive Alzheimer's neuromodulation, ideally against pathology-map targets and simple anatomical heuristics. It also makes sense to combine this framework with structural connectivity, electrophysiology, or ongoing state estimates so that the control signal is less BOLD-bound and more intervention-ready.

### 12. Why does this matter for cabbageland?
Because it makes a distinction the archive keeps needing: the most abnormal-looking place in a network is not automatically the best place to intervene. That is relevant far beyond Alzheimer's disease. It sharpens how to think about targeting, controllability, and patient-specific leverage in any distributed brain disorder.

### 13. What ideas are steal-worthy?
- Separate pathology magnitude from therapeutic leverage instead of using one as a lazy proxy for the other.
- Demand negative controls where the obviously diseased node is tested and shown to fail.
- Use a perturbable generative model as a target-selection engine rather than treating prediction and intervention as separate worlds.
- Frame adaptive stimulation around a disease-relevant state variable instead of a purely local signal if the model can support it.

### 14. Final decision
Preserve. This is one of the cleaner recent examples of a whole-brain modeling paper earning a targeting claim by showing why the intuitive target fails and by proposing a more intervention-legible alternative.
