import whisper

# Load Whisper model
model = whisper.load_model("small")

# Transcribe the MP3 file
audio_path = "meeting_recording.mp3"
result = model.transcribe(audio_path)

# Print transcript
def process_text(text):
    print("\nProcessing the selected text...\n")
    print(f"→ Whisper interprets: {text}")

# Ask the user for a segment index
segments = result["segments"]
for i, segment in enumerate(segments):
    print(f"{i}: {segment['text']}")

index = int(input("\nEnter the segment number you want to process: "))
process_text(segments[index]['text'])