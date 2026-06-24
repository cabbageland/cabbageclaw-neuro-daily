# Neural Response to Theta-Burst Stimulation Predicts Long-Term Relapse in Patients With Alcohol Use Disorder: A Pilot fMRI Study

## Basic info

* Title: Neural Response to Theta-Burst Stimulation Predicts Long-Term Relapse in Patients With Alcohol Use Disorder: A Pilot fMRI Study
* Authors: Jing-Nan Zhao, Chu-Yue Zhao, Ying-Ying Li, Li-Ping Liu, Zhi-Jun Liu
* Year: 2026
* Venue / source: Addiction Biology
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC12791151/
* Date surfaced: 2026-06-24
* Why selected in one sentence: It is one of the rarer addiction-neuromodulation papers that forces the same study to face a blinded intervention, a post-treatment neural change, and a one-year relapse endpoint instead of hiding behind immediate craving movement.

## Quick verdict

* Highly relevant

This is a small pilot, but it is much more serious than the average addiction TMS paper. The useful contribution is not just that right-DLPFC continuous theta-burst stimulation looked better than sham over a year. It is that the paper tries to link that clinical difference to a specific post-treatment cue-reactivity pattern and then asks whether the neural delta predicts relapse. The main caution is that the sample is tiny, the active group started with higher baseline AUDIT scores, and the stimulation target was the scalp F4 landmark rather than individualized imaging guidance.

## One-paragraph overview

The paper reports a randomized, double-blind, sham-controlled pilot trial in alcohol use disorder in which twenty-eight participants received ten sessions of continuous theta-burst stimulation over the right dorsolateral prefrontal cortex across two weeks. The intervention was delivered at the F4 scalp coordinate, with active stimulation at one hundred percent resting motor threshold and sham achieved by rotating the coil perpendicularly. Participants completed an alcohol-cue fMRI task before and after treatment, and relapse was followed for twelve months. The strongest result is clinical and longitudinal: the active group showed lower relapse risk than sham, with a reported hazard ratio of 0.210. The mechanistic result is narrower but still useful: active cTBS prevented the cue-induced hyperactivity seen in the sham group in the right superior frontal gyrus. The paper then pushes further by training a relapse-prediction model on intervention-induced whole-brain cue-reactivity changes and reports accuracy of 78.7 percent with area under the curve of 0.903, with increased left medial prefrontal reactivity emerging as the strongest relapse-linked feature. This does not solve addiction neuromodulation, but it does make the field answer a better question.

## Model definition

The paper contains a substantive biomarker model layered on top of a clinical intervention trial.

### Inputs
The relapse model takes intervention-induced changes in brain-wide fMRI cue-reactivity features, effectively post-treatment minus pre-treatment alcohol-cue-related neural responses across distributed brain regions of interest. The broader trial also uses treatment assignment, relapse follow-up, baseline clinical measures such as AUDIT and withdrawal craving scores, and the alcohol-cue task itself.

### Outputs
The intervention outputs changes in alcohol-cue neural reactivity and long-horizon relapse outcomes. The machine-learning component outputs predicted relapse risk or relapse class over follow-up, plus feature-attribution rankings for the contributing brain regions.

### Training objective (loss)
From the inspected full text, the safest description is supervised relapse prediction from post-minus-pre cue-reactivity changes. The exact estimator family and optimization loss were not clearly exposed in the inspected sections, so I am not going to bluff a more specific answer.

### Architecture / parameterization
The main intervention is a ten-session right-DLPFC cTBS protocol targeted to the F4 scalp location. The biomarker layer is a brain-wide machine-learning relapse classifier built on intervention-induced ROI-level fMRI changes and interpreted with SHAP-style feature attribution; the exact classifier class is not stated clearly enough in the inspected text to summarize more narrowly.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Alcohol use disorder has high relapse rates, and addiction neuromodulation studies often stop at short-lived craving outcomes without showing whether stimulation changes anything that matters months later. This paper tries to connect stimulation, neural target engagement, and actual relapse risk in one design.

### 2. What is the method?
Patients with alcohol use disorder were randomized to active or sham right-DLPFC cTBS for ten sessions over two weeks. The target was the F4 scalp landmark, stimulation intensity was set to each participant's resting motor threshold, and fMRI alcohol-cue reactivity was measured before and after the course. The authors then followed relapse over twelve months and trained a relapse-prediction model on the intervention-induced neural changes.

### 3. What is the method motivation?
If addiction relapse reflects persistent prefrontal-subcortical dysregulation, then a useful intervention should do more than transiently move self-report scores. It should measurably alter cue-reactivity circuitry and those changes should help explain who stays well versus who relapses.

### 4. What data does it use?
The trial includes twenty-eight participants with alcohol use disorder, sixteen in the active cTBS group and twelve in sham. Baseline measures included AUDIT, craving-withdrawal scores, nicotine dependence, stress, and sleep. The imaging data came from a visual alcohol-cue block-design fMRI task performed pre- and post-intervention, and relapse was assessed by follow-up calls at one, three, six, nine, and twelve months.

### 5. How is it evaluated?
Evaluation happens at three levels. First, the paper compares long-term relapse risk between active and sham groups. Second, it tests whether alcohol-cue neural responses change differently across groups after treatment. Third, it trains a relapse-prediction model from the neural deltas and examines which brain regions contribute most strongly.

### 6. What are the main results?
The active cTBS group had significantly lower relapse risk over twelve months, with a reported hazard ratio of 0.210 relative to sham. On the imaging side, the key reported group-by-intervention interaction was in the right superior frontal gyrus, where active stimulation appeared to prevent the cue-induced hyperactivity seen after sham. The relapse model reportedly reached 78.7 percent accuracy and an AUC of 0.903, with greater post-treatment left medial prefrontal cue reactivity most strongly associated with relapse risk. The paper therefore argues that intervention-induced neural change may be more useful than baseline description alone.

### 7. What is actually novel?
The novelty is not simply "TMS helps addiction" or "fMRI predicts relapse." The useful move is the three-part linkage: blinded cTBS intervention, pre/post neural response measurement, and one-year relapse outcome in the same paper. That is far more decision-relevant than another craving-correlation story.

### 8. What are the strengths?
- Randomized, double-blind, sham-controlled design instead of one-arm treatment theater.
- Twelve-month relapse follow-up, which is much more meaningful than immediate post-session craving alone.
- Explicit attempt to connect clinical outcome to post-treatment neural target engagement.
- Uses post-treatment neural change as a candidate biomarker rather than pretending static baseline features are enough.
- Full article text was accessible, which makes the methods and caveats easier to audit.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is tiny, and the paper explicitly describes itself as a pilot.
- It is a single-centre study with all the usual generalizability limits.
- The active arm had higher baseline AUDIT scores than the sham arm, which is not a fatal flaw but is an ugly imbalance in a small trial.
- The stimulation target was the generic F4 scalp coordinate rather than individualized circuit targeting or neuronavigation.
- The relapse-prediction model may be overfragile simply because the sample is so small, and the paper did not make the exact classifier class clear enough in the inspected sections.
- Neural cue-reactivity change is still a surrogate; it is better than a vibes-only endpoint, but it is not yet a deployable closed-loop marker.

### 10. What challenges or open problems remain?
The field still needs to know whether this effect survives larger multisite replication, individualized targeting, stricter control of medications and psychosocial treatment, and stronger prospective relapse-prediction validation. It also remains unclear whether right-DLPFC cTBS is the right actuator or just one tractable entry point into a broader control network.

### 11. What future work naturally follows?
Run a larger multisite trial with individualized targeting, test whether the post-treatment neural marker prospectively guides booster or retreatment decisions, compare cTBS against other addiction-relevant stimulation protocols, and ask whether relapse prediction improves when neural deltas are combined with longitudinal behavioral or ecological data instead of fMRI alone.

### 12. Why does this matter for cabbageland?
Because it upgrades the addiction-neuromodulation question from "did craving budge?" to "did stimulation move a relapse-relevant circuit in a way that predicts who stays better?" That is a much better intervention-logic frame and travels well beyond alcohol use disorder.

### 13. What ideas are steal-worthy?
- Use long-horizon relapse as the real endpoint instead of pretending immediate craving relief is enough.
- Treat post-treatment neural change as a candidate decision signal rather than worshipping baseline biomarkers.
- Force the same study to show intervention, target engagement, and longitudinal outcome together whenever possible.
- Be suspicious of non-individualized targets even when the trial result is positive; target convenience is not the same as target competence.

### 14. Final decision
Keep. This is still a small and imperfect pilot, but it clears a more useful bar than most addiction neuromodulation papers by tying a blinded intervention to both a neural shift and a one-year clinical endpoint.
