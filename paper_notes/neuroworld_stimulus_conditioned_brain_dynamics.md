# NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics

## Basic info

* Title: NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics
* Authors: Zijian Dong, Jianxiong Zhou, Kwun Kei Ng, Jan Paolo Macapinlac Balagtas, Zhizhou Li, Zijiao Chen, Juan Helen Zhou
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2608.01773
* Date surfaced: 2026-08-04
* Why selected in one sentence: It reframes naturalistic fMRI prediction as a genuinely causal latent-state rollout problem instead of another retrospective encoder that quietly benefits from future-stimulus leakage.

## Quick verdict

* Highly relevant

This is a real keep because it attacks the right failure mode. A lot of naturalistic-fMRI work is good at retrospective fitting but vague about whether the learned representation can survive recursive prediction without cheating. NeuroWorld makes that distinction explicit, removes the reconstruction-first habit, and then shows that the stricter setup still wins across three benchmarks. The main caveat is that the paper is still living in movie-fMRI territory with subject-specific output heads, so it is much closer to a serious simulator scaffold than to a clinically actionable intervention model.

## One-paragraph overview

NeuroWorld treats naturalistic brain activity as the causal evolution of an endogenous latent brain state under exogenous multimodal sensory drive. At each fMRI repetition time, ROI-level fMRI is encoded into a latent state and aligned video, audio, and text features are encoded into stimulus-action tokens. In the first stage, Latent Dynamics Learning, the model predicts the next latent state directly from past latents and past-aligned stimulus actions, without any fMRI reconstruction loss. In the second stage, Latent Rollout Decoding, that learned world model is frozen, rolled forward autoregressively from a short observed prefix, and decoded back into subject-specific whole-brain responses. Across Algonauts 2025, CineBrain, and the new SG-MIND benchmark, the model beats adapted TRIBE and MIRAGE baselines under strictly causal rollout evaluation, especially on the harder datasets where a strong retrospective encoder is not enough.

## Model definition

This paper contains a substantive learned model rather than only a descriptive analysis.

### Inputs
ROI-level fMRI time series sampled on the repetition-time grid, together with temporally aligned multimodal stimulus features. Depending on dataset, the stimulus streams include video, audio, and text. The model also uses dataset-specific hemodynamic lag alignment so the stimulus-action tokens reflect only temporally admissible sensory evidence.

### Outputs
Predicted next latent brain states during training, autoregressively rolled latent trajectories during inference, and decoded subject-specific ROI-level whole-brain fMRI responses over a forecast horizon. Evaluation outputs include global trajectory correlation, mean parcel-wise temporal correlation, and top-10 segment identification accuracy.

### Training objective (loss)
Stage 1, Latent Dynamics Learning, minimizes next-latent prediction mean-squared error plus Sketched Isotropic Gaussian Regularization, or SIGReg, to keep the latent space from collapsing. Stage 2, Latent Rollout Decoding, freezes the latent world model and minimizes masked ROI-level mean-squared error between decoded rollout predictions and observed future fMRI responses.

### Architecture / parameterization
A two-stage causal latent-space world model with an fMRI encoder, a stimulus-action encoder, an autoregressive causal predictor, and a rollout decoder with subject-specific linear heads. Stimulus actions are injected into the predictor through adaptive layer normalization, so the model explicitly separates endogenous latent-state history from exogenous sensory drive instead of mixing them into one undifferentiated token stream.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve the gap between high retrospective naturalistic-fMRI encoding scores and actual causal simulation of brain dynamics. Many existing models predict current responses from rich multimodal stimulus representations but do not enforce temporal causality strictly enough and do not optimize their latent states for recursive rollout.

### 2. What is the method?
The method is a two-stage world model. First, Latent Dynamics Learning jointly learns a latent brain-state encoder and a causal transition model that predicts the next latent state from past latent states and past-aligned stimulus-action tokens. Second, Latent Rollout Decoding freezes that learned latent dynamics model, rolls it forward autoregressively from a short observed fMRI prefix, and trains a decoder that maps the rolled latent trajectory back to subject-specific fMRI responses.

### 3. What is the method motivation?
If the real scientific goal is to model how brain activity evolves during continuous naturalistic experience, then the model should only use sensory input that has actually happened and should learn a latent state that remains stable when its own predictions are fed back into the transition. Observation reconstruction is not the same thing as transition-sufficient state learning.

### 4. What data does it use?
The preserved note is based on full-text inspection of the arXiv HTML version. The experiments use three naturalistic movie-fMRI benchmarks spanning 30 participants: Algonauts 2025 with four participants, CineBrain with six participants, and the new SG-MIND dataset with 20 participants, 8,519 paired stimulus-response clips, and 140.7 person-hours of audiovisual viewing. Stimulus features are extracted from frozen pretrained video, audio, and text models and aligned to each dataset's repetition-time grid.

### 5. How is it evaluated?
The model is evaluated under a strictly causal rollout protocol. Performance is measured with global trajectory correlation, mean parcel-wise temporal correlation, and top-10 identification accuracy for 20-TR segments. The paper also tests longer horizons out to 100 TR, modality ablations, mismatched stimulus-brain alignment, teacher-forced oracle conditions, and cortical maps of where the predictive gains land.

### 6. What are the main results?
- NeuroWorld achieves the best reported value on every metric across SG-MIND, Algonauts 2025, and CineBrain under the causal setting.
- On SG-MIND, NeuroWorld reaches r = 0.2190, Pearson = 0.2107, and Cls@Top10 = 0.8044, while the adapted TRIBE and MIRAGE baselines stay at or below r = 0.0725 and Cls@Top10 = 0.121.
- On CineBrain, causally masked TRIBE- and MIRAGE-based models collapse to r around 0.08 to 0.10, whereas NeuroWorld remains at r = 0.2928.
- On Algonauts 2025, NeuroWorld improves Pearson from 0.2535 to 0.2759 on the random split and from 0.2544 to 0.2729 on the held-out season-6 split, with especially large gains on identification accuracy.
- NeuroWorld retains useful signal out to 100 TR on Algonauts 2025, with a moderate correlation drop rather than immediate autoregressive failure.
- Breaking stimulus-brain alignment drops mean ROI-wise Pearson from 0.2759 to 0.1137, while a teacher-forced oracle reaches 0.5385, showing that both aligned exogenous drive and accurate local transitions matter.
- Video and audio carry most of the unimodal predictive weight, while text adds a smaller but real lift in higher-order association regions.

### 7. What is actually novel?
The novelty is not just using multimodal stimuli or a latent model. The paper's real move is to define naturalistic brain forecasting as causal stimulus-conditioned state evolution, optimize the latent space directly for next-state prediction rather than reconstruction, and then test the result with autoregressive rollout instead of only retrospective fitting.

### 8. What are the strengths?
- It attacks a real conceptual weakness in current naturalistic-fMRI modeling rather than only chasing a benchmark increment.
- The two-stage design cleanly separates latent dynamics learning from observation decoding.
- The SG-MIND dataset meaningfully broadens the empirical base beyond the tiny public cohorts that dominate this subfield.
- The benchmark results are strongest on the harder datasets, which is where a robust dynamics model should distinguish itself.
- The mismatch, oracle, and modality-ablation analyses do real interpretive work instead of acting like decorative extras.

### 9. What are the weaknesses, limitations, or red flags?
- This is still a preprint.
- The task is movie-fMRI forecasting, not intervention, stimulation, or clinically meaningful control.
- Generalization is over held-out runs and one held-out movie season, not over truly unseen cohorts or zero-shot unseen people.
- The model still relies on subject-specific output heads, which limits how far one should push the "general brain simulator" rhetoric.
- ROI-level fMRI remains a noisy and indirect target, and good rollout here does not automatically mean mechanistically faithful latent dynamics.

### 10. What challenges or open problems remain?
The main open problems are whether this framework generalizes to unseen participants without subject-specific heads, whether it can survive independent cohorts and different naturalistic paradigms, how it behaves with other neuroimaging modalities or higher-resolution targets, and whether a similar latent-state logic can become useful for perturbation, state estimation, or closed-loop intervention rather than only passive forecasting.

### 11. What future work naturally follows?
Test subject generalization more honestly, add uncertainty-aware rollout, extend beyond movie stimuli, evaluate on independent cohorts, and connect the latent-state scaffold to perturbational settings where endogenous state and exogenous drive matter for intervention. A particularly good next move would be to see whether this kind of causal latent-state model can predict stimulation-evoked dynamics or response heterogeneity better than retrospective encoders can.

### 12. Why does this matter for cabbageland?
Because a lot of intervention-relevant modeling depends on keeping endogenous state and exogenous drive conceptually separate. This paper offers a cleaner scaffold for thinking about that separation and a sharper evaluation standard for deciding whether a "brain model" is actually learning dynamics or just exploiting retrospective fitting shortcuts.

### 13. What ideas are steal-worthy?
- Treat causal rollout as a first-class benchmark instead of a decorative add-on to retrospective encoding.
- Optimize latent states for transition sufficiency rather than for reconstructing noisy observations.
- Separate endogenous state from exogenous drive explicitly instead of hiding both inside one generic token stream.
- Use mismatch and teacher-forced controls to diagnose whether a model's gains come from state memory, aligned sensory drive, or rollout stability.

### 14. Final decision
Preserve. NeuroWorld is not yet a clinically useful world model, but it is one of the stronger recent computational papers for forcing naturalistic brain modeling to mean something causally stricter and less decorative.
