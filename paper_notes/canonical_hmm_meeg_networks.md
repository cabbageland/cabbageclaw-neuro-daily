# Canonical Hidden Markov Model Networks for studying M/EEG

## Basic info

* Title: Canonical Hidden Markov Model Networks for studying M/EEG
* Authors: Andrew Gohil, Daniel B. Larsson, Jennifer S. Hunt, Maja Blazevic, Kristin M. Stockwell, Callum M. Smith, Qingbo Chen, Mats van Es, Diego Vidaurre, Mark W. Woolrich.
* Year: 2025.
* Venue / source: Imaging Neuroscience.
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13045528/
* Date surfaced: 2026-05-29.
* Why selected in one sentence: It turns dynamic M/EEG network inference from a boutique per-dataset ritual into a reusable reference model that could make intervention-relevant state tracking more comparable across studies.

## Quick verdict

* Highly relevant

This is not a stimulation paper, but it is a strong methods and network paper because it attacks a real bottleneck in electrophysiology state modeling: every small dataset retrains its own latent-state model and then pretends the resulting states are comparable. The useful move is to pretrain canonical HMMs on 1,849 MEG sessions and then use them as a shared dynamic-network basis for new MEG and EEG datasets. That does not solve mechanistic inference by itself, but it gives a cleaner substrate for state estimation, biomarker comparison, and eventually closed-loop intervention logic.

## One-paragraph overview

The paper proposes a family of pretrained hidden Markov models for dynamic M/EEG network analysis, with model orders from four to sixteen states in source space and sensor space. Instead of fitting a fresh HMM on each small dataset, the authors train canonical models on 621 healthy participants from Cam-CAN, spanning rest and task recordings, then show how those same state dictionaries can be applied to smaller "boutique" MEG and EEG datasets. The point is less novelty theater about HMMs and more standardization: if fast-switching electrophysiological states are going to matter for disease, cognition, or stimulation timing, then it helps to have a shared reference set rather than endlessly re-deriving slightly different latent states from underpowered datasets.

## Model definition

### Inputs
Preprocessed M/EEG time series, either source-reconstructed and parcellated data or sensor-space data aligned to the canonical training setup. The canonical models were trained on Cam-CAN MEG recordings spanning rest, sensorimotor task, and passive visual or auditory task sessions.

### Outputs
Discrete latent brain states with associated spatiotemporal and spectral network patterns, plus state-time courses and summary metrics that can be compared across individuals and datasets.

### Training objective (loss)
The accessible full text makes clear that this is an HMM fit to electrophysiological time series, but it does not present the optimization target in the plain-language sections as an explicit named loss. Operationally, the model is trained to infer latent state structure and state transitions that best explain the observed M/EEG dynamics under the HMM parameterization.

### Architecture / parameterization
A hidden Markov model family for dynamic functional connectivity in M/EEG, released as pretrained canonical models with state counts from four to sixteen in both parcel-based source space and MEG sensor space.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Dynamic electrophysiology papers often use small bespoke datasets and fit their own latent-state models in isolation, which makes cross-study comparison fragile and network estimates noisier than they need to be.

### 2. What is the method?

The authors pretrain canonical HMMs on a large Cam-CAN MEG corpus, then package those models as reusable reference network dictionaries that can be applied to smaller MEG or EEG datasets if preprocessing and spatial layout are compatible.

### 3. What is the method motivation?

If the same broad fast-switching electrophysiological networks recur across tasks, rest, and cohorts, then retraining a new latent-state basis for every boutique study is wasteful and makes comparison harder. A canonical basis could improve stability, reduce compute, and create a common reference frame.

### 4. What data does it use?

Training uses 1,849 MEG sessions from 621 healthy Cam-CAN participants aged eighteen to eighty-eight. Demonstration datasets include BioFIND resting-state MEG in mild cognitive impairment, MEGUK N-back task data, and LEMON resting-state EEG.

### 5. How is it evaluated?

The paper evaluates whether the canonical models recover interpretable dynamic networks and whether they can be transferred to smaller external datasets across both MEG and EEG. The key test is not leaderboard prediction. It is whether a common latent-state basis remains usable across datasets and recording contexts.

### 6. What are the main results?

The authors report that canonical HMMs recover a reusable set of dynamic electrophysiological networks and can be applied to boutique datasets as a public resource. The main practical gains are more stable inference, lower computational cost for new studies, and a common network reference space for comparing individuals and cohorts.

### 7. What is actually novel?

The novelty is not inventing HMMs for M/EEG. It is turning them into a large-scale pretrained reference resource, closer in spirit to a reusable network atlas than a one-off analysis script.

### 8. What are the strengths?

It uses a genuinely large electrophysiology corpus rather than pretending a small dataset can define universal latent states.

It supports both source-space and sensor-space variants, which makes transfer more practical.

It is useful infrastructure for future work on biomarkers, disease comparison, and stimulation-state reasoning.

### 9. What are the weaknesses, limitations, or red flags?

The transfer story depends heavily on preprocessing compatibility, source reconstruction choices, and sensor layout alignment. That is a real practical constraint, not a footnote.

Because the canonical models are trained on healthy Cam-CAN MEG, they may miss disease-specific or device-specific dynamics that matter for intervention settings.

A shared latent-state basis can improve comparability while still smuggling in its own inductive biases, so there is some risk of standardizing the wrong abstraction.

### 10. What challenges or open problems remain?

The next problem is to test whether canonical electrophysiology states remain useful in intracranial, stimulation, and psychiatric settings where pathology, artifacts, and task structure differ more sharply from Cam-CAN.

### 11. What future work naturally follows?

A natural next step is to use canonical dynamic-network states as priors or initialization for intervention studies, especially for brain-state estimation, biomarker transfer, and closed-loop timing logic.

### 12. Why does this matter for cabbageland?

Because a lot of adaptive neuromodulation talk quietly assumes that latent brain states are stable enough to track, compare, and control across people and datasets. This paper does not prove that assumption, but it provides a cleaner reference scaffold for testing it.

### 13. What ideas are steal-worthy?

One steal-worthy idea is to use a canonical latent-state basis as a starting point for intervention-specific state estimation rather than training from scratch on every small study.

Another is to ask whether treatment response, stimulation timing sensitivity, or symptom transitions are better organized in a shared dynamic-state space than in raw feature space.

### 14. Final decision

Keep. This is good shared infrastructure for network and computational neuro work that wants intervention relevance without pretending every new small cohort deserves its own bespoke ontology of latent states.
