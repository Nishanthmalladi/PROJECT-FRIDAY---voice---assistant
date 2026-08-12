import speech_recognition as sr
import webbrowser
import pyttsx3

import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open reddit" in c.lower():
        webbrowser.open("https://www.reddit.com")
    elif "news" in c.lower():
        webbrowser.open("https://news.google.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    print(c)
    pass

if __name__ == "__main__":
    speak("Initializing Friday...")

    while True:
        # Listen for the wake word "Friday"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=9,phrase_time_limit=1)

            command = r.recognize_google(audio)
            if command.lower() == "friday":
                speak("Yes?")
                #listen for command
                with sr.Microphone() as source:
                    print("friday active..")
                    audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)

        except Exception as e:
            print("Error: {}".format(e))
