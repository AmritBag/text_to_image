# Text-to-Image Generator with Stable Diffusion

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
* torch
* diffusers
* accelerate
* transformers (optional, but may be required depending on backend)



## Usage



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

## Notes

* GPU is highly recommended for faster image generation.
* Default values are provided for ease of use.

