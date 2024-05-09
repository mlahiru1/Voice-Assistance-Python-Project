import pyttsx3 as p

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
engine.say("hello world. My name is nova")
engine.runAndWait()