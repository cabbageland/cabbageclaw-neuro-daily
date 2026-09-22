# Neural correlates of response inhibition following cognitive behavioral therapy in obsessive-compulsive disorder: a randomized controlled EEG study

## Basic info

* Title: Neural correlates of response inhibition following cognitive behavioral therapy in obsessive-compulsive disorder: a randomized controlled EEG study
* Authors: Metin Cinaroglu, Selami Varol Ulker, Eda Yilmazer, Gokben Hizli Sayar
* Year: 2026
* Venue / source: BMC Psychology
* Link: https://doi.org/10.1186/s40359-026-05201-1
* Date surfaced: 2026-09-22
* Why selected in one sentence: It is a full-text randomized CBT-for-OCD study that pairs symptom change with a Go/No-Go EEG readout of response inhibition.

## Quick verdict

* Useful

Useful, but keep the mechanistic claim disciplined. The trial shows that 12 weeks of CBT with exposure and response prevention improved OCD symptoms, reduced obsessive beliefs and intolerance of uncertainty, reduced No-Go commission errors, and increased frontocentral No-Go P3 amplitude versus waitlist. The design does not prove that P3 change mediates therapeutic improvement, and the low-density EEG plus waitlist control limit mechanistic precision.

## One-paragraph overview

Sixty adults with DSM-5 OCD were randomized to 12 weekly online CBT sessions or waitlist. Fifty-three completed pre/post clinical assessment and EEG. The CBT group improved substantially on Y-BOCS, obsessive beliefs, intolerance of uncertainty, No-Go commission errors, and No-Go P3 amplitude, while the waitlist group changed little. The useful lesson is not that CBT has finally found "the" neural mechanism; it is that ERP-based CBT can be paired with a concrete process readout, response inhibition, and an electrophysiological marker that might eventually support treatment stratification or mechanism tests.

## Model definition

### Inputs

Inputs are treatment allocation, pre/post clinical measures, obsessive-belief and intolerance-of-uncertainty scales, Go/No-Go behavioral performance, SSRI status for sensitivity checks, and 14-channel EEG during a Go/No-Go task.

### Outputs

Outputs are Y-BOCS symptom change, treatment response and remission rates, changes in obsessive beliefs and intolerance of uncertainty, Go-trial reaction time, No-Go commission errors, frontocentral No-Go P3 amplitude, and No-Go N2 amplitude.

### Training objective (loss)

There is no trainable model and no loss function. Treatment effects are evaluated with mixed-design repeated-measures ANOVA, using Group by Time interactions as the key tests. Sensitivity analyses include SSRI status as a covariate.

### Architecture / parameterization

This is a randomized parallel-group psychotherapy trial with a waitlist control. The electrophysiology stack uses a 14-channel Emotiv EPOC EEG system, a 240-trial visual Go/No-Go task, artifact rejection with a minimum of 20 clean No-Go trials, No-Go P3 mean amplitude from 300-600 ms, and No-Go N2 mean amplitude from 200-350 ms at frontocentral electrodes.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

It asks whether CBT for OCD changes not only symptoms and beliefs but also objective behavioral and electrophysiological indices of response inhibition. This matters because OCD treatment mechanisms often stay trapped between clinical symptom scores and vague claims about cognitive control.

### 2. What is the method?

Adults with OCD were randomized 1:1 to 12 sessions of manualized CBT with exposure and response prevention or a waitlist control. Participants completed clinical scales and a Go/No-Go EEG task before and after the 12-week period. The primary clinical outcome was Y-BOCS, and the primary neurophysiological outcome was frontocentral No-Go P3 amplitude.

### 3. What is the method motivation?

Exposure and response prevention asks patients to experience obsessional distress while withholding compulsive responses. That makes response inhibition a plausible process variable. No-Go P3 is used as a scalp EEG marker associated with inhibitory control and cognitive-control allocation during response suppression.

### 4. What data does it use?

The randomized sample includes 60 adults with at least moderate OCD. The final complete-case analytic sample includes 53 participants: 27 CBT and 26 waitlist. Roughly half were on stable SSRIs. The EEG task used 180 Go trials and 60 No-Go trials, with pre/post recordings.

### 5. How is it evaluated?

The authors test Group by Time interactions for clinical scales, Go/No-Go behavior, and ERP amplitudes. They also report response and remission rates, and they run sensitivity analyses adjusting for SSRI status. EEG preprocessing and analysis were blinded to group and time point, but clinical assessment was not blinded.

### 6. What are the main results?

Y-BOCS drops from 24.8 to 14.6 in the CBT group and from 25.0 to 23.9 in the waitlist group, with Group by Time F(1,51) = 24.8, p < .001, partial eta squared = .33. Response occurs in 21 of 27 CBT participants versus 2 of 26 waitlist participants; remission occurs in 10 of 27 versus 1 of 26. OBQ-20 and IUS-12 also improve more in CBT. No-Go commission errors fall from 27.6% to 19.8% in CBT and from 28.9% to 27.4% in waitlist, p = .007. No-Go P3 increases from 5.1 to 6.8 microvolts in CBT and from 5.0 to 5.2 in waitlist, with F(1,51) = 10.9, p = .002, partial eta squared = .18. No-Go N2 does not show a reliable Group by Time effect.

### 7. What is actually novel?

The novelty is pairing ERP-focused CBT with a response-inhibition EEG marker in a randomized OCD design. CBT efficacy is not new. The useful addition is measuring whether a task-based electrophysiological index moves alongside symptom, belief, uncertainty, and inhibition-performance changes.

### 8. What are the strengths?

It is randomized and prospectively registered.

It measures clinical symptoms, cognitive treatment targets, behavior, and EEG rather than only Y-BOCS.

The ERP analysis focuses on a prespecified No-Go P3 outcome.

EEG preprocessing and analysis were blinded to allocation and time point.

The CBT protocol is recognizable ERP-based treatment rather than a vague psychotherapy label.

### 9. What are the weaknesses, limitations, or red flags?

The control is waitlist, not an active psychological control, so expectancy, therapist contact, and repeated task exposure are not fully controlled.

The clinician administering Y-BOCS was not blinded to allocation.

The EEG system has only 14 channels, limiting source localization and anatomical claims.

The sample is modest and complete-case, with no long-term follow-up.

About half the participants were on stable SSRIs, so psychotherapy-specific neural change cannot be perfectly isolated.

No mediation analysis shows that P3 change drives symptom improvement.

### 10. What challenges or open problems remain?

The main unresolved question is whether response-inhibition changes are a mechanism, a correlate, or a nonspecific marker of improved task engagement. The field also needs active controls, high-density EEG or multimodal imaging, longer follow-up, and tests of whether baseline P3 or early P3 change predicts who responds to CBT.

### 11. What future work naturally follows?

A stronger study would compare ERP-based CBT against an active control matched for therapist contact, add high-density EEG or fMRI, measure ERN and Go P3 as well as No-Go P3, and test mediation between intolerance-of-uncertainty change, commission-error change, P3 change, and Y-BOCS improvement.

### 12. Why does this matter for cabbageland?

This is a standing-interest CBT/interventional-psychiatry bridge even without stimulation. It shows how psychotherapy can be evaluated like an intervention on a measurable state/process variable. That matters for future combinations where stimulation, drugs, or psychedelics should be judged by whether they make therapy-relevant control processes more trainable.

### 13. What ideas are steal-worthy?

Use response inhibition as a process variable for OCD treatment studies.

Pair belief/uncertainty measures with task-based physiology instead of pretending self-report and neural data answer the same question.

For combination therapies, ask whether the biological intervention changes the process that therapy actually practices.

Treat low-density EEG as a scalable screening readout, but do not overinterpret it as circuit localization.

### 14. Final decision

Keep as a useful CBT mechanism note. It is not definitive mechanistic proof, but it is a solid example of making psychotherapy outcomes more measurable.
