import speech_recognition as sr
import webbrowser
import pyttsx3
import whisper

import musiclibrary


# -----------------------------
# SETUP
# -----------------------------

engine = pyttsx3.init()

# Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper loaded successfully.")


# -----------------------------
# TEXT TO SPEECH
# -----------------------------

def speak(text):
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# PROCESS COMMANDS
# -----------------------------

def processCommand(c):

    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif "open github" in c:
        webbrowser.open("https://www.github.com")

    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")

    elif "open twitter" in c:
        webbrowser.open("https://www.twitter.com")

    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")

    elif "open reddit" in c:
        webbrowser.open("https://www.reddit.com")

    elif "news" in c:
        webbrowser.open("https://news.google.com")

    elif c.startswith("play"):

        parts = c.split()

        if len(parts) > 1:

            song = parts[1]

            if song in musiclibrary.music:
                webbrowser.open(musiclibrary.music[song])
            else:
                print("Song not found:", song)

    print("Command:", c)


# -----------------------------
# SPEECH TO TEXT USING WHISPER
# -----------------------------

def transcribe(audio):

    # Convert SpeechRecognition audio
    wav_data = audio.get_wav_data()

    # Save temporary audio file
    with open("temp_audio.wav", "wb") as f:
        f.write(wav_data)

    # Whisper transcription
    result = model.transcribe(
        "temp_audio.wav",
        fp16=False
    )

    return result["text"].strip()


# -----------------------------
# MAIN PROGRAM
# -----------------------------

if __name__ == "__main__":

    speak("Initializing Friday...")

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8

    try:

        while True:

            try:

                # -----------------------------
                # LISTEN FOR FRIDAY
                # -----------------------------

                with sr.Microphone() as source:

                    print("\nCalibrating microphone...")
                    recognizer.adjust_for_ambient_noise(
                        source,
                        duration=1
                    )

                    print("Listening for Friday...")

                    audio = recognizer.listen(
                        source,
                        timeout=10,
                        phrase_time_limit=4
                    )

                word = transcribe(audio)

                print("Heard:", word)

                # -----------------------------
                # WAKE WORD
                # -----------------------------

                if "friday" in word.lower():

                    speak("Yes?")

                    # -----------------------------
                    # LISTEN FOR COMMAND
                    # -----------------------------

                    with sr.Microphone() as source:

                        print("Friday active...")

                        audio = recognizer.listen(
                            source,
                            timeout=10,
                            phrase_time_limit=6
                        )

                    command = transcribe(audio)

                    print("Command:", command)

                    processCommand(command)

            except sr.WaitTimeoutError:

                print("No speech detected.")

            except sr.UnknownValueError:

                print("Could not understand the audio.")

            except Exception as e:

                print("Error:", e)

    except KeyboardInterrupt:

        print("\nStopping Friday...")

    finally:

        try:
            engine.stop()
        except:
            pass

        print("Friday stopped.")