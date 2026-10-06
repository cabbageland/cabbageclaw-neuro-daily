# Bayesian-enhanced closed-loop optimization of ultrasound protocols for targeted and precise neuromodulation

## Basic info

* Title: Bayesian-enhanced closed-loop optimization of ultrasound protocols for targeted and precise neuromodulation
* Authors: Andrea Boscutti, Valeria Grasso, Tommaso Di Ianni
* Year: 2026
* Venue / source: bioRxiv preprint / PMC
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13308201/
* Date surfaced: 2026-10-06
* Why selected in one sentence: It turns LIFU protocol selection into an explicit closed-loop Bayesian optimization problem over measured stimulation response instead of another hand-tuned ultrasound parameter grid.

## Quick verdict

* Highly relevant

This is a serious methods keep for closed-loop neuromodulation, especially because it joins actuator parameters, online physiological readout, surrogate modeling, acquisition, and stopping into one executable loop. The caveat is large: this is a rodent preprint using fUSI-derived cerebral-blood-volume responses, not human psychiatric treatment evidence. Still, as an engineering template for personalized LIFU parameter search, it is much stronger than the usual "we tried a few settings" neuromodulation story.

## One-paragraph overview

The paper introduces BEACUN, a Bayesian-enhanced adaptive-control platform for optimizing low-intensity focused ultrasound parameters. The authors pair LIFU with functional ultrasound imaging in rats, use the evoked delta CBV/CBV response as the feedback signal, fit a Gaussian-process surrogate model over stimulation parameters, and choose the next protocol by acquisition functions such as log expected improvement or joint entropy search. They first build ground-truth and virtual response landscapes from superior-colliculus fUSI-LIFU mapping, then test live optimization against random search, run a separate in silico behavioral model based on centromedial-thalamus stimulation data, and finally show automated optimization of DLG stimulation to suppress visual-evoked responses. The useful contribution is not a therapeutic claim. It is a concrete recipe for making LIFU parameter search adaptive, data-efficient, and stoppable under an explicit posterior criterion.

## Model definition

### Inputs
LIFU protocol variables including acoustic pressure, pulse repetition frequency, duty cycle, target region, and stimulation duration depending on the experiment; the accumulated history of tested parameter combinations; real-time fUSI delta CBV/CBV response in the target ROI; initialization samples; and the chosen acquisition/stopping configuration.

### Outputs
The model outputs the next LIFU parameter set to test, a posterior estimate of the stimulation-response landscape, an estimated optimum, posterior uncertainty, and a probability-of-success signal for stopping. Experimentally, each chosen protocol also yields observed fUSI response changes and, in the behavioral-model simulation, predicted arousal-related outcomes.

### Training objective (loss)
This is black-box Bayesian optimization, not supervised training against labels. The outer objective is to find a parameter setting that optimizes the measured stimulation-response function with few evaluations, usually minimizing inhibitory fUSI response in the reported live experiments. The Gaussian-process hyperparameters are optimized by maximizing exact marginal log likelihood; acquisition functions then trade off exploration and exploitation.

### Architecture / parameterization
BEACUN uses Gaussian-process surrogate models implemented in BoTorch. Live continuous searches used SingleTaskGP; offline mixed categorical-continuous searches used MixedSingleTaskGP with continuous and categorical kernels. The authors compare RBF and Matern kernels, automatic relevance determination lengthscales, multiple acquisition functions including LogEI, qLogNEI, UCB, MES, PES, and JES, Sobol or random initialization, and a probabilistic regret bound stopping criterion.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
LIFU has a large, poorly characterized parameter space, and stimulation responses vary across subjects, targets, and states. Exhaustive parameter grids are expensive, sparse, and clinically unrealistic, while fixed protocols hide the fact that the dose-response landscape is often unknown.

### 2. What is the method?
The authors build a closed-loop system in which LIFU is delivered, fUSI measures the evoked response, a GP surrogate model is updated, an acquisition function selects the next stimulation protocol, and the loop repeats until a budget or posterior stopping criterion is met. They tune and benchmark the loop in virtual experiments, then deploy it in live fUSI-LIFU experiments in rats.

### 3. What is the method motivation?
If ultrasound neuromodulation is going to become personalized, the field needs a way to learn parameter-response maps inside the limited number of trials feasible in a subject. Bayesian optimization is attractive because it uses every prior observation to choose the next informative or promising stimulation setting.

### 4. What data does it use?
The paper uses hydrophone acoustic-field characterization, rat fUSI-LIFU recordings, superior-colliculus parameter mapping across 48 sessions in 14 rats, live BEACUN optimization sessions targeting the superior colliculus, an in silico centromedial-thalamus behavioral model based on prior real LIFU data, and live DLG optimization sessions in five rats during visual stimulation.

### 5. How is it evaluated?
The authors compare acquisition functions and initialization choices in simulated response landscapes, benchmark BEACUN against random search and grid search, test live superior-colliculus optimization against real-world random search, and test whether automated DLG optimization can suppress visual-evoked fUSI responses while meeting a posterior probability-of-success stopping criterion.

### 6. What are the main results?
In the superior-colliculus model, LogEI and qLogNEI beat random search, with LogEI showing faster and more reliable convergence. In live superior-colliculus experiments, BEACUN outperformed random search and produced a median delta CBV/CBV reduction of about -7.3% with an IQR of 1.19%. In the CMT behavioral-model simulation, joint entropy search performed best and beat grid search, while also showing that the pressure dimension remained the main source of error. In live DLG visual-stimulation experiments, BEACUN suppressed visual-evoked responses in all five rats and reached the P95 stopping criterion after 23 +/- 3.67 evaluations, far fewer than the 90-trial ground-truth search.

### 7. What is actually novel?
The novelty is the closed-loop LIFU optimization stack, not Bayesian optimization in the abstract. The paper ties online neuroimaging feedback, GP surrogate modeling, acquisition-driven protocol choice, live device control, and a posterior stopping rule into one neuromodulation workflow.

### 8. What are the strengths?
The paper attacks a real bottleneck: parameter search. It validates the optimizer both in simulation and in live experiments, compares against conventional search baselines, reports which acquisition functions work in different landscapes, and includes a principled stopping criterion rather than hand-waving about convergence. It also treats target engagement as something to measure during optimization, not something to infer after symptoms move.

### 9. What are the weaknesses, limitations, or red flags?
This is a preprint and not yet peer reviewed. The in vivo evidence is rodent-only, and the feedback signal is fUSI-derived blood-volume change, an indirect neural measure that could include vascular effects. The acoustic frequency used in the fUSI-LIFU experiments differs from typical human transcranial LIFU setups. The main demonstrated objectives are short-window physiological suppression tasks, not durable behavior or psychiatric symptoms. Data and code are promised for release at publication rather than already available in the inspected text.

### 10. What challenges or open problems remain?
The field still needs to know whether the same optimization logic survives human skull acoustics, slower and noisier human readouts, safety constraints, repeated-session plasticity, nonstationary disease states, and clinically meaningful targets. It also needs stronger baselines than random or grid search once richer controllers become available.

### 11. What future work naturally follows?
Test BEACUN-like optimization in larger animals and humans with realistic transcranial parameters; add safety-aware constrained optimization; optimize over target location as well as waveform parameters; compare fUSI, fMRI, EEG, LFP, behavioral, and symptom feedback targets; and evaluate whether optimized protocols remain stable or need scheduled re-optimization over time.

### 12. Why does this matter for cabbageland?
Because it makes a useful distinction the field often blurs: focused ultrasound's deep targeting is not enough if the parameter-response map is still guessed. The cabbageland-relevant move is to make intervention design an adaptive control problem with target engagement measured in the loop.

### 13. What ideas are steal-worthy?
Treat each stimulation trial as information for the next one. Use a posterior stopping rule so the system can stop because additional trials are low value, not because the calendar ran out. Tune the acquisition strategy to the response landscape instead of assuming one optimizer is always best. Separate the optimization target from the eventual clinical endpoint, then force future work to prove that the optimized physiological state actually matters.

### 14. Final decision
Keep. This is not clinical evidence for LIFU psychiatry, but it is a strong platform paper for how personalized ultrasound neuromodulation should search parameter space: measured response, adaptive selection, explicit uncertainty, and no worship of protocol grids.
