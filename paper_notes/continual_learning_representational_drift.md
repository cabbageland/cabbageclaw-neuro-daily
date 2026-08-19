# Continual-learning rules shape representational drift

## Basic info

* Title: Continual-learning rules shape representational drift
* Authors: Yikai Si, Shanshan Qin
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2608.16141
* Date surfaced: 2026-08-19
* Why selected in one sentence: It cleanly turns representational drift from a vague longitudinal observation into a measurable consequence of how a learning system buys stability without giving up plasticity.

## Quick verdict

* Highly relevant

This is not a neural-data paper, but it is a sharp computational note on a problem that matters for longitudinal biomarkers, adaptive decoders, and closed-loop systems that quietly assume useful internal codes should stay fixed. The best result is the intervention: when the authors explicitly anchor old representations during replay, forward learning gets worse. That makes drift look less like disposable noise and more like one cost of remaining plastic.

## One-paragraph overview

The paper asks how stable performance can coexist with changing internal codes, and whether the answer depends on the continual-learning rule used to prevent forgetting. The authors compare naive sequential training, elastic weight consolidation, learning without forgetting, and experience replay in a ResNet-18 trained on sequential ImageNet tasks, then compare naive training and replay in a continuous-time recurrent network trained on sequential cognitive tasks. Across both settings, replay preserves old-task performance while representations still drift in structured ways: later visual layers move more than earlier ones, and temporal tuning in the recurrent network moves more than mean activity. The most useful result is that directly anchoring old replay representations suppresses drift but also reduces later learning, making the stability-plasticity trade-off explicit instead of rhetorical.

## Model definition

### Inputs
For the convolutional network, the inputs are images from the first 100 classes of a processed ImageNet-1k split, arranged into 20 sequential tasks of 5 classes each. For the recurrent network, the inputs are procedurally generated cognitive-task trials containing a fixation signal, two 32-unit sensory rings, and an 18-unit one-hot task-rule cue across 18 sequential cognitive tasks.

### Outputs
The convolutional network outputs task-incremental image-class predictions for the currently active 5-class task. The recurrent network outputs a fixation signal and a 32-unit directional-response ring. For the analysis itself, the authors also track checkpoint-to-checkpoint changes in internal representations, including layer activations, population vectors, full-trial trajectories, ensemble rate vectors, and tuning-curve vectors.

### Training objective (loss)
The base objective is task-specific supervised performance. Naive training optimizes only current-task loss. Elastic weight consolidation adds a Fisher-weighted quadratic penalty on parameter movement away from earlier tasks. Learning without forgetting adds a distillation KL term over previously seen classes. Replay interleaves current-task data with buffered old samples. The representation-anchoring experiment adds a normalized mean-squared displacement penalty that explicitly keeps old probe representations near their task-1 values.

### Architecture / parameterization
The first track uses a ResNet-18 trained from scratch with Group Normalization and Weight Standardization instead of BatchNorm, under a task-incremental continual-learning setup. The second track uses a 256-unit leaky continuous-time recurrent neural network with softplus dynamics and noisy recurrent state updates, trained on sequential trial-based cognitive tasks. The paper is fundamentally a comparative continual-learning and representational-geometry study rather than a single new model family.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to explain how a system can keep behavior or memory stable while its internal population code keeps changing. In neuroscience that shows up as representational drift; in machine learning it shows up as the stability-plasticity problem. The authors want to know whether those two phenomena are actually linked.

### 2. What is the method?
They train networks on sequential tasks under different anti-forgetting rules, then repeatedly probe the same old inputs at later checkpoints and measure how the internal representation changes. In the vision track, they compare naive training, elastic weight consolidation, learning without forgetting, and replay in a ResNet-18 across 20 sequential ImageNet tasks. In the cognitive track, they compare naive training and replay in a continuous-time recurrent network across 18 sequential tasks. They also intervene inside replay by adding an explicit representation anchor that penalizes movement of old probe representations.

### 3. What is the method motivation?
If drift is just noise, stronger anchoring should be mostly good. If drift is partly the price of continued plasticity, stronger anchoring should make later learning worse. The method is built to separate those stories cleanly.

### 4. What data does it use?
It does not use longitudinal neural recordings. The convolutional track uses the first 100 classes of a processed ImageNet-1k split, arranged into 20 tasks of 5 classes each. The recurrent track uses 18 procedurally generated trial-based cognitive tasks derived from the Yang task set, with fixation, sensory, delay, and response epochs.

### 5. How is it evaluated?
The evaluation asks whether earlier tasks are retained, how quickly probe representations drift across checkpoints, and which aspects of the geometry are stable versus labile. In the CNN track, the authors examine task accuracy, checkpoint similarity, sample-level population-vector correlations, and shared low-dimensional embeddings across checkpoints. In the RNN track, they examine task retention plus drift in population vectors, full-trial trajectories, mean unit activity, and temporal tuning. The anchoring experiment evaluates the trade-off between reduced drift and reduced forward learning.

### 6. What are the main results?
Replay gives the strongest retention while still allowing progressive representational drift. Learning without forgetting also drifts, but more moderately. Elastic weight consolidation mostly freezes representations and also adapts poorly to later tasks. In the CNN, later layers drift more than earlier ones. In the RNN, temporal tuning drifts more than mean activity, while coarse trial-epoch structure remains substantially recognizable. When the authors explicitly anchor old replay representations, drift decreases and forward learning worsens.

### 7. What is actually novel?
The novelty is not simply showing drift. The novel move is treating drift as a mechanistic fingerprint of the continual-learning rule. The paper also adds a direct causal-style intervention by penalizing representational movement inside replay, showing that suppressing drift can itself reduce plasticity.

### 8. What are the strengths?
- The paper asks a mechanistic question instead of merely cataloging drift.
- It compares multiple anti-forgetting rules rather than baking one story into one model.
- It spans both feedforward vision and recurrent cognitive-task settings, which makes the core claim harder to dismiss as architecture-specific.
- The representation-anchoring intervention is especially valuable because it directly tests the cost of forcing old codes to stay still.
- The geometry analysis is more informative than accuracy-only evaluation and separates stable coarse organization from more labile fine structure.

### 9. What are the weaknesses, limitations, or red flags?
- There is no direct neural data, so the biological interpretation remains analogical rather than demonstrated.
- Replay is computationally convenient and psychologically suggestive, but it is still a cleaner and more explicit rehearsal mechanism than real brains likely use.
- The task-incremental setup gives the task identity during training and evaluation, which simplifies the continual-learning problem relative to more realistic class-incremental settings.
- The results show a trade-off under the tested conditions, not a universal law that all drift is good or necessary.
- The paper says more about internal geometry under continual learning than about symptom prediction, intervention control, or clinical transfer.

### 10. What challenges or open problems remain?
The biggest open problem is empirical grounding. The field still needs longitudinal neural datasets where stable behavior coexists with drifting codes and where different stabilization mechanisms can be tested against actual drift structure. It also remains open which geometric quantities are the right stable anchors for adaptive decoders and control systems.

### 11. What future work naturally follows?
Use similar analyses on longitudinal neural recordings, adaptive BCI decoders, and closed-loop biomarker models. Compare replay-like mechanisms with more biologically plausible consolidation schemes. Test whether preserving relational geometry or coarse population structure is a better constraint than freezing unit-level codes. And connect drift tolerance directly to intervention performance in adaptive control settings.

### 12. Why does this matter for cabbageland?
Because a lot of longitudinal brain-state work still quietly assumes that if behavior or symptoms are stable, then the internal code should be too. This paper is a good corrective. It suggests that some internal motion may be compatible with, or even required for, staying adaptive without forgetting. That matters for biomarkers, decoders, and any neuromodulation logic that depends on tracking a moving state space over time.

### 13. What ideas are steal-worthy?
- Evaluate adaptive systems by what geometry they preserve, not only by whether accuracy stays high.
- Treat representational drift as a measurable consequence of stabilization strategy rather than as undifferentiated noise.
- Prefer state features that preserve coarse relational structure when unit-level coordinates drift.
- Use direct interventions on representational anchoring to test when stability starts taxing plasticity.
- Bring the same logic into longitudinal EEG, ECoG, or symptom-state models instead of assuming a stationary codebook.

### 14. Final decision
Keep. This is one of the cleaner recent papers for turning representational drift into an explicit computational trade-off rather than a mysterious observation. It is not a clinical or neural-recording paper, so the transfer claims should stay bounded. But it is very useful for sharpening how we think about longitudinal state representations and adaptive control.

## Access note

This note is based on **full-text arXiv HTML inspection** of the paper's results and materials-and-methods sections on 2026-08-19.
