# A human subcortical connectome at 400 μm resolution

## Basic info

* Title: A human subcortical connectome at 400 μm resolution
* Authors: Chiara Maffei, Ting Gong, Clemens Neudorfer, Dongsuk Sung, Dey Mihir, Kabilar Gunalan, Satrajit S. Ghosh, Jean C. Augustinack, Susie Y. Huang, Mark Richardson, Suzanne N. Haber, Anastasia Yendiki
* Year: 2026
* Venue / source: bioRxiv
* Link: https://www.biorxiv.org/content/10.64898/2026.03.31.715699v1
* Date surfaced: 2026-04-04
* Why selected in one sentence: It builds the kind of subcortical pathway atlas that neuromodulation targeting has been needing for years.

## Quick verdict

* Highly relevant

This is not a therapeutic study, but it may be more useful than many therapy papers because targeting quality depends on anatomical truth. If the atlas and annotations are as good as advertised, this could materially improve how deep-brain stimulation sites and side effects are interpreted. The main caution is that ex vivo high-resolution anatomy is not the same thing as in vivo patient-specific targeting.

## One-paragraph overview

The paper presents an ultra-high-resolution ex vivo diffusion-MRI reconstruction of human subcortical fiber pathways at four-hundred-micrometer resolution using the Connectome 2.0 scanner. The authors focus on basal-ganglia-thalamocortical pathways that matter for deep brain stimulation and lesion procedures, then provide a high-definition atlas and publicly released annotations. As a first translational test, they align the atlas to previously reported deep-brain stimulation hotspots and side-effect locations to identify pathways associated with benefit or adverse effects. The paper matters because neuromodulation targeting often talks as if these pathways are already resolved, when in reality the field frequently relies on synthetic or coarse anatomical stand-ins.

## Model definition

This paper is not centered on a learnable predictive model.

### Inputs
Ultra-high-resolution ex vivo diffusion MRI data acquired on the Connectome 2.0 scanner, plus anatomical annotations and previously reported deep-brain stimulation hotspot and side-effect locations.

### Outputs
Reconstructed subcortical pathways, a high-definition atlas of basal-ganglia-thalamocortical circuits, and pathway-level alignments linking prior DBS hotspot findings to candidate therapeutic or side-effect tracts.

### Training objective (loss)
The accessible abstract does not describe a trainable model objective. The central work is anatomical reconstruction and atlas building rather than supervised learning.

### Architecture / parameterization
An imaging-and-atlas pipeline for ultra-high-resolution ex vivo subcortical tract reconstruction and translational alignment to prior deep-brain stimulation hotspots.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Subcortical pathways critical for deep-brain stimulation are difficult to image noninvasively, so targeting often depends on imperfect anatomy. The paper tries to provide a much higher-resolution anatomical reference for those pathways.

### 2. What is the method?
The method uses ultra-high-resolution ex vivo diffusion MRI to reconstruct fiber pathways in the human subcortex, then packages the reconstructions as an atlas and aligns them with previously reported therapeutic and side-effect hotspots from deep-brain stimulation studies.

### 3. What is the method motivation?
If the field cannot resolve the subcortical pathways it is actually modulating, targeting claims remain weak. Better anatomy should improve both interpretation and future targeting logic.

### 4. What data does it use?
The accessible abstract describes a unique ex vivo diffusion-MRI dataset acquired on the Connectome 2.0 scanner, with publicly released data and annotations, plus reported hotspots from prior DBS studies.

### 5. How is it evaluated?
It is evaluated by reconstructing pathways that are usually difficult to resolve, demonstrating single-subject feasibility in this ex vivo setting, and showing that the atlas can be aligned to previously reported therapeutic and side-effect hotspots.

### 6. What are the main results?
The paper reports the first extensive reconstruction of human subcortical fiber pathways at this resolution, a high-definition basal-ganglia-thalamocortical atlas, and pathway alignments that connect prior DBS hotspots to candidate beneficial or adverse-effect tracts.

### 7. What is actually novel?
The novelty is not just higher spatial resolution. It is the combination of unusually fine ex vivo tract reconstruction with explicit neuromodulation-facing translation to hotspot interpretation.

### 8. What are the strengths?
- Addresses a real bottleneck in neuromodulation targeting.
- Focuses on subcortical anatomy that actually matters for DBS and lesion procedures.
- Connects atlas work to clinical hotspot interpretation instead of stopping at pretty anatomy.
- Public release and extensibility increase downstream usefulness.

### 9. What are the weaknesses, limitations, or red flags?
- Ex vivo high-resolution imaging is not equivalent to in vivo patient-specific tractography.
- I only inspected the abstract, so tract-validation details remain uncertain.
- Alignment to prior hotspots can be suggestive without proving causal pathway mediation.
- The paper can improve targeting logic without solving the inter-subject variability problem by itself.

### 10. What challenges or open problems remain?
Translating this atlas into robust in vivo individualized targeting, validating pathway assignments against outcomes prospectively, and handling anatomical variability across disease populations remain major challenges.

### 11. What future work naturally follows?
In vivo adaptation pipelines, prospective pathway-informed targeting studies, side-effect prediction benchmarks, and integration with patient-specific structural and functional data.

### 12. Why does this matter for cabbageland?
Because this is the sort of infrastructure paper that can quietly improve a lot of downstream intervention work. Better anatomical truth can sharpen target selection, side-effect interpretation, and mechanistic reasoning.

### 13. What ideas are steal-worthy?
- Treat targeting atlases as intervention infrastructure, not mere background reference.
- Connect anatomy work directly to hotspot and side-effect interpretation.
- Use high-resolution reference anatomy to expose where current in vivo targeting pipelines are bluffing.
- Keep pathway-level thinking central when evaluating deep-brain stimulation claims.

### 14. Final decision
Preserve. This is strong methods and targeting infrastructure with real downstream relevance to neuromodulation.
