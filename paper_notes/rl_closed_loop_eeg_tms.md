# A first realization of reinforcement learning-based closed-loop EEG-TMS

## Basic info

* Title: A first realization of reinforcement learning-based closed-loop EEG-TMS
* Authors: Dania Humaidan, Jiahua Xu, Jing Chen, Christoph Zrenner, David Emanuel Vetter, Laura Marzetti, Paolo Belardinelli, Timo Roine, Risto J. Ilmoniemi, Gian Luca Romani, Ulf Ziemann
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2602.06907
* Date surfaced: 2026-06-19
* Why selected in one sentence: It replaces fixed user-chosen phase targeting with a real online controller that learns session-specific excitability states in humans, which is much closer to serious adaptive neuromodulation logic.

## Quick verdict

* Highly relevant

This is a real keep because it upgrades brain-state-dependent TMS from "pick a favorite phase and hope" to an actual online optimization problem. The paper is still an early proof-of-concept in healthy volunteers, and several results are weaker than the headline, especially the failed SMA-to-M1 facilitation and the lopsided DECREASE condition. But it is unusually honest about those cracks, and the core move is genuinely important: the phase that matters is not stable enough to hard-code.

## One-paragraph overview

The paper builds a real-time EEG-TMS system in which a reinforcement learning agent chooses which mu-rhythm phase bin to target on the next trial, then receives reward based on the paired-pulse motor evoked potential it just produced. Twenty-five healthy volunteers underwent paired supplementary-motor-area to primary-motor-cortex stimulation, with the agent trying either to increase or decrease corticospinal excitability relative to baseline. The useful result is not a clean therapeutic effect but a control result: the system did learn participant- and session-specific high- versus low-excitability phases, immediate post-training excitability increased when the learned phase was retested in the INCREASE condition, and post-training resting-state connectivity changed differently in the INCREASE versus DECREASE conditions. The main problem is that a more generic LTP-like increase appeared 30 minutes later across conditions, which muddies the neat closed-loop story and shows how easy it is for repeated stimulation to swamp the control signal.

## Model definition

This paper contains a real-time control model rather than a predictive biomarker model.

### Inputs
Ongoing sensorimotor mu-rhythm phase estimated online from high-density EEG, eight discrete target phase bins, paired-pulse MEP amplitudes from SMA-M1 stimulation, baseline ppMEP statistics, and the current experimental objective of either increasing or decreasing excitability.

### Outputs
The controller outputs the next phase bin to stimulate. Experimentally, the system yields ppMEP amplitudes, single-pulse MEP amplitudes, and later resting-state functional-connectivity changes in the sensorimotor network.

### Training objective (loss)
The controller is optimized through reinforcement learning, not supervised loss minimization. In the INCREASE condition, reward is current average ppMEP minus 1.5 times the baseline average ppMEP. In the DECREASE condition, reward is 0.7 times the baseline average ppMEP minus the current average ppMEP.

### Architecture / parameterization
A Deep-Q-Learning style reinforcement learning agent chooses among eight discrete mu-phase bins during a 400-trial training period. A Brain Oscillation State Sensor forward-predicts the chosen phase and triggers TMS at the predicted moment. Evaluation then tests the learned phase versus random phases, with linear mixed-effects and Bayesian mixed-effects models used for inference.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Preset phase-locked EEG-TMS assumes the experimenter already knows which phase corresponds to a high- or low-excitability state. This paper asks whether that phase can instead be discovered online from feedback during stimulation.

### 2. What is the method?
Participants received paired-pulse SMA-to-M1 stimulation while a reinforcement learning agent selected one of eight mu-rhythm phase bins for each upcoming trial. The reward signal was based on whether the trial moved ppMEP amplitude in the desired direction. The authors then tested whether the learned phase changed immediate excitability and later resting-state connectivity.

### 3. What is the method motivation?
If the optimal stimulation state varies across people and sessions, then hard-coded phase targeting is brittle. A controller that learns from immediate physiological feedback is a more credible route to individualized neuromodulation.

### 4. What data does it use?
Twenty-five healthy right-handed adults participated. After low-SNR session exclusion, the analysis retained 29 INCREASE sessions, 22 DECREASE sessions, and 19 RANDOM sessions, plus resting-state EEG, MEPs, MRI-guided targeting information, and repeated-session data for some participants.

### 5. How is it evaluated?
The paper evaluates whether the agent increasingly selects a learned phase over training, whether ppMEP amplitude changes when that learned phase is retested immediately and 30 minutes later, whether the learned phase differs across INCREASE and DECREASE conditions, and whether resting-state EEG functional connectivity changes in the stimulated sensorimotor network after training.

### 6. What are the main results?
The agent did learn preferred phases over training, and those preferred phases differed systematically across INCREASE and DECREASE sessions, with ascending mu phases more common in INCREASE and descending phases more common in DECREASE. Immediate post-training ppMEP amplitude increased in the INCREASE condition when the learned phase was retested, while the DECREASE condition did not show a significant reduction from baseline even though it was lower than INCREASE. Thirty minutes later, both conditions showed ppMEP increases, which the authors interpret as a generic LTP-like effect from the repeated paired stimulation. Resting-state connectivity between left SMA and M1 increased in the INCREASE condition and changed differentially relative to DECREASE.

### 7. What is actually novel?
The novelty is not simply "RL was used." The novelty is that the target brain state is discovered online from stimulation feedback rather than chosen in advance by the user, and that this is demonstrated in a real human EEG-TMS loop rather than only in simulation.

### 8. What are the strengths?
The paper tests a real closed-loop controller in humans instead of another offline classification story. It combines immediate excitability readouts with later network-connectivity readouts. It reports negative and messy findings instead of burying them. And it directly exposes the session-to-session instability that makes fixed-phase dogma look naive.

### 9. What are the weaknesses, limitations, or red flags?
The work is entirely in healthy volunteers and says nothing direct about patient benefit. Many sessions were excluded for low mu-rhythm SNR, which limits practical robustness. The DECREASE condition is weaker than the headline suggests. The authors failed to show SMA-to-M1 facilitation with their paired-pulse index, so part of the effect may have come from M1 more than the intended network. The 400-trial training block likely induced a generic plasticity effect that blurred the cleaner state-specific story 30 minutes later. Intra-subject variability was also high, with the learned phase not repeating reliably across same-condition sessions.

### 10. What challenges or open problems remain?
The field still needs controllers that can handle within-session state drift, lower-SNR participants, richer EEG feature spaces than eight phase bins, and real behavioral or clinical endpoints. It also needs to show that closed-loop adaptation beats simpler state-aware gating rather than merely proving feasibility.

### 11. What future work naturally follows?
Test similar controllers in patient populations, allow the policy to keep adapting during evaluation instead of freezing it to a single preferred bin, expand the state representation beyond phase alone, and compare against strong open-loop and simpler adaptive baselines.

### 12. Why does this matter for cabbageland?
Because it turns a vague intuition into an executable control architecture: the relevant stimulation state should be learned from feedback rather than declared by the operator. That is directly relevant to adaptive TMS, biomarker design, and any attempt to make neuromodulation less artisanal.

### 13. What ideas are steal-worthy?
Treat phase as a latent control variable to be learned online rather than prescribed. Separate immediate state-specific effects from slower plasticity drift, because those can point in different directions. Use delayed network-connectivity change as a secondary outcome instead of relying only on single-trial excitability. And take session-specific instability seriously as part of the problem, not as annoying noise to average away.

### 14. Final decision
Keep. This is one of the more serious recent attempts to build an actual self-optimizing stimulation loop in humans, even though the present version is still fragile, narrow, and confounded enough that nobody should oversell it as a solved adaptive-neuromodulation recipe.
