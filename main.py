import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello sir I'm your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listning...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I'm having good day sir")
speak("what can I do for you")


















