# Activity-dependent epidemic spreading on multiscale brain networks predicts Alzheimer's disease progression

## Basic info

* Title: Activity-dependent epidemic spreading on multiscale brain networks predicts Alzheimer's disease progression
* Authors: Christoffer G. Alexandersen, Suman S. Kulkarni, Jessica T. Davis, Sebastian N. Roemer-Cassiano, Nicolai Franzmeier, Dani S. Bassett
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2608.12647
* Date surfaced: 2026-08-15
* Why selected in one sentence: It upgrades pathology-spread modeling from anatomy-only diffusion into an activity-weighted threshold-and-eigenmode problem, then actually checks that framing against longitudinal human tau-PET.

## Quick verdict

* Highly relevant

This is a keep from full-text arXiv HTML inspection. The paper is not a patient-specific intervention model, and it does not solve Alzheimer's progression in any operational sense. It is still worth preserving because it makes neuronal activity part of the spreading operator itself, then shows that the resulting spectral quantities track later tau progression better than plain structure alone. That is a real conceptual upgrade for disease-spread and control-style thinking.

## One-paragraph overview

The paper treats neurodegenerative spread as a network epidemic whose transmission depends not only on structural connectivity but also on neuronal activity. It couples a general node-activity process to susceptible-infected-susceptible spreading, derives how activity changes the epidemic threshold and the dominant spreading mode, and then applies that framework to human imaging. Regional FDG-PET is used as a proxy for neuronal activity, a group structural connectome defines the spreading network, and longitudinal tau-PET measures later pathology accumulation. The main claim is that activity-weighted spectral corrections capture both *where* tau grows next and, more modestly, *how easily* pathology becomes widespread.

## Model definition

This is not a trainable deep-learning paper. The central model is a coupled dynamical-system and spectral-perturbation framework for activity-dependent pathological spreading on a weighted brain network.

### Inputs
A weighted structural connectome, node-level activity states or their region-level proxies, spreading parameters for transmission and clearance, a quiet-active-quiet neuronal activity process, normative regional FDG-PET mean and variance, regional amyloid centiloid summaries for one correction variant, and longitudinal tau-PET measurements for evaluation.

### Outputs
An activity-dependent epidemic threshold, an activity-dependent dominant eigenmode, correction terms that show how mean activity and unresolved within-region activity variation reshape spreading, fitted dominant-mode variants for regional tau-progression prediction, and subject-level inverse-threshold scores associated with tau extent.

### Training objective (loss)
There is no machine-learning loss for the core theory. The main model is analytical. In the human-data section, the authors fit amplitudes for first- and second-order eigenmode corrections to maximize agreement with later tau accumulation, but the paper is not presented as a general predictive model trained with a standard supervised objective.

### Architecture / parameterization
A coupled susceptible-infected-susceptible spreading process and quiet-active-quiet activity process run on a weighted directed network. The analysis then uses perturbation theory, Perron-mode reasoning, and a multiscale quotient-network decomposition to estimate how activity shifts both the leading eigenvalue and dominant mode of the spreading operator.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to explain why pathological spread in Alzheimer's disease is not fully captured by anatomy-only connectome models. Structure tells you where spread *can* go, but not why some seeds remain localized while others become widespread, or why some regions accumulate pathology faster than others. The paper argues that neuronal activity is one missing ingredient because it can modulate transmission along those structural routes.

### 2. What is the method?
The authors couple a generic node-activity process to susceptible-infected-susceptible dynamics on a structural brain network. That produces an activity-weighted spreading operator whose leading eigenvalue gives an epidemic threshold and whose dominant eigenmode gives the initial direction of growth. They derive first- and second-order perturbative corrections, validate them with stochastic simulations on synthetic multiscale networks, and then test the resulting quantities against longitudinal human FDG-PET, amyloid, and tau-PET data from ADNI, HABS, and A4.

### 3. What is the method motivation?
Experimental work suggests neuronal firing promotes protein release and transneuronal propagation, so pathology should not spread according to anatomy alone. If activity changes effective transmission, then the right summary objects are not just connectivity weights but activity-modified thresholds and modes. The paper also wants to bridge the mismatch between neuron-scale activity variation and region-scale imaging by explicitly modeling unresolved within-region heterogeneity.

### 4. What data does it use?
For the human analysis, it uses a Schaefer-200 group structural connectome, normative regional FDG-PET summaries, regional amyloid centiloid summaries for one correction, and longitudinal tau-PET outcomes. The regional correction analyses use FDG-PET means and variances estimated from 47 subjects without substantial amyloid pathology and compare them with annualized tau accumulation averaged across 483 non-overlapping subjects. The individual threshold analysis focuses on subject-level pairings of early FDG with later tau extent, with the strongest association appearing in the centiloid-below-50 subgroup at N = 146.

### 5. How is it evaluated?
The theory is first checked in stochastic simulations on synthetic multiscale networks to verify the threshold and dominant-mode approximations. The human regional analysis then asks whether the activity-dependent correction terms and fitted dominant modes predict future tau accumulation better than the unperturbed structural Perron mode, mean FDG, or FDG variance alone. The individual analysis asks whether the inverse activity-dependent threshold is associated with broader tau extent across subjects, especially at lower or moderate amyloid burden.

### 6. What are the main results?
The regional results are the strongest part. Parameter-free correction terms tied to mean activity and unresolved activity variation show strong associations with later tau accumulation, with partial Spearman correlations around 0.441, -0.428, 0.386, and 0.436 after covariate adjustment depending on the correction used. Fitted dominant eigenmodes remain associated with future tau accumulation with partial correlations of 0.452, 0.424, and 0.471, all with very small p-values. At the individual level, the inverse first-order threshold is only modestly associated with tau extent, peaking in the centiloid-below-50 subgroup at ρ = 0.219 and nominal p = 0.008, with a standardized regression coefficient of 0.194 after centiloid adjustment.

### 7. What is actually novel?
The novelty is not just “network diffusion plus PET.” It is the explicit coupling of neuronal activity to epidemic spreading so that activity changes both the onset threshold and the dominant spreading direction, along with a multiscale decomposition that tries to recover the effect of within-region activity variability hidden by coarse imaging. The paper also makes these theoretical quantities answerable to longitudinal human tau progression rather than leaving them as simulation curiosities.

### 8. What are the strengths?
First, the paper asks a sharper mechanistic question than most anatomy-only spread models ask. Second, it gives analytically interpretable objects instead of only simulation output. Third, it validates the approximations in stochastic synthetic networks before touching the human data. Fourth, it explicitly separates mean regional activity from unresolved within-region variation. Fifth, the human analysis is not trivial window dressing: the regional tau associations remain after adjustment for structural mode, PET inputs, and amyloid.

### 9. What are the weaknesses, limitations, or red flags?
The biggest weakness is that the human model is still group-level and proxy-heavy. The structural network is not patient-specific, FDG is only an indirect activity measure, and within-region variability is inferred rather than observed. The framework is designed for early invasion, not later aggregation, degeneration, or network damage. The individual threshold result is modest and depends on the observed best centiloid cutoff, so the p-values there are explicitly nominal. And none of this is yet an intervention or targeting demonstration.

### 10. What challenges or open problems remain?
The obvious next challenge is moving from group averages to patient-specific structural and activity estimates. The field also needs direct neural measures, not only FDG proxies, if it wants to claim activity-weighted causal leverage. Another open problem is whether this framework still works once pathology is already established and structural damage feeds back onto the network itself. Finally, the model does not yet tell us what intervention would change the threshold in practice.

### 11. What future work naturally follows?
Test the framework in patient-specific connectomes with longitudinal electrophysiology or richer functional measures, and see whether activity-weighted thresholds predict who transitions from localized to widespread pathology. Extend the model beyond early invasion into later structural deterioration and bidirectional pathology-network feedback. And if the threshold and eigenmode prove stable enough, use them to evaluate candidate activity-modulating interventions rather than treating tau spread as a passive descriptive process.

### 12. Why does this matter for cabbageland?
Because it gives a better language for state-dependent network vulnerability. Even though the disease context is Alzheimer's rather than direct neuromodulation, the useful residue is broader: pathology or perturbation does not only follow anatomy, it follows anatomy as filtered through activity. That is exactly the sort of shift that can matter for intervention logic, biomarker framing, and control-style thinking in other brain disorders too.

### 13. What ideas are steal-worthy?
Treat epidemic threshold and dominant spreading mode as intervention-adjacent audit variables rather than decorative math. Use activity-weighted corrections when evaluating whether a network model explains progression beyond static structure. Keep separate summaries for mean regional activity and unresolved within-region variability. And when coarse imaging misses signal, ask whether the missing piece is not “more features” but the wrong scale of activity representation.

### 14. Final decision
Preserve. This is not a ready-to-deploy disease model, but it is a genuine conceptual improvement over anatomy-only spreading papers and it earns the keep with both analytical clarity and nontrivial longitudinal human results. The limitations are real, especially around group averages and modest individual-level threshold effects, yet the threshold-and-eigenmode framing is useful enough to keep.
