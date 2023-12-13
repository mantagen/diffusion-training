#!/bin/bash

# parse params
while [[ "$#" > 0 ]]; do case $1 in
  -d|--data_dir) DATA_DIR="$2"; shift;shift;;
  -m|--model) MODEL="$2"; shift;shift;;
  -o|--output) OUTPUT="$2"; shift;shift;;
  -s|--subject) SUBJECT=1;shift;;
  *) usage "Unknown parameter passed: $1"; shift; shift;;
esac; done

accelerate launch diffusers/examples/dreambooth/train_dreambooth.py \
  --pretrained_model_name_or_path=runwayml/stable-diffusion-v1-5 \
  --instance_data_dir=./data/$DATA_DIR \
  --output_dir=./output/$OUTPUT_DIR \
  --instance_prompt="a photo of $SUBJECT" \
  --resolution=512 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --learning_rate=5e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps=400 \
  --mixed_precision="fp16" \
  --validation_prompt="a photo of $SUBJECT" \
  --num_validation_images=4 \
  --validation_steps=100 \
  --push_to_hub


  