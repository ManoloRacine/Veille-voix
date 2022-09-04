import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)




print(r.recognize_wit(audio, "RYURPKB3HROF4E7IGOT4NOB5SGDWBZUQ"))
#print(r.recognize_google(audio))