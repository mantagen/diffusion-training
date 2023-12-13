import os
from diffusers import StableDiffusionPipeline

import argparse

parser = argparse.ArgumentParser(description='Prompt.')
parser.add_argument('--prompt', type=str, help='Prompt', required=False)
parser.add_argument('--subject', type=str, help='Prompt', required=True)
parser.add_argument('--model', type=str, help='Prompt', required=True)
args = parser.parse_args()

if args.prompt:
    prompt = args.prompt
else:
    subject = args.subject
    prompt = f"portrait of {subject}, sun shining, photo realistic illustration by greg rutkowski, thomas kindkade, alphonse mucha, loish, norman rockwell."

model_id = args.model

device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, use_safetensors=True)
pipe = pipe.to(device)

image = pipe(prompt).images[0]

# makedir if not exists inferred/model_id ..
os.makedirs(f"inferred/{model_id}", exist_ok=True)

image.save(f"inferred/{model_id}/{prompt}.png")
