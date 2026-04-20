# An Implantable Wireless Battery-Free Selective Vagus Nerve Stimulator

## Basic info

* Title: An Implantable Wireless Battery-Free Selective Vagus Nerve Stimulator
* Authors: Edvards Rutkovskis, Enrico Ravagli, Henry Lancashire, Ahmad Shah Idil, Nicole Thompson, Justin Perkins, Ronald Challita, Joseph Hadaya, Umesh Vivekananda, Olujimi A. Ajijola, Kalyanam Shivkumar, Anna Miserocchi, Andy McEvoy, David Holder, Kirill Aristovich
* Year: 2026
* Venue / source: bioRxiv
* Link: https://www.biorxiv.org/content/10.64898/2026.04.10.717669v1
* Date surfaced: 2026-04-20
* Why selected in one sentence: It tackles the real VNS bottleneck of off-target activation by building a lighter selective interface instead of pretending whole-nerve stimulation is already precise enough.

## Quick verdict

* Highly relevant

This is early, but it is pointed at the right problem. Most VNS rhetoric hand-waves selectivity while accepting cough, hoarseness, and other off-target effects as unavoidable. This paper is still a platform demonstration, not a therapy trial, but it shows physiologic separation of vagal subfunctions in large animals and an initial human pilot, which is more useful than generic claims about bioelectronic promise.

## One-paragraph overview

The paper presents a temporary implantable selective vagus nerve stimulation device that is wirelessly powered, battery-free, NFC-controlled, and built from off-the-shelf components. The core idea is geometric selectivity across vagal regions rather than indiscriminate cuff stimulation. In a porcine study and a single human pilot, the authors report selective modulation of cardiac and laryngeal effects, including bradycardia without the same pattern of off-target activation across channels. The concept is strongest as an interface and targeting advance. It does not yet establish chronic usability or disease-specific therapeutic benefit.

## Model definition

The paper is primarily a neuroengineering device study rather than a learnable-model paper.

### Inputs
Multichannel stimulation delivered to different geometric regions of the vagus nerve using a temporary battery-free implant, with NFC control and wireless power.

### Outputs
Physiological responses associated with different vagal subfunctions, including bradycardia and laryngeal activation patterns, used to assess selectivity.

### Training objective (loss)
No trainable optimization objective is described in the accessible abstract.

### Architecture / parameterization
A wirelessly powered, battery-free, multichannel selective vagus nerve stimulation implant using off-the-shelf components for short-term implantation.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Conventional VNS often activates unwanted fibers, limiting dosing and reducing tolerability. The paper aims to improve selectivity so stimulation can target useful vagal functions with fewer side effects.

### 2. What is the method?
Build a temporary multichannel implantable VNS device with wireless power and NFC control, then test whether different stimulation sites preferentially recruit different physiological outputs in pigs and a pilot human case.

### 3. What is the method motivation?
If VNS can separate relevant fascicles or functional territories, it could reduce side effects and make the modality more usable across cardiac, inflammatory, psychiatric, and neurological applications.

### 4. What data does it use?
A porcine study with four animals and a single human pilot experiment.

### 5. How is it evaluated?
By measuring whether different stimulation channels produce separable physiological effects, especially cardiac and laryngeal responses.

### 6. What are the main results?
The authors report selective bradycardia of about twenty-three percent on average in pigs and seven and a half percent in the human participant. They also report separation between cardiac efferent, cardiac afferent, and laryngeal activity, suggesting functionally distinct vagal recruitment.

### 7. What is actually novel?
The novelty is the combination of selectivity, wireless battery-free operation, and early in-vivo testing, including an initial human demonstration.

### 8. What are the strengths?
- Targets the real problem of fascicle selectivity rather than just miniaturization.
- Uses a clinically legible physiological readout instead of only benchtop characterization.
- Includes a large-animal study and a first human pilot.
- Battery-free wireless architecture is appealing for temporary or lower-burden use cases.

### 9. What are the weaknesses, limitations, or red flags?
- The human evidence is only n equals one.
- The device is described as suitable for short-term implantation, so chronic stability is unresolved.
- The accessible abstract does not detail long-term safety, electrode reliability, or real-world implantation workflow.
- Physiological selectivity is not the same thing as disease-specific therapeutic efficacy.

### 10. What challenges or open problems remain?
Chronic encapsulation and reliability, scaling to repeatable human use, mapping fascicle-function anatomy across people, and proving that selectivity actually improves efficacy-to-side-effect tradeoffs in disease populations.

### 11. What future work naturally follows?
Longer-duration animal studies, larger human feasibility cohorts, disease-specific trials, and integration of selectivity maps with imaging or physiological feedback.

### 12. Why does this matter for cabbageland?
Because it treats interface precision as the intervention problem. If neuromodulation hardware cannot separate useful from harmful recruitment, then later personalization claims are partly theater.

### 13. What ideas are steal-worthy?
- Build stimulation interfaces around functional selectivity first.
- Use lightweight temporary implants to de-risk selective neuromodulation concepts before chronic productization.
- Evaluate devices with organ-level and side-effect-relevant physiology, not just electrical performance.

### 14. Final decision
Keep as an important neuroengineering platform note. Early, but pointed at a problem that actually matters.
