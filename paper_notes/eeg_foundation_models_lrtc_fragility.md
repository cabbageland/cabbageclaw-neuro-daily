# Foundation Models for EEG Are Blind to Long-Range Temporal Correlations: A Spectral-Temporal Dissociation Behind Their Cross-Population Fragility

## Basic info

* Title: Foundation Models for EEG Are Blind to Long-Range Temporal Correlations: A Spectral-Temporal Dissociation Behind Their Cross-Population Fragility
* Authors: Marzieh Zare
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2607.24834
* Date surfaced: 2026-08-01
* Why selected in one sentence: It turns the vague complaint that EEG foundation models "do not generalize" into a sharper mechanism claim: they preserve static spectral and site information while discarding a scale-free temporal feature that is more plausibly portable across cohorts.

## Quick verdict

* Highly relevant

This is worth preserving because it does more than show another cross-site benchmark failure. It isolates a specific blind spot, long-range temporal correlations in the alpha-envelope dynamics, and then shows that the discarded feature is more site-robust than the frozen embeddings themselves. The caveat is that the transfer arm is still underpowered and the paper is a single-author preprint built from secondary analyses of public or semi-public cohorts, so the strongest claim here is about failure mode diagnosis, not about a finished remedy.

## One-paragraph overview

The paper probes five pretrained EEG foundation models, REVE, LaBraM, BENDR, CBraMod, and BIOT, to ask whether their frozen embeddings retain long-range temporal correlations, or LRTC, in resting EEG. The target is the detrended-fluctuation-analysis exponent of the alpha-band amplitude envelope, which is dimensionless, partly site-robust, and clinically interesting because it changes in dementia and depression. Across two out-of-distribution dementia cohorts, the models fail to recover this temporal-scaling target consistently even when some of them recover the static 1/f aperiodic slope very well. The paper then adds controls that matter: ordered-versus-shuffled token tests to ask whether any apparent recovery really depends on temporal order, residualization against the aperiodic slope to show the target is not just 1/f in disguise, and recording-site decoding to test whether the embeddings are mostly carrying site identity. The core result is harsh but useful. Current frozen EEG foundation-model embeddings can preserve static spectrum and site much better than the slow temporal structure that would make a biomarker transfer across cohorts. That is a real warning for anyone trying to use them as plug-and-play backbones for neuropsychiatric biomarkers or neuromodulation readouts.

## Model definition

This paper is mainly a probing and evaluation study over pretrained EEG foundation models rather than a single new end-to-end clinical model.

### Inputs
Frozen subject-level embeddings from five pretrained EEG foundation models computed from harmonized resting-state EEG recordings, plus hand-computed classical EEG features. The main regression target is the alpha-envelope DFA exponent, computed per channel and averaged to a scalar for the encoding probe. The comparison target is the aperiodic 1/f slope. The transfer task uses the 19-channel DFA vector directly, and the site-decoding task uses frozen embeddings reduced with PCA.

### Outputs
Predicted DFA exponent, predicted 1/f slope, zero-shot dementia-versus-control transfer AUROC across cohorts, and recording-site balanced accuracy. The paper also reports whether ordered token sequences outperform shuffled sequences when reading pre-pool embeddings, which is the key diagnostic for whether any recovered signal is genuinely temporal.

### Training objective (loss)
The paper does not train a new EEG foundation model from scratch. It freezes existing models and fits supervised probes on top. For scalar recovery, it selects the best out-of-sample 5-fold cross-validated R² across ridge regression, gradient boosting, and random forest probes. For transfer, it uses a StandardScaler trained on the source cohort plus an RBF-SVM evaluated by AUROC with permutation testing and Holm correction. For site decoding, it uses PCA-50 plus logistic regression. The paper also proposes, but does not yet validate, an auxiliary LRTC-aware pretraining loss that combines a scale-freeness term with a per-recording exponent-fidelity term.

### Architecture / parameterization
The evaluated backbone families are three raw-waveform models, REVE, LaBraM, and BENDR, and two spectral-input models, CBraMod and BIOT. All are used as frozen encoders. The paper's main architectural argument is not that one named transformer is magical. It is that front-end representation and pretraining objective determine whether the model keeps static spectrum, temporal order, both, or neither.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to answer a sharper version of the EEG foundation-model generalization question. Instead of asking only whether a frozen embedding performs badly across cohorts, it asks what clinically relevant signal the embedding may have thrown away before the downstream task even begins. The chosen candidate signal is long-range temporal correlation in the alpha-envelope dynamics, because it is dimensionless, linked to disease, and defined by temporal order rather than static spectrum.

### 2. What is the method?
The method is a multi-part probe study. First, the author computes frozen embeddings from five pretrained EEG foundation models on two out-of-distribution dementia cohorts and asks how well simple probes can predict either the DFA exponent or the aperiodic 1/f slope. Second, ordered-versus-shuffled pre-pool controls test whether any apparent DFA recovery actually depends on temporal order. Third, residualization against 1/f tests whether DFA recovery is merely a shadow of static spectrum. Fourth, zero-shot cross-population transfer compares the frozen embedding against the raw DFA feature itself. Fifth, site decoding and label-free ComBat harmonization test whether the embeddings are dominated by recording-site identity.

### 3. What is the method motivation?
The motivation is good. If an EEG foundation model is going to be used as a frozen biomarker backbone, the field needs to know what kind of information that embedding actually preserves. A signal like LRTC is especially diagnostic because it is not just another amplitude feature. It is a temporal-order property that should be useful for cross-site transfer precisely because it is dimensionless and less tied to gain, montage, or other site-specific nuisances.

### 4. What data does it use?
The paper uses five resting-state clinical EEG cohorts spanning four continents. The main encoding probe uses CAUEEG, a Korean dementia-versus-normal cohort, with N = 770 subjects in the analyzed binary task, and BrainLat, a Latin-American neurodegeneration cohort with N = 79. The transfer arm adds OpenNeuro ds004504, a Greek Western cohort, as the training source. TDBRAIN is listed but excluded from REVE-based analyses because it appears in REVE's pretraining corpus, which would confound site- or disease-encoding claims. ASZED-153, a Nigerian schizophrenia cohort, is included in the released cohort set for future work but not used in the main transfer analysis because its recordings are too short for the same DFA scale range.

### 5. How is it evaluated?
The main encoding evaluation reports the best out-of-sample 5-fold cross-validated R² for predicting the DFA exponent or the 1/f slope from frozen embeddings. A classical handcrafted baseline is used as a positive control. The paper estimates a reliability ceiling for DFA recovery on CAUEEG by split-half comparison. Transfer is evaluated with train-one-cohort, test-another AUROC, repeated-resample confidence intervals, a 5000-permutation null, and Holm correction across the DFA and 1/f feature family. Site leakage is evaluated by balanced-accuracy classification of recording site from the embeddings.

### 6. What are the main results?
- No evaluated foundation model recovers the DFA target on both cohorts.
- The raw-waveform models, REVE, LaBraM, and BENDR, recover neither DFA nor 1/f in a useful way, with R² values at or below 0.12.
- The spectral-input models, CBraMod and BIOT, recover 1/f strongly, with R² = 0.59 to 0.63 on CAUEEG and 0.64 to 0.73 on BrainLat, but their weak DFA recovery on CAUEEG, 0.18 and 0.25, collapses on BrainLat to 0.06 and 0.03.
- The classical handcrafted baseline recovers DFA much better, R² = 0.32 on CAUEEG and 0.38 on BrainLat, against an empirical CAUEEG reliability ceiling of R² = 0.64.
- On CAUEEG, the alpha-envelope DFA exponent is effectively orthogonal to the aperiodic slope, r = -0.06, so the paper's DFA target is not just 1/f renamed.
- For REVE and CBraMod, ordered-versus-shuffled pre-pool controls show that the apparent signal is not meaningfully temporal. CBraMod's ordered-minus-shuffled gap is only 0.008 with p = 0.84, supporting an order-independent static proxy rather than real LRTC encoding.
- The transfer story is limited but suggestive. The frozen REVE embedding does not beat chance on the tested Western-to-Korean or Korean-to-Western transfer directions, while the raw DFA feature shows above-chance AUROCs from 0.575 to 0.740 across all tested directions, though none of the DFA-only cells survives Holm correction.
- Recording site is decodable from all five embeddings at near-ceiling balanced accuracy, 0.977 to 1.000 for the four non-REVE models and 0.994 for REVE, whereas the DFA feature itself is much more site-robust at 0.71.

### 7. What is actually novel?
The novelty is not merely "EEG foundation models sometimes generalize badly." Plenty of people already suspected that. The real contribution is the spectral-versus-temporal dissociation with concrete controls. The paper shows that some models can recover static spectrum while failing to preserve long-range temporal structure, that the failure is not reducible to mean-pooling alone, that the target is not simply a shadow of 1/f, and that site identity is often more legible in the embedding than the dynamical quantity of interest. That is a sharper and more actionable diagnosis than generic domain-shift complaining.

### 8. What are the strengths?
- It asks a concrete mechanistic question rather than only reporting downstream accuracy.
- The target choice is smart: the DFA exponent is dimensionless, clinically relevant, and order-dependent.
- The paper uses out-of-distribution cohorts instead of flattering within-site validation.
- It estimates a reliability ceiling, which makes the null results more interpretable.
- The order-control and slope-residualization analyses are exactly the sort of sanity checks this literature usually skips.
- It is careful about pretraining leakage, excluding TDBRAIN where REVE had seen that corpus before.
- The site-decoding analysis is brutal but useful because it exposes how much site identity survives freezing.

### 9. What are the weaknesses, limitations, or red flags?
- This is a preprint and a secondary analysis, not a prospective model-development study.
- The transfer arm is underpowered, especially on the smaller Western cohort, so the positive DFA-transfer story is directional rather than family-wise confirmed.
- BrainLat requires a shorter DFA scale range than CAUEEG, which the paper handles honestly, but it still makes the cross-cohort story harder to interpret.
- The paper mostly diagnoses failure in existing frozen models; the proposed LRTC-aware auxiliary loss is still a proposal, not a demonstrated rescue.
- REVE gets the deepest transfer analysis, while the other four models receive a more limited rescue comparison, so the transfer conclusions are not perfectly symmetric across backbones.
- Site dominance is near-ceiling, but the exact source of that dominance is not fully decomposed into acquisition, preprocessing, cohort composition, or latent identity leakage.
- The author discloses affiliation with NeuroGenis Inc., which is not disqualifying but is worth keeping in mind for biomarker-commercialization framing.

### 10. What challenges or open problems remain?
The main open problem is whether an EEG foundation model can be trained to preserve long-range temporal structure without sacrificing other useful features. More specifically, the field still needs prospective evidence that an LRTC-aware objective improves real cross-site clinical transfer, not just DFA decoding. It also remains unclear whether alpha-envelope DFA is the best temporal-scaling target for all clinical tasks, or simply the cleanest one for this diagnostic audit.

### 11. What future work naturally follows?
The obvious next step is to retrain or fine-tune an EEG backbone with the proposed LRTC-aware auxiliary loss and test whether DFA recovery moves from approximately zero toward the paper's classical baseline range. Beyond that, the field should run the same kind of audit on depression, neuromodulation-response, and closed-loop control tasks rather than only dementia cohorts, and should benchmark any supposedly general EEG embedding against simple dimensionless dynamical features before declaring transfer solved.

### 12. Why does this matter for cabbageland?
Because this is exactly the kind of quiet methods failure that can poison downstream neurotechnology work. If a frozen embedding preserves hospital identity and static spectrum better than the slow dynamical structure that might actually travel across cohorts, then building biomarker or stimulation logic on top of it is asking for decorative generalization. The paper is especially relevant for any EEG-guided intervention stack, depression biomarker program, or closed-loop framing that wants to treat a big pretrained encoder as a reliable representation by default.

### 13. What ideas are steal-worthy?
- Use dimensionless dynamical features as serious cold-start baselines, not as quaint classical leftovers.
- Estimate reliability ceilings before treating R² near zero as ambiguous.
- Treat near-perfect site decoding as a failure signal for foundation-model representations, not just a curiosity.
- Split representation audits into static-spectrum versus temporal-order targets instead of lumping them together.
- Add explicit auxiliary losses for the dynamical quantities you claim to care about, rather than hoping a reconstruction or contrastive objective will pick them up for free.

### 14. Final decision
Preserve. This is not the last word on EEG foundation-model transfer, and it does not yet prove that the proposed fix works. But it makes a precise, mechanistically useful argument about what current frozen embeddings keep, what they drop, and why that matters for cross-population biomarker work.
