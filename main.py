import speech_recognition as sr

print(sr.__version__)

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    audio = r.record(source)

print(r.recognize_wit(audio,'RYURPKB3HROF4E7IGOT4NOB5SGDWBZUQ'))