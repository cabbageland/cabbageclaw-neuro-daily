# Predicting rTMS treatment efficacy in depression based on modular flexibility of functional connectivity

## Basic info

* Title: Predicting rTMS treatment efficacy in depression based on modular flexibility of functional connectivity
* Authors: Ying Shao et al.
* Year: 2026
* Venue / source: Journal of Affective Disorders
* Link: https://pubmed.ncbi.nlm.nih.gov/41605354/
* Date surfaced: 2026-04-29
* Why selected in one sentence: It links individualized rTMS response in depression to a dynamic network measure, modular flexibility, instead of relying only on static connectivity stories.

## Quick verdict

* Useful

The framing is better than the average depression biomarker paper because it treats therapeutic response as partial restoration of network adaptability rather than as a static edge-counting exercise. The active-versus-sham comparison is a real plus. Still, the dataset is not large, the prediction effect is modest, and the individualized targeting logic remains more plausible than proven.

## One-paragraph overview

The study retrospectively analyzes seventy patients with major depressive disorder who received either active or sham repetitive transcranial magnetic stimulation, with resting-state functional MRI collected before and after treatment. The target was the left dorsolateral prefrontal cortex, individualized by functional connectivity to the right nucleus accumbens. The authors test whether active stimulation increases modular flexibility, defined as dynamic integration changes across time, and whether baseline flexibility predicts symptom outcome. They report that active rTMS reduces depression severity more than sham, increases medial prefrontal default-mode flexibility, and that baseline default-mode flexibility carries moderate predictive value for post-treatment Hamilton Depression scores. The useful read is that the proposed biomarker is dynamic and network-level rather than another static-connectivity slogan.

## Model definition

### Inputs
Pre-treatment and post-treatment resting-state fMRI-derived dynamic functional connectivity features, especially modular flexibility measures from default-mode-network nodes, plus baseline clinical status and treatment condition.

### Outputs
Predicted post-treatment depression severity, especially Hamilton Depression Rating Scale scores, and inference about treatment-related changes in modular flexibility.

### Training objective (loss)
The abstract states that a support vector regression model was used to predict post-treatment HAMD scores from pre-treatment flexibility features, but it does not specify the exact loss or kernel in the accessible text.

### Architecture / parameterization
A support vector regression predictor built on dynamic functional-connectivity-derived modular flexibility features, embedded within a retrospective active-versus-sham rTMS study design.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Depression rTMS response is heterogeneous, and existing predictors are weak. The paper tries to identify a mechanistically motivated network biomarker that predicts who benefits.

### 2. What is the method?
Measure dynamic functional connectivity before and after treatment, compute modular flexibility, compare active versus sham rTMS, and use baseline flexibility to predict clinical outcome with support vector regression.

### 3. What is the method motivation?
If depression involves rigid network organization, then effective neuromodulation might work partly by restoring dynamic flexibility rather than by shifting a single static connectivity value.

### 4. What data does it use?
Seventy patients with major depressive disorder, including forty-one receiving active rTMS and twenty-nine receiving sham, with pre-treatment and post-treatment resting-state functional MRI and Hamilton Depression Rating Scale outcomes.

### 5. How is it evaluated?
By comparing symptom change between active and sham groups, measuring treatment-related flexibility changes, correlating flexibility change with symptom improvement, and testing baseline flexibility as a predictor of post-treatment symptom burden.

### 6. What are the main results?
Active rTMS produces greater HAMD reduction than sham. The active group also shows increased modular flexibility in bilateral medial prefrontal cortex. That increase correlates with symptom reduction, and pre-treatment default-mode flexibility predicts post-treatment HAMD with a reported correlation of about 0.39.

### 7. What is actually novel?
The main novelty is the move from static connectivity biomarkers toward dynamic modular flexibility as both a mechanistic and predictive quantity in individualized depression rTMS.

### 8. What are the strengths?
- Includes a sham comparison rather than only pre-post active treatment.
- Uses a dynamic network metric rather than static connectivity alone.
- Connects treatment effect, biomarker change, and baseline prediction in one design.
- Keeps the proposed mechanism aligned with circuit adaptability rather than pure black-box prediction.

### 9. What are the weaknesses, limitations, or red flags?
- The study is retrospective and modestly sized.
- Prediction strength is real but not spectacular.
- Individualized targeting based on nucleus-accumbens connectivity is still not a causal proof of target optimality.
- The abstract gives little detail about cross-validation rigor, feature selection leakage risk, or test-set separation.

### 10. What challenges or open problems remain?
Prospective biomarker validation, robustness across scanners and cohorts, stronger causal evidence for flexibility as mechanism rather than correlate, and integration with behavioral or symptom-temporal data.

### 11. What future work naturally follows?
Prospective enrichment studies using baseline flexibility, dynamic biomarkers combined with symptom trajectories or EEG, and causal perturbation work that tests whether flexibility change mediates response rather than merely accompanies it.

### 12. Why does this matter for cabbageland?
Because it suggests a cleaner intervention-relevant network framing for depression neuromodulation: not just which edge is weak, but whether the system regains the ability to reconfigure.

### 13. What ideas are steal-worthy?
- Use dynamic modular flexibility as an intervention biomarker rather than static connectivity alone.
- Ask whether treatment restores adaptability, not merely whether symptoms drop.
- Tie individualized targeting claims to longitudinal network change.
- Force predictive biomarkers to compete against sham and against simpler baselines.

### 14. Final decision
Keep, but with caution. This is a worthwhile note because the network framing is better than average and the sham comparison helps, but the predictive evidence is still only moderate and not ready to carry strong personalization claims.
