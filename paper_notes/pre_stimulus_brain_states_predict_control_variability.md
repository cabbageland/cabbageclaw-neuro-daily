# Pre-stimulus brain states predict and control variability in stimulation responses

## Basic info

* Title: Pre-stimulus brain states predict and control variability in stimulation responses
* Authors: Giovanni Rabuffo et al.
* Year: 2026
* Venue / source: Brain Stimulation
* Link: https://pubmed.ncbi.nlm.nih.gov/42144100/
* Date surfaced: 2026-05-19
* Why selected in one sentence: It directly tests whether ongoing brain state can explain, predict, and partly control trial-to-trial stimulation response variability across a large intracranial-plus-scalp stimulation dataset.

## Quick verdict

* Highly relevant

This is one of the cleaner recent statements of the idea that stimulation variability is not just nuisance noise. The paper looks strong on scale and on the conceptual move from fixed-parameter stimulation toward state-aware gating. The main limitation is access: despite 10 distinct full-text acquisition attempts, I could only inspect the abstract and metadata here, so confidence is higher on framing and headline results than on implementation details.

## One-paragraph overview

The paper analyzes more than 10,000 single-pulse electrical stimulations across about 320 sessions in 36 epilepsy patients with simultaneous stereotactic EEG and high-density EEG. The authors screen many candidate pre-stimulation metrics, narrow to the most reliable ones, and ask how much pre-stimulus spontaneous activity explains post-stimulation response variance on a trial-by-trial basis. Their answer is that ongoing state matters substantially, especially when measured at whole-brain scale and with intracranial recordings. They then go one step further and argue that conditioning stimulation on favorable states can reduce response variability, which is the part that matters most for closed-loop logic.

## Model definition

### Inputs
Pre-stimulus stereotactic EEG and high-density EEG features, including measures of signal dynamics, synchronization, functional connectivity, and complexity at local and whole-brain scales, plus stimulation trials acquired across sessions.

### Outputs
Predicted variance and trial-by-trial magnitude structure of post-stimulation evoked responses, along with retrospective and prospective classification of more versus less favorable pre-stimulation states for reducing response variability.

### Training objective (loss)
The accessible text does not expose a conventional machine-learning loss in enough detail. What is clear is that the analysis quantified explained variance and out-of-sample predictive performance relating pre-stimulus metrics to post-stimulation responses.

### Architecture / parameterization
A feature-screening and predictive-analysis pipeline rather than a single named learned architecture, operating over candidate pre-stimulus biomarkers derived from local and whole-brain electrophysiology.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Whether identical stimulation parameters can produce more reproducible responses if stimulation is conditioned on ongoing brain state rather than delivered blindly.

### 2. What is the method?
Measure many candidate pre-stimulus electrophysiology metrics, identify the most reliable ones, test how much they explain post-stimulation responses within and across sessions, and compare local versus whole-brain predictors in both intracranial and scalp recordings.

### 3. What is the method motivation?
Neuromodulation keeps running into trial-to-trial variability. If that variability is partly state-dependent, then closed-loop or gated stimulation becomes more plausible and fixed-parameter open-loop recipes look less defensible.

### 4. What data does it use?
Thirty-six epilepsy patients, around 320 sessions, and more than 10,000 single-pulse electrical stimulations recorded with simultaneous stereotactic EEG and high-density EEG.

### 5. How is it evaluated?
By within-session explained variance, out-of-sample generalization, comparisons between stereotactic EEG and scalp EEG, comparisons between whole-brain and local metrics, and retrospective plus prospective analyses of state-conditioned variability reduction.

### 6. What are the main results?
Pre-stimulus state explains a meaningful fraction of post-stimulation response variance. Stereotactic EEG performs better than scalp EEG on average. Whole-brain metrics outperform local ones. Explanatory power depends on network identity, and favorable pre-stimulation states appear to reduce response variability in both retrospective and prospective analyses.

### 7. What is actually novel?
Not the generic claim that brain state matters, but the scale of the evidence, the cross-modality comparison, and the explicit move from explanation toward a state-conditioned control framing.

### 8. What are the strengths?
- Large stimulation dataset relative to most state-dependent neuromodulation studies.
- Uses both intracranial and scalp measures instead of pretending one modality settles everything.
- Compares whole-brain versus local state, which is a genuinely useful intervention-design question.
- Connects predictive structure to a practical closed-loop interpretation.

### 9. What are the weaknesses, limitations, or red flags?
- I did not get the full article body despite 10 acquisition attempts, so fine-grained methodological critique is constrained.
- The cohort is epilepsy patients undergoing invasive monitoring, which is not the same thing as everyday therapeutic neuromodulation populations.
- Single-pulse electrical stimulation is not identical to chronic therapeutic stimulation.
- The accessible text does not fully expose how robust the selected metrics are across individuals, sessions, and tasks.

### 10. What challenges or open problems remain?
Whether these biomarkers stay stable enough for chronic use, whether similar effects hold in psychiatric or movement-disorder interventions, and how much latency or sensing burden a practical state-gated system would tolerate.

### 11. What future work naturally follows?
Prospective real-time gating experiments, testing in therapeutic stimulation settings, comparing simpler versus richer state representations, and checking whether patient-specific models outperform pooled ones.

### 12. Why does this matter for cabbageland?
Because it gives unusually direct support for the view that stimulation response variability should be modeled, not merely averaged away. That is useful across TMS, DBS, VNS, ultrasound, and other adaptive-intervention discussions.

### 13. What ideas are steal-worthy?
- Treat whole-brain pre-stimulus state as a first-class control variable rather than a nuisance covariate.
- Benchmark local versus distributed biomarkers explicitly instead of assuming the recording site is sufficient.
- Make “variance reduction” a target outcome in neuromodulation design, not just mean-effect amplification.
- Use retrospective variability analyses to nominate prospective gating rules.

### 14. Final decision
Keep. Even with abstract-only access, the study is directly on the critical path for state-aware stimulation logic and is worth preserving with explicit confidence limits.
