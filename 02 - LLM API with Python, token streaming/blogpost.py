import os
import openai

# Load API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Set it as an environment variable: OPENAI_API_KEY")

client = openai.OpenAI()

# File paths
INPUT_FILE = "transcript1.txt"
OUTPUT_FILE = "blog_post.txt"

# Read the transcript
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    transcript_text = file.read()

# Define the prompt for GPT-4o
prompt = f"""
You are a professional blog writer. Based on the following transcript, generate a well-structured and engaging blog post. 
Ensure the writing is clear, concise, and formatted properly with a title, introduction, body, and conclusion.

Transcript:
{transcript_text}
"""

# Call OpenAI API
try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are an expert blog writer."},
                  {"role": "user", "content": prompt}],
        max_tokens=2048,
        temperature=0.7
    )

    blog_post = response.choices[0].message.content

    # Save to output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(blog_post)

    print(f"Blog post successfully generated and saved to {OUTPUT_FILE}")

except Exception as e:
    print(f"Error: {e}")