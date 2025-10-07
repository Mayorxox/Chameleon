#!/usr/bin/env python3
"""Compose structured prompts (JSON -> composed text) suitable for multimodal diffusion APIs.
Example usage:
  python scripts/prompt_composer.py --example data/prompts/example_prompt.json
"""
import json, argparse, os, textwrap

def compose_text_prompt(struct):
    env = struct.get('environment', {})
    dev = struct.get('device', {})
    beh = struct.get('behavior', {})
    parts = []
    parts.append(f"Scene: {env.get('scene','urban street corner')}")
    parts.append(f"Backdrop: {env.get('backdrop','sidewalk with buildings')}")
    parts.append(f"Device: {dev.get('platform','4-wheeled ground robot')} - {dev.get('function','monitoring')}")
    parts.append(f"Dimensions: {dev.get('dimensions','0.5m x 0.43m x 0.51m')}")
    parts.append(f"Behavior: maintains ~{beh.get('proxemic_distance','1.5m')} proxemic buffer; speed {beh.get('speed','1.2 m/s')}; trajectory {beh.get('trajectory','smooth along sidewalk edge')}")
    parts.append("Camera: fixed frontal viewpoint, 30fps, 15s duration.")
    parts.append("Style: photorealistic, natural lighting, slight motion blur for realism.")
    return '\\n'.join(parts)

def compose_prompt_vector(struct):
    Pvec = {
        'conditioning_image': struct.get('environment',{}).get('conditioning_image','figures/sample_frame.png'),
        'text_prompt': compose_text_prompt(struct),
        'motion_spec': {
            'duration_s': struct.get('behavior',{}).get('duration',15),
            'fps': struct.get('behavior',{}).get('fps',15)
        }
    }
    return Pvec

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', type=str, default='data/prompts/example_prompt.json')
    args = parser.parse_args()
    with open(args.example,'r') as f:
        struct = json.load(f)
    Pvec = compose_prompt_vector(struct)
    os.makedirs('data/prompts', exist_ok=True)
    with open('data/prompts/composed_prompt_veo3.json','w') as f:
        json.dump(Pvec,f,indent=2)
    with open('data/prompts/composed_prompt_veo3.txt','w') as f:
        f.write(Pvec['text_prompt'])
    print('Wrote data/prompts/composed_prompt_veo3.json and .txt')
