# Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls

## Basic info

* Title: Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls
* Authors: Marzieh Zare
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2607.24519
* Date surfaced: 2026-08-02
* Why selected in one sentence: It turns a lot of hand-wavy clinical EEG foundation-model optimism into a harder question: does the representation carry disease-relevant signal across populations, or mostly the identity of the dataset it came from?

## Quick verdict

* Highly relevant

This is worth preserving because it does not merely say "foundation models are not perfect." It shows, with targeted controls, that several flattering clinical-decoding stories weaken or reverse once you stress the representation against external-population shift, stronger classical comparators, random initialization, and explicit dataset-identity probes. The caveat is that this is still a single-author preprint built from secondary analyses, and many of the deepest control analyses are concentrated on REVE rather than symmetrically repeated across every backbone.

## One-paragraph overview

The paper benchmarks six pretrained EEG foundation models, LaBraM, EEGMamba, CBraMod, REVE, BENDR, and BIOT, across five clinical tasks and then asks a more important follow-up question than the usual leaderboard ritual. Do the apparent gains survive targeted negative controls and a change of population? The answer is mixed in a useful way. On an external Korean dementia cohort, frozen REVE trails a classical feature baseline badly, and a matched random-initialized encoder even beats the pretrained one. Meanwhile, dataset identity is almost perfectly decodable from the embeddings, including after band-limiting and z-scoring, while disease decoding on the same Korean cohort stays near chance. The paper does find one controlled positive, cross-subject ictal detection on CHB-MIT, but it is careful not to oversell that narrow success into a general deployment claim. The net result is less a victory lap than an evaluation manual for how to stop embarrassing yourself with clinical EEG foundation-model benchmarks.

## Model definition

This paper is mainly an evaluation and control study over pretrained EEG foundation models rather than a single newly trained clinical model.

### Inputs
Preprocessed EEG epochs from CHB-MIT ictal detection, TUH TUAB normal-versus-abnormal classification, OpenNeuro ds004504 Alzheimer and AD-versus-FTD classification, Sleep-EDF sleep staging, and the Korean CAUEEG dementia cohort for external stress testing. The evaluated representations are frozen embeddings from six pretrained backbones, with classical handcrafted EEG features used as explicit comparators and targeted controls built from random initialization, random features, label permutation, scrambled-label fine-tuning, and dimensionality-reduction variants.

### Outputs
Task-level predictions for seizure versus interictal epochs, normal versus abnormal EEG, Alzheimer-related diagnoses, sleep stages, and Korean dementia classes, plus auxiliary outputs for dataset-identity decoding and sensitivity analyses under matched probe pipelines.

### Training objective (loss)
The paper does not train one new end-to-end clinical decoder. It freezes pretrained encoders and evaluates probe-based downstream performance under task-appropriate splits. The inspected full text makes the evaluation workflow clear, but it does not present one neat canonical optimization loss for all probes in the compact way a model-development paper might. The main scientific point is comparative control logic rather than a novel loss.

### Architecture / parameterization
Six pretrained backbone families are compared under a harmonized frozen-probe pipeline: LaBraM, EEGMamba, CBraMod, REVE, BENDR, and BIOT. REVE receives the deepest targeted-control treatment because its published claims most directly motivate the paper's external-transfer and dataset-identity questions.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to test whether EEG foundation-model performance on clinical decoding benchmarks reflects transferable clinical signal or a more fragile mix of in-domain familiarity, evaluation leakage, and dataset-specific structure. The sharper target is not "can the model get a decent AUROC somewhere." It is "what survives when the population changes and when obvious alternative explanations are challenged directly."

### 2. What is the method?
The method is a benchmark-plus-controls study. The author runs six pretrained EEG backbones through a harmonized frozen-probe pipeline across five clinical tasks, then applies targeted controls to selected REVE findings. Those controls include matched random initialization, raw random features, label permutation, scrambled-label fine-tuning, projection-method sensitivity, stronger classical comparators, and explicit dataset-identity probes. The most important stress test is an external Korean dementia cohort, where the representation is asked to generalize beyond the Western benchmark context that dominates the rest of the literature.

### 3. What is the method motivation?
The motivation is sound and overdue. Clinical EEG foundation models are being discussed as if within-benchmark frozen-probe wins already imply transferable biomarker value. But in real psychiatric or neurological deployment, the problem is almost always cross-population and cross-site. If the embedding mostly remembers acquisition context, preprocessing history, or benchmark idiosyncrasies, then "generalization" is theater. The paper's targeted controls are designed to name those failure modes instead of politely ignoring them.

### 4. What data does it use?
It uses five task settings built from four benchmark datasets plus one external stress-test cohort. The clinical tasks include CHB-MIT cross-subject ictal detection with 23 epilepsy patients, TUH TUAB normal-versus-abnormal EEG with 253 subjects, OpenNeuro ds004504 for Alzheimer-related classification with 19-channel resting EEG, Sleep-EDF for 2-channel sleep staging, and CAUEEG for Korean dementia classification, including 1,187 recordings overall and a 770-recording healthy-control-versus-dementia binary subset discussed explicitly in the paper. Additional Western datasets such as ds003490 and TDBRAIN are used for dataset-identity probes rather than as main clinical endpoints.

### 5. How is it evaluated?
Evaluation is mostly frozen probing under leave-one-subject-out, subject-grouped, or recording-level splits depending on what identifiers are available. The paper then adds sensitivity analyses that matter: patient-disjoint held-out checks where possible, classical handcrafted baselines, random-initialized encoders, raw random-feature controls, label permutation, scrambled-label fine-tuning, PCA-versus-Gaussian-random-projection comparisons, and explicit dataset-identity decoding. The useful evaluation question is never just whether a number is high. It is whether the number still means what the paper claims after the right counterfactual is tested.

### 6. What are the main results?
- On Korean CAUEEG three-way dementia classification, frozen REVE reaches AUROC 0.568 while classical features reach 0.769.
- The same ordering survives a patient-disjoint held-out sensitivity split, 0.565 for REVE versus 0.768 for classical features.
- A matched random-initialized encoder beats pretrained REVE on the Korean dementia task, 0.659 versus 0.570, which is a deeply unflattering result for the pretrained representation.
- Dataset identity is nearly perfectly decodable from frozen REVE embeddings, AUROC 1.000 at PCA-50 and 0.9998 even after restricting signals to 0.5 to 40 hertz with per-epoch z-scoring.
- The same PCA-50 pipeline decodes Korean three-way diagnosis at only 0.528, so the representation is much cleaner on "which dataset is this" than on "which diagnosis is this."
- On Alzheimer disease classification, Gaussian random projection and PCA over the same pretrained REVE embeddings perform similarly, and classical features nominally exceed REVE once subject-level aggregation is respected.
- The clearest controlled positive is CHB-MIT ictal detection, where REVE reaches AUROC 0.793 and beats a matched random-initialized encoder by 9.2 percentage points.

### 7. What is actually novel?
The novelty is not the generic claim that EEG foundation models are mixed. Plenty of people already suspect that. The real contribution is the control logic. This paper asks a series of better questions: what happens when you compare pretrained weights against the same architecture with random initialization, when you test label dependence directly, when you compare projection choices rather than sneaking them in as architecture credit, and when you ask whether the embedding can decode dataset identity more easily than disease. That is much more useful than another soft benchmark summary.

### 8. What are the strengths?
- It evaluates multiple backbones instead of making one pet-model argument.
- The Korean CAUEEG cohort provides a real external-population stress test rather than another in-family benchmark.
- The targeted controls are well chosen and answer distinct questions instead of collapsing everything into one baseline.
- The paper is unusually honest about what a result does and does not establish.
- It keeps classical handcrafted features in the fight instead of assuming pretraining deserves default prestige.
- The dataset-identity probes are brutal in the right way and expose a failure mode that downstream benchmark reporting often hides.

### 9. What are the weaknesses, limitations, or red flags?
- This is a single-author preprint and a secondary analysis, not a prospective multi-site validation study.
- The strongest control analyses are concentrated on REVE, so the paper is not equally deep on every backbone.
- CAUEEG primary cross-validation is recording-level because public patient identifiers are unavailable, which leaves repeat-record leakage inside training insufficiently bounded.
- The dataset-identity probes establish decodable dataset membership, but they do not isolate whether the driver is site, hardware, preprocessing, cohort composition, diagnosis mix, or something else.
- CHB-MIT, TUAB, and some other evaluations are partly in-domain for some pretrained models, so some positive results are less impressive than they might first appear.
- The paper is fundamentally an evaluation workflow paper, not a repair paper. It diagnoses representational failure better than it solves it.

### 10. What challenges or open problems remain?
The field still needs prospective evidence that an EEG pretraining objective can preserve clinically useful structure across cohorts without collapsing into dataset identity. More practically, benchmark builders need better subject-disjoint metadata, cleaner exposure accounting for pretrained corpora, and more systematic external-population evaluations. It also remains open which dynamical or mechanistic targets should be explicitly audited before a frozen EEG representation is trusted for biomarker or intervention work.

### 11. What future work naturally follows?
The obvious next step is to make targeted controls routine rather than exceptional in EEG foundation-model papers. Beyond that, the field should build pretraining objectives that are explicitly punished for carrying site identity while rewarded for preserving clinically or dynamically meaningful structure. It would also be useful to repeat this style of audit on depression biomarkers, stimulation-response prediction, and closed-loop state estimation rather than mainly seizure and dementia benchmarks.

### 12. Why does this matter for cabbageland?
Because this is exactly the kind of evaluation slippage that can poison intervention logic downstream. If a frozen EEG embedding is better at telling you which dataset recorded the signal than what disease state the person is in, then any later neuromodulation, biomarker, or adaptive-treatment story built on top of that representation starts from sand. The paper is useful not because it kills EEG foundation models, but because it gives a cleaner checklist for deciding when one deserves to be taken seriously.

### 13. What ideas are steal-worthy?
- Treat dataset-identity decoding as a standard audit, not a curiosity.
- Compare pretrained weights against matched random initialization before attributing a gain to pretraining.
- Separate projection-method effects from pretraining effects instead of smuggling both into one claim.
- Keep classical handcrafted baselines strong enough to be embarrassing.
- Match the evaluation unit to the real clinical decision rather than whatever split is easiest to run.

### 14. Final decision
Preserve. This paper does not prove that EEG foundation models are useless, and it does not yet offer a clean remedy. But it does something more durable than cheerleading or contrarianism: it shows how to interrogate a clinical-decoding gain until you know whether it is carrying transferable signal or benchmark perfume.
