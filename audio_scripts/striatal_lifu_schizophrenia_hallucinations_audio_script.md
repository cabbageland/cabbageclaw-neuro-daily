Low-intensity focused ultrasound targeting striatal circuits in schizophrenia: feasibility, safety, and effects on hallucinations and striatal-temporal functional connectivity
Basic info
Title: Low-intensity focused ultrasound targeting striatal circuits in schizophrenia: feasibility, safety, and effects on hallucinations and striatal-temporal functional connectivity
Authors: Karuna Subramaniam, Grace Attalla, Miriam Mathew, John L. Alvarez, Ehsan Dadgar-Kiani, Rajiv Mahadevan, Srikantan Nagarajan, Keith R. Murphy
Year: 2026
Venue / source: Brain Stimulation
Link:
Date surfaced: 2026-06-03
Why selected in one sentence: It directly tests whether noninvasive deep-target ultrasound can perturb a psychosis-relevant striatal circuit and move hallucination symptoms with it.
Quick verdict
Useful
This is exactly the kind of circuit-level interventional psychiatry experiment the field should try more often, but the sample size is microscopic. The paper is worth preserving because it combines deep-target perturbation, individualized targeting, sham control, symptom readouts, and connectivity readouts in the same frame. It is not worth overclaiming because the study has only three patients, limited sham comparison, and only immediate post-stimulation outcomes. This note is based on the accessible full medRxiv text corresponding to the later Brain Stimulation publication.
One-paragraph overview
The study is a first-in-human, randomized, within-subject crossover feasibility trial testing low-intensity focused ultrasound directed at two striatal targets, the nucleus accumbens and caudate head, in three stable outpatients with schizophrenia who experience auditory hallucinations. Each participant received active stimulation to both targets plus one unfocused-sonication sham session, with MRI-guided targeting, acoustic simulations, and immediate symptom and resting-state fMRI readouts. The headline result is that active sonication to both striatal targets was reported as safe and was associated with large acute drops in hallucination severity and frequency, alongside reduced striatal to superior temporal cortex connectivity. The right read is not that hallucinations are now solved by ultrasound. The right read is that deep striatal LIFU may be a plausible noninvasive way to test causal circuit hypotheses in psychosis.
Model definition
Inputs
Participant-specific T1 and PETRA MRI data for targeting and skull modeling, canonical nucleus accumbens and caudate head coordinates transformed to native space, low-intensity focused ultrasound parameters, resting-state fMRI data, and hallucination symptom measures including VAS and AVHRS.
Outputs
Predicted acoustic intensity and temperature maps, safety metrics, pre-post hallucination severity and frequency changes, and pre-post striatal to superior temporal cortex functional-connectivity changes.
Training objective (loss)
There is no trainable predictive model at the center of the paper. The imaging pipeline estimates connectivity, and the acoustic simulation pipeline estimates target engagement and safety, but the main design is an interventional feasibility trial rather than a learned model.
Architecture / parameterization
Individualized MRI-guided neuronavigation and acoustic simulation for bilateral 500 kHz ultrasound delivery to nucleus accumbens and caudate-head targets, paired with symptom measurement and seed-to-voxel resting-state functional-connectivity analysis.
Key questions this summary must address
1. What problem is the paper trying to solve?
Auditory hallucinations in schizophrenia are strongly linked to deep striatal circuitry, but causal noninvasive tests of those targets have been limited because standard surface stimulation methods cannot reach them well.
2. What is the method?
A first-in-human randomized within-subject crossover feasibility study with three conditions: active LIFU to nucleus accumbens, active LIFU to caudate head, and sham unfocused sonication, each separated by a one-week washout.
3. What is the method motivation?
If aberrant striatal to superior temporal coupling helps generate hallucinations, then directly modulating those deep striatal targets should shift both symptoms and the implicated circuit. LIFU offers a way to test that idea without invasive surgery.
4. What data does it use?
Three schizophrenia participants with auditory hallucinations, high-resolution structural MRI, resting-state fMRI, individualized acoustic simulations, daily VAS hallucination ratings, and baseline plus one-week AVHRS assessments.
5. How is it evaluated?
The study evaluates feasibility and safety with acoustic simulations and session monitoring, symptom effects with repeated VAS and AVHRS measurements, and mechanistic effects with seed-to-voxel functional-connectivity changes from striatal seeds to superior temporal cortex.
6. What are the main results?
All sessions were reported as safe and well-tolerated, with simulated acoustic and thermal metrics under safety thresholds.
Active nucleus-accumbens and caudate-head sonication both produced significant immediate pre-post reductions in hallucination severity and frequency.
Every participant reportedly showed more than fifty percent reduction in severity and frequency after active sonication relative to baseline.
Baseline striatal to superior temporal hyperconnectivity decreased after active sonication in the post-LIFU imaging data that were available.
Washout periods appeared adequate, and sham blinding reportedly held up behaviorally.
7. What is actually novel?
The novelty is not merely using ultrasound. It is using individualized deep-target LIFU to test a specific psychosis circuit hypothesis, then pairing symptom change with the predicted network readout in a noninvasive first-in-human design.
8. What are the strengths?
It targets a deep circuit that surface TMS cannot directly access.
The design includes two active striatal targets plus a sham condition.
It uses individualized acoustic modeling rather than generic geometry.
It pairs symptom readouts with mechanistically relevant connectivity readouts.
It treats target engagement and safety as part of the actual scientific argument.
9. What are the weaknesses, limitations, or red flags?
The sample size is only three patients.
One participant had no hallucinations immediately before the sham session, which weakens active-versus-sham comparison.
Post-LIFU imaging was unavailable for one patient, and sham imaging was not available for mechanistic comparison.
The statistical outputs are exploratory and far too small-sample to support efficacy claims.
The effects are acute only; there is no durability evidence.
Several authors have direct company ties to the ultrasound platform.
10. What challenges or open problems remain?
The major open problems are whether the effect replicates in a properly powered sham-controlled trial, whether target choice can be improved further with connectivity-based personalization, whether repeated sessions produce durable benefit, and whether the apparent circuit effect is specific rather than driven by nonspecific arousal or expectancy factors.
11. What future work naturally follows?
Run a larger double-blind sham-controlled trial, add sham post-stimulation imaging, test multi-session durability, estimate dose-response relationships, and compare canonical-target versus individualized connectivity-guided targeting.
12. Why does this matter for cabbageland?
Because it is a rare interventional psychiatry study that actually tries to perturb a deep symptom-relevant circuit and read out both behavioral and network consequences. Even if the trial is tiny, the experimental logic is much better than another average-outcome device paper.
13. What ideas are steal-worthy?
Use noninvasive deep-target perturbation to test causal psychiatric circuit hypotheses before jumping to chronic invasive intervention.
Pair symptom readouts with a target-linked connectivity biomarker in the same session.
Preserve sensory blinding with unfocused sonication rather than a trivial no-stimulation sham.
Think about hallucination treatment as regulating striatal-temporal gating rather than as treating schizophrenia in the abstract.
14. Final decision
Preserve with caution. The trial is far too small for therapeutic confidence, but it is a worthwhile mechanistic keep because it makes a serious attempt to test and read out a deep psychosis circuit noninvasively.
