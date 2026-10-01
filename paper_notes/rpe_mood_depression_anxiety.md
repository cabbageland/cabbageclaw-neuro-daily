# Dissociable roles of reward prediction error in the contrasting mood dynamics of depression and anxiety

## Basic info

* Title: Dissociable roles of reward prediction error in the contrasting mood dynamics of depression and anxiety
* Authors: Zhihao Wang, Ting Wang, Tian Nan, Jiahua Xu, Andre Aleman, Yuejia Luo, Bastien Blain, Yunzhe Liu, Pengfei Xu
* Year: 2026
* Venue / source: eLife
* Link: https://elifesciences.org/articles/110631
* Date surfaced: 2026-10-01
* Why selected in one sentence: It separates depression-specific, anxiety-specific, and shared affective pathology into different computational signatures of momentary mood updating instead of treating mood variability as one generic symptom blob.

## Quick verdict

* Highly relevant

This is a strong computational-psychiatry keep because it takes a familiar mood-updating model and uses it to split depression and anxiety in a more mechanistic way than symptom totals allow. The note is based on full-text inspection through the Europe PMC / PMC XML, with the eLife landing page also reachable. The paper is still associative rather than causal, and the anxiety-specific result is weaker than the depression-specific result, especially in the clinical sample. But the central object is useful: RPE sensitivity becomes a candidate computational marker for how different affective dimensions update mood under uncertainty.

## One-paragraph overview

The paper studies how reward prediction errors shape momentary mood in people with different depression and anxiety dimensions. Across five experiments involving 2043 participants, including a clinical affective-disorders sample, participants completed questionnaire batteries and a gambling task with repeated "how happy are you now?" ratings. The authors used bifactor modeling to separate shared depression/anxiety burden from depression-specific and anxiety-specific factors, then fit a recency-weighted mood model in which current mood depends on certain rewards, expected values, reward prediction errors, and gradual drift. Depression-specific scores were associated with lower mood variability and reduced RPE-related mood sensitivity, including in patients. Anxiety-specific scores showed the opposite direction, higher mood variability and higher RPE sensitivity, but this was clearest only after pooling non-clinical datasets. The shared factor tracked lower baseline mood and greater risk aversion.

## Model definition

### Inputs

Inputs include trial-by-trial gambling-task events, chosen certain rewards, expected values of chosen gambles, obtained outcomes, reward prediction errors, repeated momentary mood ratings, participant age and gender covariates, task earnings, and questionnaire-derived depression/anxiety factor scores. The psychometric component uses responses to anxiety, depression, worry, mood, and personality questionnaires to estimate orthogonal general, depression-specific, and anxiety-specific factors.

### Outputs

The main mood model outputs predicted momentary happiness ratings and participant-level parameters, especially baseline mood, reward sensitivity terms for certain reward, expected value, and RPE, a recency/forgetting parameter, and a drift term. The analysis then outputs associations and mediation estimates linking depression- and anxiety-specific factors to mood variation through the RPE sensitivity parameter. A separate choice-model analysis outputs risk-attitude and approach/avoidance parameters used to probe the shared depression/anxiety factor.

### Training objective (loss)

The paper fits individual-level model parameters by maximum likelihood estimation using MATLAB `fmincon`, with 50 random starts to reduce local-minimum problems. Candidate models are compared with Bayesian information criterion. Mediation and regression analyses test whether RPE-related mood sensitivity statistically explains the relationship between symptom factors and observed mood variation.

### Architecture / parameterization

The central architecture is the classic recency-weighted linear mood model: mood at time `t` is modeled as a baseline plus discounted histories of chosen certain reward, expected value, reward prediction error, and a time-drift term. The psychiatric decomposition is a bifactor psychometric model that separates general distress from depression-specific and anxiety-specific variance. The exploratory choice component uses an approach-avoidance prospect-theory-style model with risk attitude, loss aversion, and value-independent approach/avoidance parameters.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Depression and anxiety often co-occur, so ordinary symptom totals make it hard to know whether altered mood dynamics reflect depression, anxiety, or shared distress. The paper asks whether momentary mood updating under reward uncertainty contains separable computational signatures for these dimensions.

### 2. What is the method?

Participants completed questionnaire batteries and a gambling task with frequent momentary mood ratings. The authors first estimated bifactor symptom dimensions, then fit a computational mood model to each person's trial-by-trial ratings. They tested whether depression-specific, anxiety-specific, and shared factors related differently to mood variability, RPE sensitivity, baseline mood, and risk attitude.

### 3. What is the method motivation?

The motivation is that mood disorders are not just static high or low mood states. They involve how mood changes in response to expectation, outcome, and uncertainty. RPE is a natural computational object here because it describes how surprising outcomes update affective state, and it can be estimated in a simple task with repeated subjective mood readouts.

### 4. What data does it use?

The study uses five datasets. A psychometric dataset of 901 participants establishes the anxiety/depression factor structure. A laboratory gambling-task dataset, two online gambling-task datasets, and a clinical affective-disorders dataset test the mood-model associations. The paper reports final non-clinical task samples of 44, 747, and 235 participants and a clinical sample of 116 patients after exclusions.

### 5. How is it evaluated?

Evaluation has several layers. The authors report mood-model fit across datasets, with mean R-squared values around 0.64 to 0.69 in non-clinical gambling-task datasets and 0.47 in the clinical dataset. They compare alternative mood models with BIC, run parameter-recovery checks, test correlations and covariate-adjusted regressions between factor scores and mood parameters, and use mediation analyses to test whether RPE sensitivity accounts for symptom-factor relationships with mood variability. They also use pooled non-clinical analysis and mini meta-analysis for the weaker anxiety effect.

### 6. What are the main results?

Depression-specific scores were consistently associated with dampened mood fluctuations and lower RPE-related mood sensitivity across non-clinical datasets. The same depression-related RPE hyposensitivity pattern replicated in the clinical affective-disorders sample. Anxiety-specific scores showed the opposite direction, with intensified mood fluctuations and higher RPE sensitivity, but the effect was statistically reliable mainly in the pooled non-clinical sample rather than in every dataset individually. The shared depression/anxiety factor related to lower baseline mood and greater risk aversion rather than to the same RPE-specific pattern.

### 7. What is actually novel?

The novelty is not that RPE influences mood; that is established. The useful novelty is using bifactor symptom decomposition to show that depression-specific and anxiety-specific dimensions point in opposite directions on RPE-driven mood updating, while shared distress maps onto a different baseline/risk profile.

### 8. What are the strengths?

The paper combines psychometric decomposition, computational modeling, multiple replication datasets, a clinical sample, model comparison, and public data/code. It keeps depression/anxiety comorbidity explicit instead of treating it as noise. It also gives a clinically interpretable marker candidate: depression looks like affective hyposensitivity to prediction error, while anxiety may look like affective hypersensitivity to prediction error under uncertainty.

### 9. What are the weaknesses, limitations, or red flags?

This is still association, not causal identification. The task is a stylized gambling paradigm, so translation to daily-life mood, therapy response, or stimulation response is not automatic. The anxiety-specific signal is weaker than the depression-specific signal and was not replicated cleanly in the clinical sample; the authors estimate that a much larger clinical sample would be needed to detect an anxiety effect of the observed size. Mood variation and RPE sensitivity both depend on subjective rating behavior, so scale-use differences remain a possible nuisance even though the authors probe it. Clinical medication status and diagnosis heterogeneity also limit clean interpretation.

### 10. What challenges or open problems remain?

The biggest open problems are causal validation, ecological validity, and treatment relevance. The field still needs to know whether changing RPE sensitivity changes symptoms, whether these task parameters predict response to CBT, ketamine, TMS, or psychedelic-assisted therapy, and whether the same signatures appear in longitudinal daily-life data rather than a laboratory gambling task.

### 11. What future work naturally follows?

Use the RPE mood-sensitivity parameter as a prespecified stratification or mediator in treatment studies. Test whether depression interventions normalize hyposensitivity while anxiety interventions reduce hypersensitivity or alter uncertainty handling. Combine the task with neuroimaging, physiology, or EMA so the model can connect trial-level affective updating with brain-state and real-world mood dynamics.

### 12. Why does this matter for cabbageland?

Cabbageland cares about intervention logic, not diagnostic mush. This paper gives a clean example of how a computational parameter can split comorbid symptom dimensions that ordinary labels blur. It is especially useful for thinking about psychotherapy plus interventional psychiatry: if depression and anxiety differ in how surprising outcomes update mood, then exposure, CBT, ketamine, TMS, and psychedelic therapy may need different state-change and learning-readout logic rather than one generic "mood improved" endpoint.

### 13. What ideas are steal-worthy?

Use orthogonal symptom factors before interpreting computational parameters. Treat mood variability as a model-estimated updating process, not merely a descriptive standard deviation. Separate baseline affect, risk attitude, and event-driven mood sensitivity. In treatment studies, ask whether an intervention changes the mapping from prediction error to mood, not only whether total symptom score drops.

### 14. Final decision

Preserve. This is not a finished biomarker for clinical decisions, but it is a sharp computational-psychiatry note because it turns depression/anxiety comorbidity into separable model parameters with real downstream use for stratification, mechanism, and treatment-response hypotheses.
