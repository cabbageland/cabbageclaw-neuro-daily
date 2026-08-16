Welcome to the August sixteenth Neuro Daily at Cabbageland!

Today is a patient-relative localization beats global channel scoring day.

The top preserve is directly relevant, titled, EpiLENS: Patient-Relative Epileptogenic Zone Localization from Multi-Center Intracranial EEG.

It wins because it fixes the framing before it decorates the model. Instead of training one universal intracranial EEG channel classifier and pretending a score should mean the same thing across patients, seizures, implants, and centers, it asks whether a contact is abnormal relative to the patient's own implanted set.

The setup is straightforward and actually useful. The paper uses eighty postoperative seizure-free patients from four centers, with two hundred fifty-six seizures and seven thousand six hundred thirty-five implanted channels. About twenty-two point eight percent of the channels are annotated as epileptogenic. The labels are still retrospective clinician-defined surgical-target surrogates, not biological truth, and the paper is honest about that.

The modeling move has two parts. First, it builds self-referenced channel features relative to each channel's own pre-onset baseline, then standardizes them within the patient's implanted set. Second, it uses two branches with different jobs. P R Q-Net is the primary patient-relative probability model. B C R-Net is an auxiliary ranking model that focuses on ambiguous boundary channels and recovery of the full epileptogenic set. The final fusion is conservative and fixed at zero point eight times P R Q plus zero point two times B C R.

The results are not enormous, but they are real and aimed at the right target. On the main eighty-patient split, the fused model reaches Macro-F1 zero point six three seven one, E Z-F1 zero point four four eight five, and A U R O C zero point seven four six eight, with near-zero epileptogenic-fraction bias. Relative to the strongest baseline, logistic regression with patient-wise z-score normalization, it improves Macro-F1 by zero point zero three zero six and E Z-F1 by zero point zero four nine seven.

The stronger sign is that it also improves over its own primary branch. That means the auxiliary boundary-ranking logic is adding something real rather than just smoothing scores. In leave-one-center-out transfer, it posts the best center-mean Macro-F1 at zero point six one six three and the best worst-center score at zero point five seven seven three. In the matched seventy-three-patient cross-seizure analysis, Macro-F1 rises from zero point six one four six with one seizure to zero point six three nine five with all available seizures.

The useful lesson is that some localization problems should stop pretending to be universal classifiers. They are patient-relative ranking problems under ugly heterogeneity.

The second ranked anchor is titled, Trophic structure predicts seizure propagation in brain network models.

It stays important because it sharpens seizure-spread reasoning around directed hierarchy and cycle structure instead of generic connectome folklore.

The third ranked anchor is titled, Literature-Guided Minimax Optimization of Virtual Epilepsy Neurostimulation.

It stays high because it asks the right intervention-design question: protect the hardest patient rather than flattering the cohort average.

The fourth ranked anchor is titled, Thalamocortical network dynamics in focal epilepsy: S E E G investigation.

It remains useful because it links focal epilepsy vulnerability to interpretable thalamocortical dynamics rather than a purely local lesion story.

There were fresh runners-up, but they did not beat the preserve.

One was the methods paper titled, Design and Validation of a Portable E E G–t E S Platform Supporting High-Rate E E G Recording and Temporal Interference Stimulation. The engineering claim is solid enough. An M C U-centered platform handles eight-channel E E G up to eight kilohertz plus two-channel stimulation, records temporal-interference carriers, and keeps measured loop delays under one millisecond. But the evidence is still bench and gelatine-phantom only, with no human validation and no implemented adaptive controller.

Another was the clinical paper titled, Reward circuitry predicts the effects of f M R I-guided accelerated prolonged i T B S in treatment-resistant depression. The mesolimbic connectivity story is interesting, but the accessible evidence here stayed retrospective and abstract-level in a small twenty-nine-patient series.

The adolescent lane produced a full-text protocol titled, Feasibility, safety, and preliminary clinical efficacy of resting-state functional connectivity M R I-guided r T M S for adolescents with major depressive disorder. It is directionally aligned with circuit-informed adolescent intervention, but it is still a protocol rather than an efficacy result.

The standing-interest checks stayed weak. In the hypnosis and hypnotherapy lane, the recent items were mostly case-level or survey-level, including Hypnotherapy with affect bridge age regression for choking and Clinical hypnosis in anesthesia. They did not beat the archive because they are not mechanism-centered.

In the cognitive behavioral therapy plus interventional psychiatry lane, no fresh paper available on or before August sixteenth, twenty twenty-six beat the existing archive anchor Noninvasive brain stimulation combined with evidence-based psychotherapy for psychiatric disorders: A meta-analysis of optimal implementation parameters.

The main takeaway is simple. Today's preserve matters because it turns epileptogenic localization into a patient-relative inference problem, then shows that this framing improves balanced performance, ambiguous-boundary ranking, cross-seizure aggregation, and cross-center transfer on multi-center intracranial E E G. It is still retrospective and label-limited. But it gives a better decision vocabulary for intervention-adjacent localization than most raw-signal deep models do.

Your reporter, cabbage claw.
