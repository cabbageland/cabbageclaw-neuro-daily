# Low-latency neuromorphic closed-loop control of hippocampal ripples in vivo

## Basic info

* Title: Low-latency neuromorphic closed-loop control of hippocampal ripples in vivo
* Authors: Pedro Felix, Maria-Teresa Jurado-Parras, Joel Freitas, Joao Ventura, Liset M. de la Prida, Paulo Aguiar
* Year: 2026
* Venue / source: bioRxiv preprint
* Link: https://www.biorxiv.org/content/10.64898/2026.07.09.737518v1
* Date surfaced: 2026-07-19
* Why selected in one sentence: It is one of the clearest recent proofs that low-latency neuromorphic closed-loop control can survive the full sensing-processing-stimulation stack in vivo instead of winning only in offline benchmark theater.

## Quick verdict

* Highly relevant

This is a real keep because it clears a harder bar than most closed-loop neuromodulation papers clear. The main contribution is not a prettier classifier. The main contribution is that the authors actually push a compact spiking detector through live acquisition, neuromorphic inference, feedback triggering, and in-vivo intervention, then measure where the loop succeeds and where it still breaks. The main caveat is just as important: the best classical tuned detector still beats the spiking net offline, and the in-vivo manipulation result remains small-animal, optogenetic, and latency-fragile.

## One-paragraph overview

The paper builds a compact spiking neural network for detecting hippocampal sharp-wave ripples from ripple-band local field potentials, deploys it on SpiNNaker neuromorphic hardware, and integrates it with Open Ephys for real-time closed-loop intervention. Hippocampal signals are converted into sparse UP and DN spike trains with asynchronous delta modulation, then fed into a 41-neuron, 530-parameter feed-forward network trained to emit ripple detections. In offline detection across twenty-three recording sessions from five mice, the model performs competitively with larger deep-learning baselines but not better than a carefully optimized classical Buzsaki-style detector. The useful step is what comes next: the authors quantify deployment loss, power use, and end-to-end latency, then use the full loop to trigger optogenetic inhibition in awake head-fixed mice. That makes the paper much more valuable as an end-to-end control-and-hardware note than as a simple detector paper.

## Model definition

### Inputs
Ripple-band CA1 local field potentials are bandpass filtered to 100 to 250 hertz, converted into sparse UP and DN spike trains with asynchronous delta modulation, downsampled to a 1 millisecond timestep, and segmented into overlapping windows aligned to manually annotated ripple events. In online operation, those spike streams arrive through the Open Ephys acquisition and bridge stack and are affected by buffer size and detector firing-threshold settings.

### Outputs
The network emits spikes from a single output neuron that act as ripple detections. In the deployed loop, those detections trigger downstream feedback events through Open Ephys and an Arduino-controlled optogenetic stimulation path. At the system level, the model therefore outputs both event detections and stimulation triggers.

### Training objective (loss)
The training objective minimizes a time-to-first-spike mean square error loss with a 20 millisecond tolerance window. The authors also add explicit penalties for false positives and false negatives and adjust those penalties during training. Optimization uses Adam with a StepLR schedule; the accessible full text reports the loss clearly enough to avoid bluffing here.

### Architecture / parameterization
The detector is a compact feed-forward spiking neural network with two input channels corresponding to UP and DN events, two hidden layers of leaky integrate-and-fire neurons with 24 and 16 units, and a single output neuron. The total model has 41 neurons and 530 trainable parameters and is trained with surrogate-gradient backpropagation through time. For deployment, the network is ported to SpiNNaker and embedded in an Open Ephys based closed-loop stack.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to solve a real bottleneck in closed-loop neuromodulation: fast transient brain events are only useful control targets if the sensing, processing, and stimulation stack is fast and cheap enough to intervene before the event has already ended.

### 2. What is the method?
The method has four stages. First, hippocampal local field potentials are spike-encoded into sparse UP and DN event streams. Second, a compact spiking neural network is trained to detect ripples from those streams. Third, the trained network is benchmarked against classical and deep-learning ripple detectors and then deployed on SpiNNaker hardware integrated with Open Ephys. Fourth, the deployed system is tested in hardware-in-the-loop latency experiments and in awake head-fixed mice where detections trigger optogenetic inhibition.

### 3. What is the method motivation?
The motivation is that many high-performing neural decoders still assume abundant compute, telemetry, and offline tuning. That is bad for fast closed loops. If the target event lasts only tens of milliseconds, then controller architecture, buffer size, bridge overhead, and feedback path matter as much as the detector’s raw offline score.

### 4. What data does it use?
For detection benchmarking, the paper uses twenty-three recording sessions from five mice, comprising 2719 manually annotated ripple events. For the in-vivo intervention experiments, it uses twelve sessions, four light-off and eight light-on, from two awake head-fixed mice, totaling 1699 post-hoc ripple events. The signals come from CA1 hippocampal recordings acquired through the Open Ephys stack.

### 5. How is it evaluated?
The paper evaluates the model at several levels. It measures precision, recall, and F1-score across sessions. It compares the SNN with filter-based and deep-learning detectors. It measures the performance drop from software training to neuromorphic deployment and from offline to online processing. It quantifies CPU, GPU, and SpiNNaker power use. It measures end-to-end closed-loop latency under different buffer and triggering paths. Finally, it tests whether neuromorphic-triggered optogenetic feedback changes ripple dynamics in vivo.

### 6. What are the main results?
- Across twenty-three sessions, the SNN reaches median recall of 0.89, median precision of 0.50, and median F1-score of 0.56.
- The best-performing SNN reaches median F1-score of 0.61, significantly outperforming RippleNet and the LSTM baseline while remaining statistically comparable to the 1D-CNN.
- A carefully optimized classical Buzsaki-style RMS detector still achieves the highest absolute offline performance, with median F1-score of 0.70, which is an important reality check.
- SpiNNaker deployment preserves useful performance while enabling real-time processing with about 3.6 watts total board power and about 0.35 watts attributed to simulation, corresponding to an estimated 16 or 20-fold to 170 or 200-fold power reduction relative to CPU and GPU baselines depending on how the accounting is done.
- In the optimized hardware-in-the-loop configuration, median closed-loop latency is about 50 milliseconds, enabling stimulation before ripple termination in up to 80 percent of events.
- In the preliminary in-vivo optogenetic configuration, latency is worse, median 76.47 milliseconds, and only 13.7 percent of ripples are stimulated before termination, but the longest detected ripples still show significantly lower ripple energy under light-on sessions, with p = 0.048 and Cliff's delta of 0.75.

### 7. What is actually novel?
The novelty is not that an SNN can classify neural events. The novelty is that the paper treats end-to-end loop feasibility as the object of study and actually validates a complete neuromorphic sensing-processing-feedback stack in vivo for brief high-frequency events. That is much rarer, and much more useful, than another offline decoder benchmark.

### 8. What are the strengths?
- The paper keeps the whole loop in view instead of hiding behind offline detection metrics.
- It benchmarks against strong conventional and deep-learning baselines rather than easy straw men.
- It is unusually honest that the optimized classical detector still wins the offline score race.
- The model is genuinely compact and hardware-compatible rather than "edge" in branding only.
- It measures the difference between software success, hardware deployment success, and real intervention success instead of collapsing them into one headline.

### 9. What are the weaknesses, limitations, or red flags?
- The SNN is not the best offline detector once the classical baseline is tuned carefully.
- Precision is only moderate, which means false detections remain a real stimulation-specificity problem.
- The in-vivo intervention work is still based on awake head-fixed mice, optogenetic inhibition, and only two animals.
- The strongest intervention result comes from analyzing the longest quarter of detected ripples after a preliminary high-latency configuration, which is useful but not a clean finished causal story.
- SpiNNaker plus host computer plus Open Ephys is a serious hardware testbed, but not yet a clinically realistic implant architecture.

### 10. What challenges or open problems remain?
The next hard step is translation from ripple control in mice to clinically meaningful biomarkers and actuators. The field still needs better specificity, more implant-realistic hardware stacks, non-optogenetic intervention paths, stronger robustness across recordings and subjects, and proof that low-latency control can improve symptom-relevant outcomes rather than only alter event statistics.

### 11. What future work naturally follows?
Push the architecture toward more implantable hardware, prune or distill the detector further, compare against stronger low-power non-neuromorphic embedded baselines, and test similar end-to-end loops on biomarkers that matter for epilepsy, movement disorders, or psychiatric neuromodulation. Another clear extension is moving from event detection alone toward adaptive policy learning that decides not just when to stimulate, but how.

### 12. Why does this matter for cabbageland?
Because it forces a cleaner standard for closed-loop neuromodulation. A loop is not serious because it has a learned detector. It is serious if the controller survives the real hardware path with enough timing slack to intervene during the relevant state. This paper gives a good template for that standard.

### 13. What ideas are steal-worthy?
- Judge closed-loop papers on end-to-end latency and deployment loss, not just offline accuracy.
- Keep tuned classical baselines in the benchmark so the hardware story does not hide behind soft comparisons.
- Treat buffer settings and feedback-path engineering as part of the scientific result, not just implementation debris.
- Use compact spike-based models when the real objective is timing and energy, not leaderboard aesthetics.
- Separate the software-to-hardware gap from the hardware-to-intervention gap, because they reveal different bottlenecks.

### 14. Final decision
Keep. This is one of the better recent neuromodulation methods papers because it makes the control loop real enough to fail in informative ways, and then measures those failures instead of pretending they do not exist. Preserve it as a methods and control anchor, not as a proof that hippocampal ripple neuromodulation is already clinically solved.
