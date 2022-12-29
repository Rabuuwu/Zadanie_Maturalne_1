import speech_recognition as sr
import pyttsx3

# Set up the speech recognition object
r = sr.Recognizer()

# Set up the text-to-speech engine
engine = pyttsx3.init()

while True:
    # Prompt the user to speak
    print("Speak now:")

    # Record the user's audio using the speech recognition object
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Convert the audio to text using the speech recognition object
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except Exception as e:
        print("Error:", e)
        continue

    # Convert the text to speech using the text-to-speech engine
    engine.say(text)
    engine.runAndWait()