#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent
WEB_ROOT = ROOT.parent / 'cabbageclaw-neuro-daily-web'
VENV_PYTHON = ROOT.parent / '.venv-piper' / 'bin' / 'python'
VOICE_CACHE_DIR = Path.home() / '.cache' / 'piper-voices'
LEGACY_VOICE_DIR = WEB_ROOT / 'audio' / 'voices'
GENERATED_DIR = WEB_ROOT / 'audio' / 'generated'
SCRIPT_DIR = ROOT / 'audio_scripts'
CONTENT_JSON = WEB_ROOT / 'data' / 'content.json'
VOICE_NAME = 'en_US-hfc_male-medium'
SPEECH_RATE = 0.95
SILENCE_BETWEEN_CHUNKS_SEC = 0.32


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8').replace('\r\n', '\n')


def strip_inline_markup(text: str) -> str:
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = text.replace('**', '').replace('*', '')
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def spokenize_markdown(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_code = False
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not stripped:
            out.append('')
            continue
        if re.match(r'^#{1,6}\s+', stripped):
            content = re.sub(r'^#{1,6}\s+', '', stripped)
            out.append(strip_inline_markup(content))
            out.append('')
            continue
        if re.match(r'^[-*]\s+', stripped):
            content = re.sub(r'^[-*]\s+', '', stripped)
            out.append(strip_inline_markup(content))
            continue
        if re.match(r'^\d+\.\s+', stripped):
            content = re.sub(r'^\d+\.\s+', '', stripped)
            out.append(strip_inline_markup(content))
            continue
        out.append(strip_inline_markup(stripped))
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'\s+\n', '\n', text)
    return text.strip() + '\n'


def voice_urls(voice_name: str) -> tuple[str, str]:
    parts = voice_name.split('-')
    if len(parts) < 3:
        raise ValueError(f'Unexpected Piper voice name: {voice_name}')
    locale = parts[0]
    speaker = parts[1]
    quality = parts[2]
    base = f'https://huggingface.co/rhasspy/piper-voices/resolve/main/en/{locale}/{speaker}/{quality}/{voice_name}.onnx'
    return f'{base}?download=true', f'{base}.json?download=true'


def resolve_voice_files(voice_name: str) -> tuple[Path, Path]:
    VOICE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    model = VOICE_CACHE_DIR / f'{voice_name}.onnx'
    config = VOICE_CACHE_DIR / f'{voice_name}.onnx.json'
    if model.exists() and config.exists():
        return model, config

    legacy_model = LEGACY_VOICE_DIR / f'{voice_name}.onnx'
    legacy_config = LEGACY_VOICE_DIR / f'{voice_name}.onnx.json'
    if legacy_model.exists() and legacy_config.exists():
        model.write_bytes(legacy_model.read_bytes())
        config.write_bytes(legacy_config.read_bytes())
        return model, config

    model_url, config_url = voice_urls(voice_name)
    for url, out in [(model_url, model), (config_url, config)]:
        subprocess.run([
            'python', '-c',
            (
                'import requests,sys; '
                'url=sys.argv[1]; out=sys.argv[2]; '
                'r=requests.get(url,stream=True,timeout=60); r.raise_for_status(); '
                'f=open(out,"wb"); '
                '[f.write(c) for c in r.iter_content(chunk_size=1024*1024) if c]; f.close()'
            ),
            url,
            str(out)
        ], check=True)
    return model, config


@dataclass
class AudioJob:
    source_path: str
    script_path: Path
    audio_path: Path
    label: str


def build_jobs() -> list[AudioJob]:
    jobs: list[AudioJob] = []
    SCRIPT_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    for path in sorted((ROOT / 'daily_papers').glob('*.md')):
        if path.name == '.gitkeep':
            continue
        jobs.append(AudioJob(
            source_path=f'daily_papers/{path.name}',
            script_path=SCRIPT_DIR / f'{path.stem}_digest_audio_script.md',
            audio_path=GENERATED_DIR / f'{path.stem}_digest.wav',
            label='listen',
        ))

    for path in sorted((ROOT / 'paper_notes').glob('*.md')):
        if path.name == '.gitkeep':
            continue
        jobs.append(AudioJob(
            source_path=f'paper_notes/{path.name}',
            script_path=SCRIPT_DIR / f'{path.stem}_audio_script.md',
            audio_path=GENERATED_DIR / f'{path.stem}.wav',
            label='listen',
        ))

    for path in sorted((ROOT / 'related_work').glob('*.md')):
        if path.name == '.gitkeep':
            continue
        jobs.append(AudioJob(
            source_path=f'related_work/{path.name}',
            script_path=SCRIPT_DIR / f'{path.stem}_audio_script.md',
            audio_path=GENERATED_DIR / f'{path.stem}.wav',
            label='listen',
        ))
    return jobs


def write_scripts(jobs: Iterable[AudioJob]) -> None:
    for job in jobs:
        source = ROOT / Path(job.source_path)
        script = spokenize_markdown(read_text(source))
        job.script_path.write_text(script, encoding='utf-8')


def synthesize(jobs: Iterable[AudioJob]) -> None:
    jobs_list = list(jobs)
    voice_model, voice_config = resolve_voice_files(VOICE_NAME)
    script = f'''
import wave
from pathlib import Path
from piper.voice import PiperVoice
from piper.config import SynthesisConfig
voice = PiperVoice.load(r"{voice_model}", r"{voice_config}")
config = SynthesisConfig(length_scale={1/SPEECH_RATE}, noise_scale=0.667, noise_w_scale=0.8)
jobs = {[(str(j.script_path), str(j.audio_path)) for j in jobs_list]!r}
for script_path, out_path in jobs:
    text = Path(script_path).read_text(encoding='utf-8').strip()
    with wave.open(out_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(voice.config.sample_rate)
        first = True
        for chunk in voice.synthesize(text, syn_config=config):
            if not first:
                wav_file.writeframes(b"\\x00\\x00" * int(voice.config.sample_rate * {SILENCE_BETWEEN_CHUNKS_SEC}))
            wav_file.writeframes(chunk.audio_int16_bytes)
            first = False
    print('wrote', out_path)
'''
    subprocess.run([str(VENV_PYTHON), '-c', script], check=True)


def update_content_json(jobs: Iterable[AudioJob]) -> None:
    data = json.loads(CONTENT_JSON.read_text(encoding='utf-8'))
    audio = {}
    for job in jobs:
        audio[job.source_path] = {
            'label': job.label,
            'scriptPath': str(job.script_path.relative_to(ROOT)),
            'audioPath': str(job.audio_path.relative_to(WEB_ROOT)),
            'voice': VOICE_NAME,
            'rate': SPEECH_RATE,
        }
    data['audio'] = audio
    CONTENT_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def main() -> None:
    jobs = build_jobs()
    write_scripts(jobs)
    synthesize(jobs)
    update_content_json(jobs)
    print(f'generated {len(jobs)} audio items')


if __name__ == '__main__':
    main()
