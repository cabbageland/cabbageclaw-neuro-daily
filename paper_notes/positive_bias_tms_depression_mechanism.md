# Positive bias in brain and behaviour as a mechanism of transcranial magnetic stimulation depression treatment

## Basic info

* Title: Positive bias in brain and behaviour as a mechanism of transcranial magnetic stimulation depression treatment
* Authors: Verena Sarrazin, Paulo Suen, Beatriz Cavendish, Marieke Martens, Pedro Henrique Rodrigues da Silva, Anne Britto, Matheus Rassi, Mariana Baptista, Andre R. Brunoni, Jacinta O'Shea
* Year: 2026
* Venue / source: Molecular Psychiatry
* Link: https://doi.org/10.1038/s41380-026-03485-8
* Date surfaced: 2026-06-06
* Why selected in one sentence: It is one of the cleaner recent attempts to test an actual early-treatment mechanism for depression TMS instead of inferring mechanism from resting-state target folklore after the fact.

## Quick verdict

* Highly relevant

This is worth keeping because it does more than correlate baseline features with outcome. The paper asks whether early task-evoked shifts in emotional processing during intermittent theta-burst stimulation predict later clinical improvement, and it finds a legible signal in both behavior and task-fMRI. The main caution is also the main limitation: the study is open label, modest in size, and already sees symptom change by Week 2, so this is a mechanism candidate rather than settled causal proof.

## One-paragraph overview

The study followed forty-nine adults with major depressive disorder through twenty daily sessions of left dorsolateral prefrontal intermittent theta-burst stimulation and measured emotional-processing changes after roughly eight sessions using a facial-expression task and task fMRI. The central claim is not that TMS simply improves depression scores. It is that responders showed an early shift toward positive bias, behaviorally as a greater tendency to classify ambiguous faces as positive and neurally as increased positive-versus-negative bias in rostral anterior cingulate and default-mode-network activity and connectivity. That makes the paper useful because it tests a time-local mechanism during treatment rather than pretending resting-state site heuristics already explain how antidepressant TMS works.

## Model definition

This paper does not present a trainable predictive model. It uses behavioral and fMRI marker analyses to test whether early treatment-induced changes in emotional processing predict later outcome.

### Inputs
Baseline and Week 2 behavioral emotional-bias measures, baseline and Week 2 task-fMRI activity and connectivity during happy-versus-fearful face processing, baseline clinical severity, demographic covariates, medication status, and the delivered intermittent theta-burst stimulation course.

### Outputs
Clinical response and continuous HAM-D improvement at Week 4, plus associations between those outcomes and early changes in behavioral positive bias, rostral anterior cingulate activity, default-mode-network activity, and task-related connectivity.

### Training objective (loss)
There is no learnable model or explicit optimization loss. The core analysis is regression and group-comparison testing of whether early behavioral or neural changes predict later symptom improvement.

### Architecture / parameterization
An open-label longitudinal biomarker design combining repeated behavioral testing, task fMRI, and clinical outcome measurement during a four-week left dorsolateral prefrontal intermittent theta-burst stimulation course.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Depression TMS still has a mechanism problem. A lot of the literature points to resting-state target correlations, but much less is known about what information-processing changes during treatment actually accompany later improvement.

### 2. What is the method?
Participants completed baseline behavioral and fMRI emotional-face-processing tasks, received twenty daily sessions of left dorsolateral prefrontal intermittent theta-burst stimulation over four weeks, repeated the tasks after about eight sessions, and were then assessed for clinical outcome at Week 4. The analyses asked whether early changes in positive bias predicted later response.

### 3. What is the method motivation?
The paper is motivated by the neuropsychological theory that antidepressant treatments work partly by shifting processing away from negative bias and toward positive information. The authors test whether TMS shows that kind of early shift rather than merely assuming it shares drug mechanisms.

### 4. What data does it use?
Forty-nine completers with major depressive disorder from the BRAEN-MAP study in Sao Paulo. Participants were adults aged eighteen to sixty-five, not necessarily treatment resistant, and thirty were taking stable psychoactive medication. Behavioral data came from a facial-expression-recognition task, and neural data came from task fMRI using happy-versus-fearful face processing.

### 5. How is it evaluated?
Clinical response was defined as at least fifty percent HAM-D reduction by Week 4, with HAM-D improvement also analyzed continuously. The authors tested whether baseline-to-Week-2 changes in several behavioral positive-bias metrics and in task-fMRI activity or connectivity predicted those Week 4 outcomes while controlling for baseline severity and other covariates.

### 6. What are the main results?
- Thirty-three participants were classified as responders and sixteen as non-responders.
- The only behavioral metric that significantly tracked response was positive-bias misclassification, meaning responders became more likely to interpret ambiguous facial expressions as positive.
- That behavioral shift predicted categorical clinical response after covariate adjustment, though it did not significantly predict continuous HAM-D improvement.
- Clinically greater HAM-D improvement was associated with increased positive-versus-negative bias in rostral anterior cingulate and other default-mode-network regions during the emotional task.
- Improvement was also associated with more positive-bias task-related connectivity between rostral anterior cingulate and posterior default-mode-network, sensorimotor, and visual areas.
- The neural signals predicted later outcome beyond early symptom change, which makes the mechanism story more interesting than a simple reflection of already-improved mood.

### 7. What is actually novel?
The novelty is not that TMS can help depression. The useful novelty is testing an early-treatment task-evoked mechanism directly, with both behavioral and neural measures, instead of reading mechanism backward from resting-state targeting or only comparing pre-treatment to post-treatment endpoints.

### 8. What are the strengths?
- Full text was accessible, so this note is not based on abstract theater.
- The study measures a plausible mechanism during treatment rather than only before and after treatment.
- It combines behavior and task-fMRI instead of relying on one modality.
- The neural effects still predicted outcome after accounting for early symptom change, which raises the bar above simple state mirroring.
- The paper gives TMS a more specific mechanism candidate than generic cortico-limbic normalization language.

### 9. What are the weaknesses, limitations, or red flags?
- There is no sham or other control arm, so placebo and natural trajectory effects cannot be ruled out.
- Symptoms had already improved by Week 2, which weakens temporal-causality claims.
- The sample is modest and skewed toward women.
- Participants were not restricted to treatment-resistant depression, so the result is not a clean TRD-specific mechanism story.
- Many participants were on psychoactive medication, which may interact with the observed changes.
- Only one of the four behavioral positive-bias metrics clearly tracked response, which limits the sense of a broad robust behavioral effect.

### 10. What challenges or open problems remain?
The obvious next challenge is replication in a sham-controlled design with earlier sampling points so one can tell whether the positive-bias shift truly precedes clinical improvement. The field also still needs to know whether these task-evoked measures add value over physiology, connectomics, or structural-route features when combined in one response-prediction stack.

### 11. What future work naturally follows?
Run sham-controlled and multisite replications, sample behavior and neural markers earlier than Week 2, compare TMS directly with antidepressant drugs or psychotherapy arms, and test whether task-evoked positive-bias changes combine usefully with biomarkers such as MMN or structural pathway metrics.

### 12. Why does this matter for cabbageland?
Because it pushes depression TMS toward a less embarrassing mechanism story. Instead of pretending a cortical target coordinate already explains efficacy, the paper asks whether the treatment is visibly changing an intervention-relevant cognitive-affective process during the course itself.

### 13. What ideas are steal-worthy?
- Measure candidate mechanisms during treatment, not only before versus after treatment.
- Treat task-evoked positive-versus-negative bias as a sharper object than generic resting-state normalization.
- Ask whether response prediction improves when dynamic task markers are layered on top of structural or physiological baselines.
- Keep mechanism claims probabilistic and staged rather than declaring victory from one open-label study.

### 14. Final decision
Keep. This is one of the more useful recent depression-TMS mechanism papers, but it should be read as a promising mechanism candidate constrained by open-label design rather than as settled proof.
