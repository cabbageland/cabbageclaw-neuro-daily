# A Network Target for Memory Dysfunction Derived from Brain Lesions and Stimulations

## Basic info

* Title: A Network Target for Memory Dysfunction Derived from Brain Lesions and Stimulations
* Authors: Calvin W. Howard, Savir Madan, Arun Garimella, Frederic Schaper, Isaiah Kletenik, Marcus C. Ng, Philip Mosley, Jordan Grafman, Rohit Bakshi, Bonnie Glanz, Lisa Fosdick, Amy Johnson, Ryan Colyer, Constantine G. Lyketsos, Mae Morton-Dutton, John Giftakis, Yasin Temel, Rob P.W. Rouhl, Ji H. Ko, Rabea Schmahl, Juan C. Baldermann, Özgür Onur, Pablo Andrade-Montemayor, Veerle Visser-Vandewalle, Jens Kuhn, Maurizio Corbetta, Robert S. Fisher, Thomas Picht, Katharina Faust, Molly Hermiller, Joel Voss, Tanuja Chitnis, Michael K. Kahana, Gwenn S. Smith, Andres Lozano, Shan H. Siddiqi, Andreas Horn, Michael D. Fox
* Year: 2026
* Venue / source: medRxiv preprint
* Link: https://www.medrxiv.org/content/10.64898/2026.03.10.26348082v1.full
* Date surfaced: 2026-05-26
* Why selected in one sentence: It is a rare network-targeting paper that combines lesions, DBS, and TMS into one causal target-discovery frame and then tests whether that target explains heterogeneity in memory-stimulation outcomes.

## Quick verdict

* Highly relevant

This is the strongest paper of the morning because it does not just claim that memory lives in a broad connectomic cloud. It combines twelve causal datasets across lesions, DBS, and TMS, derives a convergent memory network, validates it in held-out cohorts, and then checks whether overlap with that network explains effect sizes in prior Alzheimer stimulation trials. The main caveat is that the network is built from normative connectivity and verbal-memory-heavy tasks, so it is not yet a patient-specific intervention recipe.

## One-paragraph overview

The authors study memory change across 1,247 patients from twelve independent datasets spanning focal lesions, deep brain stimulation, and transcranial magnetic stimulation. Instead of asking which single anatomical spot is best, they map how each lesion or stimulation site connects into a normative whole-brain functional connectome and identify connectivity patterns associated with verbal episodic memory impairment or improvement. Those modality-specific maps converge on a common memory network whose core nodes include hippocampus, retrosplenial cortex, precuneus, lateral parietal cortex, prefrontal cortex, and cerebellar regions. In held-out lesion, DBS, and TMS datasets, connectivity to this convergent network explained more memory variance than modality-specific maps or legacy anatomical candidates. The useful claim is not “here is the memory circuit” in some mystical sense. It is that cross-modal causal convergence can refine stimulation targets better than staying inside one modality silo.

## Model definition

### Inputs
Lesion locations, DBS electrode locations, TMS stimulation sites, corresponding verbal episodic memory outcomes, and normative whole-brain functional connectivity profiles derived from a healthy connectome.

### Outputs
Cohort-level memory network maps, modality-level convergent memory maps, an optimized cross-modal convergent memory network, and target-overlap metrics that predict memory outcomes or prior trial effect sizes.

### Training objective (loss)
There is no single trainable predictive model in the clinical sense. The main optimization step learns a weighted combination of eleven cohort-level network maps that maximizes explained variance in a left-out twelfth cohort, then repeats this in cross-validation before deriving the final convergent memory network on the full dataset.

### Architecture / parameterization
A cross-modal lesion-network-mapping and stimulation-network-mapping pipeline using normative functional connectivity, cohort-level rho maps, weighted network aggregation, held-out validation, and meta-analytic target-overlap analysis.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Memory-stimulation trials have targeted many different brain regions and produced highly variable results. The paper tries to derive a better neuroanatomical target for memory neuromodulation by combining multiple causal data sources instead of trusting any one modality.

### 2. What is the method?
For each lesion or stimulation site, estimate normative whole-brain connectivity and test which connections covary with verbal episodic memory outcomes. Build cohort-level maps, combine them into cross-modal convergent maps with an optimized weighting procedure, and validate the resulting network in unseen lesion, DBS, and TMS datasets.

### 3. What is the method motivation?
Lesions, DBS, and TMS each provide partial causal evidence but each also carries its own confounds. If they converge on the same network, that network should be a stronger candidate target than any single modality map or legacy atlas-based structure.

### 4. What data does it use?
The discovery analysis spans 1,247 patients in twelve datasets, including lesion cohorts, DBS cohorts, and TMS cohorts with objective verbal episodic memory measurements. Validation adds three held-out cohorts involving epilepsy-related hypometabolism, forniceal DBS for Alzheimer disease, and parietal TMS for age-related memory loss.

### 5. How is it evaluated?
By testing spatial convergence across cohort-level maps, measuring how well the convergent map explains memory variance in left-out datasets, comparing it against modality-specific maps and legacy structures, and relating target overlap to effect size in twenty-one prior Alzheimer brain-stimulation trials.

### 6. What are the main results?
Lesion and stimulation sites affecting verbal memory converge on a common network rather than a single coordinate. The convergent memory network outperformed modality-specific maps in held-out lesion, DBS, and TMS datasets, explaining about 19 percent more variance for lesion-like validation data, 14 percent more for DBS, and 34 percent more for TMS. In a meta-analysis of twenty-one prior Alzheimer stimulation trials, studies whose targets overlapped positive regions of the derived memory target network showed better cognitive effect sizes than studies targeting outside it.

### 7. What is actually novel?
The novelty is not just another lesion-network map. It is the explicit convergent-causal-mapping frame that combines lesions, DBS, and TMS into one target-discovery procedure and then checks whether that cross-modal target helps explain real stimulation-trial heterogeneity.

### 8. What are the strengths?
- Stronger causal footing than ordinary connectome correlation papers.
- Uses multiple intervention and lesion modalities instead of one silo.
- Includes held-out validation rather than only discovery-set storytelling.
- Links the derived network back to prior Alzheimer stimulation trials, which makes the targeting claim more intervention-relevant.

### 9. What are the weaknesses, limitations, or red flags?
- The connectivity backbone is normative rather than patient-specific.
- Verbal episodic memory is a useful proxy, but not the whole memory landscape.
- The Alzheimer trial meta-analysis is retrospective and inherits the weaknesses of old heterogeneous studies.
- A convergent network is still not the same thing as a prospectively validated stimulation target.

### 10. What challenges or open problems remain?
The next problems are patient-specific targeting, state dependence, longitudinal durability, and whether the same convergent-network logic survives when the task is not verbal episodic memory.

### 11. What future work naturally follows?
Prospective target selection in memory-neuromodulation trials, individualized connectome versions of the target map, and joint optimization of target location with stimulation timing or state estimation.

### 12. Why does this matter for cabbageland?
Because it is exactly the kind of network paper that sharpens intervention logic instead of just decorating it. It gives a more serious answer to “where should we stimulate?” and does so by combining causal evidence sources rather than by worshipping one imaging modality.

### 13. What ideas are steal-worthy?
- Use convergent causal mapping across lesions and perturbations instead of staying inside one modality.
- Treat target selection as a network-overlap problem, not just a coordinate problem.
- Compare derived targets against prior trial heterogeneity instead of only reporting internal cross-validation.
- Keep lesion and stimulation signs explicit rather than forcing a fake one-direction map.

### 14. Final decision
Preserve. This is one of the more useful recent papers on network-guided memory stimulation and target discovery.