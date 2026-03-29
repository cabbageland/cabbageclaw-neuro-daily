# Optimal Deep Brain Stimulation Locations for Gilles de la Tourette Syndrome

## Basic info

* Title: Optimal Deep Brain Stimulation Locations for Gilles de la Tourette Syndrome
* Authors: I. A. S. and a large multicenter consortium including Konstantin Butenko, Kara A. Johnson, Till Dembek, Michael S. Okun, Christopher R. Butson, Veerle Visser-Vandewalle, and Andreas Horn.
* Year: 2026.
* Venue / source: medRxiv.
* Link: https://www.medrxiv.org/content/10.64898/2026.02.21.26346772v1
* Date surfaced: 2026-03-29.
* Why selected in one sentence: It is a serious cross-target DBS mapping paper that tries to explain Tourette tic improvement through shared structural pathway logic rather than target-specific folklore.

## Quick verdict

* Highly relevant

This is one of the more useful recent targeting papers because it does not pretend one DBS nucleus owns Tourette syndrome. Instead, it pools thalamic, pallidal, and STN cohorts and asks whether response peaks line up along identifiable pallidothalamic and thalamostriatal bundles. The result is not a solved prediction system — only a modest fraction of variance is explained, and the whole study is retrospective — but it does give the field a more mechanistic targeting frame than another single-center sweetspot map.

## One-paragraph overview

The paper tackles a real problem in Tourette DBS: several targets are used clinically, but it remains unclear whether they work through distinct mechanisms or different access points into overlapping circuits. The authors assembled a retrospective multicenter cohort of 115 patients across 12 centers, spanning thalamic, pallidal, and subthalamic DBS, localized electrodes with an imaging pipeline, and applied voxel-wise sweetspot mapping to identify regions associated with tic improvement. Because the resulting response maps visually followed fiber trajectories, they then interpreted them anatomically against specific pallidothalamic and thalamostriatal bundles. Their main claim is that tic-response peaks across the three targets align with a common structural pathway logic, and that this cross-target mapping explains outcomes better than treating each target as an isolated therapy.

## Model definition

This is not a learned predictive model paper in the usual machine-learning sense. It is an imaging-based response-mapping and anatomical interpretation pipeline.

### Inputs
Imaging data for bilateral DBS implants, lead localizations, stimulation locations or overlaps, target labels (thalamus, pallidum, STN), and clinical tic-improvement outcomes across 115 Tourette patients from 12 centers.

### Outputs
Voxel-wise response maps, sweetspot landscapes within each target region, bundle-overlap metrics for candidate structural pathways, and statistical associations between those maps or overlaps and tic improvement.

### Training objective (loss)
There is no trainable model and no explicit optimization loss described in the accessible paper text. The core method is voxel-wise response mapping plus correlation/regression-style explanation of outcome variance.

### Architecture / parameterization
Retrospective DBS imaging pipeline with sweetspot mapping, anatomical fiber delineation, cross-target response-map comparison, and validation in an independent cohort.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Tourette DBS uses multiple targets, but the field lacks a clear targeting logic that explains whether those targets are therapeutically distinct or simply different access points into a shared circuit. Without that logic, target choice remains partly historical and center-specific.

### 2. What is the method?

The authors collected retrospective multicenter DBS outcome and imaging data, mapped stimulation locations across thalamic, pallidal, and STN targets, estimated voxel-wise tic-response landscapes, and then interpreted those landscapes using known pallidothalamic and thalamostriatal fiber anatomy. They also tested whether the resulting maps generalized to an independent cohort.

### 3. What is the method motivation?

If Tourette symptoms improve when stimulation engages a common therapeutic pathway, then target selection should be grounded in that pathway rather than in loyalty to one anatomical nucleus. A cross-target mapping framework is the obvious way to test that idea.

### 4. What data does it use?

A retrospective cohort of 115 bilateral DBS patients with Gilles de la Tourette syndrome across 12 centers worldwide: thalamus (n=43), pallidum (n=56), and subthalamic nucleus (n=16). Median follow-up was 6 months. An additional independent test cohort of 8 patients was used for validation.

### 5. How is it evaluated?

The main evaluation asks whether response maps reveal reproducible tic-improvement peaks, whether outcomes in one target can be explained using maps derived from the other targets, whether stimulation overlap with anatomically plausible bundles explains clinical variance, and whether the mapping transfers to an independent cohort.

### 6. What are the main results?

The paper reports three tic-response peaks in both thalamus and pallidum. Response maps from thalamic and pallidal cohorts were able to explain outcomes in the STN cohort with a reported correlation of R = 0.58 (p = 0.019). Across targets, response landscapes followed the anatomical course of the ansa lenticularis, fasciculus lenticularis, and projections from posterior intralaminar thalamic nuclei to the lentiform nucleus. Bundle overlap explained 19% of variance in tic improvement across targets, and the response maps explained variance in an independent cohort (n = 8, R = 0.70, p = 0.026). OCD-related response maps were less clean and less effective, especially in thalamus.

### 7. What is actually novel?

The novelty is the attempt to unify several Tourette DBS targets into a single pathway-oriented response model. Many DBS papers publish sweetspots; fewer ask whether different targets trace the same therapeutic bundles and then test that logic across cohorts.

### 8. What are the strengths?

First, the cohort is large by Tourette DBS standards and multi-center rather than idiosyncratic.

Second, the paper explicitly addresses cross-target structure, which is much more useful than another local sweetspot map.

Third, the authors try to interpret statistical maps anatomically instead of stopping at colorful voxel blobs.

Fourth, they include an independent test cohort, which the literature badly needs.

### 9. What are the weaknesses, limitations, or red flags?

The study is retrospective, which means target choice, programming practices, imaging quality, and outcome assessment may all vary by site in ways that are hard to fully control.

Explained variance is still limited. Nineteen percent is not nothing, but it is also nowhere near a clinically complete prediction story.

The STN cohort is relatively small.

And the paper is much stronger for tic response than for broader psychiatric symptom dimensions like OCD, which matters if one wants multisymptom DBS claims.

### 10. What challenges or open problems remain?

The main open problem is prospective validation: can these maps actually improve target choice or programming in future patients? It also remains unclear how much of the residual variance reflects symptom heterogeneity, programming heterogeneity, anatomy, comorbidities, or limitations of the imaging model.

### 11. What future work naturally follows?

A prospective targeting or programming study using the fiber-informed maps would be the obvious next step. It would also be useful to test symptom-specific maps for tics versus obsessive-compulsive symptoms versus affective comorbidity, rather than assuming one pathway should optimize everything.

### 12. Why does this matter for cabbageland?

Because this is the kind of paper that makes neuromodulation targeting more legible. It does not solve Tourette DBS, but it pushes the field toward a transferable circuit logic: different targets may be useful because they touch overlapping therapeutic fibers, not because each nucleus has its own isolated magic.

### 13. What ideas are steal-worthy?

One steal-worthy idea is to treat multi-target therapies as different access points into a shared control graph and explicitly test that rather than arguing target identity by tradition.

Another is to force response maps into anatomical interpretation instead of leaving them as uninterpretable statistics.

A third is that symptom dimensions may need separate pathway models; the weaker OCD result is informative, not incidental.

### 14. Final decision

Keep this as a strong targeting reference and a good example of cross-target mechanistic framing. Useful now for thinking, and potentially more useful later if prospective validation appears.
