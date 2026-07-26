# Proximity to an SGC-DLPFC Individualized Functional Target and outcomes in large rTMS clinical trials for Treatment-Resistant Depression

## Basic info

* Title: Proximity to an SGC-DLPFC Individualized Functional Target and outcomes in large rTMS clinical trials for Treatment-Resistant Depression
* Authors: Elizabeth Gregory, Shan H. Siddiqi, Michael D. Fox, Daniel M. Blumberger, Jonathan Downar, Zafiris J. Daskalakis, Katharine Dunlop, Fidel Vila-Rodriguez
* Year: 2026
* Venue / source: bioRxiv preprint inspected in full; peer-reviewed version later published in Brain Stimulation
* Link: https://doi.org/10.1101/2025.07.09.662866
* Date surfaced: 2026-07-26
* Why selected in one sentence: It pressure-tests personalized connectivity-guided DLPFC targeting in a 501-patient dataset and mostly says that once neuronavigated group targeting is already decent, simple proximity to individualized SGC or CDC targets does not explain antidepressant outcome.

## Quick verdict

* Highly relevant

This is one of the more useful recent negative papers in precision neuromodulation because it attacks a cherished claim with a dataset big enough to be annoying. I inspected the full 27-page bioRxiv preprint plus the July 25, 2026 PubMed record for the peer-reviewed Brain Stimulation version. The null result does not prove individualized targeting is worthless, because the imaging here is short, single-echo, and fairly legacy. But it does make the lazy version of the personalization story look much less credible.

## One-paragraph overview

The paper asks a blunt question: if individualized functional targets inside left DLPFC really matter for depression TMS, should patients do better when the clinically applied neuronavigated target lands closer to those individualized targets? The authors test that across 501 patients pooled from the THREE-D and CARTBIND trials, both of which delivered 4 to 6 weeks of neuronavigated left-DLPFC stimulation to the same optimized group target. From each patient's baseline resting-state fMRI they retrospectively compute two individualized functional targets, one based on subgenual cingulate anticorrelation and one based on the broader causal depression circuit. Most individualized targets end up already close to the actual group target, and that proximity does not predict percent HRSD change, response, remission, or target-connectivity effects. The paper is useful not because it kills personalization outright, but because it shows that a good group target plus a wide TMS electric field may erase much of the practical advantage that the individualized-target rhetoric assumes.

## Model definition

This paper does not center a trainable predictive model. It centers an individualized target-localization pipeline plus outcome association tests.

### Inputs
Baseline T1 and 10-minute resting-state fMRI scans, a left-DLPFC search mask, an SGC seedmap, a causal depression circuit map, neuronavigated treatment-target coordinates, stimulation protocol metadata, and baseline and end-of-treatment HRSD-17 scores.

### Outputs
Two individualized functional target coordinates per patient, one SGC-derived and one CDC-derived; Euclidean distance from each individualized target to the clinically applied group target; target connectivity estimates; and associations between those measures and antidepressant outcome.

### Training objective (loss)
There is no learned loss in the machine-learning sense. The core procedure selects clusters of the most anticorrelated or correlated voxels within DLPFC, then tests whether distance to those selected targets relates to symptom change.

### Architecture / parameterization
A seedmap-based individualized targeting pipeline: construct SGC- and CDC-weighted timeseries, compute voxelwise functional connectivity within a DLPFC search region, threshold to the top 0.5 percent of candidate voxels, take the largest cluster, and use its center of gravity as the individualized target.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Precision-TMS work keeps claiming that patient-specific connectivity targets inside left DLPFC should improve antidepressant outcomes, but much of that claim still rests on small studies, indirect comparisons, or mixed-up effects of targeting, protocol, and patient selection. This paper asks whether proximity to individualized connectivity-derived targets actually predicts outcome inside two large clinical-trial datasets where stimulation was already neuronavigated to a strong group target.

### 2. What is the method?

The authors retrospectively analyze 501 patients from the THREE-D and CARTBIND depression trials. Everyone received 4 to 6 weeks of left-DLPFC rTMS or iTBS at 120 percent resting motor threshold, targeted with neuronavigation to MNI coordinates minus 38, 44, 26. Using each patient's baseline resting-state fMRI, they compute two individualized functional targets: one maximizing SGC-related connectivity logic, and one maximizing causal-depression-circuit logic. They then test whether shorter distance from the applied target to either individualized target predicts better clinical outcome.

### 3. What is the method motivation?

If individualized connectivity targeting is genuinely clinically important, then even in retrospective data the patients whose delivered target sits closer to their own optimal cortical entry point should tend to do better. The paper also asks whether a broader circuit-derived target, not just the classic sgACC anticorrelation story, gives a stronger personalization signal.

### 4. What data does it use?

The analytic sample includes 501 patients with moderate to severe major depressive disorder after excluding 24 for high framewise displacement. THREE-D contributes 337 patients and CARTBIND contributes 164. Baseline resting-state scans are 10 minutes long with 300 volumes, acquired on 3T scanners with single-echo protocols and relatively large voxels. Clinical outcome is HRSD-17 change, plus response and remission.

### 5. How is it evaluated?

The main tests are Spearman correlations between individualized-target distance and percent HRSD-17 change, along with t-tests comparing responders versus non-responders and remitters versus non-remitters. The authors also test target functional connectivity itself, vary cluster thresholds, try an alternate searchlight localization method, and probe whether scanner site, cohort, signal quality, or stimulation protocol explains the null.

### 6. What are the main results?

Most individualized targets are already close to the actual group target. Median distance is 12.8 millimeters for the SGC-derived target and 13.8 millimeters for the CDC-derived target, with 74 percent and 69 percent of targets respectively falling within 20 millimeters.

Distance does not predict outcome. HRSD change is not significantly correlated with SGC-target distance, with rho equal to 0.02 and p equal to 0.6, or CDC-target distance, with rho equal to 0.05 and p equal to 0.3.

There is also no meaningful responder or remitter separation by distance. Group-target functional connectivity itself is similarly unhelpful, with no significant correlation to HRSD change for either SGC or CDC connectivity.

The two individualized-target frameworks are not meaningfully orthogonal. Their whole-brain functional-connectivity maps are strongly inversely related and the individualized targets themselves sit close together for most patients, with median separation around 7.9 millimeters.

Sensitivity analyses do not rescue the story. Changing thresholding, localization method, signal-quality handling, cohort, site, or treatment assignment does not create a positive proximity effect.

### 7. What is actually novel?

The novelty is not another pretty sgACC-targeting narrative. The useful novelty is the scale and the willingness to publish a clinically inconvenient null. The paper stress-tests two individualized-targeting frameworks inside large neuronavigated trial datasets and finds that the expected proximity advantage basically does not show up.

### 8. What are the strengths?

The sample is much larger than the small retrospective studies that helped build the personalization story.

The analysis directly compares two target definitions, classic SGC anticorrelation and the broader causal depression circuit, instead of pretending one biomarker is obviously correct.

Because everyone was already treated with neuronavigation to a strong group target, the test is harder and more clinically relevant than comparing an individualized method against a sloppy scalp heuristic.

The authors run enough sensitivity analyses that the null cannot be dismissed as a single arbitrary threshold choice.

### 9. What are the weaknesses, limitations, or red flags?

This is still retrospective and therefore not a clean randomized head-to-head test of individualized versus group targeting.

The imaging quality is a real limitation. The scans are single-echo, only 10 minutes long, and use fairly large voxels, which is a bad combination for stable individualized target estimation in DLPFC and especially ugly around sgACC-related signal.

The group target may already have been close enough to most individualized targets that there was not much usable variance left to detect a proximity effect.

The accessible full text in this run was the bioRxiv preprint rather than the full peer-reviewed publisher article, so I am trusting the preprint for the detailed methods and statistics.

The paper also does not solve electric-field variability prospectively; it mainly argues that field spread and less focal coil geometry may blur any targeting advantage.

### 10. What challenges or open problems remain?

The main unresolved question is whether individualized targeting truly fails, or whether current clinical fMRI quality is simply too noisy and too short to estimate useful individualized targets reliably. The field also still needs to separate targeting effects from protocol intensity, plasticity differences, coil focality, and symptom heterogeneity.

### 11. What future work naturally follows?

Run a prospective randomized trial that compares a high-quality neuronavigated group target against individualized targets derived from better imaging, ideally with longer and possibly multi-echo resting-state scans.

Integrate electric-field modeling prospectively rather than treating it as after-the-fact decoration.

Test whether individualized targeting matters only in specific depression biotypes or symptom dimensions rather than in average MDD outcomes.

Compare targeting gains against other individualization levers, especially plasticity enhancement and dosing logic.

### 12. Why does this matter for cabbageland?

Because precision-neuromodulation claims keep getting louder than their calibration. This paper is valuable exactly because it says a decent group target may already buy most of the practical benefit that personalized-connectivity marketing likes to attribute to itself. That does not end the targeting question, but it forces the field to prove that personalization adds something real on top of competent neuronavigation and not just on top of weak comparators.

### 13. What ideas are steal-worthy?

Benchmark individualized-target methods against a genuinely good group target, not just against BeamF3 or other weak heuristics.

Treat scan reliability as part of the causal question rather than as background nuisance, because a personalization method that needs unrealistic imaging quality is not yet clinically ready.

Use large nulls as design guidance: if most individualized targets cluster within the TMS electric field of a strong group target, the next gain may come from symptom-specific circuits, e-field shaping, or plasticity control rather than another prettier coordinate map.

### 14. Final decision

Keep. This is not a final verdict against individualized targeting, but it is a strong and badly needed calibration paper. If future precision-TMS claims cannot outperform this null on better data and in prospective designs, they are still mostly branding.
