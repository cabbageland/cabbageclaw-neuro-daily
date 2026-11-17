# Assessing the validity and reliability of computational phenotyping of motivation

## Basic info

* Title: Assessing the validity and reliability of computational phenotyping of motivation
* Authors: Claire Jaffré; Pablo Carrillo; Etienne Pigeon; Jean Daunizeau; Raphaël Le Bouc; Jacob Dhôte; Mathias Pessiglione; Fabien Vinckier
* Year: 2026
* Venue / source: PLOS Mental Health 3(11), e0000730; published November 16, 2026
* Link: https://doi.org/10.1371/journal.pmen.0000730
* Date surfaced: 2026-11-17
* Why selected in one sentence: It audits which computational motivation parameters are recoverable and temporally stable, while exposing why a stable group mean is not a validated individual treatment-response signal.

## Quick verdict

* Highly relevant

Preserve as a measurement-design paper, not as a ready-made treatment-selection biomarker. Mean preference values and performance-task reward/effort parameters fare substantially better than fatigue, but model-based measures do not outperform simpler measures in test–retest reliability. The important intervention-facing distinction is between recovering a parameter, preserving people's rank order, and detecting clinically meaningful within-person change.

## One-paragraph overview

Jaffré and colleagues test two existing computational approaches to motivation: jointly fitting ratings and choices about everyday rewards, punishments, and efforts, and fitting handgrip force as an effort-allocation decision under monetary incentives. They combine simulations, parameter-recovery and misspecification checks, held-out choices, and two visits four weeks apart. Of 72 recruited healthy adults, 67 contribute preference-task retests and 58 complete both task families. Results support selected parameters rather than a unitary, interchangeable motivation phenotype: preference and performance estimates do not significantly correlate across people, fatigue is weakly stable, and changes in performance parameters do not significantly track changes in the assessed affect/distress scores. All task earnings were explicitly fictitious; only the fixed participation compensation was paid.

## Model definition

### Inputs

- Preference model: item identities/dimensions, continuous likeability or aversiveness ratings, within-dimension binary choices, and accept/reject choices trading effort, punishment, and reward. Each dimension has 24 natural items; additional monetary items appear in the reward/punishment ratings.
- Performance model: six nominal incentive levels across 60 handgrip trials, trial index, observed peak force, and calibration/proxy information about maximum force. Incentives range from €0.01 to €20 but are not paid out.
- Questionnaire scores and demographics are validation/covariate data, not inputs to a learned clinical response predictor.

### Outputs

- Preference model: one latent subjective value per item, three task-specific sigmoid slopes, and predicted ratings/choice probabilities. Dimension-level means are the main retained phenotypes; between-item dispersion is poorly recovered.
- Performance model: incentive sensitivity `Ki`, effort-cost sensitivity `Kc`, fatigue sensitivity `Kf`, and a maximum-performance parameter `Pmax`; predicted force follows from the model's optimal effort on each trial.
- Neither model emits a stimulation setting, diagnosis, treatment recommendation, or demonstrated response forecast.

### Training objective (loss)

Models are inverted separately for individual participants using the VBA toolbox's variational Bayes/Laplace approximation, trading likelihood fit against prior/model complexity through approximate model evidence. Continuous ratings use a measurement-noise precision with Gamma hyperpriors; binary choice/acceptance observations use Bernoulli likelihoods. The performance model compares predicted optimal performance with observed force. This is Bayesian behavioral-model inversion, not supervised training against clinical outcomes. Maximizing expected net value is the modeled participant's decision rule, distinct from the investigator's fitting objective.

### Architecture / parameterization

The preference model shares item values across three sigmoid observation mappings. Slopes are task-specific but shared across reward, punishment, and effort: this constrains dimension-specific differences to appear in inferred values. Multiplying values and inversely rescaling slopes leaves predicted behavior unchanged, so absolute value scale and slopes are not separately identifiable; priors anchor the estimates. The performance model maps effort through a saturating force-production function, then chooses effort to maximize performance/reward benefits minus quadratic effort cost multiplied by a fatigue term increasing linearly with trial number. `Pmax` can be fitted with a proxy-centered prior rather than fixed to an imperfect proxy. There is no neural network, circuit model, or learned feedback policy.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Can computational motivation measures be interpreted across repeated assessments, or do nonidentifiability, calibration error, and retest effects undermine apparent clinical changes?

### 2. What is the method?

Fit shared subjective values to three preference subtasks and an effort-allocation model to handgrip performance. Audit simulations against known parameters, perturb maximum-force assumptions and selected functional forms, predict held-out choices, and compare fitted parameters across two visits using correlations, ICCs, mean differences, and Bayesian model comparison.

### 3. What is the method motivation?

Similar apathy scores could reflect different reward valuations or effort costs. Decomposing them is useful only if the task/model can distinguish those quantities. Explicit recovery and retest checks are stronger than naming a fitted coefficient a mechanism.

### 4. What data does it use?

Seventy-two French-speaking healthy adults were recruited in 2018–2019. Four missed the second visit and one was excluded for psychiatric symptoms, leaving 67 preference-task participants, including 58 who completed both task families. The retained sample was predominantly female, mean age about 53; the reported age range was 27–69. Visits were four weeks apart. Behavioral tasks and questionnaires are combined, but there are no neural recordings, patient treatment outcomes, or adolescent data. Code/data are linked by the authors at https://doi.org/10.5281/zenodo.20644806; not independently executed here.

### 5. How is it evaluated?

Simulation recovery separates item values, dimension summaries, and nuisance slopes, including noise-free and limited misspecified-model checks. Held-out-choice comparisons remove six choices of each type, repeated 12 times, and compare joint latent-value estimates with ratings alone. Empirical longitudinal evaluation uses within-person visit contrasts and across-person temporal correlations/ICCs. These answer different questions: fit/recovery, predictive choice accuracy, and temporal stability are not interchangeable measures of clinical responsiveness.

### 6. What are the main results?

- Simulated preference dimension means recover well: generative-versus-fitted correlations are **0.89 / 0.88 / 0.91** for effort/punishment/reward. Between-item SD recovery is weaker, **0.46 / 0.43 / 0.42**, and remains only modest without observation noise. The binary-choice slope itself recovers poorly (`r = 0.04`).
- Empirical preference means show four-week correlations of **0.53 / 0.57 / 0.70**, without significant mean visit differences. Joint values generally improve held-out-choice prediction over ratings alone, but the binary-effort comparison is only a trend (`p = 0.09`).
- Performance-task correlations are **0.71 for Ki, 0.47 for Kc, and 0.18 for Kf**; corresponding ICCs are **0.55 / 0.41 / 0.28**. Fatigue's temporal correlation is not significant (`p = 0.17`). Reward sensitivity increases modestly at visit two (`d = 0.27`, `p = 0.037`).
- Bayesian model comparison favors allowing individual `Kc` and `Kf` to vary between visits, despite nonsignificant group mean differences. Group cancellation is not individual stability.
- Preference and performance estimates do not significantly correlate for effort (`r = -0.18`, `p = 0.19`) or reward (`r = -0.11`, `p = 0.42`). No performance-parameter change significantly correlates with LAPS/EFQ score change.
- The authors find **no test–retest reliability advantage over model-free measures**; those are generally as reliable and sometimes slightly more reliable. Fitting `Pmax` improves simulated recovery when its proxy is unreliable, but does not establish a clinical calibration solution.

### 7. What is actually novel?

The contribution is a parameter-specific psychometric audit of existing models, not a new motivation algorithm or causal circuit discovery. The useful combination is recovery, repeated measurement, calibration uncertainty, and explicit negative findings about cross-task convergence and denoising.

### 8. What are the strengths?

The paper reports failures rather than hiding them: nuisance-scale ambiguity, weak dispersion/fatigue recovery, nonconvergent tasks, and absent model-based reliability gains. It tests realistic noise, selected model misspecifications, and maximum-performance uncertainty, and separates group effects from individual classification.

### 9. What are the weaknesses, limitations, or red flags?

Healthy-volunteer retest stability is not sensitivity to actual treatment-induced change. Only one interval is tested, tasks occur in fixed order, and hypothetical earnings limit transfer to consequential effort allocation. Latent values depend on priors and shared-slope assumptions; forcing dimension differences into values does not prove that the brain changed valuation rather than response processes. Fatigue is modeled by trial number, not accumulated exertion, and partly trades off with effort cost. Demographic analyses are exploratory, with a small male subgroup and reported uncorrected performance-task age/sex tests. Some phenotype-recovery simulations tolerate false-positive rates below 0.15, which is not uniformly nominal 0.05 control. Strong fits or recovery under the chosen generative family cannot exclude different real mechanisms. The abstract's suggestion that between-assessment disparities can be readily interpreted is broader than these data justify.

### 10. What challenges or open problems remain?

Separate measurement error from genuine state change; establish individual change thresholds; test patient and site generalization; and determine whether these measures add prediction beyond questionnaires and simple behavior. A low retest coefficient can reflect noise or true state variation, so it should neither automatically disqualify a state marker nor be excused without validation.

### 11. What future work naturally follows?

Use repeated baselines and a randomized intervention with independent functional outcomes, multiple intervals, and participant-level held-out evaluation. Compare model-free summaries, a hierarchical/shrinkage model, and the original inversion under the same data budget. Test actual versus hypothetical rewards and a fatigue process driven by recent effort. Validate change estimates before testing treatment-response stratification.

### 12. Why does this matter for cabbageland?

Psychiatric neuromodulation needs interpretable readouts of what changed, not just symptom totals. These tasks could complement network/electrophysiology state estimates, but the paper does not identify stimulation targets or show controllability of reward/effort parameters. It earns a limited computational-measurement claim, not mechanistic psychiatry in the causal-intervention sense.

### 13. What ideas are steal-worthy?

- Gate every proposed control-state coordinate on recovery, individual temporal uncertainty, and intervention sensitivity separately.
- Keep calibration parameters uncertain rather than fixing a noisy maximum and letting other coefficients absorb its error.
- Require model-free and questionnaire baselines before calling latent-state estimation a denoising improvement.
- Report cross-task disagreement and parameter-specific failures; do not average them into one flattering motivation score.
- For CBT-plus-stimulation studies, predefine whether the intended change is valuation, experienced effort, or clinical function, then measure it with more than a shared label.

### 14. Final decision

**Highly relevant; preserve for biomarker and longitudinal-study design.** Prefer selected mean preference values and reward/effort-cost estimates over a standalone fatigue marker, subject to patient-specific validation. Do not interpret a recovered parameter or stable group mean as proof of a clinically meaningful, individually controllable state.

Inspection scope: publisher full-text HTML, including model descriptions, main results, methods, discussion, and figure captions. Supplementary figure files, numerical table downloads, repository code, and the underlying data were not independently audited.
