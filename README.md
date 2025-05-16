# Text-to-Image Generator with Stable Diffusion

---

````markdown
# Text-to-Image Generator with Stable Diffusion

[![Open in Colab][(https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/your-notebook-url-here)](https://colab.research.google.com/drive/16Gv2FbThTOpwE9gDUqQuZU2yDR1IxiIn?usp=drive_link)
````
Generate images from text prompts using Stable Diffusion with customizable settings.

## Features

* Uses `runwayml/stable-diffusion-v1-5` via Hugging Face’s `diffusers` library
* Supports GPU and CPU execution
* Customizable:
  * Text prompt & negative prompt
  * Image size (height & width)
  * Guidance scale
  * Inference steps
  * Output image path
* Interactive command-line interface

## Requirements

* Python 3.7+
* `torch`
* `diffusers`
* `accelerate`
* `transformers` (optional, but may be required depending on backend)

You can install the dependencies using:

```bash
pip install torch diffusers accelerate transformers
```

## Usage

Run the main script:

```bash
python main.py
```

You'll be prompted to enter:

* A text prompt (e.g., "A futuristic cityscape at sunset")
* An optional negative prompt
* Guidance scale (e.g., 7.5)
* Number of inference steps (e.g., 50)
* Image height and width (e.g., 512x512)
* Path to save the generated image (e.g., `./generated_image.png`)

## Example Output

A sample prompt like:

```text
Prompt: A cyberpunk city at night with neon lights
Negative Prompt: blurry, distorted, low quality
```

Will generate a high-quality image saved to your specified path.

## Code Overview

This project is structured around two main Python files: `model.py` and `main.py`.

### `model.py`

This module contains the core functionality for working with the Stable Diffusion model:

* **`load_pipeline()`**: Loads the `StableDiffusionPipeline` from Hugging Face’s `diffusers` library, with optional GPU acceleration.
* **`get_user_input()`**: Collects user input from the terminal, including prompts, image dimensions, inference settings, and output path.
* **`generate_image()`**: Uses the configured pipeline to generate an image from the input prompt.
* Also includes a preload step to initialize the pipeline when the file is imported.

### `main.py`

This is the entry point of the application. It performs the following tasks:

1. Loads the Stable Diffusion pipeline.
2. Gathers input from the user.
3. Generates an image using the pipeline and user-provided parameters.
4. Saves the resulting image to disk.
5. Provides console feedback throughout the process.

## Notes

* GPU is highly recommended for faster image generation.
* Default values are provided to streamline the input process.
* Make sure you have access to the Hugging Face model checkpoint (`runwayml/stable-diffusion-v1-5`).

---

Feel free to fork this project, improve it, or adapt it to your needs. Pull requests are welcome!

````

---


```markdown
[Open in Colab][(https://colab.research.google.com/your-notebook-url-here)](https://colab.research.google.com/drive/16Gv2FbThTOpwE9gDUqQuZU2yDR1IxiIn?usp=drive_link)
````

with your actual Colab notebook URL.

Let me know if you'd like a badge for GitHub stars, license, or Python version too!
