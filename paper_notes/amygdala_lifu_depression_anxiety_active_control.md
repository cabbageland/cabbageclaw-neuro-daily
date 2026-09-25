# Low-Intensity Focused Ultrasound of the Amygdala in Depression and Anxiety: A First-in-Human Active-Controlled Trial

## Basic info

* Title: Low-Intensity Focused Ultrasound of the Amygdala in Depression and Anxiety: A First-in-Human Active-Controlled Trial
* Authors: Amanda R. Arulpragasam, Mascha van 't Wout-Frank, Yosef A. Berlow, Emily Aiken, Alison Gorbatov, Ryan Van Patten, Julia G. Gillotti, Hannah R. Swearingen, Christiana R. Faucher, Hannah Adams, Nicole C. R. McLaughlin, Israel Liberzon, Jennifer Barredo, Stephen Correia, Benjamin Greenberg, Noah S. Philip
* Year: 2026
* Venue / source: medRxiv preprint / PMC Preprint Pilot
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13596687/
* Date surfaced: 2026-09-25
* Why selected in one sentence: It is a rare patient study that tests whether low-intensity focused ultrasound can engage the amygdala with anatomical specificity against an active-control target, while keeping efficacy claims properly restrained.

## Quick verdict

* Highly relevant

Keep this as a target-engagement paper, not as an antidepressant efficacy paper. The study is small, single-blind, crossover, and explicitly not powered to prove clinical benefit. Its value is that right-amygdala sonication produced convergent ASL, BOLD, and connectivity signals relative to S1 control, while also showing why "more target engagement" is not automatically better: one participant worsened clinically after a very large perfusion shift.

## One-paragraph overview

The paper tests MRI-guided low-intensity focused ultrasound targeting the right amygdala in 10 veterans with major depressive disorder, using left primary somatosensory cortex as an active control in a randomized single-blind crossover design. The intervention used two 10-minute sonication blocks per session and evaluated safety, ASL perfusion, BOLD activity during sonication, resting-state connectivity, symptom scales, spontaneous reports, and post hoc acoustic modeling. Nine participants completed both sessions. The strongest finding is target engagement: amygdala FUS changed perfusion more in the target than in S1 or adjacent hippocampal head, recruited vmPFC/rACC/insula during sonication, and decreased basolateral-amygdala connectivity with sensorimotor regions. Symptoms improved over time but did not separate by condition, so the correct conclusion is precision deep-target feasibility with safety and dose-response questions still open.

## Model definition

This is not a trainable predictive model paper. The relevant model is an interventional crossover target-engagement design with neuroimaging and safety endpoints.

### Inputs
Participant diagnosis and baseline symptoms, sonication target condition, FUS parameters, MRI-guided target placement, CT-informed post hoc acoustic modeling, ASL perfusion, task/block BOLD during sonication, resting-state fMRI, adverse-event ratings, neuropsychological testing, neurological/MRI safety checks, and depression/anxiety/PTSD symptom scales.

### Outputs
Safety and tolerability outcomes, target-region perfusion changes, FUS-on versus FUS-off BOLD responses, right basolateral amygdala connectivity changes, symptom trajectories, spontaneous subjective reports, acoustic targeting estimates, and imaging-symptom correlations.

### Training objective (loss)
There is no machine-learning loss. Statistical tests estimate whether amygdala sonication produces target-specific physiological changes relative to active S1 control, and exploratory models/correlations test symptom change and imaging-symptom associations.

### Architecture / parameterization
A randomized single-blind crossover clinical target-engagement study. Each participant received right-amygdala FUS and left-S1 control FUS at least one week apart. FUS used a 650 kHz Brainsonix transducer, 10 Hz pulse repetition frequency, 5 ms pulse width, two applications of ten 30-second sonications with 30-second off periods, and reported derated intensities within diagnostic ultrasound safety limits.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

It asks whether a noninvasive tool can directly and selectively engage a deep affective target in psychiatric patients. That is the prerequisite question for focused ultrasound psychiatry. If the field cannot show safe, anatomically specific engagement of structures like the amygdala, later symptom trials become expensive mood-theater.

### 2. What is the method?

Ten veterans with MDD entered a randomized crossover study. Each participant received one right-amygdala FUS session and one active-control S1 session, with blinded MADRS ratings and safety assessments around each session. The authors measured ASL perfusion immediately after sonication, BOLD activity during sonication blocks, resting-state connectivity before and after FUS, clinical scales through one week, and post hoc acoustic-model estimates from CT.

### 3. What is the method motivation?

The amygdala is a deep affective-circuit node implicated in depression, anxiety, trauma, salience, autonomic regulation, and emotional learning. Ordinary noninvasive stimulation mainly reaches cortex and infers downstream effects. Low-intensity FUS could in principle perturb deep targets directly, but the translational standard should be target engagement before efficacy.

### 4. What data does it use?

The analyzed sample was 10 participants, age 33 to 69, mostly male veterans, with MDD and frequent comorbid PTSD or generalized anxiety disorder. Nine completed both sonication sessions. Data included clinical MRI safety scans, neurological exams, neuropsychological batteries, SAFTEE adverse-event ratings, MADRS, IDS-SR, GAD-7, PCL-5, CGI scores, ASL, BOLD fMRI, resting-state fMRI, and CT-based acoustic modeling.

### 5. How is it evaluated?

Primary evaluation is safety plus biological target engagement. The target-engagement tests compare amygdala sonication against S1 control and adjacent hippocampal head using perfusion, BOLD activation, and resting-state connectivity. Clinical outcomes are exploratory and analyzed as time effects, order effects, and imaging-symptom correlations, not as a definitive efficacy test.

### 6. What are the main results?

No serious adverse events, MRI-detectable injury, neurological worsening, sustained cognitive decline, or suicidality worsening were observed, but adverse events were more frequent after amygdala than S1 sonication, 2.50 versus 1.11 events per exposure, p = 0.028. Amygdala FUS produced greater perfusion change in the targeted right amygdala than in S1 control, t(9) = 5.15, p < 0.001, and than in adjacent hippocampal head, t(9) = 4.70, p < 0.001. Group ASL showed bilateral amygdala and right rACC perfusion increases. During amygdala FUS, BOLD increased in vmPFC, right rACC, and left insula. Post-sonication resting-state connectivity decreased between right BLA and sensorimotor regions. Symptoms improved over time, but improvement did not clearly separate by sonication condition. Seven of 10 participants spontaneously reported calm, clarity, or lightness after amygdala FUS, while none did after S1 FUS. One participant had protocol-defined depression worsening after amygdala FUS with a 441 percent target-region perfusion increase; both perfusion and symptoms returned near baseline by one month.

### 7. What is actually novel?

The useful novelty is the active-control patient demonstration of anatomically specific amygdala engagement across multiple imaging modalities. The paper is also valuable because it refuses the lazy jump from target engagement to efficacy and instead flags a possible nonlinear response window where excessive physiological perturbation may be bad.

### 8. What are the strengths?

The active-control crossover design is much better than a pure open-label feasibility readout. The paper uses multimodal target-engagement evidence rather than a single convenient biomarker. Safety monitoring is unusually explicit: MRI, neurological exam, neuropsychological testing, suicidality checks, and structured adverse-event capture. It also reports the uncomfortable worsening case instead of burying it.

### 9. What are the weaknesses, limitations, or red flags?

The sample is tiny and demographically narrow. There is no full sham condition, only an anatomical active control. The crossover design may be vulnerable to carryover if FUS effects persist. Imaging was measured at limited timepoints, so durability and temporal dynamics remain thin. Current methods cannot directly measure the intracranial beam location, and post hoc acoustic modeling is not proof of where energy landed. No multiple-comparison correction was applied across some exploratory clinical/imaging associations. Most importantly, symptom improvement over time should not be mistaken for condition-specific efficacy.

### 10. What challenges or open problems remain?

The field still needs dose-ranging, parallel-group sham-controlled trials, better individual acoustic-field verification, repeated-dose safety data, physiological measures of amygdala output such as pupil or heart-rate responses, and clearer mapping from acute target engagement to later symptom change.

### 11. What future work naturally follows?

A strong next study would compare amygdala FUS, anatomical active control, and sham in a larger parallel-group design; prespecify dose levels; model skull/anatomy-driven delivery differences prospectively; measure autonomic and task-based amygdala outputs; and separate target engagement, acute state change, and durable clinical response as different endpoints.

### 12. Why does this matter for cabbageland?

It sharpens the standard for deep noninvasive psychiatric neuromodulation. The interesting claim is not "ultrasound treats depression." The interesting claim is "we can perturb a deep affective target in patients, see local and circuit-level consequences, and start learning the response window." That is a better design primitive for future intervention logic.

### 13. What ideas are steal-worthy?

Treat precision as a gate before efficacy. Use active anatomical controls when full sham is not enough to disambiguate target-specific effects. Keep target engagement, subjective state change, symptom movement, and safety as separate proof surfaces. Interpret overshooting the target response as a potential harm signal, not as stronger mechanism.

### 14. Final decision

Keep. This is a strong translational target-engagement preserve for focused ultrasound psychiatry, with the caveat written in red ink: it supports anatomical specificity and feasibility, not clinical efficacy.
