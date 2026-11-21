# Adaptive behaviors emerge from Hebbian-like plasticity through flexible attractors

## Basic info

* Title: Adaptive behaviors emerge from Hebbian-like plasticity through flexible attractors
* Authors: Chenguang Li; Jonah Brenner; Hanming Ye; Benjamin Du Pont; Matas Kudarauskas; Joanna Aloor; Chunyu A. Duan; Jason Chen; Jeffrey C. Erlich
* Year: 2026
* Venue / source: bioRxiv preprint; version 1 posted November 19, 2026; not peer reviewed
* Link: https://doi.org/10.64898/2026.11.18.767638
* Date surfaced: 2026-11-21
* Why selected in one sentence: It makes action-dependent feedback and plastic weights explicit parts of an attractor mechanism, with testable behavioral consequences rather than a descriptive brain-state embedding.

## Quick verdict

* Highly relevant

Preserve as computational mechanism and experiment-design inspiration, not as a biological identification result or a treatment study. Local plasticity plus a responsive environment can produce reward-like adaptive behavior without an explicit reward objective in the synaptic update. Prospective configuration is the most broadly successful rule across the reported tests, but operating-point selection, task-specific settings, minimal architectures, and immediate feedback sharply qualify any claim of general superiority.

## One-paragraph overview

The authors put small feedforward rate networks into environments that respond to the networks' choices. A chosen action can return a scalar sensory input; that input drives the circuit, changes its weights, and biases subsequent choices. Six local learning rules and a reward-prediction-error comparator can all seek signal in suitable regimes. For prospective configuration, reduced activity–weight coordinates make the mechanism legible: persistent behavior follows flexible attractors sustained jointly by learning and environmental feedback. Reward magnitude, feedback timing, and interfering input change the geometry and behavioral statistics. These simulations show one way to generate familiar animal behaviors, not that actual animals use this learning rule.

## Model definition

### Inputs

At each step, the environment returns a scalar input conditional on the previous winner-take-all action. The network receives this as ordinary sensory drive, not a separately labeled reward term for the six local rules. Internal variables include neuronal activities, plastic feedforward weights, and rule-specific running statistics. Parameters include activity update rate α, weight update rate β, activity-noise scale η, and, for some rules, averaging rate τ. Environment definitions specify reward probabilities, baiting, competition, and inter-trial intervals. The separate RPE comparator explicitly uses reward prediction error.

### Outputs

The action is the index of the more active output neuron, with random tie-breaking. Outputs are choices, activity trajectories, and changing weights—not diagnoses, treatment responses, or stimulation parameters. Reduced coordinates for the smallest prospective-configuration network are input activity, output-activity difference, and output-weight difference. A separate analysis HMM emits probabilities of rewarded versus unrewarded choices and assigns descriptive explore/exploit states.

### Training objective (loss)

Activities take noisy, rectified, clipped updates toward external plus presynaptic input. The Methods express the deterministic activity step as descent on a squared local prediction loss, L = Σᵢ(xᵢ − x̂ᵢ)², holding presynaptic predictions fixed with a stop-gradient. For prospective configuration, the weight increment before clipping is proportional to xⱼeᵢ, where eᵢ = xᵢ − ΣₖW̃ᵢₖxₖ. This is a local negative prediction-loss gradient up to a constant factor; activities and weights evolve together instead of using a separate settling phase.

The other local rules use their specified plasticity updates rather than this same objective. None of the six local rules directly maximizes accumulated reward; this does **not** mean the experimental pipeline is free of performance-based optimization. The researchers select hyperparameters using task scores. The analysis HMM is fitted by Baum–Welch maximum likelihood with Bernoulli emissions; it is not the mechanism generating actions.

### Architecture / parameterization

Feedforward, all-excitatory rate networks with nonnegative plastic weights, Gaussian activity noise, rectification, and clipping. The principal behavioral architectures contain either one input and two output neurons (3 neurons, 2 synapses), or one input, 50 hidden neurons, and two outputs (53 neurons, 150 synapses). There are no recurrent neural connections in this architecture; the action-to-input environment closes the loop. A memory-retention task uses two input and two output neurons. The compared rules are BCM, Oja, Law–Cooper, prospective configuration, covariance, latent predictive learning, and the three-factor RPE comparator.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Can local activity-dependent learning produce adaptive, apparently reward-seeking behavior when a network acts on its own input stream? More specifically, can the resulting dynamics account for learning-rate changes, choice allocation, persistence, and memory without inserting a global reward-maximization objective into every synaptic update?

### 2. What is the method?

Compare seven rules within a shared noisy rate-network framework across deterministic and probabilistic two-choice tasks, matching pennies, interference/retention conditions, and additional representation-learning tasks. Sweep parameters, evaluate behavioral signatures, and interpret prospective-configuration trajectories in activity–weight space. In the smallest deterministic network, the fixed-point geometry can be derived: with unit input, the output-activity and weight differences align along a line; without input, activity vanishes while weight differences can persist. The responsive environment joins these regimes into a behavior-sustaining loop.

### 3. What is the method motivation?

Reward-like input need not be a special teaching signal to affect future behavior. When an action produces input, presynaptic activity drives both output and plasticity; when it produces none, the drive disappears and noise can redirect choice. Treating the environment as part of the dynamical system exposes this recurrence. It also separates memory stored in weights from memory visible in ongoing activity.

### 4. What data does it use?

Primarily simulated choices, neural activities, and synaptic weights. The grid spans 15 α values, 15 β values, six noise values, and, where applicable, four averaging rates: 1,350 or 5,400 cells per rule and architecture, with 20 independent networks per cell. Published mouse datasets provide behavioral comparisons; for example, the reward-magnitude panel reanalyses hidden-target navigation data, and matching-pennies results compare with existing mouse behavior. These are not new neural recordings or a patient cohort. Simulation seeds are not biological sample sizes, and simulation steps are not validated physiological time units.

### 5. How is it evaluated?

Use task performance, reward-magnitude effects on learning rate versus plateau, probability matching, choice entropy under competition, HMM-defined persistence/switching, run-length distributions, and memory after different interference conditions. Selected HMM switching patterns are rerun for five million steps with new seeds. Drift/diffusion estimated from separate simulated networks predicts held-out simulated learning curves. Run-length analyses compare a fitted discrete power law with an exponential using a likelihood-ratio test; they do not establish uniqueness against all plausible heavy-tailed alternatives.

Parameter selection must stay visible: the default operating point maximizes deterministic-bandit performance, while some figures use task-specific scores or settings. The behavior-grid summary can select each rule's best cell separately for each score. This is not a locked-parameter, held-out-battery comparison of complete agents.

### 6. What are the main results?

- All six local rules and the RPE comparator can seek signal in suitable parameter regimes. The ability is not exclusive to prospective configuration.
- At the selected reward-seeking settings, prospective configuration reproduces faster learning with larger reward without necessarily increasing asymptotic performance. Other rules can show related patterns elsewhere in their grids.
- Several rules probability-match. For prospective configuration, attractor geometry helps explain why similar average choice ratios can coexist with different within-block variability.
- Several rules exhibit recurrent HMM-described explore/exploit behavior. Prospective configuration also produces persistent-choice run lengths that change when feedback is temporally separated or randomized.
- Removing input can preserve a learned weight difference while activity falls silent; intervening input or reversal changes those weights. Thus apparent forgetting depends on interference, not simply elapsed time.
- This is not a complete animal fit: in the reported matching-pennies comparison, prospective configuration reaches 1.87 bits of three-choice block entropy versus 2.81 ± 0.06 in seven mice. Capturing a qualitative signature does not mean matching its magnitude.

### 7. What is actually novel?

The useful contribution is a common comparison framework plus an explicit account of flexible, world-in-the-loop attractors in joint activity–weight space. It connects local plasticity to several behavioral phenomena and predicts how environmental timing should alter persistence. It does not invent Hebbian reward-seeking, probability matching, line attractors, or the general idea that behavior closes a sensorimotor loop; the paper acknowledges relevant prior work.

### 8. What are the strengths?

The mechanism is specified well enough to inspect rather than inferred from a convenient embedding. The common rule template and broad sweeps expose substantial parameter dependence. Small networks permit geometric analysis, and separate-seed prediction/long-run checks are stronger than showing a single attractive trajectory. The authors give concrete behavioral predictions and acknowledge the gap between minimal simulations and biological learning.

### 9. What are the weaknesses, limitations, or red flags?

- **Sufficiency, not identification:** Similar behavior is compatible with several rules. No new neural perturbation or biological model-selection result identifies prospective configuration as the brain's mechanism.
- **Selection and fairness:** Task-informed tuning, best-cell summaries, figure-specific parameters, and supplementary operating-point exceptions complicate headline comparisons. The framework is reward-objective-free locally, not reward-information-free experimentally.
- **Toy feedback:** A scalar action-contingent signal arrives quickly. Delayed/sparse reward, aversion, competing values, sensory ambiguity, and inhibitory circuitry are not resolved.
- **Geometry:** The strongest direct attractor derivation is for the smallest network. A low-dimensional projection in a larger system is not by itself a stability proof.
- **Temporal statistics:** Run lengths are pooled across selected seeds in one analysis, and power-law-versus-exponential preference does not eliminate mixture or truncated-tail explanations. HMM classifications also depend on explicit fitting/selection criteria.
- **Biological realism:** Rectification, clipping, noise, and learning timescales matter; the model omits homeostasis and neuromodulation. The mouse learning criterion in one reanalysis is reconstructed because the original exact criterion was unavailable in public code.
- **Artifacts:** Code and simulation-data locations are reported, but neither was independently audited here. The Methods describe the code as all-rights-reserved at this version, with an intended future open-source license; available code is not automatically reusable without restriction.

### 10. What challenges or open problems remain?

Distinguishing local rules from behavior alone; observing an attractor that partly resides in synaptic weights; testing stability in larger, more realistic circuits; and separating learning-driven persistence from activity-only recurrence or environmental autocorrelation. No response biomarker, patient stratification method, stimulation-target selection, or clinical controller is validated. In particular, an environment-sensitive attractor need not be a desirable or safely reachable therapeutic state.

### 11. What future work naturally follows?

Use a preregistered, locked-parameter test battery with held-out environments and stronger reward-learning baselines. Experimentally vary inter-trial intervals and action–input contingency, including yoked/replayed input controls that preserve sensory exposure. Add delayed reward and competing or aversive inputs. Test frozen versus plastic weights where experimentally possible, and compare predictions at both behavioral and neural-population levels. For run lengths, evaluate alternative tail families and individual-seed distributions rather than relying on pooled two-family comparisons.

### 12. Why does this matter for cabbageland?

It sharpens the state and plant definitions needed for intervention reasoning. A fixed brain coordinate can omit the learning state and the feedback that maintains a behavior. In neuromodulation-plus-psychotherapy designs, a stimulation pulse and a change in task contingency are different inputs to a coupled learning system; their timing is therefore a testable design variable. This is an extrapolation for experiment design, not evidence that this model explains a psychiatric disorder or predicts combined-treatment benefit.

### 13. What ideas are steal-worthy?

- Model joint activity, plasticity, and action-dependent feedback instead of freezing weights and calling the remaining embedding a complete state.
- Distinguish an intervention that changes attractor occupancy from one that changes the feedback or plasticity sustaining the attractor.
- Use environmental timing as a perturbation with matched sensory-dose controls.
- Demand locked-parameter transfer and quantitative behavioral predictions before declaring a local rule broadly explanatory.
- Keep a clinical outcome test separate from mechanistic plausibility; neither a persistence shift nor a target-map correlation establishes therapeutic benefit.

### 14. Final decision

Preserve as a highly relevant computational/network-mechanism reference, adjacent to clinical intervention design. Focused full-text reading used the direct bioRxiv v1 PDF, including main mechanism/results, limitations, and selected network, plasticity, parameter-selection, HMM, run-length, and availability methods. Supplementary figures, external code, simulation archives, and animal datasets were not independently reproduced. The actionable claim is that learning and environmental contingency can jointly create persistent behavior—not that reward circuitry is dispensable or that a clinical control law has been found.
