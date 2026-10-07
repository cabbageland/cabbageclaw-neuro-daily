# Deep learning-based control of electrically evoked activity in human visual cortex

## Basic info

* Title: Deep learning-based control of electrically evoked activity in human visual cortex
* Authors: Pehuen Moure, Jacob Granley, Fabrizio Grani, Leili Soo, Antonio Lozano, Rocio Lopez-Peco, Adrian Villamarin-Ortiz, Cristina Soto-Sanchez, Shih-Chii Liu, Michael Beyeler, Eduardo Fernandez
* Year: 2026
* Venue / source: Neuron
* Link: https://doi.org/10.1016/j.neuron.2026.07.006
* Date surfaced: 2026-10-07
* Why selected in one sentence: It is a rare human bidirectional-implant paper that uses learned models to synthesize stimulation patterns and then tests whether those patterns causally shape recorded cortical activity and percepts.

## Quick verdict

* Highly relevant

This is worth keeping because it makes neural stimulation control concrete: train a forward model from stimulation plus current cortical state to evoked population activity, invert it with either gradient optimization or an inverse network, then deliver the generated patterns back into a human visual cortical implant. It is not psychiatry, and it is one blind participant with a temporary Utah array, so the translation should stay modest. But as a proof of model-driven neural activity shaping in a human implant, it is exactly the kind of control logic that neuromodulation keeps promising and rarely demonstrates.

## One-paragraph overview

The paper studies a 27-year-old blind participant implanted with a 96-channel Utah Electrode Array near early visual cortex as part of a cortical visual prosthesis trial. Across 26 recording days, the authors collected thousands of stimulation-evoked neural responses and percept reports, then trained a deep forward model to predict trial-level changes in multi-unit activity from a stimulation pattern and daily pre-stimulation activity. They then used that model in two inverse-control modes: a gradient optimizer that searches stimulation currents for a target neural response, and a learned inverse network that maps target responses to stimulation patterns fast enough for real-time use. Both learned approaches beat one-to-one, linear, dictionary, and random baselines; optimized patterns required lower currents, better reproduced target neural activity, and produced percept reports closer to the original target-associated percepts. The most transferable lesson is that controllable stimulation targets live on an intrinsic neural manifold; model-driven control works best when it respects that geometry rather than pretending arbitrary electrode patterns can make arbitrary brain states.

## Model definition

### Inputs

The forward model takes a 96-electrode stimulation-current vector and the average pre-stimulation activity for each electrode on a given day. The core neural response target is delta envelope multi-unit activity, computed from 100-200 ms after stimulation offset relative to a -110 to -10 ms baseline. The perception decoders use stimulation parameters, neural responses, pre-stimulation activity, or combinations of those features to predict reported phosphene detection, brightness, and color.

### Outputs

The forward model predicts the 96-channel evoked neural response. The gradient-based inverse controller outputs a stimulation-current pattern optimized for a desired target response. The learned inverse network outputs a stimulation pattern in one forward pass. Perception models output binary detection, color class, or brightness category.

### Training objective (loss)

The forward model is trained with mean squared error between predicted and observed delta MUAe responses. The gradient inverse minimizes the forward-model response error to a target neural response plus L1 regularization on stimulation amplitude. The inverse network is trained through the frozen forward model to minimize target-response reconstruction error plus L1 stimulus regularization. The perception decoders are trained with cross-entropy loss.

### Architecture / parameterization

The forward model is a 10-layer fully connected neural network with dropout, batch normalization, residual connections, and about 1.2 million trainable parameters. It processes stimulation through four fully connected layers, concatenates daily pre-stimulation activity, then uses six more fully connected layers to output 96 response units. The learned inverse model is a fully connected network with three 96-unit hidden layers, residual connections, ReLU activations, dropout, and output scaling to the valid 0-50 microamp stimulation range. The gradient controller freezes the forward model and optimizes the stimulation vector directly with Adam.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Cortical visual prostheses can stimulate cortex, but current systems still rely heavily on manual electrode-by-electrode calibration and crude assumptions about mapping electrodes to percepts. Multi-electrode stimulation produces nonlinear, state-dependent population responses, so simple visuotopic or linear recipes do not scale. The paper asks whether a learned neural response model can synthesize stimulation patterns that produce intended cortical activity and more stable perceptual outcomes.

### 2. What is the method?

The authors collect multi-session human intracortical stimulation and recording data from a Utah array implanted near early visual cortex. They train a forward neural network to predict evoked population activity from stimulation and daily pre-stimulation state. Then they invert that forward model with two control strategies: slower gradient-based optimization for accuracy and a faster inverse neural network for real-time stimulation synthesis. The generated stimulation patterns are delivered in vivo and compared with conventional one-to-one mapping, linear models, dictionary approaches, replayed original stimuli, and random baselines.

### 3. What is the method motivation?

The core motivation is that stimulation parameters are not the right endpoint. The device needs to control neural population activity that is closer to perception than raw electrode currents. If neural responses are nonlinear and vary by day, then a controller should model the current neural state and learn the response surface instead of pretending each electrode has a stable, independent percept.

### 4. What data does it use?

The dataset comes from one blind male volunteer, age 27, with a 96-channel Utah Electrode Array implanted in the right occipital cortex, likely near V1. Data span 26 daily sessions over the six-month implantation period. The stimulation dataset includes 5,818 random multi-electrode patterns, 484 structured patterns, and 2,389 single-electrode threshold/response observations. On 5,515 trials, the participant reported whether a phosphene was perceived; 704 trials include percept descriptions such as shape, color, brightness, and size. The forward model trains on 19 days and evaluates on held-out data from five non-consecutive days.

### 5. How is it evaluated?

Forward prediction is evaluated with MSE, R2, and an adapted Wasserstein earth mover's distance over electrodes, using 54 valid channels with recorded spiking and response variance. Inverse stimulation synthesis is evaluated by delivering generated patterns in vivo and comparing the measured response to natural or synthetic target responses. The paper also compares simulated forward-model predictions with in vivo outcomes and evaluates whether neural activity predicts percept reports better than stimulation parameters alone.

### 6. What are the main results?

The forward neural network predicts held-out evoked responses better than all tested baselines, including linear and idealized dictionary models, supporting the claim that multi-electrode stimulation responses are not simple linear combinations of single-electrode responses. For natural targets, both learned inverse approaches outperform conventional baselines; gradient optimization is most accurate but takes roughly 10-20 seconds per stimulus, while the inverse network is less exact but generates patterns in about 50 microseconds. For synthetic targets, learned methods still beat baselines, but performance degrades when targets are farther from the intrinsic neural response manifold. Ten latent factors explain 95% of the response-manifold variance, while stimulation parameters require 86 factors for the same variance threshold; target distance from this manifold strongly predicts control error. Neural activity also predicts percept reports better than stimulation alone: adding neural activity and pre-stimulus state improves detection accuracy from 74.2% to 88.7%, color from 49.4% to 76.7%, and brightness from 44.8% to 60.9%.

### 7. What is actually novel?

The novelty is not just "deep learning for a prosthesis." The useful novelty is closing the loop around measured human cortical population activity: model the stimulation-response surface, synthesize new stimulation patterns, deliver them back into the implant, and show that the measured neural and perceptual outcomes improve over simpler mappings. The manifold result also matters because it defines a realistic controllability boundary instead of treating the stimulation space as arbitrarily programmable.

### 8. What are the strengths?

The paper uses human intracortical stimulation and recording rather than only simulation or animal data. It evaluates control by actually delivering optimized stimuli in vivo. It includes multiple baselines, including strong dictionary and linear controls. It uses pre-stimulation state to handle day-to-day drift, which is exactly the kind of nuisance that breaks real implants. It also links neural-response control to percept reports instead of stopping at a neural metric.

### 9. What are the weaknesses, limitations, or red flags?

This is a single-participant study, so generalization across people, implants, cortical locations, and etiologies remains open. The implant location could not be verified with fMRI because of metal fragments in the skull. The percept outputs are still simple phosphenes, not rich vision. The forward model overestimates absolute in vivo performance even though it preserves relative method ranking. Synthetic target control is limited by the neural manifold, which is both a useful result and a warning against overclaiming arbitrary neural-state writing. The full detailed read came from the NIH/PMC bioRxiv preprint version plus peer-reviewed PubMed/DOI metadata; the peer-reviewed PMC and Europe PMC article pages were blocked by browser-challenge layers in this run.

### 10. What challenges or open problems remain?

The field still needs replication in more participants and other cortical implants, online adaptation during longer real-world use, stronger perceptual tasks, and safety testing for repeated optimized multi-electrode patterns. A serious controller also needs to handle state drift continuously, not just use average daily pre-stimulation activity. More broadly, stimulation control has to learn feasible target manifolds rather than optimizing toward biologically unreachable patterns.

### 11. What future work naturally follows?

Run the same modeling stack prospectively during real-time prosthetic use, update the controller online from new neural responses, test closed-loop percept optimization directly, and compare manifold-aware targets against naive pixel-to-electrode mappings. Outside visual cortex, the same recipe should be tested in bidirectional DBS, sensory cortex, motor cortex, and epilepsy or psychiatric implants where neural activity is both recorded and stimulated.

### 12. Why does this matter for cabbageland?

It gives cabbageland a clean example of intervention logic that is actually executable: stimulation should be optimized against a measured neural state, constrained by the system's reachable manifold, and validated by downstream percept or behavior. That is much better than saying "personalized stimulation" while only changing a contact or frequency by hand.

### 13. What ideas are steal-worthy?

Use a learned forward model as the simulator, then invert it for stimulation design. Include current brain state as an input because the same stimulation pattern does not mean the same thing every day. Treat reachable neural manifolds as controllability constraints, not as inconvenient noise. Separate the accurate but slow optimizer from the fast inverse network, because deployed controllers may need both an offline planner and an online policy. Most importantly, require the model to predict something closer to experience or behavior than electrode current.

### 14. Final decision

Keep. It is not a psychiatry paper and not a general solution to brain control, but it is a strong human neuroengineering paper. It earns preservation because it turns bidirectional stimulation into a model-based control problem and tests the loop in vivo.
