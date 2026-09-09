# Cholinergic-dependent dopamine signals in mouse dorsomedial striatum are regulated by frontal but not sensory cortices

## Basic info

* Title: Cholinergic-dependent dopamine signals in mouse dorsomedial striatum are regulated by frontal but not sensory cortices
* Authors: Hannah C. Goldbach, Rachele Rimondini, Evan S. Swanson, Jung Hoon Shin, Michael E. Authement, Lucy G. Anderson, Han Bin Kwon, Ron Paletzki, Charles R. Gerfen, Linda M. Amarante, Richard J. Krauzlis, Veronica A. Alvarez
* Year: 2026
* Venue / source: Nature Communications
* Link: https://doi.org/10.1038/s41467-026-77168-x
* Date surfaced: 2026-09-09
* Why selected in one sentence: It cleanly separates frontal corticostriatal control of local dopamine release from generic sensory input to the striatum.

## Quick verdict

* Highly relevant

This is a keeper because it makes dopamine release less cartoonish. The paper shows that salient visual cues can evoke dopamine in the dorsomedial striatum partly through a local cholinergic interneuron mechanism, but the cortical pathway that can drive that mechanism is frontal, especially prelimbic/anterior cingulate input, not primary sensory cortex. The direct clinical translation is limited, but the circuit logic is exactly the kind of causal decomposition that psychiatric stimulation and computational psychiatry usually need and rarely have.

## One-paragraph overview

The paper asks how sensory events gain access to striatal dopamine signals. Using in vivo fiber photometry, cell-type-specific calcium and acetylcholine sensors, retrograde rabies tracing, ex vivo electrophysiology, fast-scan cyclic voltammetry, optogenetic stimulation, and nicotinic receptor blockade, the authors show that visual stimuli recruit a striatal cholinergic mechanism that contributes to dopamine release in anterior dorsomedial striatum. The key anatomical and functional distinction is that frontal cortical inputs, including prelimbic and anterior cingulate cortex, strongly connect to and recruit striatal cholinergic interneurons, while primary visual and auditory cortices mostly target medium spiny neurons and fail to drive cholinergic-dependent dopamine release. For cabbageland, the useful move is decomposing a "sensory dopamine response" into a gated corticostriatal microcircuit: sensory salience is not enough; the right frontal route has to recruit the local cholinergic gate.

## Model definition

This is not a learned predictive-model paper. It is a causal circuit and systems-neuroscience paper built around anatomical tracing, optical recording, optogenetic perturbation, pharmacology, and slice physiology.

### Inputs
Visual or auditory sensory cues; optogenetic stimulation of prelimbic/anterior cingulate, visual, auditory, or somatosensory corticostriatal terminals; pharmacological blockade with mecamylamine; genetically encoded dopamine, calcium, and acetylcholine sensor signals; rabies tracing of inputs to striatal cholinergic interneurons; and whole-cell electrophysiology from striatal cell types.

### Outputs
Dopamine transients in dorsomedial striatum, midbrain dopamine-neuron somatic calcium responses, cholinergic interneuron calcium responses, local acetylcholine release, excitatory postsynaptic currents in cholinergic interneurons and medium spiny neurons, anatomical counts of cortical input sources, and blocker-sensitive fractions of evoked dopamine responses.

### Training objective (loss)
There is no machine-learning loss. The analytic objective is to test whether sensory and frontal corticostriatal pathways differentially recruit striatal cholinergic interneurons and whether that recruitment causally contributes to dopamine release.

### Architecture / parameterization
A multi-assay causal circuit design: in vivo fiber photometry with dopamine, calcium, and acetylcholine sensors; ChAT-Cre-based cell targeting; monosynaptic rabies tracing; ex vivo optogenetic stimulation with electrophysiology and fast-scan cyclic voltammetry; and pharmacological nicotinic receptor blockade.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It asks which circuit routes allow sensory events to shape dopamine release in dorsomedial striatum. The deeper problem is that striatal dopamine is often treated as if midbrain dopamine-neuron firing or generic sensory input explains the whole signal, while local acetylcholine-dependent axonal regulation can reshape dopamine release inside the striatum.

### 2. What is the method?
The authors combine in vivo optical recordings from dopamine neurons and striatal dopamine sensors with calcium and acetylcholine measurements in striatal cholinergic interneurons. They then use nicotinic receptor blockade, monosynaptic rabies tracing, slice electrophysiology, optogenetic activation of selected cortical terminals, and fast-scan cyclic voltammetry to test which cortical inputs actually recruit cholinergic interneurons and drive dopamine.

### 3. What is the method motivation?
If sensory cortex directly drove the cholinergic gate, then sensory input could locally control dopamine timing in striatum. If frontal cortex is the privileged driver, then striatal dopamine responses to sensory events are not simply sensory relays; they are filtered through frontal associative circuitry that may carry salience, task context, or learned relevance.

### 4. What data does it use?
The full text reports mouse data across several cohorts. Fiber photometry experiments used animals expressing dopamine sensors, dopamine-neuron calcium sensors, cholinergic interneuron calcium sensors, or acetylcholine sensors in dorsomedial striatum or midbrain. Slice physiology used 47 mice, rabies tracing used 12 ChAT-IRES-Cre mice, and the photometry methods list 63 animals across dopamine, calcium, and acetylcholine recording configurations. The experiments include both male and female mice.

### 5. How is it evaluated?
The paper evaluates whether visual and auditory stimuli evoke dopamine, acetylcholine, and cell-type-specific calcium responses; whether systemic or local mecamylamine reduces dopamine without blocking upstream sensory responses; whether candidate cortical areas anatomically synapse onto striatal cholinergic interneurons; whether those inputs are functionally strong in slice recordings; and whether optogenetic stimulation of frontal corticostriatal terminals can evoke acetylcholine-dependent dopamine in vivo.

### 6. What are the main results?
Visual stimuli evoked dopamine in dorsomedial striatum, and systemic mecamylamine reduced the visual-evoked dopamine response to about 41 +/- 4.8% of baseline while sparing somatic dopamine-neuron calcium responses. Visual stimuli also recruited striatal cholinergic interneurons and local acetylcholine release. Rabies tracing showed strong anterior cingulate input to dorsomedial-striatal cholinergic interneurons, with sparse visual and auditory cortical input. Slice electrophysiology confirmed the asymmetry: anterior cingulate and prelimbic inputs produced large excitatory currents in cholinergic interneurons, while visual and auditory inputs were weak or absent there despite reliable input to medium spiny neurons. Finally, optogenetic stimulation of prelimbic/anterior cingulate terminals in dorsomedial striatum evoked acetylcholine and dopamine responses, and local mecamylamine reduced the optogenetically evoked dopamine response to about 38-39% across stimulation levels.

### 7. What is actually novel?
The novelty is the circuit decomposition. The paper does not merely say sensory cues evoke dopamine or that acetylcholine modulates dopamine. It identifies a route by which frontal corticostriatal inputs, but not primary sensory inputs to the same striatal region, can recruit cholinergic interneurons and trigger local dopamine release.

### 8. What are the strengths?
The design triangulates the claim with multiple assays instead of leaning on one readout. It separates upstream sensory detection from local dopamine release by showing that nicotinic blockade reduces dopamine while leaving several upstream responses intact. It uses anatomical tracing and functional physiology to test whether cortical projections that reach the same striatal territory target the same interneuron gate. The in vivo optogenetic terminal stimulation is especially useful because it tests whether the frontal pathway can drive the proposed mechanism in the intact animal.

### 9. What are the weaknesses, limitations, or red flags?
The study is in mice and uses head-fixed sensory cue paradigms, so the behavioral meaning of the dopamine signals remains narrower than a full learning or decision task. Optogenetic stimulation of corticostriatal terminals can activate passing axons or collaterals, and the authors explicitly note that prelimbic/anterior cingulate projections also collateralize to midbrain dopamine regions. Sensor kinetics differ across dopamine, calcium, and acetylcholine measurements, making fine timing comparisons cautious. The study also does not yet show how this circuit changes with learning, compulsive behavior, psychiatric disease models, or chronic stimulation.

### 10. What challenges or open problems remain?
The main open problem is linking this microcircuit to behavior across learning, not just to cue-evoked physiology. The field still needs to know when frontal recruitment of cholinergic interneurons is necessary for reinforcement learning, how it interacts with midbrain-originated dopamine signals, whether it changes in disease-relevant states, and whether stimulation protocols can selectively bias this frontal-CIN-dopamine route without producing broad nonspecific effects.

### 11. What future work naturally follows?
Pair this circuit assay with reward learning, avoidance, habit formation, and compulsivity tasks; record dopamine and acetylcholine while manipulating frontal inputs during learning rather than passive cue exposure; compare disease or stress models; and test whether DBS-like or TMS-like perturbations of frontal-striatal loops preferentially recruit this cholinergic dopamine gate.

### 12. Why does this matter for cabbageland?
Cabbageland cares about interventions that change circuit state, not target names painted over mush. This paper gives a concrete example of why "stimulating striatum" or "modulating dopamine" is too blunt. The same striatal region can receive sensory cortical input that reaches medium spiny neurons but fails to recruit the cholinergic dopamine gate; frontal input can recruit that gate and reshape dopamine release. That is the level of decomposition psychiatric stimulation should aspire to.

### 13. What ideas are steal-worthy?
Separate anatomical projection from functional gate access: reaching a region is not the same thing as recruiting the mechanism that matters. Treat local neuromodulator release as a circuit computation rather than a global broadcast. Use receptor blockade to distinguish upstream sensory drive from downstream dopamine release. For stimulation design, ask which axons and interneuron gates are recruited, not just which atlas coordinate is near the electrode or coil field.

### 14. Final decision
Preserve. This is a strong causal circuit note, not a clinical neuromodulation result, but it sharpens the language of dopamine, corticostriatal control, and stimulation mechanism. It belongs in the archive as a reminder that the useful intervention unit is often a gated microcircuit, not an anatomical noun.
