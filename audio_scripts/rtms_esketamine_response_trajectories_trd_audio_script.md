Comparing transcranial magnetic stimulation and esketamine treatment response trajectories in resistant depression
Basic info
Title: Comparing transcranial magnetic stimulation and esketamine treatment response trajectories in resistant depression
Authors: Lindsay L. Benster, Jordan N. Kohn, Benjamin Wade, Noah Stapper, Cory R. Weissman, Jean-Philippe Miron, Zafiris J. Daskalakis, Lawrence G. Appelbaum
Year: 2026
Venue / source: Journal of Affective Disorders
Link:
Date surfaced: 2026-08-28
Why selected in one sentence: It cleanly separates faster relief from better ultimate efficacy in a real-world rTMS-versus-esketamine TRD cohort, which is exactly the distinction interventional psychiatry keeps blurring.
Quick verdict
Highly relevant
This is a preserve-worthy sequencing paper, not a mechanistic breakthrough. Its value is that it asks the clinically real question with a decent amount of discipline: when you compare standard real-world rTMS against intranasal esketamine, what differs most is not final efficacy but speed. Esketamine separates early on depression response and suicidal-ideation improvement, while the curves converge later. That is useful, but it does not earn a causal treatment-selection algorithm because the comparison remains retrospective, non-randomized, cadence-confounded, and protocol-heterogeneous.
One-paragraph overview
The paper retrospectively compares 279 rTMS patients and 93 intranasal esketamine patients treated for treatment-resistant depression at the UC San Diego Interventional Psychiatry Program between 2017 and 2025. Using inverse-probability treatment weighting, Cox time-to-response models, restricted mean survival time over 90 days, and sensitivity analyses, the authors show that esketamine was associated with faster antidepressant response and faster improvement in suicidal ideation. Median response occurred at 36 days for esketamine versus 49 days for rTMS, and suicidal-ideation improvement occurred at 9 versus 26 days. But by roughly 90 days the response curves converge enough that the honest interpretation is speed advantage, not proved superiority in overall effectiveness. That makes the paper clinically relevant for triage and sequencing, especially in more acute presentations.
Model definition
Inputs
Treatment modality, longitudinal PHQ-9 measurements, PHQ-9 item 9 for suicidal ideation, and baseline covariates including age, baseline PHQ-9, BMI, trauma history, anxiety comorbidity, benzodiazepine use, tobacco-use history, concurrent substance use, and number of psychiatric comorbidities.
Outputs
Propensity scores for treatment assignment, weighted time-to-response estimates, hazard ratios, restricted mean survival time differences, remission and suicidal-ideation improvement summaries, and modality-specific baseline predictors of faster or slower response.
Training objective (loss)
The paper uses logistic regression to estimate propensity scores, IPTW Cox proportional-hazards models for time-to-response, restricted mean survival time as a robustness summary under nonproportional hazards, and logistic regression for endpoint response analyses. The exact optimization details beyond those model families are only partly exposed in the main text.
Architecture / parameterization
A comparative observational analysis stack: baseline propensity-score model, stabilized and winsorized IPTW weighting, weighted Cox survival models, Kaplan-Meier and RMST summaries, plus within-modality predictor models and sensitivity analyses excluding prior-rTMS overlap and harmonizing assessment windows.
Key questions this summary must address
1. What problem is the paper trying to solve?
Clinicians choosing between rTMS and esketamine for TRD often need to know not just whether both work, but which one tends to relieve symptoms sooner, especially when suicidality or acute suffering makes time matter.
2. What is the method?
The authors run a retrospective head-to-head comparison using electronic medical records, treating time-to-response as the main object rather than only endpoint scores. They use IPTW Cox modeling, Kaplan-Meier curves, RMST over 90 days, and sensitivity analyses to reduce obvious baseline imbalances and test whether the early separation survives alternative assumptions.
3. What is the method motivation?
The motivation is straightforward and good: modality choice in interventional psychiatry is partly a time-allocation problem. A treatment that works a bit sooner can matter a lot in acute cases, even if longer-horizon outcomes later look similar.
4. What data does it use?
The cohort includes 372 adults with TRD and primary MDD treated at UCSD-IPP: 279 with rTMS and 93 with intranasal esketamine. The rTMS arm pools several real-world protocols, including iTBS, bilateral TBS, high-frequency left DLPFC, and low-frequency right DLPFC. Esketamine was delivered under supervised clinic conditions, typically twice weekly with dose escalation from 56 mg to 84 mg as tolerated.
5. How is it evaluated?
The primary evaluation is time-to-response, defined as at least 50 percent reduction in PHQ-9. The paper also examines remission, suicidal-ideation improvement using PHQ-9 item 9, propensity-balance diagnostics, prior-rTMS sensitivity analyses, and harmonized 7-day and 14-day assessment-window checks to address differential measurement frequency.
6. What are the main results?
Esketamine was associated with earlier response over the 90-day horizon, with RMST showing roughly 11.9 fewer days to response and IPTW Cox giving HR 1.62. Median response times were 36 days for esketamine and 49 days for rTMS. Response and remission rates were numerically higher for esketamine, but the paper argues the real difference is timing because the curves converge by about 90 days. Suicidal-ideation improvement was also earlier with esketamine, with median improvement at 9 versus 26 days. Within the rTMS arm, comorbid anxiety and benzodiazepine use predicted slower response, while former tobacco use predicted faster response. No clear baseline predictors emerged for esketamine, likely at least partly because the sample was smaller.
7. What is actually novel?
The novelty is not that ketamine-type treatments can act quickly. That is old news. The useful novelty is putting standard real-world rTMS and intranasal esketamine in the same temporal frame and showing that the honest takeaway is "faster early relief" rather than "better treatment, full stop."
8. What are the strengths?
It compares two clinically important modalities in the same health system instead of leaving the reader to mentally average across unrelated trials.
It treats time-to-response as the main outcome, which is the right object for acute interventional decision-making.
The weighting, sensitivity analyses, and explicit nonproportional-hazards caution make the analysis more serious than a simple retrospective mean comparison.
The separate suicidal-ideation analysis is clinically important and not just a decorative subgroup.
9. What are the weaknesses, limitations, or red flags?
This is non-randomized real-world data, so selection bias is unavoidable.
Prior rTMS exposure was much more common in the esketamine group, which tells you these populations were not naturally exchangeable.
The rTMS arm pools multiple protocols, which improves realism but weakens modality-specific interpretation.
Assessment density differed by modality, with PHQ-9 collected about weekly in rTMS and at each esketamine session, so earlier response detection may partly reflect clinic structure rather than only biology.
The paper does not provide biomarker, circuit, or cognitive features that would make treatment selection mechanistically legible.
10. What challenges or open problems remain?
The main unresolved problem is distinguishing true modality-specific speed effects from the surrounding care architecture, including visit frequency, monitoring intensity, and accelerated versus standard protocol design. It also remains unclear which patients should be routed immediately toward esketamine, rTMS, ketamine, or ECT in a prospective stratified workflow.
11. What future work naturally follows?
A randomized or at least much more tightly harmonized head-to-head comparison is the obvious next move, ideally including accelerated rTMS arms, standardized symptom-assessment cadence, and biomarkers that might explain who benefits from speed versus who simply needs persistence.
12. Why does this matter for cabbageland?
Because it helps force a cleaner language for interventional psychiatry. The useful question is not only "does this work?" but "how fast does it help, for whom, and what should happen if the early trajectory looks bad?" This paper pairs well with the archive trajectory note because together they sharpen early-pivot logic for severe or suicidal TRD.
13. What ideas are steal-worthy?
Make time-to-response, not just endpoint response, a first-class target in treatment-selection studies.
Analyze suicidal-ideation trajectory separately from total depression score when clinical urgency is part of the use case.
Use modality-comparison papers to define when a patient should pivot rather than only which average curve looks nicer.
14. Final decision
Keep. This is not causal proof and not mechanistic psychiatry, but it is a strong sequencing note because it says something clinically concrete without pretending that observational timing differences are the same thing as deep treatment superiority.
