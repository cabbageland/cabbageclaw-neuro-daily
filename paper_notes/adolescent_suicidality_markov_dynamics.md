# Modelling temporal dynamics of suicidal ideation and behaviour across pre- to early adolescence using a Markov framework

## Basic info

* Title: Modelling temporal dynamics of suicidal ideation and behaviour across pre- to early adolescence using a Markov framework
* Authors: Sieun Lee, Ben Cardoen, Marianne Etherson, Nitish Jawahar, Ellen Townsend, Kapil Sayal, Peter Fonagy, Aja Murray, Joanna Lockwood, Ayan Mahamud, Chris Hollis, Rory O'Connor, Dorothee Auer
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2608.02896
* Date surfaced: 2026-08-07
* Why selected in one sentence: It turns early-adolescent suicidality from a static risk-label problem into an explicit state-transition and uncertainty problem that is much closer to how monitoring and intervention decisions actually have to work.

## Quick verdict

* Highly relevant

This is not a mechanistic brain paper, but it is still a strong preserve after full-text inspection because it gives developmental suicidality a better computational frame than the usual trait-score mush. The useful move is not just fitting transitions. It is combining age-indexed Markov dynamics, first-passage queries, bootstrap uncertainty, and entropy so that remission, escalation, persistence, and volatility can be discussed in the same language. The limits are equally clear: annual self-report is coarse, the first-order Markov assumption is untested, and the model is cohort-level and descriptive rather than an individualized predictor.

## One-paragraph overview

The paper uses child self-report data from 11,864 participants in the ABCD Study from ages 9-10 through 12-13 to build a time-inhomogeneous discrete-time Markov chain over eight states defined by suicidal ideation or behaviour severity and the presence or absence of co-reported non-suicidal self-injury, or NSSI. Instead of treating suicidality as a single scalar or assuming smooth latent trajectories, the authors estimate year-specific transition matrices, multi-year transition probabilities, first-passage probabilities to suicidal behaviour, and uncertainty measures for different trajectories. The main pattern is clinically legible and not trivial: remission to a no-report state is common but declines with age and with more advanced starting states, while co-reported NSSI consistently shifts children toward higher risk, lower remission, and greater trajectory instability. The paper matters because it preserves volatility rather than smoothing it away and makes that volatility queryable.

## Model definition

### Inputs
Annual child-report KSADS-derived binary DSM-5 indicators for current and lifetime non-suicidal self-injury, passive suicidal ideation, active suicidal ideation, suicidal preparatory action, and suicide attempt from the ABCD cohort, aggregated into eight discrete longitudinal states across four yearly time points from ages 9-10 to 12-13.

### Outputs
Year-specific state-to-state transition matrices, multi-year transition probabilities, first-passage probabilities to target states such as suicidal behaviour, bootstrap confidence intervals for transition estimates, entropy-based uncertainty scores for each origin state, and statistical comparisons between queried trajectory families.

### Training objective (loss)
There is no trainable predictive model or optimization loss in the machine-learning sense. Transition probabilities are estimated empirically from observed counts, then uncertainty is quantified with bootstrap resampling and Shannon entropy.

### Architecture / parameterization
A first-order, time-inhomogeneous discrete-time Markov chain over eight states, paired with bootstrap-based uncertainty estimation, normalized Shannon entropy for transition unpredictability, and a regular-expression-like query system for custom multi-year trajectory patterns.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to describe how suicidal ideation, suicidal behaviour, and NSSI actually move over time in pre- to early adolescence without pretending they are either static labels or smooth continuous trajectories. The paper wants a framework that can talk about escalation, remission, persistence, and instability directly.

### 2. What is the method?
The method is a time-varying Markov model over eight clinically defined states. The authors estimate separate one-year transition matrices for each age interval, derive multi-year transition and first-passage probabilities, and quantify both sampling uncertainty with bootstrapping and dynamical uncertainty with entropy.

### 3. What is the method motivation?
The motivation is that sparse annual community-cohort data do not support fancy continuous trajectory stories very honestly, and suicidality in youth is visibly volatile rather than smoothly monotone. A state-transition model respects that structure better and lines up more naturally with ideation-to-action reasoning.

### 4. What data does it use?
It uses ABCD Study child self-report KSADS data from 11,864 U.S. children recruited at age 9-10 and followed annually through age 12-13 in the released dataset used here. Parent reports are described, but the main transition analyses are based on child reports because they better capture subjective internal experience.

### 5. How is it evaluated?
The paper evaluates the framework by inspecting prevalence and co-occurrence trends, year-to-year transition matrices, NSSI-versus-no-NSSI comparisons with bootstrap confidence intervals, entropy patterns across states and ages, and custom multi-year trajectory queries such as the probability that passive ideation progresses to suicidal behaviour within three years.

### 6. What are the main results?
- Any lifetime suicidal ideation or behaviour is already common in this cohort, around 9 percent at age 9-10 and above 12 percent by age 13-14, with active ideation and suicidal behaviour rising more sharply than passive ideation.
- Remission to a no-report state is the most likely next-year outcome for most starting states, but that remission probability drops with age and with more advanced starting states.
- NSSI is not just an additive bad sign. It systematically lowers remission, raises escalation to or persistence in suicidal behaviour, and increases transition uncertainty.
- By age 11-12, children with active ideation plus NSSI have about a 6 percent next-year probability of transitioning to suicidal behaviour, versus about 4 percent for active ideation without NSSI.
- A child with passive ideation at age 9-10 has about a 7.8 percent three-year probability of reaching suicidal behaviour, which rises to about 11 percent when NSSI is co-reported.
- Child-parent concordance is poor, with most reports endorsed by only one informant.

### 7. What is actually novel?
The novelty is not Markov chains by themselves. The useful novelty is applying a time-inhomogeneous multistate Markov framework, with uncertainty and first-passage queries, to a large developmental suicidality dataset in a way that preserves categorical structure and volatility instead of washing everything into a risk score or latent curve.

### 8. What are the strengths?
- The cohort is large for this kind of youth mental-health trajectory work.
- The state definitions are clinically legible rather than mathematically decorative.
- The method is interpretable, reproducible, and easy to query for clinically meaningful scenarios.
- It treats uncertainty as part of the phenomenon, not just error bars to ignore.
- The NSSI findings are stronger than a vague "higher risk" claim because they show both directional shift and reduced predictability.

### 9. What are the weaknesses, limitations, or red flags?
- The data are annual and coarse, so within-year onset and remission get collapsed together.
- Current and lifetime indicators are aggregated, which creates temporal ambiguity.
- The first-order Markov assumption may miss important history effects.
- The model is cohort-level and descriptive, not individualized prediction or causal identification.
- There are no intervention variables, neural measures, or biologically grounded moderators inside the main state model.
- ABCD sampling and attrition biases may underrepresent structurally disadvantaged families.

### 10. What challenges or open problems remain?
The big open problems are how to condition these transitions on treatment, social context, developmental stage, and biological measures, how to handle longer history dependence without losing interpretability, and how to move from annual cohort summaries to clinically useful higher-frequency monitoring.

### 11. What future work naturally follows?
Natural next steps are higher-order or covariate-conditioned transition models, integration of neuroimaging or genetic measures as moderators, validation in higher-risk or clinical cohorts, and coupling the state model to intervention histories so monitoring and prevention become adaptive instead of static.

### 12. Why does this matter for cabbageland?
Because interventional psychiatry and developmental psychiatry both need better state logic. This paper suggests that youth suicidality is not just a matter of higher or lower average risk; it is a structured transition problem in which NSSI marks both elevated danger and elevated volatility. That is exactly the kind of framing that can later connect to biomarkers, adaptive monitoring, or treatment sequencing.

### 13. What ideas are steal-worthy?
- Model psychiatric trajectories as explicit state transitions rather than only scalar symptom curves.
- Preserve volatility and quantify it directly with entropy instead of smoothing it away.
- Treat self-harm modifiers such as NSSI as state dimensions, not just background covariates.
- Build queryable first-passage and multi-step trajectory estimates for clinically meaningful questions.
- Use uncertainty itself as a triage signal for follow-up intensity.

### 14. Final decision
Preserve. This is not the mechanistic endgame, but it is a sharp and reusable computational psychiatry scaffold for thinking about developmental suicidal trajectories, monitoring logic, and uncertainty-aware intervention design.
