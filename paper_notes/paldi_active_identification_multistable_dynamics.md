# Beyond the attractor: closed-loop stimulation design for learning multistable neural dynamics

## Basic info

* Title: Beyond the attractor: closed-loop stimulation design for learning multistable neural dynamics
* Authors: Hyungju Jeon; Il Memming Park
* Year: 2026
* Venue / source: bioRxiv preprint; version 1 posted October 12, 2026; not peer reviewed
* Link: https://www.biorxiv.org/content/10.64898/2026.10.05.756678v1.full
* Date surfaced: 2026-11-07
* Why selected in one sentence: It chooses perturbations that distinguish unknown neural dynamics from latent-state uncertainty and tests whether the resulting identified model transfers to a separate control task.

## Quick verdict

* Highly relevant

Preserve as a computational/control-methods reference, not clinical evidence. The useful contribution is an uncertainty-aware acquisition objective for learning a partially observed multistable circuit, with both predictive and intervention evaluations. All neural evidence is simulated, the observation model is known or separately calibrated using simulator states, and near-reference prediction still leaves a meaningful control-success gap.

## One-paragraph overview

Passive trajectories near an attractor can reveal little about how a circuit behaves elsewhere. PALDI—Planning-based Active Latent Dynamics Identification—actively chooses bounded stimulation inputs, estimates hidden state from spike counts, and updates unknown dynamics parameters as observations accumulate. Its finite-horizon planner seeks approximate parameter information, combining sensitivity of dynamics to parameters with how well observations resolve the resulting states and discounting information confounded by state uncertainty. The authors test a model-matched Wilson–Cowan circuit, degraded observation conditions, a diagnostic acquisition-objective ablation, and a spiking decision network fitted by a deliberately reduced model. A separate change-of-mind task tests whether better identification buys better intervention. It does within these simulations, but not at the fitted-reference model's success rate.

## Model definition

### Inputs

- Online observations: vectors of binned neural spike counts and the known applied input history.
- Maintained beliefs: approximate Gaussian state and parameter means/covariances, plus local sensitivities of predicted state to parameters.
- Assumed observation model: Poisson counts with log mean `C z + b`. The loading matrix and bias are treated as known during online identification; learning them jointly with the dynamics is not demonstrated.
- Wilson–Cowan case: two latent excitatory/inhibitory population activities, observed through 20 simulated Poisson neurons; separate inputs to the E and I populations.
- Spiking-network case: spikes from 40 of 240 excitatory neurons in each of two selective pools, 80 recorded neurons total, in 5-ms bins. A fixed readout is fitted first from paired simulator population states and spike counts in separate simulations. The online agent does not receive population states, but is told when the circuit resets.

### Outputs

- Filtered latent-state estimates and an approximate posterior over unknown dynamics parameters.
- A planned input sequence, of which an initial segment is executed before replanning.
- Wilson–Cowan: four synaptic-weight parameters.
- Reduced spiking-network model: five shared coefficients—self-excitation, cross-inhibition, background drive, activation scale, and input gain—parameterizing two slow NMDA population states.
- Downstream evaluation: frozen learned dynamics supplied to a common controller that tries to reverse the circuit's initial decision under current and energy constraints.

### Training objective (loss)

This is sequential approximate Bayesian system identification, not a neural network trained on symptom labels. Online inference combines a Gaussian state-transition model, Poisson observation likelihood, and Gaussian parameter beliefs. Up to constants, the Poisson negative log likelihood is `sum_j[exp(eta_j) - y_j eta_j]`; state/parameter priors also contribute. State prediction uses an EKF linearization, observation correction uses a single-step Laplace approximation, and parameter updates accumulate approximate score/curvature over blocks.

Input selection has a different objective: maximize a local surrogate of parameter expected information gain, expressed as a log-determinant reduction in parameter covariance. Dynamics sensitivity, observation Fisher information, and attenuation for uncertain latent state determine the information increments. Candidate rollouts hold parameter beliefs fixed and use deterministic mean trajectories; this is not exact mutual-information optimization. The main text says the spiking readout is separately fitted, but its full fitting recipe is deferred to appendices not independently reviewed here.

### Architecture / parameterization

An explicitly structured nonlinear state-space model with separate Gaussian state/parameter beliefs, dual estimation, block-truncated parameter sensitivities, and an improved cross-entropy method (iCEM) receding-horizon planner. Coarse-grid planning and adaptive update/replanning intervals extend its horizon and respond to information accumulation or tracking errors. It is neither model-free reinforcement learning nor a learned end-to-end stimulation policy. The neural models supply biological structure, but their identified coefficients remain effective model parameters, not verified biological synaptic measurements.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

How should a closed-loop experiment stimulate a partially observed, nonlinear circuit to learn the dynamics needed for later control? Passive data can stay trapped near one attractor; unpredictable responses can reflect noisy state estimation rather than useful information about the circuit.

### 2. What is the method?

At each observation, update the latent-state belief. After a block, update parameter beliefs using local score and curvature. Plan candidate finite-horizon inputs to maximize approximate parameter-information gain, execute an initial segment, and repeat. The objective discounts responses that could be explained by uncertainty in state rather than changes in parameters. Section II supplies the inference and planning approximations; Section III tests identification and control.

### 3. What is the method motivation?

There are three distinct requirements for an informative perturbation: unknown parameters must affect the response; the sensors must resolve that response; and state uncertainty must not provide an alternative explanation. Exploring a large state-space region or maximizing predictive variance alone does not guarantee any of these. Planning ahead also permits crossing uninformative regions to reach informative ones beyond an attractor basin.

### 4. What data does it use?

Entirely simulated data. The core rate-model benchmark is a bistable Wilson–Cowan excitatory/inhibitory circuit. A designed three-gate system separates parameter sensitivity, observation information, and nuisance-state ambiguity. The neural mismatch benchmark is a Wang decision network simulated in Brian 2, identified with a reduced two-state model and an approximate Poisson readout. Main-text captions report 100 seeds for Wilson–Cowan and the three-gate study, and 20 training seeds for the spiking-network study. These are simulation runs, not independent animals, patients, or sites.

### 5. How is it evaluated?

- **Model-matched dynamics:** global rollout R² from a prescribed latent-state region, using true simulator dynamics as a diagnostic. Independent noise draws mean the true-model reference need not equal one and is not a strict upper bound.
- **Observation robustness:** weaker Fisher SNR and biased observation-loading geometry, with the dynamics and interaction budget fixed.
- **Acquisition ablation:** in the three-gate experiment, inference/planning machinery is held fixed while the objective changes.
- **Spiking-network prediction:** held-out simulations, 500-ms rollouts, initialized from recorded population state with no later spike corrections. This tests learned dynamics, not end-to-end decoding from an unknown initial state.
- **Control transfer:** freeze each learned model and use the same iCEM controller for decision reversal. Figure 6 reports 20 training seeds on seven shared valid task trials, with bounded current and a fixed total budget. This is a narrow simulated intervention test, not population-level therapeutic validation.

Baselines include random inputs, PRBS, a myopic information policy, FLEX, and receding-horizon curiosity with uncertainty sampling (RHC-US). Interaction budgets are matched. FLEX retains a different parameter estimator; the main comparison is not wholly estimator-matched or established as compute-matched.

### 6. What are the main results?

- **Wilson–Cowan, default observations:** median rollout R² of 0.89 for PALDI versus 0.91 for the noisy true-model reference; RHC-US 0.85, PRBS 0.78, Myopic 0.77, random 0.74, stabilized FLEX 0.25 (Section III-B; Figure 3).
- **Observation degradation:** PALDI's median is 0.88 at −15 dB and 0.87 with biased loading; RHC-US falls to 0.58 and 0.18, respectively (Section III-C). These are task-specific simulated robustness results, not general noise guarantees.
- **Three-gate diagnostic:** accounting for latent-state uncertainty avoids a nuisance region that attracts variance-based or unattenuated objectives. This is a constructed explanatory test, not an independently sampled biological environment (Section III-D; Figure 4).
- **Spiking mismatch:** median held-out R² improves from 0.49 after one identification trial to 0.90 after 20; the separately fitted reference reaches 0.91, Myopic 0.86, and RHC-US 0.82 (Section III-E; Figure 5).
- **Decision reversal:** at the reported 480 pA²·s budget, success is 0.76 for PALDI after 20 identification trials, 0.97 for the fitted reference, 0.55 for Myopic, 0.57 for maximum-amplitude model-free input, and zero for the constant-amplitude strategy (Section III-E; Figure 6). Near-reference prediction therefore does not erase the downstream control gap.

### 7. What is actually novel?

The contribution is a practical synthesis for partially observed neural system identification: finite-horizon planning with an approximate parameter-information objective that explicitly accounts for measurement information and latent-state uncertainty. Neither active identification nor Bayesian experimental design nor iCEM is new. The model-mismatch control evaluation strengthens the paper beyond an acquisition-score demonstration, but does not establish a new biological mechanism.

### 8. What are the strengths?

- Separates state inference, dynamics identification, and downstream control instead of conflating them.
- Tests noisy and geometrically biased observations, not only a favorable fully observed simulator.
- Includes a same-machinery objective ablation and a separate spiking generative system.
- Evaluates an intervention with frozen learned parameters and a common controller, not prediction alone.
- Reports medians/IQRs and acknowledges negative-score tails, approximation errors, and known-readout assumptions.

### 9. What are the weaknesses, limitations, or red flags?

- **Causal scope:** changing inputs in a simulator is a controlled intervention within that model, not causal identification of a living neural circuit or a psychiatric mechanism.
- **Identifiability:** assuming the observation map is known removes a major ambiguity between latent coordinates, readout, and dynamics. In the spiking example, that map is calibrated with paired simulator states unavailable in ordinary human recordings.
- **State initialization:** held-out prediction starts from recorded latent population state. Its R² is not an online clinical decoder's performance.
- **Approximation:** Gaussian beliefs can miss multimodality; parameter covariance derivatives and second-order terms are omitted; sensitivities reset at block boundaries; planning omits future measurement corrections to covariance. The error relative to true expected information gain is not quantified.
- **Actuation realism:** independent population inputs and pool-specific currents do not model TMS field spread, electrode selectivity, side effects, or stimulation artifacts.
- **Baseline interpretation:** FLEX changes its estimator and requires stabilization under filtered observations. PALDI's advantage cannot all be assigned to the acquisition objective. Matched interaction budgets do not establish matched computation.
- **Robustness:** seed variability does not replace subject heterogeneity, nonstationarity, device variation, or external replication. Seven shared control trials give limited task diversity.
- **Safety and speed:** bounded simulated inputs are not a clinical safety specification, and the paper explicitly leaves hardware-latency feasibility to future work. Do not infer real-time deployment from 5-ms observation bins.

### 10. What challenges or open problems remain?

Jointly identifying the readout and dynamics without hidden ground truth; calibrating posterior uncertainty under mismatch; retaining identifiability when inputs spread across multiple circuits; handling parameter drift; and learning without unsafe exploration. A model can predict common trajectories well yet be wrong near a separatrix where control decisions matter most.

### 11. What future work naturally follows?

1. Test on a physical neural preparation or hardware-in-the-loop system with measured planning latency and artifact contamination.
2. Compare acquisition policies using the same estimator, actuation bounds, interaction budget, and explicit compute allowance.
3. Perturb or learn the observation map and test multimodal or correlated observation noise.
4. Use held-out intervention objectives and initial-state inference from recordings, not oracle initialization alone.
5. Add safety constraints, drift, and patient/device-specific input geometry before making an adaptive-therapy claim.

### 12. Why does this matter for cabbageland?

It improves the intervention-development question from “which state should we stimulate in?” to “which safe perturbation would tell us how this circuit responds?” That is a useful bridge between perturbational TMS-EEG, network-control models, and adaptive stimulation. The present method is adjacent inspiration: no depression, hypnosis, psychotherapy-combination, or patient-response evidence is supplied. Its transferable value is disciplined experimental design under partial observability.

### 13. What ideas are steal-worthy?

- Give the stimulation protocol an explicit **identification phase**, distinct from the therapeutic/controller evaluation phase.
- Score candidate perturbations by parameter sensitivity × measurement information, with an explicit penalty for latent-state ambiguity.
- Inspect where high predictive uncertainty is irreducible nuisance rather than an opportunity to learn.
- Judge a learned intervention model on both held-out prediction and a fixed-budget control task; expose the gap between them.
- Make input geometry, observation calibration, and latency part of the model contract rather than implementation footnotes.

### 14. Final decision

Keep as a **highly relevant computational/control-methods reference** and a baseline candidate for active neural experimental design. It earns “closed-loop” and “model-based identification” within its simulated setting; it does not earn clinical mechanism, precision-psychiatry efficacy, or hardware-ready adaptive therapy. The next upgrade in confidence requires a physical preparation with imperfect sensing and realistic actuation, not more claims drawn from the same simulator.

Access record: the bioRxiv full main article was read through Methods II, Results III, Discussion IV, and figure captions; the PDF was also obtained. Equations were cross-checked against the PDF where HTML text extraction omitted mathematical notation. The separately linked supplementary-material page returned HTTP 429; supplementary appendices, code, and implementation-level settings were not independently audited. Numerical claims above come from the main text and captions.
