# Fear Learning–Induced Brain Dynamics Predict Individual Extinction Memory Expression following Transcranial Magnetic Stimulation

## Basic info

* Title: Fear Learning–Induced Brain Dynamics Predict Individual Extinction Memory Expression following Transcranial Magnetic Stimulation
* Authors: Kai Zhang, Lihan Cui, Isabel Moallem, Hani Meelad, Zakiya Atiyah, Muhammad Badarnee, Isabella Mason, Zhenfu Wen, Mark S. George, and Mohammed R. Milad
* Year: 2026
* Venue / source: bioRxiv preprint
* Link: https://www.biorxiv.org/content/10.64898/2026.03.20.713275v1
* Date surfaced: 2026-04-09
* Why selected in one sentence: It is a good example of network-state analysis being used to sharpen neuromodulation logic rather than just decorating a fear-learning study with TMS.

## Quick verdict

* Useful

This is not clinical therapy evidence, but it is exactly the kind of intervention-relevant network paper that should stay on the board. The useful contribution is the claim that spontaneous post-learning state reorganization can prospectively predict individual extinction-memory expression under TMS-modulated learning. The caveat is that I only inspected the abstract, and the whole argument depends on analysis choices that need full-method scrutiny and replication.

## One-paragraph overview

The paper asks whether fear conditioning leaves behind measurable reorganization in spontaneous brain dynamics, and whether that reorganization predicts how people later express extinction memory when dorsolateral prefrontal cortex transcranial magnetic stimulation is applied during extinction learning. Eighty-seven healthy adults completed a three-day threat-learning protocol with resting-state functional MRI before and after conditioning, TMS during extinction learning, and functional MRI during later recall and renewal. Using coactivation-pattern analysis and a hidden Markov model over a twenty-four-node threat-circuit parcellation, the authors identify a post-conditioning state marked by global coactivation and elevated transition uncertainty. They then claim that connectivity reorganization within that state predicts individual differences in recall and renewal under TMS-modulated extinction, but not under natural extinction. If that holds up, the paper matters because it treats brain state as part of the intervention substrate rather than as nuisance variance.

## Model definition

### Inputs
Resting-state functional MRI before and after fear conditioning, threat-circuit node activity summarized within a twenty-four-node parcellation, TMS condition during extinction learning, and later recall and renewal imaging and behavioral measurements.

### Outputs
Hidden brain-state assignments or coactivation-pattern structure after conditioning, functional-connectivity reorganization measures within the identified state, and predictions of individual extinction-recall and renewal expression under TMS-modulated extinction.

### Training objective (loss)
The accessible abstract does not specify the exact optimization objective. The paper reportedly uses coactivation-pattern analysis with a hidden Markov model, but I do not have enough source detail to state the precise likelihood or fitting procedure without bluffing.

### Architecture / parameterization
A state-based network analysis stack combining coactivation-pattern analysis, hidden Markov modeling, and predictive association between conditioning-induced network reorganization and later TMS-linked extinction outcomes.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to solve a familiar neuromodulation problem: why does the same stimulation manipulation have different effects across individuals? Here the authors ask whether the answer partly lives in how fear learning reorganizes spontaneous threat-circuit dynamics before extinction begins.

### 2. What is the method?
Participants completed a three-day Pavlovian threat-learning protocol. Resting-state functional MRI was acquired before and after conditioning on day one. On day two, dorsolateral prefrontal cortex TMS was applied during extinction learning. On day three, functional MRI during extinction recall and renewal was collected. The authors then used coactivation-pattern analysis and a hidden Markov model in a twenty-four-node threat-circuit parcellation to characterize post-learning brain states and their reorganization.

### 3. What is the method motivation?
The usual stimulation framing asks whether TMS helps on average. A better framing asks whether prior learning leaves the brain in states that determine whether TMS has leverage. That is the motivation here.

### 4. What data does it use?
The accessible abstract describes eighty-seven healthy adults in a three-day fear-conditioning and extinction paradigm with resting-state and task functional MRI plus TMS during extinction learning.

### 5. How is it evaluated?
It is evaluated by identifying a conditioning-induced brain state, quantifying connectivity reorganization within that state, and testing whether those features predict later recall- and renewal-related neural and behavioral expression under TMS-modulated extinction. The abstract reports cross-validated correlations and permutation testing.

### 6. What are the main results?
The authors report a fear-learning-induced state with global threat-circuit coactivation, elevated engagement, and transition uncertainty after conditioning. Connectivity reorganization within this state predicted individual differences in extinction recall and renewal under TMS-modulated extinction, with reported cross-validated correlations of about 0.47 for recall and 0.37 for renewal, but not under natural extinction. Similar associations were reportedly observed for behavioral expression.

### 7. What is actually novel?
The novelty is not TMS plus fear learning by itself. The useful novelty is the attempt to convert post-learning spontaneous dynamics into an interpretable biomarker for neuromodulation-linked memory expression. That is more mechanistically promising than generic outcome prediction from baseline averages.

### 8. What are the strengths?
- Explicitly state-dependent intervention framing.
- Reasonably sized healthy sample for this kind of imaging protocol.
- Uses dynamic-state analysis rather than static connectivity summaries alone.
- Tests prediction under TMS-modulated extinction versus natural extinction, which is the right comparison.
- Keeps the problem tied to a defined threat-circuit parcellation rather than whole-brain mush.

### 9. What are the weaknesses, limitations, or red flags?
- It is a preprint and I only inspected the abstract.
- Healthy fear-learning paradigms are not the same thing as clinical PTSD intervention.
- Hidden Markov and coactivation-pattern findings can be analysis-sensitive, so method details matter a lot.
- The predictive result may shrink under stricter external validation.
- Even if real, the biomarker is not yet a ready-made targeting rule.

### 10. What challenges or open problems remain?
The field still needs replication, stronger external validation, tests in clinical populations, and clarification of whether the relevant state features are causal levers or merely correlates of who learns well under extinction-plus-stimulation.

### 11. What future work naturally follows?
Translating the same framework into trauma-exposed or PTSD cohorts, testing whether stimulation timing can be adapted to state occupancy or transition structure, and comparing this dynamic-state marker against simpler baseline predictors.

### 12. Why does this matter for cabbageland?
Because it sharpens intervention logic. It suggests that spontaneous network dynamics after a learning event may be part of what determines whether neuromodulation changes memory expression. That is exactly the kind of state-transition framing worth tracking.

### 13. What ideas are steal-worthy?
- Treat post-learning spontaneous dynamics as intervention substrate, not idle background.
- Compare predictive features under neuromodulated versus natural learning to isolate intervention-relevant variance.
- Use interpretable state models as a bridge between network description and stimulation logic.
- Focus on transition uncertainty and state occupancy, not just mean activation.

### 14. Final decision
Keep, but with bounded confidence. This is a preserve-worthy network-and-intervention paper if the full methods hold up, not because it proves therapy but because it offers a better state-dependent framing for when neuromodulation should work.
