# Feasible closed-loop stimulation for neural latent dynamics control

## Basic info

* Title: Feasible closed-loop stimulation for neural latent dynamics control
* Authors: Kyle A. Johnsen; Yijun Lai; Lavan Vivekanandasarma; Gordon J. Berman; Chethan Pandarinath; Christopher J. Rozell
* Year: 2026
* Venue / source: bioRxiv preprint, version 1 posted November 7, 2026; not peer reviewed
* Link: https://www.biorxiv.org/content/10.64898/2026.11.06.762216v1
* Date surfaced: 2026-11-10
* Why selected in one sentence: It treats neural control as a joint sensing-and-actuation hardware problem and tests spatial stimulation granularity, inferred-state feedback, and channel allocation in the same simulation pipeline.

## Quick verdict

* Highly relevant

Preserve for experimental-interface design, not as an in-vivo feasibility certificate. The useful result is that stimulation dimensionality and observation capacity must be budgeted jointly, with explicit spatial input geometry and identification data. The numerical optima depend on simplified, deliberately low-dimensional networks, equal nominal channel costs, and—in the first experiment—ground-truth state access.

## One-paragraph overview

The authors train spiking networks to reproduce latent dynamics and EMG-like outputs for an eight-direction reaching task, then add spatial optogenetic stimulation and simulated electrophysiological recording using Cleo. Random perturbations identify linear input-driven dynamics; a constrained model-predictive controller then substitutes stimulation for the directional task cue. One experiment isolates actuator granularity with oracle latent states. A second divides 100 interface channels between stimulation and recording, fits behavior-predictive factors, and closes the loop through a Kalman filter. Both show useful resource trade-offs, but the causal map from factors to behavior is manufactured by the simulator, rather than established experimentally.

## Model definition

### Inputs

- Identification: known optical input histories, task cues, and either true simulated factors or synthetic LFP/multiunit observations, plus behavioral readouts for behavior-predictive identification.
- Online: current factor state or its Kalman estimate, desired future factor/behavior trajectory, and task inputs when included in the modeling condition. In that condition current and future task inputs are known perfectly.
- Actuation is nonnegative, spatially distributed blue-light intensity with an optical propagation model; the controller is not given independent current injection into each latent dimension.

### Outputs

- Identified state-transition, input, observation, and behavioral-readout matrices, with process/measurement noise estimates.
- A future sequence of optical intensities; MPC applies its first step and replans. Behavioral outputs are two EMG-like channels plus a stabilizing signal, not measured patient outcomes.
- Evaluation-only classification uses three-nearest-neighbor matching between evoked and reference behavioral trajectories to label reach direction.

### Training objective (loss)

- Factor-based spiking-network recurrent parameters use recursive least squares to reproduce target factors, derived from principal components of a rate-RNN trajectory; an affine readout maps factors to EMG targets. This is target-dynamics construction, not independent discovery of a biological causal variable. The inspected description does not reconstruct the upstream rate-RNN training objective in detail.
- Oracle-state LDS fitting uses least squares; noise covariances come from residuals. Recording-based identification uses linear BRAID with one-step-ahead prediction loss and no behaviorally irrelevant factors. Exact internal weighting of that implementation's prediction terms is not specified in the inspected main-text description.
- Control minimizes a finite-horizon quadratic tracking-error term plus squared optical input, subject to fitted linear dynamics and `0 <= intensity <= 75 mW/mm²` per channel. The reported stage/input weights are 1 and 0.001; these are controller costs, not the BRAID training loss.

### Architecture / parameterization

A low-rank factor-based spiking network is the simulated plant. The controller uses a linear Gaussian state-space model: `x[t+1] = A x[t] + B u[t] + Btask utask[t] + w`, `y[t] = C x[t] + v`, and `z[t] = Cz x[t]`. Recording-based experiments combine BRAID identification, Kalman filtering, and quadratic-program MPC. Reference control updates every 10 ms with a 300-ms horizon; solver budgets and latency-aware variants are analyzed. Nominal update rate is not demonstrated hardware timing.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

How much independent spatial actuation is necessary to steer neural population dynamics, and how should a finite interface budget be divided between measuring and perturbing the system? Recording many channels while stimulating through one broad source may leave a highly observable but poorly steerable system.

### 2. What is the method?

Run the full identification-to-control pipeline across interface configurations. In experiment one, group a fixed 32-by-32 light grid into 1–1,024 contiguous actuator groups, preserving total light emission while changing independent granularity. In experiment two, partition a 10-by-10 grid into `k` light sources and `100-k` recording electrodes. Compare feedback with open loop and latency-aware control; vary beam width, recording modality, identification data, density, area, and factor complexity.

### 3. What is the method motivation?

A low-dimensional neural manifold does not ensure that available physical inputs span its important directions. Conversely, more actuators can be wasted if the state estimate or identified input map is poor. Coupling optical spread, recording geometry, and control avoids pretending that hardware provides abstract, perfectly independent latent inputs.

### 4. What data does it use?

Control and identification data are simulated. Condition-averaged macaque EMG supplies behavioral templates, not an in-vivo closed-loop test. The reference plant has 1,024 neurons, low-rank trained dynamics, no distinct cell types or laminar structure, and a deliberately sparse density of 125 neurons/mm³ because dense biological-scale simulations are costly. Uniform opsin expression and simplified optical/electrophysiological models further constrain transfer.

### 5. How is it evaluated?

Each channel sweep uses eight random seeds, with 100 control trials per setting and 100 identification trials in the reference configuration. The controller receives no directional task cue during control, so optical inputs must induce the desired trajectory. Tracking quality is `1 - controlled trajectory error / zero-stimulation trajectory error`, using the ratio of trajectory L2 errors; it is not explained variance. The second experiment also classifies simulated behavioral trajectories. The oracle experiment measures factor tracking, whereas the inferred-state experiment measures behavior tracking: their information regimes and endpoints differ.

### 6. What are the main results?

- In the reference oracle-state experiment, the knee occurs at 200 independent actuator groups out of 1,024 light sources, attaining **85.0 ± 1.91% of peak tracking capacity**. This is relative to peak capacity, not an 85% absolute tracking score or a claim that 200 channels are universally sufficient.
- In the 100-channel inferred-state experiment, the best stimulation fraction is **0.525 ± 0.031**, with **66.2 ± 2.28% tracking-error reduction** and **93.6 ± 2.63% reach-direction classification accuracy**. Reported uncertainties are SEM across seeds.
- More identification data shifts the optimum toward stimulation; broader illumination shifts it toward recording. Observation modality also changes the optimum. These dependencies matter more than treating the reference split as a design constant.

### 7. What is actually novel?

The contribution is a systematic, spatially instantiated interface-design survey linking actuator dimensionality to observation/actuation allocation. Linear models, Kalman filters, MPC, low-rank spiking networks, and optogenetics are established ingredients. This is not a new clinical controller or a causal discovery result from neural recordings.

### 8. What are the strengths?

The two experiments isolate actuator limits before adding state-estimation limits. Fixed optical grids make grouping comparisons interpretable, controls include open loop and latency effects, and the parameter sweeps expose important dependencies. The model definition keeps stimulation geometry, neural dynamics, state inference, and behavior mapping separable enough to inspect.

### 9. What are the weaknesses, limitations, or red flags?

- Oracle-state fitting and feedback in experiment one bypass biological inference and factor alignment. Do not transfer that experiment's channel-efficiency result directly to unknown neural states.
- The plant is trained to have low-dimensional dynamics and a factor-to-behavior readout. Recovering control in this construction does not validate real-brain latent causation.
- Equal nominal channel costs ignore modality-specific power, volume, wiring, heat, bandwidth, and interference. The half-and-half optimum is conditional.
- Generic, low-density networks omit biological cell-type/laminar organization; simplified current injection does not establish realistic opsin kinetics, safety, or tissue response.
- Reach-direction classification is proximity to a synthetic target trajectory, not successful animal behavior, rehabilitation, or clinical response.
- Eight seeds and within-simulator sweeps address implementation variability, not patient/site/device heterogeneity. Model drift and clinical artifact burden remain untested.

### 10. What challenges or open problems remain?

Identify the relevant state without privileged access, learn safe perturbation maps under limited data, preserve useful observability during stimulation, and account for compute/measurement delays. It is also necessary to show that controlled factors are causal rather than merely behavior-predictive, and that trajectories remain biologically valid rather than achieving the readout through off-manifold activity.

### 11. What future work naturally follows?

Test a small set of hardware allocations in vivo with matched identification budgets; cost channels using actual device constraints. Add local E/I connectivity, realistic density and opsin dynamics, artifacts, drift, uncertainty, and thermal constraints. Evaluate held-out tasks and sessions, separate factor accuracy from behavioral control, and preregister comparisons against open loop under measured latency.

### 12. Why does this matter for cabbageland?

It makes intervention design an explicit observation-and-input-map problem rather than a contest for the most electrodes. The framing transfers to neuromodulation and personalized targeting, but the optogenetic channel counts do not transfer numerically to TMS, DBS, or ultrasound.

### 13. What ideas are steal-worthy?

- Plot the marginal benefit of sensing versus actuation under an actual hardware budget, not two independent performance curves.
- Keep an oracle-state upper bound beside the deployable inferred-state controller; their gap diagnoses an observation/identification bottleneck.
- Recompute the actuator-efficiency knee under limited identification data and real delays.
- Pair trajectory control with mechanistic perturbation tests: matching a readout can hide a different internal solution, as the rhythm-switching companion note shows.

### 14. Final decision

**Preserve as a highly relevant simulation-based interface-design reference.** Inspection used the primary full-text PDF: main methods/results/discussion, relevant captions, and parameter-table portions. Code was not run or audited, and not every supplemental analysis was rederived. Treat numerical channel optima as hypotheses to validate, not implant specifications or therapeutic claims.
