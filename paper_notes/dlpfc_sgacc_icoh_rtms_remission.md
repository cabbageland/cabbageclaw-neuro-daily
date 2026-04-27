# Reduced pre-treatment isolated effective coherence between the dorsolateral prefrontal cortex and the subgenual anterior cingulate cortex as a potential predictive marker for remission following repetitive transcranial magnetic stimulation in major depressive disorder

## Basic info

* Title: Reduced pre-treatment isolated effective coherence between the dorsolateral prefrontal cortex and the subgenual anterior cingulate cortex as a potential predictive marker for remission following repetitive transcranial magnetic stimulation in major depressive disorder
* Authors: Toshiyuki Shimizu et al.
* Year: 2026
* Venue / source: World Journal of Biological Psychiatry
* Link: https://pubmed.ncbi.nlm.nih.gov/42035414/
* Date surfaced: 2026-04-27
* Why selected in one sentence: It asks whether a directional pre-treatment circuit marker can separate rTMS remitters from nonremitters in depression.

## Quick verdict

* Useful

This is a decent biomarker paper by current depression-TMS standards because it at least tests a directional circuit quantity with a clinically legible outcome. The result is promising but not clean enough to treat as a ready-made personalization rule. Single-center, source-localized EEG effective-connectivity biomarkers can look sharper in one dataset than they do in the wild.

## One-paragraph overview

The paper examines whether pre-treatment effective connectivity between left dorsolateral prefrontal cortex and subgenual anterior cingulate cortex predicts remission after high-frequency left DLPFC rTMS in major depressive disorder. Using source-localized EEG and isolated effective coherence, the authors report that lower baseline alpha-band connectivity from left DLPFC to sgACC was associated with remission, with no corresponding theta-band effect. The useful read is that the field may need directional circuit measures, not just static anticorrelation slogans, if it wants serious personalization. The obvious caveat is that thirty patients is not enough to settle a biomarker story.

## Model definition

### Inputs
Pre-treatment EEG, source-localized estimates for left DLPFC and sgACC, alpha- and theta-band directed connectivity features, and remission outcomes after high-frequency left DLPFC rTMS.

### Outputs
Isolated effective coherence values by direction and frequency band, remission versus nonremission discrimination metrics, and multivariable associations between baseline connectivity and remission.

### Training objective (loss)
There is no main trainable prediction model described in the accessible abstract beyond statistical modeling. The core analysis uses isolated effective coherence estimation and logistic regression rather than a machine-learning system with a distinct optimization loss reported.

### Architecture / parameterization
A source-localized EEG effective-connectivity pipeline using exact low-resolution electromagnetic tomography and isolated effective coherence, followed by statistical discrimination and regression.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Depression rTMS still lacks reliable pre-treatment markers that identify who will actually remit.

### 2. What is the method?
Estimate directed alpha- and theta-band connectivity between left DLPFC and sgACC from pre-treatment EEG and test whether those values differ between remitters and nonremitters after rTMS.

### 3. What is the method motivation?
If therapeutic response depends on how stimulation enters and propagates through depression-relevant circuitry, then a directional connectivity measure may be more informative than static undirected associations.

### 4. What data does it use?
Thirty adults with major depressive disorder treated at a single center with high-frequency left DLPFC rTMS, along with pre-treatment EEG and clinical outcome data.

### 5. How is it evaluated?
By comparing baseline iCoh values between remission groups, calculating area under the curve for remission discrimination, and testing whether the marker remains significant in multivariable logistic regression.

### 6. What are the main results?
Lower baseline alpha-band effective connectivity from left DLPFC to sgACC was associated with remission. The reported effect size was large, the discrimination AUC was 0.75, and the association remained significant in multivariable analysis. Theta-band connectivity did not show a significant group difference.

### 7. What is actually novel?
The useful novelty is not the DLPFC-sgACC pair itself, which is already familiar. The better move is using a directional effective-connectivity estimate rather than another static connectivity or simple scalp-power marker.

### 8. What are the strengths?
- Directional circuit framing is better than connectivity folklore.
- Remission is a stricter outcome than loose symptom improvement.
- The signal is frequency-specific instead of indiscriminate.
- The paper stays reasonably close to a real clinical targeting problem.

### 9. What are the weaknesses, limitations, or red flags?
- Small single-center sample.
- Source-localized EEG connectivity can be sensitive to preprocessing and modeling choices.
- No external validation cohort.
- An AUC of 0.75 is encouraging but not enough for deployment.
- The accessible abstract does not show whether this clearly beats simpler baseline predictors.

### 10. What challenges or open problems remain?
Replication, robustness across EEG pipelines and rTMS protocols, comparison with structural and functional imaging markers, and testing whether the biomarker can actually improve target or protocol selection.

### 11. What future work naturally follows?
Prospective multicenter validation, combination with connectomic or symptom-based markers, repeated-measures designs to track whether the same circuit changes during treatment, and head-to-head comparison against simpler baseline predictors.

### 12. Why does this matter for cabbageland?
Because it points toward a more serious personalization standard for depression stimulation. If a biomarker is going to matter, it should say something directional about how the intervention enters the circuit, not just that two regions happen to correlate.

### 13. What ideas are steal-worthy?
- Replace static-connectivity rhetoric with directional pre-treatment circuit markers.
- Treat frequency specificity as part of the personalization claim, not decorative detail.
- Ask whether low effective drive from stimulation entry point to deep target marks a more modifiable circuit regime.
- Compare source-localized EEG circuit markers against structural route models and stimulation-evoked measures.

### 14. Final decision
Preserve, but with caution. This is a respectable biomarker candidate paper, not a solved targeting rule.
