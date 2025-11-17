# Sampling through Generative Art

## Concept

This project expands the concept of sampling, which originated from a musical practice where musicians mixed and matched "samples" of pre-existing music to create distinct results. This project extends that practice across mediums: audio is reinterpreted by Stable Diffusion into generative art, and then translated back to audio. Machine learning systems treat audio and images as interchangeable data—arrays that can be reshaped and reinterpreted. This system exploits that property to create a translation chain where unexpected meaning emerges through gaps in conversion.

**Process:**
1. Audio → Spectrogram (visual representation)
2. Spectrogram → Abstract art (via Stable Diffusion)
3. Abstract art → Audio (via data conversion methods)

The same source material produces radically different results depending on conversion method. This variability is the point—it reveals how meaning is constructed through our methods of reading data.

## Technical Overview

### What's a Spectrogram?

A spectrogram is a time-frequency representation of audio:
- X-axis: time
- Y-axis: frequency
- Intensity: amplitude (rendered as brightness/color)

This creates a visual "map" of sound. When fed to Stable Diffusion—an AI trained on images, not audio—the model interprets these patterns as visual information and transforms them according to its training, with no awareness of the sonic origin.

### The Conversion Chain

**Audio → Visual:**
The system extracts a spectrogram using standard signal processing (librosa), then converts it to a PIL image format compatible with Stable Diffusion.

**Visual → Art:**
Stable Diffusion reinterprets the spectrogram as abstract art. The deliberate choice of abstract prompts avoids anthropomorphic or object-based associations, creating space for interpretation.

**Art → Audio:**
This is where multiple methods diverge:
- **RGB Mean**: Averages color channel values to derive amplitude information
- **Chirp**: Uses scipy signal processing to reinterpret pixel data as frequency sweeps

Different conversion methods extract different information from the same visual data, producing distinct sonic results. This multiplicity is central to the project's investigation of how meaning is constructed through technical choices.

---

## Usage

### Setup
The notebook runs in Google Colab. First run takes several minutes to load models; subsequent runs are significantly faster.

### Basic Operation
1. Open the notebook
2. Upload your audio file
3. Run all cells sequentially
4. Download output audio

### Experimentation
Parameters available for modification:
- Stable Diffusion prompts (affects visual interpretation)
- Hyperparameters (guidance scale, inference steps)
- Conversion method selection

Modification doesn't require deep technical knowledge—parameters can be adjusted empirically to observe results.

---

## Technical Details

<details>
<summary>Dependencies & Implementation</summary>

**Core libraries:**
- torchaudio (audio processing, spectrogram generation)
- Stable Diffusion & HuggingFace (generative art)
- PIL (image manipulation)
- scipy (chirp conversion method)
- numpy/PyTorch (array operations enabling cross-modal conversion)

**Implementation notes:**

The system leverages the fact that machine learning models operate on numerical arrays regardless of modality. Audio waveforms, spectrograms, and images all reduce to matrices of numbers. The conversion process:

1. Audio loaded as waveform array
2. Spectrogram computed via FFT
3. Spectrogram normalized and converted to PIL RGB image
4. Image processed through Stable Diffusion pipeline
5. Output image converted back to array
6. Array reinterpreted as audio via conversion method:

Each conversion method constitutes a different "reading" of the visual data, extracting different information and producing different sonic results from identical visual input.

</details>

---

## Conceptual Framework

This project operates at the intersection of several questions:

 - On sampling: If hip-hop sampling recontextualizes music, what happens when we sample across modalities? Is it still sampling if the outcome passes through a different format?

 - On ownership: Who has the right to claim work coming out of this system? The person who created the original audio? This system itself? The user?

 - On translation: Every conversion (audio→visual→audio) is interpretive, not neutral. The technical choices I make about how to read data determine what meaning survives the translation.

 - On computing as artistic medium: AI/ML systems don't distinguish between audio and visual data. Both are multidimensional arrays. I exploited this interchangeability as a creative opening.

 - On multiplicity: Different conversion methods extract different "meanings" from identical data.

---

## Context

Created as a final project for Poetics and Protocols of Sampling (Autumn 2025) at the School of Poetic Computation. SFPC is an experimental online school hosting classes that blend art, code, and critical theory.

