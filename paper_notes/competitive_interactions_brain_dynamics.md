# Competitive interactions shape mammalian brain network dynamics and computation

## Basic info

* Title: Competitive interactions shape mammalian brain network dynamics and computation
* Authors: Fernando P. Rosas et al.
* Year: 2026
* Venue / source: Nature Neuroscience
* Link: https://www.nature.com/articles/s41593-026-02205-3
* Date surfaced: 2026-04-07
* Why selected in one sentence: It is a strong whole-brain modeling paper because it tests a hidden assumption inside a lot of network-control and connectome-guided intervention rhetoric: that long-range interactions should be modeled as cooperative by default.

## Quick verdict

* Highly useful, adjacent

This is not a neuromodulation outcome paper, but it is very relevant infrastructure for thinking about network interventions. If the best generative models of brain dynamics require long-range competitive as well as cooperative interactions, then simplistic intervention logic based on purely cooperative spread is probably missing something important.

## One-paragraph overview

The paper asks whether whole-brain models should allow competitive, effectively net-negative interactions between regions rather than assuming that long-range coupling is always cooperative. The authors build species-specific generative models for human, macaque, and mouse brains using structural connectivity plus functional MRI, compare cooperative-only against cooperative-plus-competitive architectures, and examine the resulting dynamics and computational properties. Across species, the models allowing competition fit empirical data better, were more subject-specific, and produced more realistic hierarchy, synergy, and metastability. The result is less a clinical prescription than a better dynamical prior for any attempt to think seriously about network control or stimulation.

## Model definition

### Inputs
Species-specific structural connectivity and functional MRI data from humans, macaques, and mice.

### Outputs
Generative effective connectivity matrices, simulated whole-brain dynamics, model-fit measures to empirical functional connectivity, and secondary dynamical and computational measures such as hierarchy, metastability, synergy, and neuromorphic reservoir-computing capacity.

### Training objective (loss)
The model iteratively adjusts connection weights to improve the fit between empirical and simulated functional connectivity, including lag-aware structure, at the individual-subject level.

### Architecture / parameterization
Whole-brain Hopf-model style dynamics using nonlinear Stuart-Landau oscillators near the Hopf bifurcation, coupled by species-specific structural connectomes. The key model comparison is between cooperative-only coupling and coupling that allows both cooperative and competitive effective interactions.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Most connectome-based models assume that long-range interactions are effectively cooperative, but real brain activity contains persistent anticorrelations and competitive organization. The paper asks whether allowing competition improves the mechanistic account of macroscale dynamics.

### 2. What is the method?
Fit subject-level whole-brain models to empirical data in human, macaque, and mouse cohorts, once under a cooperative-only constraint and once allowing competitive interactions, then compare fit quality and emergent dynamical properties.

### 3. What is the method motivation?
If connectome-based models begin with the wrong sign assumptions, then any downstream claims about controllability, intervention spread, or network optimization may inherit those errors.

### 4. What data does it use?
The accessible text reports human diffusion-tractography-based structural data and fMRI for 100 individuals, macaque data for 19 subjects with tractography augmented by CoCoMac tract-tracing information, and mouse data for 10 subjects with tract-tracing-based structural information plus fMRI.

### 5. How is it evaluated?
By comparing empirical fit of simulated to observed functional connectivity and lag structure, by quantifying the proportion of competitive edges that the model converges on, and by assessing emergent dynamical properties such as subject-specificity, synergy, hierarchy, and metastability.

### 6. What are the main results?
Across all three species, the better-fitting models consistently included substantial proportions of competitive interactions. These models improved fit to empirical functional connectivity, produced more realistic dynamical structure, and yielded stronger subject-specificity than cooperative-only models. The authors argue that the best-fitting solutions combine modular cooperative interactions with more diffuse long-range competitive interactions.

### 7. What is actually novel?
The novelty is not just better fit. It is the explicit challenge to a widely inherited sign assumption in macroscale brain modeling and the cross-species demonstration that relaxing that assumption improves realism and individual specificity.

### 8. What are the strengths?
- Cross-species scope instead of a single human dataset story.
- Attacks a hidden modeling assumption rather than just tuning another parameter.
- Uses individual-level fitting rather than only group-average behavior.
- Connects improved fit to richer dynamical and computational properties.
- Gives network neuroscience a more serious baseline for mechanistic inference.

### 9. What are the weaknesses, limitations, or red flags?
- It remains a generative modeling paper, not direct evidence about stimulation outcomes.
- Competitive effective interactions are an inferred mesoscale description, not a literal map of inhibitory anatomy.
- Results depend on the modeling family and fitting approach; other model classes may recover related behavior differently.
- Translational relevance is real but indirect.

### 10. What challenges or open problems remain?
How to map these inferred competitive interactions onto intervention design, how robust the conclusions are across other dynamical model classes and datasets, and how to connect whole-brain dynamical priors to symptom-level or patient-level stimulation planning.

### 11. What future work naturally follows?
Revisit controllability and optimal-stimulation models under competitive-plus-cooperative dynamics, test whether patient-specific disease models gain predictive power from the same architecture, and examine whether stimulation-induced state transitions are better described in this richer dynamical setting.

### 12. Why does this matter for cabbageland?
Because a lot of network-targeted neuromodulation talk quietly assumes that if you perturb one node the rest of the system mainly cooperates along positive pathways. This paper says the underlying dynamical prior may be more antagonistic, more hierarchical, and more realistic than that.

### 13. What ideas are steal-worthy?
- Treat sign structure in effective connectivity as a first-class modeling question.
- Use cross-species consistency as a sanity check for mechanistic priors.
- Judge whole-brain models not only by fit but by emergent realism and subject-specificity.
- Reframe intervention logic around integration-segregation balance rather than pure propagation.

### 14. Final decision
Keep as a conceptual anchor for network-control, connectome-guided targeting, and mechanistic modeling. Not a therapy paper, but exactly the sort of adjacent infrastructure paper that improves future intervention thinking.
