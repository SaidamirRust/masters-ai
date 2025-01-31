import openai
import os
import requests
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define styles
styles = [
    "in the style of a watercolor painting",
    "in the style of a futuristic cityscape",
    "in the style of an oil painting",
    "in the style of a pixel art game",
    "in the style of a vintage photograph",
    "in the style of a comic book",
    "in the style of a surrealist painting",
    "in the style of a retro 80s neon art",
    "in the style of an abstract painting"
]


# Function to generate images
def generate_images(prompt):
    images = []
    for style in styles:
        styled_prompt = f"{prompt} {style}"
        try:
            # Generate image using OpenAI's image API
            response = openai.images.generate(
                model="dall-e-3",
                prompt=styled_prompt,
                n=1,  # Generate 1 image per style
                size="1024x1024"
            )

            image_url = response.data[0].url  # Get the image URL

            # Download and save the image
            img_response = requests.get(image_url)
            img = Image.open(BytesIO(img_response.content))
            image_filename = f"{style.replace(' ', '_')}.png"
            img.save(image_filename)
            images.append(image_filename)
            print(f"Generated image: {image_filename}")

        except Exception as e:
            print(f"Error generating image for style '{style}': {e}")

    return images


# Main function
if __name__ == "__main__":
    user_prompt = input("Enter a prompt to generate images: ")
    generated_images = generate_images(user_prompt)
    print(f"Generated images: {generated_images}")
