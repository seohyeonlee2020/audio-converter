import io
from datetime import datetime
import torch
import torchaudio
import torchaudio.transforms as T
import torchvision.transforms as vtrans
import matplotlib.pyplot as plt
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline as Img2ImgPipeline  # or AudioLDM if you prefer


def normalize_spectrogram(spec):
    """Normalize a spectrogram tensor to 0–1 range for visualization."""
    spec_min, spec_max = spec.min(), spec.max()
    return (spec - spec_min) / (spec_max - spec_min + 1e-8)


def audio2image(uploaded_file, pipe):
    """
    Takes a WAV file uploaded through Streamlit and generates an abstract image.
    Returns a PIL image.
    """
    # --- load audio ---
    waveform, sample_rate = torchaudio.load(uploaded_file)

    # --- compute spectrogram ---
    spectrogram_transform = T.Spectrogram(n_fft=512)
    spec = spectrogram_transform(waveform)
    normalized_spec = normalize_spectrogram(spec)

    # --- convert to RGB image ---
    img_transform = vtrans.ToPILImage()
    rgb_img = img_transform(normalized_spec).convert("RGB")
    spec_image = rgb_img.resize((400, 300))

    # --- choose prompt ---
    prompt = (
        "caffeinated thoughts of a tired college student pulling their 2nd all-nighter, "
        "flying saucers and jellyfish living forever — abstract, no concrete objects"
    )

    # --- run diffusion model ---
    result = pipe(
        prompt=prompt,
        negative_prompt="no letters, no objects, no people",
        image=spec_image,
        strength=0.9,
        guidance_scale=1.5,
    ).images

    # --- save result with timestamp ---
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_image_{timestamp}.png"
    result[0].save(filename)

    print(f"Saved as {filename}")
    return result[0]
