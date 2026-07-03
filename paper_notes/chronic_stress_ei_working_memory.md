# Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks

## Basic info

* Title: Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks
* Authors: Mauricio A. Diaz, Manuela A. Beyer, Janina Hesse
* Year: 2026
* Venue / source: arXiv
* Link: https://arxiv.org/abs/2606.27529
* Date surfaced: 2026-07-03
* Why selected in one sentence: It turns vague chronic-stress E/I-balance talk into a concrete circuit-perturbation hypothesis and then shows that robustness to that perturbation can cost out-of-distribution flexibility.

## Quick verdict

* Highly relevant

This is a strong computational psychiatry keep because it does not stop at "stress disrupts excitation and inhibition" as a slogan. It systematically compares candidate perturbations inside a biologically constrained recurrent network and gets a sharp answer: stronger inhibitory-to-excitatory synapses best reproduce the targeted stress signatures. The most useful extra move is the resilience result, where networks trained to tolerate the stressor preserve performance but become more specialized and less delay-generalizable. That is a much better story about stress-related rigidity than generic deficit language.

## One-paragraph overview

The paper uses Dale-constrained recurrent neural networks trained on a delayed parametric working-memory task to model chronic stress as an external circuit perturbation. The authors compare eight candidate stress operators, defined either as synaptic-weight changes or activity-gain changes, against three experimentally motivated targets: inhibitory dominance at excitatory cells, excitatory hypofunction, and impaired task performance. Across those candidates, selectively increasing inhibitory-to-excitatory synaptic weights is the only single mechanism that jointly reproduces all three targets. They then train "resilient" networks under that perturbation and show a trade-off: the trained networks preserve performance and stay close to baseline geometric and energetic structure under stress, but they generalize worse to longer delays outside the training distribution. The useful read is that stress resilience in a circuit may look less like global robustness and more like specialization that buys stability by sacrificing flexibility.

## Model definition

### Inputs
Three task inputs drive the network: fixation timing plus two scalar stimuli that must be compared across a delay. The stress-analysis pipeline then perturbs recurrent circuitry with one of eight candidate operators, either by scaling specific recurrent synaptic submatrices or by scaling excitatory or inhibitory activity gains. The main biologically motivated operator increases inhibitory-to-excitatory connectivity.

### Outputs
The network emits two output channels representing whether the first or second stimulus is larger. The paper also reads out internal observables including excitatory and inhibitory drive, excitatory firing, E/I ratio, decision confidence, task accuracy, mean-squared error, population geometry, metabolic-energy proxies, and delay-generalization performance under stressed versus unstressed conditions.

### Training objective (loss)
Networks are trained by minimizing masked mean-squared error between the readout and the target choice signal, plus a firing-rate regularization term. The loss weights fixation and decision periods more heavily than stimulus and delay periods to discourage premature decisions while still constraining delay dynamics.

### Architecture / parameterization
The core model is a fully connected 200-neuron rate RNN with 80 percent excitatory and 20 percent inhibitory units constrained by Dale's law. Recurrent weights are split into E-to-E, E-to-I, I-to-E, and I-to-I submatrices, initialized with signed Gamma-distributed magnitudes and rescaled to a spectral radius of 1.5. Resilience is modeled by retraining otherwise identical networks while the selected stress operator is active during training.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Chronic stress is often described as producing prefrontal dysfunction and altered E/I balance, but that language is usually too coarse to tell us which circuit perturbation actually matters or why stress-resilient behavior can become rigid. The paper tries to turn that mush into a tractable mechanism-comparison problem.

### 2. What is the method?
Train biologically constrained recurrent networks on a working-memory comparison task, then apply eight candidate chronic-stress perturbations and test which one best reproduces experimentally motivated signatures of prefrontal stress dysfunction. After that, retrain networks under the best perturbation to study computational resilience.

### 3. What is the method motivation?
If stress-related psychiatric dysfunction really reflects altered prefrontal circuit balance, then a controlled recurrent model should let us isolate candidate perturbations instead of treating inhibitory dominance, excitatory hypofunction, and cognitive impairment as separate vibes. It also gives a way to ask what resilience computationally costs.

### 4. What data does it use?
This is a simulation and model-comparison paper rather than a human-subject dataset paper. The empirical grounding comes from prior chronic-stress findings in prefrontal circuitry, especially evidence for inhibitory dominance, reduced excitatory output, and working-memory impairment, which are translated into target signatures for the trained networks.

### 5. How is it evaluated?
The authors evaluate candidate operators by asking whether they produce the target triad of inhibitory dominance, excitatory hypofunction, and impaired task performance. They then compare naive and resilience-trained networks on in-distribution task accuracy, out-of-distribution delay generalization, recurrent-population geometry, energy organization, density and reciprocity of recurrent connectivity, and robustness across stress magnitudes and network sizes.

### 6. What are the main results?
- Selectively increasing inhibitory-to-excitatory synaptic strength is the only single stress operator that jointly reproduces all three targeted stress signatures.
- Resilience-trained networks preserve task performance under the trained stress perturbation better than naive networks.
- That resilience comes with a delay-generalization cost: resilient networks degrade faster on longer, untrained delays.
- Resilient networks preserve baseline geometric and energetic organization under stress and show reduced density and reciprocity, suggesting a more specialized recurrent solution.

### 7. What is actually novel?
The novelty is not "stress hurts working memory." The novelty is the explicit operator-comparison framework plus the computational claim that resilience to a chronic-stress-like perturbation can emerge as specialization with reduced generalization, rather than as free robustness.

### 8. What are the strengths?
- It asks a mechanistic question sharp enough to fail.
- The stress candidates are compared systematically instead of being hand-picked after the fact.
- The resilience result is genuinely interesting because it links robustness, geometry, and flexibility.
- The model is simple enough to interpret yet constrained enough to avoid pure black-box theater.
- The paper generates experimentally testable signatures rather than just conceptual slogans.

### 9. What are the weaknesses, limitations, or red flags?
- It is still a deliberately simplified rate-RNN model, so apparently minor design choices can change the learned solution.
- The paper models chronic stress as an external operator rather than deriving it from internal plasticity or neuromodulatory dynamics.
- The task is a single delayed comparison paradigm, which is a narrow slice of stress-relevant cognition.
- Strict Dale-constrained units are a useful first-order approximation, but real biology has richer co-transmission and neuromodulatory structure.
- The results are mechanistically suggestive, not causal proof about actual human or rodent prefrontal microcircuit changes.

### 10. What challenges or open problems remain?
The biggest open problem is closing the loop between the external stress operator and biologically realistic stress induction, plasticity, and recovery dynamics. It also remains unclear whether the resilience-generalization trade-off survives in richer tasks, continuous-attractor settings, or more realistic multi-scale stress models.

### 11. What future work naturally follows?
Model stress as an internally generated adaptation rather than an externally imposed perturbation, test mixtures of operators across molecular and circuit scales, examine rapid recovery dynamics after stress, and see whether the rigidity trade-off appears in broader cognitive tasks and more realistic prefrontal architectures.

### 12. Why does this matter for cabbageland?
Because it upgrades stress-related computational psychiatry from fuzzy E/I rhetoric to a falsifiable circuit story. It also gives a clean way to think about why a system can look resilient on familiar demands while becoming less flexible on novel ones, which is a much better framing for psychiatric rigidity and stress-adaptation trade-offs.

### 13. What ideas are steal-worthy?
- Treat psychiatric circuit hypotheses as perturbation-comparison problems, not just descriptive correlates.
- Use resilience training as a way to study what kinds of robustness a circuit buys and what kinds of flexibility it gives up.
- Look at geometric and energetic organization, not just top-line task accuracy, when claiming a network is robust.
- Frame stress-related rigidity as a specialization cost rather than as a generic deficit.

### 14. Final decision
Preserve. This is not an intervention paper and it is not biologically complete, but it is one of the cleaner recent attempts to turn chronic-stress circuit rhetoric into a specific perturbation hypothesis with an interpretable computational trade-off.
