# Optimal photostimulation selection for iterative activity maps

## Basic info

* Title: Optimal photostimulation selection for iterative activity maps
* Authors: Jacob J. Morra, Kaitlyn E. Fouke, Owen Traubert, Eva A. Naumann
* Year: 2026.
* Venue / source: arXiv preprint (q-bio.NC).
* Link: https://arxiv.org/abs/2607.12930
* Date surfaced: 2026-07-15
* Why selected in one sentence: It treats causal circuit mapping as a budgeted intervention-selection problem instead of pretending exhaustive perturbation is the natural baseline, and it actually tests that idea on in vivo all-optical data.

## Quick verdict

* Highly relevant

This is a strong keep because it aims at a real bottleneck in perturbation neuroscience: not just how to infer a connectome from collected trials, but how to choose the next perturbation when trials are expensive and potentially damaging. The paper's core move is simple and useful: maintain posterior uncertainty over target-responder edges, then spend trials where the map is still ambiguous. The caveat is that the setting is larval-zebrafish all-optical circuit mapping rather than human therapeutic neuromodulation, but the intervention-design logic is real and transfers.

## One-paragraph overview

The paper introduces OPhELIA, a Bayesian framework for selecting photostimulation targets or ensembles during all-optical causal circuit mapping. Each target-responder edge is modeled with a Beta-Bernoulli posterior that updates from repeated success or failure outcomes, and the next intervention is chosen with an ambiguity score that prefers edges that remain both uncertain and near maximal Bernoulli entropy. The framework can also incorporate learned priors from spontaneous and visually evoked activity, and it is layered onto active-learning and compressed-sensing style action selection. In simulations OPhELIA beats round-robin, Thompson sampling, and upper-confidence-bound style target selection, and in combinatorial zebrafish experiments its compressed-sensing variant comes closest to an exhaustive reference connectome using only 5 percent of available trials.

## Model definition

### Inputs
Repeated photostimulation outcomes for each stimulated target or target ensemble and downstream responder, represented as binary evoked or non-evoked responses. For the prior-informed variants, the model also takes pre-perturbation spontaneous and visually evoked activity features derived from calcium traces.

### Outputs
Posterior edge probabilities for target-responder connectivity, target-level or ensemble-level informativeness scores, predicted mean responder entropy from the learned prior model, and the selected next stimulation target or combination to query.

### Training objective (loss)
The core connectivity model is not trained with a conventional loss. It uses conjugate Beta-Bernoulli updates, so posterior parameters are updated directly from observed successes and failures. The learned prior component is a random-forest regressor trained to predict mean responder entropy from pre-perturbation activity features, but the paper does not spell out a custom objective beyond standard regression training. The intervention policy then maximizes an ambiguity-based acquisition score, optionally blended with the learned prior using a fixed weight lambda equal to 0.35.

### Architecture / parameterization
A modular adaptive experimental-design stack: Beta-Bernoulli edge inference for functional connectivity, an ambiguity-maximization acquisition heuristic based on posterior variance and closeness to 0.5 response probability, a random-forest prior over target informativeness, and augmentations of active learning and compressed sensing in standalone and combinatorial stimulation regimes.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

The paper is trying to make causal circuit mapping practical when exhaustive photostimulation is too expensive, slow, and physically constrained. In all-optical experiments the number of possible targets and target combinations explodes quickly, while tissue heating, photodamage, bleaching, and experiment time put hard limits on trial count.

### 2. What is the method?

The method keeps a probabilistic posterior over each target-responder connection and uses that posterior to choose informative perturbations. For standalone target selection it treats targets as arms in a bandit problem. For combinatorial selection it operates over candidate subsets of targets. OPhELIA can run as a pure ambiguity-guided selector or can augment active learning and compressed sensing with learned priors from prestimulation physiology.

### 3. What is the method motivation?

Many connectivity-mapping methods focus on reconstructing a map from undersampled data, but they leave the action-selection problem underdeveloped. This paper argues that the next-stimulation policy is itself part of the scientific method, because a bad policy wastes scarce perturbation budget on already-resolved or low-value queries.

### 4. What data does it use?

The paper uses both simulations and in vivo larval-zebrafish all-optical experiments. Standalone experiments involved six- to nine-day-post-fertilization zebrafish expressing rsChRmine and GCaMP6s, with around fifty candidate target locations and about five thousand responders across imaged midbrain regions. Combinatorial experiments used three fish, five candidate target cells per fish, twenty-one non-empty target combinations excluding pairs, and twelve trials per combination. Prestimulation spontaneous and visually evoked activity was used to build prior features.

### 5. How is it evaluated?

It is evaluated by how closely the inferred connectome matches a trial-exhaustive reference connectome, measured with Kullback-Leibler divergence between Beta posteriors. In simulations the paper compares OPhELIA against round robin, Thompson sampling, and upper confidence bounds. In the combinatorial setting it compares OPhELIA-augmented active learning and compressed sensing against adapted noisy group testing and low-rank matrix recovery baselines. The paper also checks whether prior features predict target informativeness and runs ablations removing the ambiguity heuristic or the prior.

### 6. What are the main results?

- In simulation, ambiguity-guided OPhELIA outperformed round robin, Thompson sampling, and upper confidence bounds in approaching the exhaustive reference connectome under a limited trial budget.
- In real standalone zebrafish experiments, prior-informed OPhELIA achieved lower mean Kullback-Leibler divergence than strategies without prior information when restricted to 25 percent of trials.
- Prestimulation spontaneous and motion-evoked activity features were informative enough for a random-forest regressor to separate high-entropy from low-entropy targets.
- In the combinatorial in vivo setting, OPh-CS most closely matched the exhaustive reference map and achieved the lowest mean divergence at budgets as low as 5 percent of available trials.
- Ablations showed that prior information mattered especially for OPh-CS, while both ambiguity and prior information mattered for OPh-AL.

### 7. What is actually novel?

The novel part is not just Beta-Bernoulli inference or compressed sensing. The useful novelty is that the paper treats photostimulation choice as an explicit adaptive policy problem, builds a simple uncertainty object around that, and shows that physiological priors can improve which perturbations get queried before the experiment starts.

### 8. What are the strengths?

The paper is aimed at a real intervention-design bottleneck rather than decorative modeling.

It uses in vivo data rather than staying in simulation.

It compares against sensible action-selection and reconstruction baselines instead of a straw man.

The ambiguity heuristic is interpretable enough to reason about.

The learned prior is modest and useful rather than bloated.

### 9. What are the weaknesses, limitations, or red flags?

The work is in larval-zebrafish all-optical circuit mapping, not in human or even mammalian therapeutic neuromodulation.

The Beta-Bernoulli formulation reduces responses to binary success or failure, which throws away graded amplitude and temporal-response structure.

The method assumes successful activation of the intended stimulation site and does not model laser-power or targeting-calibration uncertainty.

There is no true functional-connectome ground truth in vivo, only a trial-exhaustive experimental reference.

The combinatorial demonstration is still small in absolute scale: five candidate targets per fish across three fish.

### 10. What challenges or open problems remain?

The main open problems are scaling to much larger action spaces, incorporating graded temporal dynamics instead of binary outcomes, and running the policy online during live experiments rather than only in post hoc replay. A second challenge is coupling target-selection logic with stimulation-quality calibration, since a smart policy is less useful if actual target engagement is unstable.

### 11. What future work naturally follows?

The obvious next steps are online deployment during ongoing experiments, richer response models that preserve amplitude and timing, and extension to other perturbation modalities such as focused ultrasound or electrical stimulation. It would also be useful to test whether similar ambiguity-guided policies can help choose targets in behavior-linked or disease-linked experiments rather than purely connectomic ones.

### 12. Why does this matter for cabbageland?

Because adaptive intervention papers often skip the most operational question: what do you perturb next when budget is tight and uncertainty is unevenly distributed? This paper matters less as a zebrafish connectomics paper than as a template for budgeted causal probing. It sharpens how to think about trial-efficient target discovery before anyone starts making grander claims about closed-loop therapy.

### 13. What ideas are steal-worthy?

One steal-worthy idea is to treat intervention selection itself as a probabilistic uncertainty-reduction problem rather than a neutral data-collection detail.

Another is to use prestimulation physiology to learn priors over which interventions are likely to be informative.

A third is evaluative: the right benchmark for a perturbation-design method is how much exhaustive search it replaces, not how pretty its posterior plots look.

### 14. Final decision

Preserve. This is a strong methods and neuroengineering note because it gives a compact, testable policy for choosing interventions under hard budget constraints and validates that policy on real all-optical data. Keep it as an anchor for causal perturbation design, not as evidence that therapeutic closed-loop neuromodulation is already solved.
