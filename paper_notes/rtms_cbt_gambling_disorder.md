# A randomized double-blind sham-controlled preliminary study of a 5-week protocol of repetitive transcranial magnetic stimulation (rTMS) combined with cognitive behavioral therapy (CBT) for gambling disorder in Indonesia

## Basic info

* Title: A randomized double-blind sham-controlled preliminary study of a 5-week protocol of repetitive transcranial magnetic stimulation (rTMS) combined with cognitive behavioral therapy (CBT) for gambling disorder in Indonesia
* Authors: Kristiana Siste, Lee Thung Sen, Belinda Julivia Murtani, Enjeline Hanafi, Kevin Surya Kusuma, Astria Aryani, Christopher Tan, Fitri Dona Nainggolan, Nur Aida, Yunyun Setiawan
* Year: 2026
* Venue / source: Addictive Behaviors Reports
* Link: https://doi.org/10.1016/j.abrep.2026.100722
* Date surfaced: 2026-09-24
* Why selected in one sentence: It is a rare randomized full-text test of CBT plus active versus sham rTMS for gambling disorder, and its negative primary result is at least as useful as its faster craving/cognition signal.

## Quick verdict

* Useful

Keep this as a cautious combination-treatment note, not as evidence that active rTMS clearly improves gambling disorder symptoms. Both groups received CBT, both groups improved substantially on gambling severity, and active rTMS did not beat sham rTMS on the primary G-SAS symptom trajectory. The useful residue is narrower: active left-DLPFC rTMS may have accelerated reductions in tonic gambling urge and two gambling-cognition domains, but the study is small, baseline-imbalanced on those secondary domains, and vulnerable to overfitting.

## One-paragraph overview

The paper tests whether 15 sessions of 10 Hz left-DLPFC rTMS over five weeks add anything to a 12-session CBT program for gambling disorder. Twenty-seven Indonesian adults with ICD-11 gambling disorder were randomized to active rTMS plus CBT or sham rTMS plus CBT, with outcomes measured through treatment, post-treatment, and six-month follow-up. The main gambling severity measure improved over time in both arms, but active rTMS did not significantly separate from sham. Active rTMS did show steeper reductions in gambling urge, gambling expectancies, and perceived inability to stop gambling. That makes the paper useful for designing hybrid interventions, but the correct read is "possible process acceleration" rather than "active stimulation works."

## Model definition

This is not a trainable predictive model paper. The relevant analytic model is a repeated-measures clinical trial analysis of active stimulation plus CBT versus sham stimulation plus CBT.

### Inputs
Treatment arm, time point, baseline gambling severity and cognition measures, gambling symptom scores, craving scores, gambling-related cognition subscales, mental-health scales, neurocognitive battery scores, and adverse-event records.

### Outputs
Primary and secondary clinical outcomes including G-SAS gambling severity, G-SAS response status, Gambling Urge Scale score, Gambling Related Cognitions Scale subdomains, SRQ-20, PHQ-9, CGI-S, neurocognitive changes, follow-up retention, and adverse events.

### Training objective (loss)
There is no machine-learning loss. The paper uses generalized linear mixed models and related repeated-measures analyses to estimate time, group, and group-by-time effects. The crucial inferential target is whether active rTMS plus CBT changes symptom trajectories more than sham rTMS plus CBT.

### Architecture / parameterization
A preliminary double-blind, sham-controlled, parallel-arm randomized trial. Active rTMS targeted left DLPFC with Beam F3 localization, 10 Hz stimulation, 120 percent resting motor threshold, 4-second trains, 11-second intertrain intervals, 75 trains, 3000 pulses per session, 15 sessions total. Both arms received the same 12-session CBT program for gambling disorder.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

It asks whether noninvasive brain stimulation can usefully augment CBT for gambling disorder rather than being tested as a free-floating device intervention. That is the right question because gambling disorder is maintained by craving, cue reactivity, distorted expectancies, and weak self-control beliefs, all of which CBT tries to modify behaviorally.

### 2. What is the method?

The authors ran a preliminary randomized double-blind sham-controlled trial at a Jakarta hospital. Participants with ICD-11 gambling disorder were assigned to active rTMS plus CBT or sham rTMS plus CBT. Active stimulation targeted left DLPFC for 15 sessions over five weeks. CBT was delivered in 12 individualized sessions covering psychoeducation, harms, motivation, stages of change, triggers, gambling cycle, craving and extinction strategies, alternative routines, financial management, interpersonal repair, emotional regulation, and relapse prevention.

### 3. What is the method motivation?

The rationale is that DLPFC-centered executive-control networks are involved in cue reactivity, craving regulation, response inhibition, and gambling-related decision-making. CBT supplies the explicit behavioral and cognitive training, while rTMS is supposed to make the prefrontal control system more able to downshift craving and maladaptive gambling beliefs.

### 4. What data does it use?

The randomized sample includes 27 participants, 13 active and 14 sham. All participants gambled online. Outcomes include G-SAS, GUS, GRCS subscales, SRQ-20, PHQ-9, CGI-S, and a neurocognitive battery. Assessments occurred at baseline, mid-treatment after the seventh rTMS session, post-treatment after the fifteenth rTMS session and final CBT session, three-month follow-up, and six-month follow-up.

### 5. How is it evaluated?

The primary evaluation is change in gambling severity on G-SAS and categorical G-SAS response. Secondary analyses test gambling urge, gambling-related cognitions, mental-health symptoms, clinician severity, neurocognitive outcomes, and adverse events. Mixed models test time, group, and group-by-time effects, with baseline imbalances in GUS, GRCS-GE, and GRCS-ISG handled as covariates and checked with sensitivity analyses.

### 6. What are the main results?

Both active and sham groups improved over time on G-SAS, but group and group-by-time effects were not significant for gambling severity. At post-treatment, 11 of 13 active participants and 11 of 14 sham participants met G-SAS response criteria; at six months, available follow-up participants in both arms maintained response. Active rTMS showed steeper reductions in gambling urge, with group-by-time slope difference B = 2.63, 95 percent CI 0.55 to 4.70, p = 0.015. It also showed steeper reductions in gambling expectancies, B = 1.84, p <= 0.001, and perceived inability to stop gambling, B = 1.70, p = 0.014. Adverse events were mild and self-limiting, mainly headache and tingling, with no discontinuations.

### 7. What is actually novel?

The novelty is not left-DLPFC rTMS by itself. The useful novelty is testing active versus sham rTMS as an adjunct to a standardized CBT program in gambling disorder and repeatedly measuring tonic craving and gambling-cognition trajectories instead of only pre/post symptom severity.

### 8. What are the strengths?

The study uses a sham-controlled randomized design, gives both arms the same CBT program, includes follow-up to six months, specifies stimulation parameters clearly, and measures process-relevant outcomes rather than only global symptom severity. It also reports the negative primary result plainly, which makes the secondary signals easier to interpret without pretending they are the main event.

### 9. What are the weaknesses, limitations, or red flags?

The sample is tiny. Baseline urge and key cognition scores were already worse in the active group, which complicates the interpretation of steeper change. The active and sham coils did not perfectly match scalp sensation. Outcomes rely heavily on self-report, and the study did not measure cue-induced craving or gambling episodes directly. The mixed models risk overfitting relative to the sample size and covariate count. Most importantly, the primary gambling severity outcome did not show active superiority.

### 10. What challenges or open problems remain?

The field still needs to know whether stimulation changes a therapy-relevant mechanism or merely changes short-term subjective urge. It also needs better dosing studies, better sham matching, cue-reactivity readouts, gambling behavior counts, longer relapse follow-up, and subgroup analyses that are planned rather than rescued from small samples.

### 11. What future work naturally follows?

A stronger next trial would use a larger preregistered sample, active sensory control, weekly craving and cue-reactivity probes, objective gambling-behavior or financial-harm outcomes, and mechanistic markers of DLPFC-salience or frontostriatal change. It should also test whether stimulation timing relative to CBT sessions matters, rather than treating "same treatment window" as enough.

### 12. Why does this matter for cabbageland?

It is a clean warning label for interventional psychiatry combinations. The combination may move process variables faster, but the headline symptom outcome still failed to separate. That distinction is exactly what future CBT-plus-stimulation, CBT-plus-ketamine, and CBT-plus-psychedelic designs need to preserve instead of collapsing everything into a vague synergy story.

### 13. What ideas are steal-worthy?

Measure the process variable that the psychotherapy actually tries to train. Repeated tonic-craving measurement is better than a single before/after craving score. Separate gambling severity from gambling expectancies and perceived inability to stop. Treat faster cognitive change as a hypothesis for mechanism, not as a substitute for clinical efficacy.

### 14. Final decision

Keep. The paper is not a strong positive efficacy trial, but it is a useful full-text data point for hybrid psychotherapy-plus-neuromodulation design because it shows how an adjunct can look promising on process measures while failing the main symptom contrast.
