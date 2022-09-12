import pyttsx3

engine = pyttsx3.init()

text = "this is a test of the text to speech"

engine.say(text)

engine.runAndWait()

