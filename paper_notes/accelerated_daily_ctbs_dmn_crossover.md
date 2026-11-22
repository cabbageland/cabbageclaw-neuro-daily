# Accelerated vs. Daily TMS: Resting-State Functional Connectivity in a Within-Subjects Crossover Trial

## Basic info

* Title: Accelerated vs. Daily TMS: Resting-State Functional Connectivity in a Within-Subjects Crossover Trial
* Authors: Jillian G. Connolly; Sophia H. Blyth; Libby C. Tunison; Maxwell J. Roeske; Simon Vandekar; Baxter P. Rogers; Roscoe O. Brady; Heather Burrell Ward
* Year: 2026
* Venue / source: medRxiv preprint; version 1 posted November 20, 2026; not peer reviewed
* Link: https://doi.org/10.64898/2026.11.17.26368336
* Date surfaced: 2026-11-22
* Why selected in one sentence: It compares matched-dose daily and accelerated cTBS within people using a network endpoint, while exposing the distinction between an undetected schedule effect and demonstrated neural equivalence.

## Quick verdict

* Useful

Preserve as a neural-endpoint and schedule-comparison design reference, not evidence that pulse count makes timing irrelevant. The within-person comparison is valuable, but everyone received daily treatment first, the reported schedule-effect interval is broad, and the study is not a formal noninferiority/equivalence trial. It does not establish comparable clinical efficacy or a causal DMN-mediated treatment mechanism.

## One-paragraph overview

Returning participants from two clinical trials received five daily sessions of individualized left-parietal DMN cTBS, then five sessions in one day after an average interval of about a year. Each session delivered 600 pulses at 100% active motor threshold; accelerated sessions had 30-minute intersession intervals. In 34 analyzed adults with psychotic or other psychiatric disorders, bilateral parietal resting-state connectivity decreased across courses, but the difference in change between schedules was not significant. The endpoint was measured several days after treatment, so the result concerns delayed pairwise BOLD connectivity—not equivalent acute plasticity, symptom change, or whole-network control.

## Model definition

This is an explanatory imaging-analysis study, not a learned controller or validated individual response predictor. The modeled components are linear mixed-effects analyses of connectivity and connectivity change; target construction is a connectivity-mapping procedure.

### Inputs

- Resting-state fMRI and a standard DMN template warped to native space define an individual left posterior inferior-parietal connectivity cluster; its averaged center supplies the neuronavigated target used for both courses.
- For the outcome, the main text describes BOLD time courses from 6-mm parietal ROIs, including left coordinates (-46, -66, +30), correlated and z-transformed. Do not silently equate these fixed outcome coordinates with the individual stimulation coordinates.
- Analyses use pre/post visit or baseline connectivity and change, treatment schedule, psychosis/non-psychosis group, age in an exploratory model, and participant identity.

### Outputs

Fitted mean connectivity or connectivity change, schedule/group/age associations, and inferential statistics with participant random effects. No stimulation action, optimized schedule, prospective clinical response probability, or estimated biological transition law is produced.

### Training objective (loss)

Linear mixed-model estimation rather than a policy-learning objective. The main text does not specify an explicit loss formula, optimizer, or ML versus REML estimation; do not invent those details. The reported t tests evaluate fitted associations, not held-out prediction accuracy or an equivalence margin.

### Architecture / parameterization

Linear fixed effects with a participant random effect; the main text does not fully specify the random-effects covariance structure. Separate models test pre/post change, schedule adjusted for baseline connectivity, schedule-by-diagnostic-group interaction, and exploratory age effects. Correlation-based targeting is not a mechanistic network model, and these analyses are not closed-loop control.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Does compressing a matched number of parietal cTBS sessions into one day alter a delayed neural endpoint compared with daily delivery in the same participants? This is narrower than asking whether accelerated TMS is clinically noninferior across disorders, targets, or doses.

### 2. What is the method?

Fixed-order within-person comparison: five daily sessions first, five same-day sessions later. Each course totals 3,000 nominal pulses. Courses were at least 121 days apart, with a mean interval of 379.26 days and maximum of 972 days. Individualized parietal targeting and nominal session parameters are matched; mixed-effects analyses compare Fisher-z-transformed bilateral parietal connectivity and its change.

### 3. What is the method motivation?

Comparing the same people reduces stable between-person heterogeneity, while a previously studied parietal connectivity endpoint supplies a tractable neural readout outside the usual depression/DLPFC setting. Matching dose makes schedule a clearer experimental variable—but only if period effects, baseline differences, and measurement timing are also controlled.

### 4. What data does it use?

Thirty-six adults aged 18–65 enrolled; 34 completed both schedules and entered analysis, including 19 with psychotic disorders and 15 with other psychiatric disorders. The study reports 126 usable pre/post scans after quality control, fewer than four scans per analyzed participant overall. Imaging used a single 3-T Philips scanner with multiple 10-minute resting-state runs. Post-treatment scans occurred within eight days: mean 4.39 days after daily treatment and 4.91 after accelerated treatment. Missing-scan handling and detailed preprocessing were not independently audited here.

### 5. How is it evaluated?

In-sample mixed-effects inference tests the pooled pre/post change, baseline-adjusted schedule contrast, diagnostic interaction, and exploratory age association. There is no prespecified neural equivalence margin, no held-out individual prediction test, and no sham course in the reported schedule comparison. Retention across a long interval is a strength, but returning participants are not necessarily representative of everyone who starts treatment.

### 6. What are the main results?

- Pooled across schedules and participants, connectivity decreased: t(90.16) = -2.07, p = 0.0416. Without a sham comparison, this is a pre/post association rather than isolation of a stimulation-specific effect.
- The schedule contrast was not significant: t(31.27) = -0.44, p = 0.67; reported Cohen's d = 0.12, 95% CI [-0.45, 0.69]. The interval leaves appreciable differences unresolved; a null test does not establish equivalence.
- Diagnostic group did not significantly predict change, and the schedule-by-group interaction was not significant (p = 0.292). Small subgroups do not establish transdiagnostic invariance.
- Older age was associated with greater reduction in an exploratory model: t(26.91) = -2.21, p = 0.036. This is not a validated age-based treatment-selection rule.
- Baseline connectivity strongly predicted its own change. Because change contains baseline by definition, regression to the mean and measurement coupling need testing before this becomes a response biomarker.
- No serious adverse events were reported. Minor adverse-event tables were not independently examined; this sample cannot establish rare-event safety.

### 7. What is actually novel?

The useful contribution is a within-person comparison of delayed neural effects from matched-dose schedules at an individualized parietal DMN target in a mixed psychiatric sample. The authors frame this as the first neural-effects comparison; that priority claim was not independently established here. The work does not newly demonstrate clinical noninferiority or prove that cumulative dose dominates schedule.

### 8. What are the strengths?

Matched nominal stimulation dose, the same individuals across courses, anatomically/network-informed neuronavigation, a predefined regional endpoint with prior experimental use, and repeat imaging. The discussion explicitly acknowledges fixed order, limited precision, and lack of formal noninferiority power rather than concealing those problems.

### 9. What are the weaknesses, limitations, or red flags?

- **Causal identification:** schedule is confounded with period/order. A long washout reduces one carryover concern but cannot erase illness progression, medication changes, aging, or participation effects.
- **Equivalence:** no prespecified margin, broad interval, and small sample. The discussion's broader cumulative-dose principle is stronger than the data warrant.
- **Targeting:** an individualized correlational DMN target is not a demonstrated optimal therapeutic site. The main-text relationship between fixed outcome ROIs and individual stimulation locations deserves explicit sensitivity analysis.
- **Timing:** four-to-five-day follow-up may miss schedule-dependent acute dynamics, metaplasticity, or recovery kinetics. Equal endpoint values can arise through different trajectories.
- **Heterogeneity:** psychosis/non-psychosis bins collapse diverse conditions; null interactions are not evidence that patient-level modifiers do not exist.
- **Biomarkers:** baseline-versus-change coupling and age associations need reliability assessment, independent replication, and prospective validation.
- **Evaluation scope:** regional undirected BOLD correlation is not effective connectivity, cellular inhibition, controllability, or clinical benefit. No symptoms-to-connectivity mediation claim is established by this comparison.
- **Transfer:** one site, parietal cTBS, five sessions, and a particular interval cannot license conclusions about DLPFC iTBS, full treatment courses, other coils/devices, adolescent treatment, or long-term outcomes.

### 10. What challenges or open problems remain?

Which endpoint and equivalence margin would make two schedules meaningfully interchangeable? Do acute trajectories or clinically relevant subgroups differ despite similar delayed regional connectivity? How stable are individualized targets and the readout across the long inter-course interval? A scalar connectivity change does not answer those questions.

### 11. What future work naturally follows?

Randomize or counterbalance schedule order, include sham where needed to identify target engagement, and power a prespecified equivalence/noninferiority analysis. Measure immediate, intersession, next-day, and delayed responses alongside symptoms and adverse events. Replicate across targets/devices and estimate reliability-adjusted baseline effects; evaluate a locked individual-response model on new participants if personalization is claimed.

### 12. Why does this matter for cabbageland?

Schedule is an intervention variable, not administrative packaging. This study supplies a concrete neural-endpoint design and a warning against reducing a control problem to total pulse count. Treat network targeting, state readout, and schedule-dependent transition dynamics as separate components that each require validation.

### 13. What ideas are steal-worthy?

- Match nominal dose within people, but counterbalance order and model period effects explicitly.
- Compare complete response trajectories rather than only a delayed post-treatment scalar.
- Predeclare what difference would matter, then report whether the interval excludes it.
- Separate target-localization reliability, readout reliability, and treatment-response prediction; do not let a baseline/change correlation stand in for all three.

### 14. Final decision

Keep as **Useful**, directly relevant protocol-design and network-endpoint context. Do not cite it as proof that accelerated and daily schedules are neurally equivalent, clinically interchangeable, or governed only by cumulative dose. Inspection: main full-text PDF, including methods, results, limitations, and selected figure/table descriptions; separate supplements, raw data/code, and trial-registration history were not audited.
