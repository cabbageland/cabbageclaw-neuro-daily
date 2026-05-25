Early Feasibility Study of Sensing-enabled Ventral Capsule Deep Brain Stimulation in 10 Participants with Intractable Obsessive-Compulsive Disorder
Basic info
Title: Early Feasibility Study of Sensing-enabled Ventral Capsule Deep Brain Stimulation in 10 Participants with Intractable Obsessive-Compulsive Disorder
Authors: Sameer A. Sheth, Nicole R. Provenza, Sarah Soubra, Thomas Hamre, Ben Shofty, Garrett P. Banks, Nisha Giridharan, Faiza Momin, Greg Vogt, Sarah McKay, Michelle Avendano Ortega, Luke Jumper, Andrew D. Wiese, Eric A. Storch, Wayne K. Goodman
Year: 2026
Venue / source: medRxiv
Link:
Date surfaced: 2026-05-25
Why selected in one sentence: It is a rare OCD DBS paper that treats sensing, programming, ERP sequencing, and blinded discontinuation as one translational problem instead of four disconnected anecdotes.
Quick verdict
Highly relevant
This is not definitive evidence for biomarker-guided OCD DBS. It is a ten-person early feasibility study with heavy open-label exposure and all the usual small-cohort fragility. But it is still one of the more useful translational OCD DBS papers in the recent pile because it combines sensing-capable hardware, a structured programming phase, ERP augmentation, and a blinded discontinuation challenge. That stack is much more informative than another pure symptom-improvement case series.
One-paragraph overview
The study implanted ten patients with severe treatment-resistant OCD with bilateral ventral-capsule DBS leads connected to bidirectional devices, and the second half of the cohort also received orbitofrontal cortical strip electrodes for recording only. The trial was staged: initial open-label programming, then a structured ERP course, then a double-blind discontinuation phase, followed by open-label continuation. Mean OCD severity fell substantially over the study and all participants chose to resume stimulation after discontinuation, which supports a real stimulation contribution rather than pure placebo drift. The preserve-worthy part is not the raw response rate alone. It is that the paper tries to make OCD DBS legible as a sensing and state-tracking problem while also acknowledging that psychotherapy timing matters.
Model definition
Inputs
Local field potentials and sensing data from ventral-capsule DBS leads, orbitofrontal recordings in the latter half of the cohort, longitudinal symptom scales including Y-BOCS and mood measures, and stimulation-parameter history across programming visits.
Outputs
Clinical state estimates, candidate neural biomarkers for therapeutic efficacy or adverse behavioral states, and clinician-guiding information for stimulation programming. The paper does not present a finalized closed-loop controller.
Training objective (loss)
The accessible full text does not describe a central learnable predictive model with an explicit optimization loss. This is primarily a clinical feasibility and biomarker-discovery study rather than a train-and-evaluate machine-learning paper.
Architecture / parameterization
A sensing-enabled DBS platform with bilateral ventral-capsule stimulation, optional orbitofrontal recording strips, longitudinal symptom tracking, and exploratory biomarker discovery layered onto a staged clinical trial.
Key questions this summary must address
1. What problem is the paper trying to solve?
OCD DBS programming is usually a slow trial-and-error process because useful acute feedback during clinic visits is weak and core OCD symptoms move on a much slower timescale than motor symptoms do in Parkinson disease. The paper is trying to build a more objective programming and target-engagement logic by adding chronic neural sensing.
2. What is the method?
Ten patients with severe refractory OCD received ventral-capsule DBS. Five later participants also received bilateral orbitofrontal recording strips. The study proceeded through open-label programming, then ERP, then a blinded discontinuation month, then open-label follow-up, while collecting symptom scales and neural recordings.
3. What is the method motivation?
The authors want an objective signal that reflects therapeutic benefit or adverse behavioral states, because programming based on vague mood or energy impressions is a bad control interface for OCD. They also want to know whether sensing-capable hardware can support future biomarker-guided or even closed-loop approaches.
4. What data does it use?
It uses a ten-patient severe-OCD cohort, longitudinal psychiatric ratings, stimulation histories, and neural recordings from implanted DBS leads, with orbitofrontal recordings added in half the sample.
5. How is it evaluated?
The paper evaluates feasibility, symptom change over time, tolerability, ability to record neural data at home and in clinic, and whether blinded discontinuation provokes relapse or worsening that supports a real stimulation effect.
6. What are the main results?
Mean Y-BOCS reduction was reported as about sixty percent at study end, with eight of ten participants meeting responder criteria. Depression severity also improved. All patients resumed stimulation after the discontinuation phase, which is an important anti-handwaving result. The paper also reports the practical feasibility of collecting neural recordings in clinic and at home, though it does not yet validate a robust therapeutic biomarker.
7. What is actually novel?
The novelty is not just that the device senses. It is the integration of sensing-enabled hardware with a staged translational design that includes formal programming, psychotherapy augmentation, and sham-disambiguating discontinuation.
8. What are the strengths?
First, it uses bidirectional hardware in a disorder where objective programming signals are badly needed. Second, it does not stop at open-label symptom change but includes a double-blind discontinuation phase. Third, it tests ERP as a sequenced augmentation layer rather than treating psychotherapy as background noise.
9. What are the weaknesses, limitations, or red flags?
The biggest problem is scale. Ten participants cannot validate biomarkers or give stable subgroup conclusions. The response numbers are encouraging but still exposed to cohort selection, site expertise, and open-label expectation effects. The ERP layer is clinically sensible but makes causal disentangling harder. And any biomarker claims should be treated as exploratory until replicated.
10. What challenges or open problems remain?
The hard part is moving from “we can record signals” to “we can use signals to improve programming or control.” It remains unclear which neural features are stable, specific, and actionable enough to guide therapy in OCD, and whether they generalize across targets or symptom dimensions.
11. What future work naturally follows?
Replicate in a larger cohort, define pre-registered biomarker candidates, relate sensing features to symptom dimensions and adverse states, and test whether biomarker-informed programming actually beats expert manual programming.
12. Why does this matter for cabbageland?
Because it reframes psychiatric DBS as a state-estimation and feedback problem rather than a static lesion-replacement fantasy. It also supports the idea that psychotherapy sequencing should be part of neuromodulation design, not an afterthought.
13. What ideas are steal-worthy?
Treat OCD DBS programming as an interface problem with missing feedback. Use blinded discontinuation whenever possible to separate real benefit from slow expectation drift. And think about sensing plus psychotherapy as a designed stack rather than separate silos.
14. Final decision
Keep. This is not closed-loop victory, but it is one of the sharper current translational scaffolds for where OCD DBS should go.
