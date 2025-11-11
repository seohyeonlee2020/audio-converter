import io
from pydub import AudioSegment
import streamlit as st

# Core imports
import os
import torch
from torch import nn, optim

# Audio
import torchaudio
import torchaudio.transforms as T

# Visualization
import matplotlib.pyplot as plt
import numpy as np

from diffusers import StableDiffusionImg2ImgPipeline
from audio_to_image import audio2image

device = "cuda" if torch.cuda.is_available() else "cpu"
model_id_or_path = "stable-diffusion-v1-5/stable-diffusion-v1-5"
torch_dtype = torch.float16 if device == "cuda" else torch.float32

"""
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype=torch_dtype)
pipe = pipe.to(device) """

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32
).to("mps")


st.title("Audio To Image")

uploaded_files = st.file_uploader(
    "Upload an audio file you want to convert", accept_multiple_files=True, type=".wav"
)

for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        try:
            filename = uploaded_file.name
            print('filename', filename)

            image = audio2image(uploaded_file, pipe)
            st.image(image, caption= f"Abstract Art Generated From {filename}", use_column_width=True)

        except Exception as e:
            print(f"Error converting '{filename}': {e}")
