from diffusers import StableDiffusionPipeline
import torch

def load_pipeline(model_name="runwayml/stable-diffusion-v1-5", use_cuda=True):
    device = "cuda" if use_cuda and torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    )
    pipe = pipe.to(device)
    return pipe

def get_user_input():
    def get_input(prompt_text, cast_type=str, default=None):
        user_input = input(f"{prompt_text} " + (f"[default: {default}] " if default else ""))
        if not user_input.strip():
            return default
        try:
            return cast_type(user_input)
        except ValueError:
            print(f"Invalid input. Using default: {default}")
            return default

    prompt = input("Enter your prompt: ")
    negative_prompt = input("Enter your negative prompt (optional): ")

    guidance_scale = get_input("Enter guidance scale (e.g., 7.5):", float, 7.5)
    num_inference_steps = get_input("Enter number of inference steps (e.g., 50):", int, 50)
    height = get_input("Enter image height (e.g., 512):", int, 512)
    width = get_input("Enter image width (e.g., 512):", int, 512)
    path = get_input("Enter path to save image (e.g., ./generated_image.png):", str, "./generated_image.png")

    return {
        "prompt": prompt,
        "negative_prompt": negative_prompt if negative_prompt else "blurry, distorted, low quality",
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps,
        "height": height,
        "width": width,
        "path": path
    }


def generate_image(pipe, config):
    image = pipe(
        prompt=config["prompt"],
        negative_prompt=config["negative_prompt"],
        guidance_scale=config["guidance_scale"],
        num_inference_steps=config["num_inference_steps"],
        height=config["height"],
        width=config["width"],
    ).images[0]
    return image

    
print("Loading Stable Diffusion pipeline...")
pipe = load_pipeline()
