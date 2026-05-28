# Machine learning-based optimization of dual subthalamic nucleus and substantia nigra targeting in deep brain stimulation

## Basic info

* Title: Machine learning-based optimization of dual subthalamic nucleus and substantia nigra targeting in deep brain stimulation
* Authors: Janis B. Roediger and colleagues
* Year: 2026
* Venue / source: npj Parkinson’s Disease
* Link: https://www.nature.com/articles/s41531-026-01406-8
* Date surfaced: 2026-05-28
* Why selected in one sentence: It turns one-lead dual STN plus SN DBS from an anecdotal surgical trick into a quantified trajectory-planning problem with practical heuristics.

## Quick verdict

* Highly relevant

This is a strong translational targeting paper. The machine learning here is not decorative, because the real product is not a black-box score but a set of patient-native rules for when a single STN trajectory is likely to engage SNr or SNc as well. The main caveat is that the paper validates geometric engagement, not downstream gait or balance outcomes, so clinical superiority remains unproven.

## One-paragraph overview

The paper asks whether a single deep brain stimulation lead aimed at the subthalamic nucleus can be planned to also engage the substantia nigra in a controlled way, rather than by accident. Using 612 reconstructed trajectories from 306 Parkinson disease patients, the authors classify whether standard STN trajectories reach SNr, SNc, both, or neither, then model the relationship between target coordinates and trajectory angles with Gaussian process classifiers. They show that dual engagement is often feasible, especially with longer arrays or deeper extension, and they derive usable rules of thumb for biasing a trajectory toward SNr versus SNc while preserving good STN engagement. The useful contribution is not the words machine learning. It is the conversion of variable anatomy into explicit planning logic for multi-target DBS.

## Model definition

### Inputs
Patient-native trajectory features derived from reconstructed DBS leads, including the X and Y coordinates of the trajectory intersection at the plane of maximal red nucleus cross-section, plus midsagittal and AC-PC angles.

### Outputs
Predicted probability that a planned trajectory engages the substantia nigra pars reticulata or pars compacta while also serving STN targeting goals.

### Training objective (loss)
The paper uses Gaussian Process Classifiers to classify SNr and SNc engagement. The accessible full text describes cross-validated classification accuracy, but does not foreground the exact optimization loss beyond the standard classifier fitting objective.

### Architecture / parameterization
Gaussian Process Classifier models fit on geometric trajectory features in patient-native space, alongside simpler logistic regression for depth-based SN engagement rules.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Dual STN plus SN stimulation is increasingly interesting for gait and balance problems in Parkinson disease, but in practice it is often treated as a lucky consequence of a standard STN trajectory. The paper tries to make that geometry explicit and reproducible.

### 2. What is the method?

The authors reconstruct implanted leads from a large Parkinson cohort, label whether trajectories engage STN, SNr, and SNc, simulate deeper or extended contacts, and train Gaussian Process Classifiers on trajectory coordinates and angles to estimate the probability of dual-target engagement.

### 3. What is the method motivation?

If different nigral subregions matter and standard STN trajectories do not reliably reach them, then therapeutic planning needs better rules than “go ventral and hope.” A probabilistic geometric model can support that planning without pretending there is one magic coordinate.

### 4. What data does it use?

The main dataset comprises 612 trajectories from 306 Parkinson disease patients that passed reconstruction quality checks. Analyses are performed in patient-native space, with regions including STN, SNr, and SNc and with simulated volumes of activated tissue for overlap analyses.

### 5. How is it evaluated?

Evaluation includes descriptive engagement rates for real and virtually extended trajectories, overlap analyses for STN and SN volumes of activated tissue, and five-fold cross-validated classifier accuracy for predicting SNr and SNc engagement from geometric features.

### 6. What are the main results?

Among implanted trajectories, 61 percent engaged SNr, 36 percent engaged SNc, 10 percent engaged both, and 13 percent engaged neither. Virtual extension improved SNr engagement to 76 percent and SNc engagement to 49 percent, with 27 percent engaging both and only 2 percent failing to reach SN at all. The Gaussian Process Classifiers achieved five-fold cross-validated accuracies of 90 percent for SNr and 87 percent for SNc, rising to 99 percent and 98 percent for high-confidence predictions. The paper also gives concrete rules of thumb, such as more lateral and steeper AC-PC trajectories for SNr and more posterior, less lateral, more midsagittal trajectories for SNc.

### 7. What is actually novel?

The novel part is not merely putting ML on surgical coordinates. The real novelty is separating SNr from SNc targeting logic and translating reconstructed trajectory data into practical planning corridors for one-lead dual targeting.

### 8. What are the strengths?

Large trajectory dataset for this kind of surgical-geometry paper.

Patient-native analysis rather than only template-space storytelling.

Clear distinction between SNr and SNc instead of treating the substantia nigra as one blob.

Practical output in the form of trajectory heuristics rather than only classifier metrics.

### 9. What are the weaknesses, limitations, or red flags?

The paper predicts anatomical engagement, not symptom improvement.

Volumes of activated tissue are simulated with simple assumptions.

Trajectory success is partly defined by contact overlap rules that may not capture true current spread or physiology.

The proposed rules may travel imperfectly across centers with different imaging, hardware, or targeting philosophies.

### 10. What challenges or open problems remain?

The main open problem is prospective outcome validation. It is still unclear when SNr versus SNc engagement actually helps freezing of gait, balance, or other symptoms, and how stimulation parameters interact with that geometry.

### 11. What future work naturally follows?

Prospective dual-target planning trials, coupling these heuristics to postoperative physiology and symptom readouts, and extending the framework to other multi-target DBS problems where one lead may plausibly serve two circuits.

### 12. Why does this matter for cabbageland?

Because this is exactly the kind of paper that sharpens intervention logic without pretending the hard part is solved. It asks what the hardware can physically hit, separates subregions that are often blurred together, and turns vague personalization language into concrete trajectory tradeoffs.

### 13. What ideas are steal-worthy?

Use patient-native geometry rather than template averages when the control lever is literally a lead trajectory.

Model multi-target reachability explicitly before debating adaptive algorithms that depend on those targets.

Translate classifier outputs into rules of thumb clinicians can actually use instead of stopping at ROC-style performance.

### 14. Final decision

Keep as a highly relevant translational targeting note. It does not prove better outcomes, but it meaningfully improves the planning logic for dual-target DBS.