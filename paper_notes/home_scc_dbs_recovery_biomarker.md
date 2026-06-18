# Common Electrophysiology Biomarkers Collected at Home Robustly Track Depression Recovery With Deep Brain Stimulation

## Basic info

* Title: Common Electrophysiology Biomarkers Collected at Home Robustly Track Depression Recovery With Deep Brain Stimulation
* Authors: Elif Ceren Fitoz, Sankaraleengam Alagapan, Jungho Cha, Ki Sueng Choi, Martijn Figee, Brian Kopell, Mosadoluwa Obatusin, Stephen Heisig, Tanya Nauvel, Aida Razavilar, Parisa Sarikhani, Isha Trivedi, Jamie Gowatsky, Jessa Alexander, Romain Guignon, Maryam Khalid, Gutemberg Bobby Forestal, Ha Neul Song, Tim Denison, Shannon O'Neill, Shreesh Karjagi, Allison C. Waters, Patricio Riva-Posse, Helen S. Mayberg, Christopher J. Rozell
* Year: 2026
* Venue / source: medRxiv preprint
* Link: https://www.medrxiv.org/content/10.64898/2026.04.13.26350107v1
* Date surfaced: 2026-06-18
* Why selected in one sentence: It is one of the clearest recent attempts to turn chronic psychiatric DBS from mood-scale guesswork into a sensor-guided recovery-tracking problem.

## Quick verdict

* Highly relevant

This is a strong preserve because it attacks a real clinical bottleneck rather than celebrating implantation theater. The useful claim is not just that SCC local field potentials correlate with outcome, but that a previously trained biomarker generalizes across a new cohort, a new device stack, and messy at-home recordings while separating core depression recovery from anxiety-heavy noise better than standard rating-scale drift. The caution is equally important: this is still a small preprint, three of ten implanted participants were dropped from electrophysiology analyses because of unexplained device shifts, and the "ground truth" remains anchored to clinician-rated recovery thresholds.

## One-paragraph overview

The paper extends earlier subcallosal cingulate deep brain stimulation work in treatment-resistant depression by moving biomarker collection out of rare in-clinic downloads and into a high-compliance home-monitoring workflow. Ten participants implanted with the Medtronic Summit RC+S system completed twice-daily sessions that captured SCC local field potentials, symptom ratings, and video diaries, and the authors then applied a previously trained Generative Causal Explainer model to derive a spectral discriminative component, or SDC, indexing recovery state without retraining the model on the new cohort. The main result is that this biomarker still tracks the transition from depressed to stable recovery reasonably well, stays comparatively stable during anxiety-heavy symptom noise, worsens when stimulation is interrupted early, and relates to pre-DBS white-matter and resting-state network features that plausibly constrain response speed. The paper matters because it makes psychiatric DBS look less like artisanal programming and more like a slow-timescale state-estimation problem.

## Model definition

The paper contains a substantive biomarker model rather than only descriptive statistics.

### Inputs
Ten-second SCC local field potential segments from bilateral chronic DBS recordings, converted into a 20-dimensional feature set including spectral power, coherence across canonical bands, and delta-to-high-beta/gamma phase-amplitude coupling. For correlational follow-up analyses, the study also uses pre-DBS diffusion MRI and resting-state functional MRI, but those are not primary biomarker-model inputs.

### Outputs
A weekly spectral discriminative component value transformed into the probability of being in a "sick" versus stable-recovery state, plus simpler surrogate band-power markers intended to approximate the biomarker on more deployment-friendly hardware.

### Training objective (loss)
The accessible preprint makes clear that the SDC is produced by projecting the new cohort's features through the feature-compression network of a previously trained Generative Causal Explainer model. The exact optimization objective is defined in the prior model paper rather than restated cleanly here, so the safest summary is that the model was trained to extract latent electrophysiological structure that discriminates depressed versus stable-recovery states.

### Architecture / parameterization
A previously trained low-dimensional latent biomarker model built with a Generative Causal Explainer framework, applied without retraining to new longitudinal SCC DBS recordings; the paper also derives simpler left- and right-hemisphere 5-Hz-band surrogates to mimic the biomarker.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
SCC DBS can help treatment-resistant depression, but ongoing programming decisions are still guided by symptom scales that mix core recovery with anxiety, sleep problems, and ordinary life turbulence. The paper tries to identify a practical electrophysiological marker that tracks DBS-responsive recovery state more selectively and could support better stimulation-adjustment decisions.

### 2. What is the method?
The authors built an at-home monitoring platform on the Summit RC+S research device so participants could collect twice-daily SCC LFP recordings alongside mood measures. They extracted spectral and coupling features from these recordings, fed them through a previously trained GCE biomarker model from an earlier PC+S cohort, compared the resulting SDC trajectories against Hamilton Depression Rating Scale recovery transitions, and then examined robustness, symptom specificity, discontinuation sensitivity, and imaging correlates.

### 3. What is the method motivation?
If psychiatric DBS is going to scale beyond a few expert centers, clinicians need something sturdier than subjective weekly impressions. The authors are explicitly trying to build a decision-support layer that reflects DBS-sensitive core depression recovery rather than every temporary fluctuation in distress.

### 4. What data does it use?
Ten treatment-resistant depression participants implanted with SCC DBS using the Summit RC+S platform, with twice-daily home recordings across a 24-week observation window and weekly HDRS assessments. Electrophysiology analyses ultimately use seven participants after excluding three because of abrupt device-related recording changes. The transfer model itself was trained previously on a separate five-participant PC+S cohort.

### 5. How is it evaluated?
The primary evaluation compares weekly SDC-derived sick-versus-well states against HDRS-derived stable-response states in the new cohort without retraining. Additional evaluations test whether the biomarker stays informative with stimulation-on recordings, evening recordings, brief stimulation discontinuations, anxiety-heavy symptom periods, and simple surrogate band-power measures, and whether pre-DBS white-matter integrity and SCC resting-state connectivity relate to time-to-response.

### 6. What are the main results?
The transferred SDC predicted HDRS-defined recovery-state transitions in the RC+S cohort with an accuracy of 0.72 +/- 0.16, which the authors argue is comparable to the earlier PC+S cohort despite different hardware and a different clinical team. Mean adherence to the home workflow was about 94 percent. At the cohort level, mean HDRS fell from 23.93 before surgery to 10 by six months, with seven of ten participants meeting response by the prespecified endpoint and one additional participant crossing response one week later. The biomarker also looked more specific than HDRS to DBS-sensitive core recovery in cases where anxiety remained elevated, worsened after an early unintended discontinuation but stayed stable during later brief planned discontinuations, and showed plausible structure-function correlates: lower fractional anisotropy in left cingulum bundle, right uncinate/ventral amygdalofugal pathway, and left forceps minor, as well as weaker SCC connectivity to dACC, anterior insula, and vmPFC, were associated with slower response.

### 7. What is actually novel?
The novelty is not just another biomarker claim. The paper shows cross-cohort and cross-device transfer of a psychiatric DBS recovery marker, demonstrates that it can be gathered at home with high compliance, and argues that it is clinically useful precisely because it is not a generic distress meter. That combination is more interesting than yet another offline decoder benchmark.

### 8. What are the strengths?
- It tests a previously trained biomarker on genuinely new hardware and a new cohort instead of quietly retraining until things look good.
- The at-home collection design is much closer to realistic clinical deployment than sparse research-visit downloads.
- The paper treats symptom specificity as a first-class requirement rather than assuming every score fluctuation should trigger DBS changes.
- Discontinuation case studies give the biomarker a more intervention-relevant stress test than plain correlation tables.
- The imaging analyses connect electrophysiology back to tract and network constraints instead of leaving the marker as a floating black box.

### 9. What are the weaknesses, limitations, or red flags?
- It is still a preprint and the analyzed electrophysiology sample is tiny.
- Three of ten implanted participants were excluded for unexplained device-related recording shifts, which matters if the whole pitch is robustness.
- The stable-response benchmark still depends on HDRS thresholds, so the biomarker is not fully independent of the noisy clinical instrument it is meant to improve on.
- Most of the evidence is observational and retrospective rather than a true prospective biomarker-guided programming trial.
- The work is all from a narrow SCC DBS ecosystem, so cross-center and cross-target generalization remains open.

### 10. What challenges or open problems remain?
The big unresolved question is whether using the biomarker prospectively actually improves decisions, outcomes, or clinician efficiency. It also remains unclear how stable the signal will be on more commercial hardware, across more sites, across longer follow-up, or when medication and psychotherapy changes are less controlled.

### 11. What future work naturally follows?
Run a prospective trial where stimulation adjustments are explicitly biomarker-guided, validate the surrogate band-power markers on commercial devices, expand to multi-site cohorts, and develop complementary markers for anxiety or other DBS-insensitive symptoms so clinicians can tell what kind of intervention is actually indicated.

### 12. Why does this matter for cabbageland?
Because it sharpens the right psychiatric-neuromodulation question: not "does DBS work on average," but "can we infer the patient's slow recovery state well enough to steer treatment intelligently?" That is exactly the missing middle layer between electrode placement and therapeutic storytelling.

### 13. What ideas are steal-worthy?
- Treat chronic psychiatric DBS as a slow-timescale state-estimation problem rather than only a stimulation-delivery problem.
- Separate DBS-sensitive core recovery from nuisance symptom fluctuations instead of collapsing everything into one clinical score.
- Use home longitudinal sensing to collect the kind of dense trajectories that make practical biomarkers possible.
- Translate complex latent biomarkers into simpler hardware-friendly surrogate bands once the real signal is established.

### 14. Final decision
Keep as a core reference for SCC DBS recovery-state tracking and clinician decision-support logic. It is still a small preprint and should not be treated as deployment-ready truth, but it is much closer to useful psychiatric closed-loop infrastructure than most papers in this lane.
