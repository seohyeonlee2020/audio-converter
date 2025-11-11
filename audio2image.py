# %%
# Core imports
import os
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset

# Audio
import torchaudio
import torchaudio.transforms as T

# Visualization
import matplotlib.pyplot as plt
import numpy as np

#Image
import torchvision.transforms
import torchaudio.transforms as T

# Optional: reproducibility
torch.manual_seed(0)


# %%
#take input



# %%
#get spectrogram from audio file
# Define transform

spectrogram_transform = T.Spectrogram(n_fft=512)

# Perform transform
spectrogram = spectrogram_transform(waveform)
normalized_spectrogram = normalize_spectrogram(spectrogram)

#visualize spectrogram as is

fig, axs = plt.subplots(2, 1)
plot_waveform(waveform, sample_rate, title="Original waveform", ax=axs[0])
plot_spectrogram(spec[0], title="spectrogram", ax=axs[1])
fig.tight_layout()

img_transform = torchvision.transforms.ToPILImage()
rgb_img = img_transform(normalized_spectrogram).convert("RGB")

#set spectrogram as initial image
#init_image = Image.open(BytesIO(response.content)).convert("RGB")
spec_image = rgb_img.resize((400, 300))

prompt = "caffeinated thoughts of a tired college student pulling their 2nd all nighter flying saucers and jellyfish living forever abstract image no concrete objects"
abstract_prompt = "abstract art"
jackson_pollock_prompt = "jackson pollock style painting, no objects"
gibberish_prompt = "wjoeidjwlejdk;oqiope wuepidujqewidjj"
#custom_prompt = input("write your own prompt: ")


#strength (0 < st < 1)Indicates extent to transform the reference image
#guidance_scale (float, optional, defaults to 7.5) — A higher guidance scale value encourages the model to generate images closely linked to the text prompt at the expense of lower image quality. Guidance scale is enabled when guidance_scale > 1.
image = pipe(prompt=prompt, negative_prompt = "no letters, no objects, no people", image=spec_image, strength=0.9, guidance_scale=1.5).images

from datetime import datetime
# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20251112_153045

# Build filename
filename = f"generated_image_{timestamp}.png"

# Save image
image[0].save(filename)

print(f"Saved as {filename}")
image[0]

# %%



