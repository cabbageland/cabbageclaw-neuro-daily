# Skull-Conforming Acoustic Holographic Lenses for Transcranial Targeting

## Basic info

* Title: Skull-Conforming Acoustic Holographic Lenses for Transcranial Targeting
* Authors: Mihir Pewekar, Hrishikesh Kulkarni, Yunruo Ni, Nathan Sambo, Adam Maxwell, Eli Vlaisavljevich, Wynn Legon, and Shima Shahab
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/html/2604.21207
* Date surfaced: 2026-06-01
* Why selected in one sentence: It attacks one of the real bottlenecks in ultrasound neuromodulation, namely subject-specific skull distortion plus poor coupling, instead of waving those problems away.

## Quick verdict

* Highly relevant

This is a good methods paper because it improves the physical honesty of transcranial focused ultrasound targeting. The strongest move is not merely personalized phase correction. It is the combination of subject-specific wavefront optimization with a conformal coupling layer that is meant to reduce reflection losses and stabilize geometry at the head interface. The main caveat is that the validation is still simulation-heavy with ex vivo skull confirmation, so the translational promise is ahead of in vivo efficacy evidence.

## One-paragraph overview

The paper proposes a subject-specific volumetric holography pipeline for transcranial focused ultrasound in which acoustic holographic lenses are designed from individual CT and MRI data and paired with a skull- and skin-conforming coupling layer. The core idea is that deep or volumetric ultrasound targeting fails not only because of skull-induced phase aberration, but also because the interface between transducer and head is geometrically messy and acoustically lossy. The authors therefore optimize both the holographic phase plate and the coupling geometry together, then test performance across multiple subjects and target regions in simulation and in ex vivo human skull experiments. The useful contribution is not a clinical result. It is a more realistic delivery stack for future ultrasound neuromodulation work.

## Model definition

This paper is not centered on a learned predictor. It is an optimization-driven acoustic design framework.

### Inputs
Subject-specific CT-derived skull geometry, MRI-derived anatomical targets, selected target volumes and source pathways, acoustic properties of the conforming layer and cranial tissues, and design constraints related to focal coverage and pressure safety.

### Outputs
A personalized acoustic holographic lens thickness map, a skull-conforming coupling layer design, simulated and experimentally validated three-dimensional pressure fields, and performance metrics such as target-volume coverage and off-target suppression.

### Training objective (loss)
The method uses optimization losses that minimize mismatch between the generated three-dimensional pressure field and the desired target volume, then augments that objective with penalties to suppress unwanted off-target energy. It is a physics-optimization loss, not a supervised predictive loss.

### Architecture / parameterization
A subject-specific volumetric holography framework using mixed-domain wave propagation, coarse-to-fine hierarchical hologram optimization, and a manufacturable 3D-printable acoustic holographic lens paired with a conformal coupling interface.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

It is trying to make transcranial ultrasound targeting more reliable in the face of skull-induced aberration, anatomical variability, coupling mismatch, and the need to cover realistic three-dimensional target volumes rather than an idealized focal point.

### 2. What is the method?

The authors build a subject-specific pipeline that combines CT and MRI data, defines target regions and source paths, models propagation through heterogeneous tissue, and computes a personalized acoustic hologram with a hierarchical optimization procedure. They also add a skull- and skin-conforming coupling layer so the physical interface preserves alignment and impedance continuity better than a generic water-coupled setup.

### 3. What is the method motivation?

A lot of ultrasound neuromodulation work talks as if the beam can simply be aimed, but skull geometry and poor interface coupling distort the wavefront before it reaches the target. If those problems are not solved explicitly, claims about deep precision are partly theater.

### 4. What data does it use?

The framework uses subject CT scans for skull geometry, MRI scans for target definition, and simulations across five subjects with multiple target regions, including hippocampus, insula, and cuneus variants. Experimental validation is performed using ex vivo human skull specimens.

### 5. How is it evaluated?

Evaluation focuses on whether the designed holograms reconstruct the intended volumetric pressure field under realistic heterogeneous propagation, maintain target coverage within safety limits, and remain physically manufacturable and usable with a conformal coupling layer. The authors also compare simulated fields with ex vivo acoustic reconstructions through human skulls.

### 6. What are the main results?

The paper reports consistent volumetric focusing and reliable target coverage across multiple subjects and targets in simulation, with pressure fields kept within stated safety limits. The ex vivo validation is presented as showing accurate fabrication, effective coupling, and faithful reconstruction of the designed three-dimensional acoustic field.

### 7. What is actually novel?

The novelty is not just another acoustic lens. The more important move is integrating individualized phase synthesis with a conformal acoustic interface and a target-volume optimization framework, rather than treating skull correction, coupling, and manufacturability as separate side problems.

### 8. What are the strengths?

It attacks a real translational bottleneck rather than another decorative beam-shaping problem.

It treats acoustic coupling as part of the targeting problem, which is the correct instinct.

It uses subject-specific anatomy and validates the design with ex vivo skull experiments instead of simulation alone.

It is explicit about volumetric targeting, which matters more than a pretty focal hotspot picture.

### 9. What are the weaknesses, limitations, or red flags?

It is still preclinical delivery work, not a demonstration of neural target engagement or therapeutic benefit in humans.

Only five subjects are modeled, so the robustness of the framework across broader anatomical variation is still uncertain.

Ex vivo skull validation is useful, but it does not capture the full messiness of in vivo positioning, tissue motion, and biologic variability.

The optimization framework is only as good as the assumed acoustic properties and registration accuracy.

### 10. What challenges or open problems remain?

The obvious next problems are in vivo validation, device-to-device reproducibility, fast subject-specific fabrication, integration with neuronavigation workflows, and proof that improved pressure-field realism translates to better neural and clinical outcomes.

### 11. What future work naturally follows?

The most natural next step is to pair this delivery stack with human target-engagement studies, ideally with concurrent imaging or physiology, then move to controlled clinical pilots where the physical targeting advantage can be tested against simpler baselines.

### 12. Why does this matter for cabbageland?

It matters because ultrasound neuromodulation is full of papers that talk about deep precision while hiding the delivery problem under the rug. This paper is useful precisely because it works on the rug. If future intervention design is going to include ultrasound seriously, the targeting physics has to become as explicit as the circuit claim.

### 13. What ideas are steal-worthy?

Treat coupling geometry and wavefront correction as a single optimization problem, not separate engineering chores.

Prefer target-volume coverage metrics over focal-spot aesthetics.

Use subject-specific manufacturable interfaces as part of the intervention definition rather than as optional accessories.

Force methods papers to say what anatomical uncertainty, alignment drift, and tissue-property mismatch do to the delivered field.

### 14. Final decision

Keep and cite selectively. This is not evidence that ultrasound neuromodulation works clinically, but it is a worthwhile methods note because it improves the physical realism of how future ultrasound targeting claims should be judged.
