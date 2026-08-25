# Cross-species brain-wide mapping reveals convergent mesocorticolimbic engagement by nucleus accumbens deep brain stimulation

## Basic info

* Title: Cross-species brain-wide mapping reveals convergent mesocorticolimbic engagement by nucleus accumbens deep brain stimulation
* Authors: Austin Y. Feng, Daniel A. N. Barbosa, Austen B. Casey, Daniel R. Rijsketic, Juliana S. Salgado, Harvey Huang, Robert C. Malenka, Dora Hermes, Kai J. Miller, Casey H. Halpern, Boris D. Heifets
* Year: 2026
* Venue / source: Molecular Psychiatry; full text inspected through the accessible 2024 bioRxiv preprint version of the same study
* Link: https://www.nature.com/articles/s41380-026-03828-5
* Date surfaced: 2026-08-25
* Why selected in one sentence: It turns nucleus accumbens DBS from a vague reward-circuit story into a concrete cross-species network-engagement claim.

## Quick verdict

* Highly relevant

This is one of the better recent NAc DBS papers because it replaces target mystique with an explicit network map. It does not show symptom change, and the human half is only one epilepsy patient, so this is not therapeutic proof. But the combination of unbiased whole-brain mouse mapping and direct human NAc evoked-potential motifs makes it much more useful than another paper that just says the accumbens is part of reward circuitry. The note is grounded in full-text inspection of the 2024 bioRxiv preprint plus abstract and metadata checks against the 2026 Molecular Psychiatry version, whose title is slightly updated.

## One-paragraph overview

The paper asks which mesocorticolimbic nodes are actually engaged by NAc DBS, rather than assuming the answer from anatomy diagrams. In mice, the authors apply bilateral medial-shell NAc stimulation and use whole-brain iDISCO clearing, light-sheet imaging, voxel-wise permutation testing, and single-cell Fos counting to identify activated clusters. The strongest noncontiguous clusters sit in basolateral amygdala, ventral hippocampus, lateral orbitofrontal cortex, and gustatory cortex, with strong cross-cluster correlations that suggest a coordinated intrinsic network rather than scattered downstream spillover. In a human epilepsy participant with an electrode traversing the NAc, the paper then records NAc stimulation-evoked potentials while stimulating 21 distant sites and uses basis profile curves to cluster response motifs. Hippocampal, amygdala, and insular stimulation sites group into distinct NAc response families, which gives the paper its main claim: NAc DBS appears to engage a conserved mesocorticolimbic network across species.

## Model definition

This is not primarily a predictive-model paper, but it does contain learnable analysis components that matter for the claims.

### Inputs
The mouse side takes bilateral medial-shell NAc stimulation in 18 TRAP2:Ai14 mice, with active versus sham DBS, followed by whole-brain Fos imaging. The human side takes single-pulse bipolar stimulation from 21 implanted sites in one epilepsy participant while recording from a single NAc contact, yielding 844 non-artefactual evoked-potential trials.

### Outputs
The mouse pipeline outputs voxel-wise maps of DBS-associated Fos changes and cluster-level Fos-positive cell densities. The human pipeline outputs stimulation-evoked NAc waveforms, projection weights, and basis profile curve assignments that summarize distinct response motifs from different stimulation sites.

### Training objective (loss)
There is no trainable clinical predictor or controller. The learnable pieces are an Ilastik random-forest pixel classifier used for cell detection and a non-negative matrix factorization step used in basis profile curve identification, where reconstruction error is iteratively reduced under non-negativity and degeneracy constraints.

### Architecture / parameterization
The important parameterization is a two-part cross-species stack: mouse whole-brain iDISCO plus GLM and permutation-based cluster discovery, then human NAc stimulation-evoked-potential clustering with basis profile curves. The biological intervention uses bilateral NAc shell DBS in mice at 130 Hz, 0.1 mA, 90 us biphasic pulses and convergent single-pulse intracranial stimulation in the human participant at 6 mA, 200 us per phase, 0.5 Hz.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve the mechanism gap in NAc DBS. The field treats the accumbens as an appealing psychiatric target, but usually with loose reward-circuit language rather than a specific, tested account of which downstream network is engaged.

### 2. What is the method?
The method is a cross-species bridge. In mice, the paper maps brain-wide Fos responses after active versus sham NAc DBS. In a human participant, it measures NAc evoked potentials during single-pulse stimulation of anatomically related sites and clusters those responses into canonical motifs with basis profile curves.

### 3. What is the method motivation?
If psychiatric DBS is going to mature beyond target branding, it needs a real account of network engagement. Whole-brain rodent mapping gives candidate nodes, and rare human intracranial recordings test whether analogous projections actually produce structured NAc responses.

### 4. What data does it use?
It uses 18 mice, split into active DBS and sham cohorts with equal male and female representation, plus one stereo-EEG participant with medically intractable epilepsy. The human analysis includes 844 non-artefactual NAc recordings from stimulation across 21 sites, with about 40 trials per site on average.

### 5. How is it evaluated?
The mouse side is evaluated with voxel-wise permutation inference, cluster extraction, and confirmatory single-cell Fos density counts. The human side is evaluated by whether anatomically related stimulation sites produce stable, separable basis profile curve motifs in the NAc and whether those motifs line up with the mouse network map.

### 6. What are the main results?
Active NAc DBS increased Fos-associated activity across a distributed set of cortical and subcortical structures, then narrowed into five discrete clusters for follow-up: NAc, basolateral amygdala, ventral hippocampus, lateral orbitofrontal cortex, and gustatory cortex. Compared with sham, active DBS significantly increased Fos-positive cell density in basolateral amygdala, ventral hippocampus, lateral orbitofrontal cortex, and NAc, while gustatory cortex did not reach significance but still tracked strongly with NAc activity. Correlations between cluster densities were generally strong, especially between NAc and basolateral amygdala, ventral hippocampus, and lateral orbitofrontal cortex. In the human participant, three distinct NAc basis profile curves emerged, with hippocampal, amygdala, and insular stimulation sites tending to share characteristic response motifs. The combined read is that NAc DBS engages a coordinated mesocorticolimbic network rather than only producing a local accumbens effect.

### 7. What is actually novel?
The novelty is not just that NAc has broad connections. That was already known. The paper's real novelty is the cross-species method stack: unbiased whole-brain neuronal activation mapping in mice paired with direct human NAc evoked-potential motif analysis to test whether a comparable network appears in people.

### 8. What are the strengths?
The paper uses a better mechanistic bridge than the usual clinical-abstract story. The mouse mapping is genuinely broad rather than restricted to a few hand-picked slices. The cluster validation goes beyond voxel intensity and counts Fos-positive cells directly. The human intracranial component is rare and gives the study real translational bite.

### 9. What are the weaknesses, limitations, or red flags?
The human sample is one epilepsy participant, so the translational half is hypothesis-supporting rather than population-stable. The rodent work uses healthy animals and one stimulation parameter set, not a disease model or symptom assay. The human stimulation sites are sampling-limited and there was no lateral orbitofrontal cortex electrode for a cleaner homologous test. The published journal version is paywalled in this environment, so the full-text read comes from the earlier preprint version even though the abstract and framing align closely.

### 10. What challenges or open problems remain?
The big open problem is whether this same network predicts symptom change, biomarker shifts, or closed-loop targets in actual psychiatric cohorts. Another challenge is disentangling which parts of the network are therapeutic effectors versus generic consequences of stimulating a densely connected ventral-striatal hub.

### 11. What future work naturally follows?
The obvious next steps are replication in more human participants, disease-state animal models, and patient cohorts receiving NAc DBS for depression, OCD, addiction, or eating-related disorders. A stronger next generation would connect network-engagement profiles to behavior, symptom response, or adaptive control signals instead of stopping at anatomical and electrophysiologic plausibility.

### 12. Why does this matter for cabbageland?
It matters because cabbageland cares about intervention logic, not just target folklore. This paper gives a cleaner network hypothesis for NAc-based psychiatry work and suggests specific nodes and motifs that could matter for biomarker design, target comparison, and closed-loop reasoning.

### 13. What ideas are steal-worthy?
Use whole-brain activation mapping to nominate candidate network nodes, then test homologous human connectivity with convergent stimulation and a fixed recording site. Treat basis profile curves as reusable network fingerprints rather than only as one-off visualization tools. Ask whether a DBS target preserves an intrinsic network, recruits a new one, or changes coupling among existing nodes, because those are different mechanism claims.

### 14. Final decision
Preserve. This is not clinical efficacy evidence, but it is a high-value mechanistic map with a real cross-species bridge. For NAc DBS, that is more useful than another paper that says reward circuitry and stops there.
