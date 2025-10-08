# Chameleon — Testing Repo

Chameleon is a developer-ready repository implementing a two-phase generative pipeline for
synthesizing study-ready videos of autonomous devices. It supports:
- Phase I: Input trajectory scripting (JSON trajectories)
- Phase II: Compositional prompt generation (structured JSON prompts and composed text prompts)
- Phase III: Video synthesis & refinement stubs (temporal/physical regularizers)
- Phase IV: Instrumentation for interaction studies

This repo is intentionally modular and ready to extend to real generative backends (e.g., Google Veo 3, Runway).

## Quick start
```bash
# (optional) set up environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# generate example trajectory and prompts
python scripts/generate_trajectories.py
python scripts/prompt_composer.py --example data/prompts/example_prompt.json

# simulate refinement (placeholder)
python scripts/simulate_video_refinement.py
```

## Structure
- `scripts/` — utilities and pipeline stubs
- `data/prompts/` — example structured prompts and composed text prompts for generators
- `sections/` — LaTeX sections for paper integration
- `figures/` — placeholder images for the pipeline

## Notes
- The prompt composer creates both a structured JSON prompt and a natural-language composed prompt suitable for passing to diffusion backbones. 
- This repository does not call any proprietary API by default. Integration with specific services (Google Veo 3, DeeVid, Runway) should use their official SDKs and authentication.
