from gtts import gTTS
import os

def generate_hindi_audio(text, output_file="output.mp3"):
    tts = gTTS(text, lang="hi")
    tts.save(output_file)
    return output_file

if __name__ == "__main__":
    text = "टेस्ला की नई गाड़ी ने बिक्री का रिकॉर्ड तोड़ दिया।"
    generate_hindi_audio(text)
    os.system("start output.mp3")  # Opens the audio file
