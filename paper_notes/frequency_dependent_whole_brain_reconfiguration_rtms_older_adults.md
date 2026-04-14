# Frequency-Dependent Whole-Brain Reconfiguration Following Left DLPFC rTMS in Older Adults: A 106-Channel fNIRS Study

## Basic info

* Title: Frequency-Dependent Whole-Brain Reconfiguration Following Left DLPFC rTMS in Older Adults: A 106-Channel fNIRS Study
* Authors: Yingpeng Wang, Yutong Li, Hui Wang, Chuan Wang, Ailin Xiu, Jian Wang, Suxia Zhang, Chen Qiao, Tianzi Jiang, Shitong Qie
* Year: 2026
* Venue / source: Sensors (Basel)
* Link: https://pubmed.ncbi.nlm.nih.gov/41977966/
* Date surfaced: 2026-04-14
* Why selected in one sentence: It is a useful network-level rTMS paper because it measures distributed immediate reconfiguration in older adults and explicitly shows that the standard one-hertz-versus-ten-hertz story is too coarse.

## Quick verdict

* Useful

This is not a clinical efficacy result and it is not strong enough to settle mechanism. But it is worth keeping because it looks at the right unit of analysis: whole-brain network response rather than target folklore. The paper is especially useful because it reports both the expected broad frequency split and the awkward local exceptions that simpler stimulation narratives usually hide.

## One-paragraph overview

The study asks how one-hertz and ten-hertz repetitive transcranial magnetic stimulation over the left dorsolateral prefrontal cortex immediately reshape resting-state whole-brain connectivity in healthy older adults. Thirty participants aged sixty to seventy-five completed both stimulation conditions in a randomized single-blind crossover design, with one-hundred-and-six-channel functional near-infrared spectroscopy before and after each visit. At summary-network level, ten hertz was associated with more positive changes in global topology and spatially distributed connectivity, while one hertz tended in the opposite direction. But the more interesting result is that local exceptions remained, including bilateral primary-motor-cortex effects that ran against the crude frequency rule. The paper therefore helps mainly as a network-reconfiguration caution against binary stimulation slogans.

## Model definition

### Inputs
Resting-state functional near-infrared spectroscopy signals from a one-hundred-and-six-channel whole-brain recording setup, collected before and after left-dorsolateral-prefrontal one-hertz and ten-hertz repetitive transcranial magnetic stimulation in the same healthy older adults.

### Outputs
Channel-level, region-of-interest-level, and network-summary estimates of post-stimulation connectivity change, including graph-theoretic measures such as global efficiency, local efficiency, clustering coefficient, and mean node strength.

### Training objective (loss)
There is no trainable predictive model described in the accessible abstract. The analysis is inferential and graph-analytic rather than a learned decoder or predictor.

### Architecture / parameterization
A randomized single-blind crossover stimulation study coupled to whole-brain functional near-infrared spectroscopy connectivity analysis and graph-theoretic summary metrics.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to move rTMS interpretation beyond the old simplification that low frequency inhibits and high frequency excites. In older adults especially, distributed network responses may be more complex than that slogan suggests.

### 2. What is the method?
Participants underwent separate one-hertz and ten-hertz left-dorsolateral-prefrontal rTMS sessions. Whole-brain resting-state functional near-infrared spectroscopy was recorded before and immediately after stimulation, and the authors compared connectivity and graph metrics across frequency and time.

### 3. What is the method motivation?
If neuromodulation acts through distributed networks rather than only local excitability changes, then measuring whole-brain reconfiguration should be more informative than relying on coarse frequency labels. Aging brains are a good place to test that because compensation and reorganization may matter more.

### 4. What data does it use?
Thirty healthy older adults aged sixty to seventy-five, each contributing pre-post resting-state fNIRS data from both one-hertz and ten-hertz stimulation visits.

### 5. How is it evaluated?
It is evaluated by whether connectivity and graph-theoretic summaries change differently across the two frequencies, and by whether those changes survive correction at global or edge levels.

### 6. What are the main results?
Ten-hertz stimulation tended toward more positive network-summary changes, while one-hertz tended toward more negative changes. Frequency-by-time interaction effects were reported for global efficiency, local efficiency, clustering coefficient, and mean node strength. At edge level, only a small number of effects survived false-discovery-rate correction, and broader connection-wise patterns were treated as exploratory. Those exploratory patterns still suggested widespread enhancement after ten hertz and reduction after one hertz, along with localized paradoxical effects such as bilateral primary-motor-cortex increases after one hertz and decreases after ten hertz.

### 7. What is actually novel?
The novelty is not that rTMS changes connectivity. The useful novelty is the combination of whole-brain fNIRS coverage, older-adult focus, and an explicit emphasis on local exceptions to the classic excitation-inhibition shorthand.

### 8. What are the strengths?
- Whole-brain measurement instead of narrow target-neighborhood analysis.
- Within-subject crossover design reduces some between-person variance.
- Willingness to foreground exceptions rather than oversell the standard frequency dichotomy.
- Good framing for network-level intervention logic in aging.

### 9. What are the weaknesses, limitations, or red flags?
- Healthy older adults, not a clinical treatment cohort.
- No sham condition in the accessible abstract, which limits causal specificity for immediate changes.
- The strongest edge-wise effects were sparse after multiple-comparison correction.
- No behavioral or symptom endpoint tied directly to the network changes in the accessible text.
- Functional near-infrared spectroscopy gives a useful distributed readout, but not deep-circuit resolution.

### 10. What challenges or open problems remain?
The main open problem is whether these immediate network changes actually predict anything meaningful: symptom response, cognitive effects, durability, or individualized target selection. Another is whether the observed frequency effects survive in larger sham-controlled samples.

### 11. What future work naturally follows?
Sham-controlled replication, coupling the network measures to behavior or cognition, longitudinal follow-up, and testing whether baseline network state predicts who shows which reconfiguration pattern.

### 12. Why does this matter for cabbageland?
Because it is exactly the kind of paper that pushes intervention reasoning from recipe language toward network language. It does not solve targeting, but it does help break the lazy habit of acting as though frequency labels are already mechanism.

### 13. What ideas are steal-worthy?
- Measure distributed immediate network consequences whenever possible instead of inferring them from stimulation parameters.
- Treat localized paradoxical effects as informative rather than as inconvenient noise.
- Use aging cohorts to stress-test simplistic neuromodulation heuristics.
- Tie future targeting logic to network reconfiguration patterns rather than only scalp coordinates and frequency bins.

### 14. Final decision
Keep as a useful network-level neuromodulation note. It is not clinically decisive, but it is a good corrective to oversimplified rTMS mechanism talk.
