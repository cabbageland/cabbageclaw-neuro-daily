# EpiLENS: Patient-Relative Epileptogenic Zone Localization from Multi-Center Intracranial EEG

## Basic info

* Title: EpiLENS: Patient-Relative Epileptogenic Zone Localization from Multi-Center Intracranial EEG
* Authors: Yuanchu Gong, Zibo Yan, Yibo Lyu, Chen Chen, Sixian Chan, Yalin Wang
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2608.01076
* Date surfaced: 2026-08-16
* Why selected in one sentence: It treats epileptogenic localization as a patient-relative decision problem rather than a universal channel-classification problem, then shows that this framing improves balanced localization across heterogeneous four-center iEEG data.

## Quick verdict

* Highly relevant

This is a real keep because it takes heterogeneity seriously instead of pretending one global decision boundary should work across patients, seizures, implants, and centers. The strongest move is not architectural flash. It is the patient-relative framing plus the conservative fusion between a primary probability model and an auxiliary ranking model aimed at ambiguous boundary channels. The gains are meaningful rather than miraculous, which is exactly why the paper is useful: it improves localization without pretending the label problem or cross-center messiness disappeared.

## One-paragraph overview

The paper targets channel-level epileptogenic-zone localization from intracranial EEG in drug-resistant epilepsy, where the practical problem is to identify which implanted contacts belong to tissue that must be resected or otherwise treated. Instead of training a model to score channels on a universal cross-patient scale, the authors construct self-referenced features relative to each channel's own pre-onset baseline and standardize them within the patient's implanted set. They then run two independently trained branches: PRQ-Net, which produces patient-relative non-epileptogenic probabilities with multi-seizure aggregation and a lower-tail correction for intermittent but strong epileptogenic evidence, and BCR-Net, which focuses on difficult boundary channels and recovery of the full patient-specific epileptogenic set. A fixed conservative fusion rule combines them at inference. On a four-center cohort of postoperative seizure-free patients, the resulting EpiLENS system beats both feature baselines and raw-iEEG neural baselines on the paper's primary balanced localization metrics.

## Model definition

EpiLENS is a learned patient-relative localization stack with two independently parameterized branches whose outputs are fused at inference.

### Inputs
Multi-seizure intracranial EEG recordings organized by patient, seizure, channel, and temporal window. For each channel-window, the model uses nine spectral and waveform descriptors transformed into four self-referenced views: absolute values, differences from the same channel's pre-onset baseline, baseline-standardized deviations, and log-relative ratios. The inputs therefore include within-channel temporal reference information and within-patient channel context, but not surgical metadata or postoperative outcome as predictive features.

### Outputs
Channel-level probabilities that a contact is non-epileptogenic, equivalently epileptogenic scores via one minus that probability, plus a patient-specific ranking of channels intended to put the annotated epileptogenic set above non-epileptogenic contacts.

### Training objective (loss)
PRQ-Net is trained as the primary probabilistic classifier with a lower-tail quantile correction so that strong epileptogenic evidence that appears only in a subset of seizures is not erased by averaging. BCR-Net is trained with auxiliary boundary and coverage objectives that emphasize ambiguous epileptogenic versus non-epileptogenic boundaries and recovery of the full annotated epileptogenic set. The fused CDEL output itself is not learned by end-to-end training; it uses a locked inference rule of `0.8 * p_PRQ + 0.2 * p_BCR`.

### Architecture / parameterization
Two attention-based feature encoders with shared high-level design but independent parameters. Each branch uses a 32-dimensional encoder, two attention heads, and patient-batched training. PRQ-Net is the primary classifier. BCR-Net is a complementary ranking model. Their outputs are fused conservatively in probability space at inference.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to localize epileptogenic tissue from intracranial EEG more robustly across patients and centers. Standard channel-wise models trained globally tend to assume comparable values mean comparable pathology across people, which breaks under heterogeneous implants, recording systems, seizure patterns, and center-specific practice.

### 2. What is the method?
Build patient-relative evidence first, then classify and rank channels with two complementary branches. PRQ-Net aggregates recurrent epileptogenic evidence across seizures while retaining a lower-tail correction for intermittent but strong events. BCR-Net learns to rank ambiguous epileptogenic candidates higher by focusing on boundary discrimination and coverage of the full annotated epileptogenic set. At inference, use a fixed conservative fusion rule instead of retraining a meta-fusion model.

### 3. What is the method motivation?
The authors' core claim is that localization should be judged relative to the patient's own implanted channel set, not against a universal electrophysiological scale. That is plausible clinically and technically: the main nuisance is not just noise but person-specific context, montage differences, and class imbalance where epileptogenic contacts are a minority.

### 4. What data does it use?
The evaluation uses 80 postoperative seizure-free patients from four centers, with 256 valid seizures and 7,635 implanted channels. Of those channels, 1,743, or 22.83 percent, are annotated as epileptogenic. The labels are retrospective clinician-defined surgical-target surrogates rather than direct biological truth, which the paper states explicitly.

### 5. How is it evaluated?
The main protocol uses fixed patient-wise five-fold outer splits with seeds 42, 52, and 62, strict separation of outer-test patients, and one fold-level threshold selected only on validation patients. Metrics are computed per patient and macro-averaged. The primary metric is Macro-F1, with EZ-F1, NEZ-F1, AUROC, EZ-fraction bias, EZ-AUPRC, and NDCG-EZ as secondary metrics. The paper also runs ablations, within-patient permutations, cross-seizure analyses on a matched 73-patient subset, and leave-one-center-out transfer tests.

### 6. What are the main results?
On the 80-patient localization splits, CDEL reaches Macro-F1 `0.6371 ± 0.0072`, EZ-F1 `0.4485 ± 0.0118`, accuracy `0.7526 ± 0.0029`, and AUROC `0.7468 ± 0.0004`, while maintaining near-zero EZ-fraction bias at `+0.0034`. Relative to the strongest baseline, logistic regression with patient-wise z-score normalization, it improves Macro-F1 by 0.0306 and EZ-F1 by 0.0497. Relative to PRQ-Net alone, it improves Macro-F1 by 0.0089, EZ-F1 by 0.0186, and AUROC by 0.0052. In leave-one-center-out evaluation, CDEL achieves the best center-mean Macro-F1 at 0.6163 and the best worst-center score at 0.5773, beating the best external LOCO baseline by 0.0422 in center mean. In the matched 73-patient cross-seizure analysis, Macro-F1 rises from 0.6146 with one seizure to 0.6395 with all available seizures.

### 7. What is actually novel?
The real novelty is not merely using another deep model on iEEG. It is the decision to treat abnormality as patient-relative, then separate stable probabilistic evidence from boundary-sensitive ranking evidence and fuse them conservatively rather than letting the auxiliary branch dominate. That is a more thoughtful response to heterogeneity than simply scaling up a raw-signal model.

### 8. What are the strengths?
First, the evaluation protocol is patient-wise and center-aware rather than sloppy channel-wise leakage. Second, the paper focuses on balanced localization metrics instead of hiding behind majority-class performance. Third, it explicitly tests mechanism through ablation, permutation, boundary-channel analysis, and leave-one-center-out transfer. Fourth, the gains concentrate where they matter most, namely ambiguous epileptogenic boundary channels and multi-seizure aggregation under heterogeneous data.

### 9. What are the weaknesses, limitations, or red flags?
The labels are still retrospective surgical-target surrogates, not clean biological ground truth. The cohort includes only postoperative seizure-free patients, which helps supervision quality but narrows the distribution. The learned representation uses engineered spectral and waveform descriptors rather than richer multimodal or connectomic context. The improvements are real but modest, so this is better viewed as a serious framing paper than a solved-clinical-product paper. And because it is retrospective, it does not show that prospective surgical or stimulation decisions would improve.

### 10. What challenges or open problems remain?
The biggest open problem is whether patient-relative localization survives prospective deployment when label noise, uncertain target margins, and non-seizure-free cases are included. It is also unclear how this framework should interact with structural imaging, network models, stimulation response, or resection simulation rather than staying inside the iEEG feature world.

### 11. What future work naturally follows?
Test the framework prospectively in surgical planning, include non-seizure-free cohorts, combine patient-relative iEEG evidence with connectomic or imaging priors, and use the resulting rankings to inform stimulation or resection simulations rather than only retrospective localization metrics.

### 12. Why does this matter for cabbageland?
Because it sharpens a principle that generalizes beyond epilepsy: many intervention problems are not "find the universal biomarker" problems but "find the patient-relative abnormality and rank the controllable boundary" problems. That is useful language for seizure targeting, adaptive stimulation, and any setting where cross-patient averages flatten away the clinically decisive structure.

### 13. What ideas are steal-worthy?
Patient-relative normalization as a first-class modeling choice rather than a preprocessing footnote. Conservative fusion between a primary calibrated probability model and a complementary ranking model. Lower-tail aggregation to keep intermittent but high-value pathological evidence from being averaged away. And evaluation that cares about hardest-boundary channels instead of only global discrimination.

### 14. Final decision
Preserve. This is one of the better recent examples of a paper improving intervention-adjacent inference by choosing a better decision frame instead of just a bigger network. It does not solve epileptogenic localization, but it meaningfully upgrades how the problem should be posed.
