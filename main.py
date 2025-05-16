from model import get_user_input, generate_image, load_pipeline

def main():
    print("Loading Stable Diffusion pipeline...")
    pipe = load_pipeline()

    print("Getting user input...")
    config = get_user_input()

    print("Generating image...")
    image = generate_image(pipe, config)

    save_path = config.get("path", "generated_image.png")
    image.save(save_path)
    print(f"Image saved at '{save_path}'")

    print("Image generation complete!")

if __name__ == "__main__":
    main()
