# cabbageclaw-neuro-daily

A curated neuro / psychiatry / neuromodulation research scouting repository for cabbageland.

This repo is not a neuroscience title dump. It exists to track recent work with judgment: selective scouting, sharp notes, transferable mechanisms, clinical relevance when real, and less tolerance for hype than the average med-tech feed.

The point is simple:

- find recent papers worth attention,
- reject weak adjacency,
- extract the mechanism,
- say what is actually novel,
- separate computational substance from clinical theater,
- preserve the useful bits in a repository that reduces future cognitive load.

## What this repo does

On a good day, the workflow:

1. searches recent papers relevant to cabbageland's neuro research taste,
2. filters aggressively,
3. ranks the strongest hits,
4. writes a compact daily digest,
5. creates structured paper notes for papers that actually matter,
6. updates topic-level synthesis notes when patterns emerge,
7. commits and pushes the result when credentials and permissions exist.

The standard is not volume. The standard is judgment.

## What cabbageland tends to care about here

This repository prioritizes papers around:

- neuroscience
- computational neuroscience
- network neuroscience
- psychiatry and computational psychiatry
- adolescent / adolescence neuropsychiatry and development when it intersects intervention, biomarkers, circuit function, or longitudinal risk
- psychedelics and psychedelic-assisted psychiatry / neurobiology
- neuromodulation, including adolescent / developmental neuromodulation when clinically or mechanistically meaningful
- brain stimulation
- invasive stimulation (DBS, VNS, RNS, cortical stimulation, epidural stimulation)
- noninvasive stimulation (TMS, tDCS, tACS, ultrasound, related modalities)
- neuroengineering and closed-loop stimulation systems
- biomarkers for response prediction, state estimation, and adaptive control
- circuit mechanisms and causal perturbation studies
- stereo-EEG and intracranial electrophysiology, including sEEG, iEEG, ECoG, and LFP-guided intervention logic
- inclusive data modalities: behavior, symptoms, clinical scales, EEG/MEG, LFP/ECoG/iEEG/sEEG, fMRI, diffusion/connectomics, physiology, wearables, speech, text, imaging, multimodal longitudinal cohorts, and intervention logs
- inclusive computational methods: statistical modeling, causal inference, dynamical systems, network models, Bayesian modeling, mechanistic modeling, control, optimization, ML, deep learning, generative modeling, representation learning, reinforcement learning, and neurosymbolic or hybrid models
- ML methods that genuinely improve mechanistic understanding, patient stratification, or intervention design

These topics matter most when the paper improves one of the following:

- causal understanding over correlational fog
- mechanism over branding
- adaptive control over one-shot intervention recipes
- explicit state, biomarkers, or circuit models over vague latent storytelling
- clinically meaningful heterogeneity over average-effect sludge
- stronger links across modalities rather than single-modality tunnel vision
- computational breadth when it buys real inference, control, or mechanistic clarity
- transferable abstractions over one-off pipeline hacks

## What this repo refuses to be

This repo is **not**:

- a dump of every neuro-adjacent title,
- a placebo effect fan club,
- an abstract rewriting machine,
- a politeness layer for underpowered clinical studies,
- a decorative AI-for-brains scrapbook,
- a place where p < 0.05 and a shaky subgroup analysis get treated like mechanism.

If nothing good appears on a given day, the correct output is: nothing worth logging.

## Repository structure

### `daily_papers/`
Daily digests with ranking, verdicts, and a one-paragraph synthesis.

### `paper_notes/`
Structured, single-paper notes with explicit verdicts, mechanism analysis, weaknesses, and steal-worthy ideas.

### `related_work/`
Cross-paper synthesis notes organized around real research lenses rather than keyword buckets.

### `reading_queue/`
Optional prioritized reading lists when follow-up is warranted.

## Writing standard

The writing here should be:

- direct
- skeptical
- compact
- high-signal
- concrete
- unembarrassing

It should avoid:

- generic praise
- novelty inflation
- clinical overclaiming
- biomarker mysticism
- citation theater
- pretending correlation is causation

## Operating principle

> optimize for research judgment, not paper throughput.

A good day is not fifteen weak stimulation papers.
A good day is two or three papers that genuinely sharpen future thinking about brain, behavior, intervention, or mechanism.

## Automation note

This repository is designed for recurring updates. The detailed workflow and quality bar live in [`TASK.md`](./TASK.md).

If audio transcripts are generated for digests or notes, they must be written as spoken briefings rather than markdown read aloud: clean spoken prose, strong information flow, no literal markdown artifacts, and slightly slowed delivery by default when the TTS system supports it.

Detailed conversion rules for turning markdown into TTS-friendly spoken scripts live in [`tts_conversion_instructions.md`](./tts_conversion_instructions.md). Treat that file as the default style guide for future digest and note audio-script generation.

## Daily email workflow

The repo includes `neuro_daily_email.py`, which renders and sends the same-day Neuro Daily digest email using Python SMTP instead of Himalaya's send path.

Behavior:

- subject format: `Neuro Daily, [DATE], Reporter: cabbageclaw`
- reads recipients from `recipients.csv` (one email per line)
- keeps `recipients.csv` out of git via `.gitignore`
- derives paper links and note links from the current digest and note files
- sends multipart email with both plain-text and HTML versions
- expects SMTP settings and password command in `~/.config/himalaya/config.toml`

Examples:

```bash
python3 neuro_daily_email.py --date 2026-05-18 --dry-run
python3 neuro_daily_email.py --date 2026-05-18 --preview-path neuro_daily_email_preview.eml
python3 neuro_daily_email.py
```

The intended cron schedule is 7:30 AM local time, sending that day's digest after a quick render sanity check using the generated preview.
