# Implant-Friendly MRI of Deep Brain Stimulation Patients at 3T

## Basic info

* Title: Implant-friendly MRI of deep brain stimulation patients at 3T
* Authors: Nur Izzati Huda Zulkarnain, Sadeghi-Tarakameh, Thotland, Harel, Yigitcan Eryaman
* Year: 2026.
* Venue / source: NeuroImage.
* Link: https://pubmed.ncbi.nlm.nih.gov/41862107/
* Date surfaced: 2026-04-11.
* Why selected in one sentence: It tackles an unglamorous but decisive neuroengineering constraint by showing a practical workflow for reducing RF-induced heating and artifact in 3T MRI of DBS patients.

## Quick verdict

* Useful

This is not a breakthrough targeting paper, but it is worth preserving because platform constraints quietly determine what mechanistic DBS science is possible. The authors extend implant-friendly optimization from unilateral to bilateral DBS configurations and show a streamlined workflow with phantom validation plus three patient demonstrations. The sample is tiny, so the right read is “credible enabling method,” not “DBS MRI safety solved.”

## One-paragraph overview

The paper addresses the safety and image-quality problems that make MRI difficult in patients with implanted deep brain stimulation hardware. The authors extend a previously described current-mitigation strategy to bilateral DBS leads and optimize an implant-friendly mode that aims to reduce RF-induced current on both electrodes while preserving usable B1 performance. They validate the approach in a head phantom and then demonstrate an on-console workflow in three DBS patients. According to the abstract, the unilateral configuration fully mitigated induced current, the bilateral configuration reduced current by up to seventy-four percent relative to circularly polarized excitation, artifact was reduced, and the active pre-scan workflow stayed under six minutes. The important claim is practical: safer and lower-friction imaging could make longitudinal DBS physiology and targeting studies more feasible.

## Model definition

This paper does not present a trainable predictive model. It presents an optimization and workflow method for MRI acquisition in DBS patients.

### Inputs
DBS implant configuration information, two-transmit-channel MRI setup, current-analysis measurements derived from imaging artifact, and phantom or patient imaging data.

### Outputs
Electrode-specific or bilateral implant-friendly excitation modes intended to reduce RF-induced current and artifact while maintaining imaging performance.

### Training objective (loss)
There is no learnable training loss in the accessible abstract text. The optimization target is to reduce RF-induced currents on electrodes while maximizing overall B1 performance.

### Architecture / parameterization
A practical acquisition-optimization workflow for MRI transmit settings in unilateral and bilateral DBS implant configurations.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

MRI in DBS patients is valuable for research and clinical follow-up, but implanted hardware creates serious RF-heating risks and image artifacts. Those constraints sharply limit what imaging can be done and how often.

### 2. What is the method?

The authors optimize an implant-friendly transmit mode designed to reduce induced current on DBS leads, validate it in a phantom, and then apply the workflow to unilateral and bilateral DBS patients while comparing it against circularly polarized excitation.

### 3. What is the method motivation?

If DBS imaging remains dangerous or cumbersome, a lot of mechanistic questions stay unanswerable. A practical workflow that reduces current and artifact without heavy external hardware could widen what is feasible in implanted cohorts.

### 4. What data does it use?

An anthropomorphic head phantom and three DBS patients, including one bilateral and two unilateral implant cases.

### 5. How is it evaluated?

The paper evaluates heating-reduction capability, induced-current mitigation, artifact reduction, imaging workflow duration, and practical console-based usability.

### 6. What are the main results?

The phantom study confirmed heating-reduction capability. In patient and phantom testing, artifact reduction was observed. In the unilateral case, induced current was fully mitigated, and in the bilateral case it was reduced by up to seventy-four percent relative to circularly polarized excitation. The pre-scan protocol took less than six minutes of active scan time and required minimal external hardware.

### 7. What is actually novel?

The interesting part is the move from a single-electrode setting toward bilateral DBS configurations with a workflow that looks practical rather than purely bespoke. That matters because bilateral implants are common in many therapeutic settings.

### 8. What are the strengths?

It addresses a real operational bottleneck instead of aesthetic MRI-methods work detached from use.

The combination of phantom validation and patient demonstration is appropriate for an enabling paper.

The on-console, minimal-hardware framing improves the odds of real adoption if the method holds up.

### 9. What are the weaknesses, limitations, or red flags?

The patient sample is extremely small.

The abstract-level read does not reveal how broadly the method generalizes across implant vendors, lead trajectories, pulse generators, and MRI sequences.

Even a strong current-reduction result does not automatically resolve every safety or workflow issue in real clinical environments.

### 10. What challenges or open problems remain?

The next challenge is broader validation across hardware configurations and imaging protocols. Another is whether the workflow can be standardized enough for wider deployment without specialist oversight.

### 11. What future work naturally follows?

Larger multi-configuration validation is the obvious next step. It would also be useful to connect this safety workflow to actual functional or longitudinal imaging use cases that matter for DBS programming and mechanism research.

### 12. Why does this matter for cabbageland?

Because precision neuromodulation is not only about targets and biomarkers. It is also about whether the platform can support repeated safe measurement. If DBS patients cannot be imaged well, a lot of personalization talk stays speculative. This kind of enabling method is part of the real stack.

### 13. What ideas are steal-worthy?

One steal-worthy idea is to treat imaging safety optimization as part of the intervention pipeline, not as an external constraint.

Another is that artifact-derived current analysis can become an operational signal rather than just an engineering curiosity.

A third is practical: methods that stay on-console and avoid bespoke external hardware have a much better chance of becoming real infrastructure.

### 14. Final decision

Keep as a methods and infrastructure note. Important enabling work, but still early and narrowly demonstrated.
