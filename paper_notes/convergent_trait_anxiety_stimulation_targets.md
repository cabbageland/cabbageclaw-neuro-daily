# Convergent Network Localization of Brain Stimulation Targets for Trait Anxiety

## Basic info

* Title: Convergent Network Localization of Brain Stimulation Targets for Trait Anxiety
* Authors: Shan H. Siddiqi, Julian Klingbeil, Ryan Webler, Ian H. Kratter, Daniel M. Blumberger, Michael D. Fox, Mark S. George, Jordan H. Grafman, Alvaro Pascual-Leone, Andrew R. Pines, R. Mark Richardson, Pratik Talati, Fidel Vila-Rodriguez, Jonathan Downar, Tamara Hershey, Kevin J. Black
* Year: 2026
* Venue / source: American Journal of Psychiatry
* Link: https://doi.org/10.1176/appi.ajp.20250198
* Date surfaced: 2026-07-25
* Why selected in one sentence: It upgrades anxiety-target discovery from correlation-heavy folklore to a convergent causal circuit argument spanning lesions, TMS, individualized connectivity, and DBS.

## Quick verdict

* Highly relevant

This is one of the stronger recent symptom-circuit papers in psychiatry because it does not ask the user to trust one modality, one target, or one retrospective story. I could inspect the full PMC-hosted preprint text, and that PMC page explicitly notes that a peer-reviewed American Journal of Psychiatry version has now been published. The main confidence limit is not the core logic but the remaining gap between the accessible full preprint and the inaccessible final publisher full text. Even with that caveat, the paper is strong enough to keep because it makes anxiety target discovery more causal, more transdiagnostic, and more clinically awkward in a useful way.

## One-paragraph overview

The paper tries to localize a brain-stimulation target for trait anxiety by forcing several natural experiments to converge on the same circuit instead of trusting any single one. The authors combine scalp-based TMS datasets, lesion datasets, an individualized-connectivity TMS dataset, and subthalamic DBS datasets across 936 people. They map the connectivity of sites that relieve anxiety or cause anxiety, control for depression, and ask whether the results converge. They do. The combined circuit peaks in the right superior frontal gyrus and right lateral parietal lobe, individualized TMS connectivity to that circuit predicts anxiety change, and STN DBS overlap with the circuit predicts anxiety worsening even though the circuit was derived without subthalamic sites. The useful claim is not merely that anxiety has a network. The useful claim is that a trait-anxiety circuit can be localized in a way that is specific enough to propose new stimulation targets and to explain why some depression-oriented targets may worsen anxiety.

## Model definition

This paper does not center a trainable clinical model. The relevant machinery is multimodal circuit mapping plus out-of-sample validation.

### Inputs
Localized TMS sites, brain lesions, and STN DBS sites; validated anxiety and depression measures; a normative functional connectome with n equals 1000; and individualized resting-state fMRI connectivity for the THREE-D TMS cohort.

### Outputs
Dataset-level anxiety circuit maps, a convergent weighted-mean causal anxiety circuit, predicted anxiety change from TMS-site connectivity to that circuit, and predicted anxiety outcomes from DBS-site overlap with that circuit.

### Training objective (loss)
There is no trainable loss in the machine-learning sense. The core analyses use voxel-wise partial correlations controlling for depression, spatial correlations between circuit maps, permutation tests against shuffled outcome-to-imaging assignments, and weighted averaging across datasets.

### Architecture / parameterization
A multimodal lesion-network and stimulation-site mapping framework: two scalp-target TMS datasets, two lesion datasets, one individualized-connectivity TMS dataset, and two STN DBS validation datasets, all combined into a convergent causal anxiety circuit.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Brain stimulation can change anxiety, but the field still lacks a serious way to discover anxiety targets rather than recycling depression targets, fear-conditioning lore, or generic right-versus-left prefrontal habits. The paper asks whether a causal trait-anxiety circuit can be localized across several different natural experiments.

### 2. What is the method?

The authors localize TMS sites, lesions, and DBS sites in standard space, estimate each site's connectivity using a normative connectome or individualized resting-state fMRI, and compare those connectivity maps with anxiety outcomes while controlling for depression. They then combine the resulting maps into a convergent anxiety circuit and validate it against independent individualized-connectivity TMS data and STN DBS outcomes.

### 3. What is the method motivation?

Any one modality has ugly confounders. Lesions are causal but noisy and opportunistic. TMS has intervention value but limited targeting precision. DBS reaches deep circuits but comes from different diseases and indications. If all of them converge on similar circuitry, the target-discovery claim becomes much harder to dismiss as one dataset's accident.

### 4. What data does it use?

Seven datasets totaling 936 individuals. These include two scalp-based DLPFC TMS datasets with 111 combined participants, two lesion datasets with 451 combined lesions, one individualized-connectivity TMS dataset with 300 depression patients from THREE-D, and two Parkinson's STN DBS datasets totaling 74 patients for external validation.

### 5. How is it evaluated?

Evaluation happens at several levels. The paper checks whether lesion and TMS maps resemble each other more than chance, whether the individualized-connectivity TMS map resembles the normative convergent map, whether TMS-site connectivity to the circuit predicts anxiety change, whether DBS-site overlap predicts anxiety change, and whether these effects are specific to trait rather than state anxiety.

### 6. What are the main results?

The four initial TMS and lesion maps show strong convergence, with mean spatial cross-correlation around 0.58 and permutation p equals 0.008.

The combined TMS map and combined lesion map correlate at r equals 0.68 with p equals 0.01.

In the individualized-connectivity TMS cohort, the derived map resembles the normative anxiety circuit at spatial r equals 0.39 with p equals 0.02, and TMS-site connectivity to the circuit predicts anxiety change at r equals 0.14 with p equals 0.02.

Negative connectivity to the anxiety circuit is associated with categorical anxiety worsening after TMS.

The convergent circuit peaks in the right superior frontal gyrus and right lateral parietal lobe, both surviving family-wise-error permutation testing.

Across two STN DBS datasets, overlap with the anxiety circuit predicts anxiety worsening at r equals 0.32 with p equals 0.006.

Trait-versus-state specificity is real. In trait-anxiety analyses, lesion connectivity and DBS overlap track trait anxiety, not state anxiety, with key p values around 0.003.

### 7. What is actually novel?

The novelty is not just another anxiety network picture. The useful novelty is the convergence logic. The paper makes lesion mapping, scalp-target variability, individualized connectivity, and DBS outcomes answer the same question, then uses that convergence to nominate a new anxiety target rather than merely re-explaining a known depression site.

### 8. What are the strengths?

The paper is unusually strong on causal triangulation for a psychiatry target paper.

It treats anxiety and depression as separable enough to test, rather than as one blended symptom sludge.

It checks trait versus state anxiety instead of assuming they are interchangeable.

It turns anxiety worsening under stimulation into signal about the circuit instead of burying it as an annoying side effect.

It benchmarks the circuit against alternative target-discovery strategies and reports that the convergent circuit outperforms those comparators.

### 9. What are the weaknesses, limitations, or red flags?

This is still a natural-experiment synthesis rather than a prospective randomized trial of the newly proposed anxiety target.

The datasets are heterogeneous in imaging quality, site localization precision, diagnosis, and outcome measures.

Lesion analyses cannot use pre-lesion anxiety measurements and must assume pre-lesion anxiety is randomly distributed with respect to lesion location.

The individualized-connectivity effect sizes are real but modest, and the paper itself notes that older low-resolution fMRI in THREE-D may blunt personalization signal.

My inspection used the full PMC preprint plus the peer-reviewed AJP abstract and metadata, not the full publisher text, because the publisher page was bot-walled in this run.

### 10. What challenges or open problems remain?

The obvious next challenge is whether directly stimulating the proposed right superior frontal target helps anxiety disorders prospectively, rather than only explaining existing variability. The field also still needs cleaner patient-level assignment rules, better anxiety side-effect monitoring in depression trials, and finer separation of rumination-like trait anxiety from more phasic fear or arousal states.

### 11. What future work naturally follows?

Prospective randomized trials targeting the right superior frontal and adjacent medial prefrontal circuit in primary anxiety disorders.

Patient-specific connectome-guided target optimization rather than one fixed target for everyone.

Studies that explicitly trade off antidepressant and anxiolytic circuit goals instead of assuming they point in the same direction.

Mechanistic work linking this trait-anxiety circuit to rumination, fear extinction, and other candidate processes rather than only symptom totals.

### 12. Why does this matter for cabbageland?

Because it sharpens a recurring cabbageland problem: symptom-specific target discovery needs something better than average depression outcomes plus retrospective storytelling. This paper suggests that anxiety may require its own target logic, may partly anti-align with some depression-optimized targets, and should be treated as a first-class circuit problem rather than as background mood noise.

### 13. What ideas are steal-worthy?

Use convergence across lesions, TMS, and DBS as a target-discovery standard instead of trusting a single modality.

Treat anxiety worsening after stimulation as target-information, not just safety paperwork.

Separate trait from state anxiety when building targets, biomarkers, or intervention logic.

Ask whether symptom-specific circuits for comorbid dimensions are anti-correlated, because that may explain why broad depression targeting so often disappoints.

### 14. Final decision

Keep. This is one of the more convincing recent papers on how psychiatry brain-stimulation targets should be discovered. It does not yet prove that the proposed anxiety target works prospectively, but it makes the target-discovery standard meaningfully harder to fake.
