# import speech_recognition as sr
# r = sr.Recognizer()
import os

# mic = sr.Microphone()

# with mic as source:
#  audio = r.listen(source)


# print(r.recognize_wit(audio, "RYURPKB3HROF4E7IGOT4NOB5SGDWBZUQ"))
# print(r.recognize_google(audio))

import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import sys

# code basé sur les fichiers de test de vosk

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


import pyttsx3

engine = pyttsx3.init()

model = Model("vosk-model-fr-0.22")
sd.default.device = 1
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
    rec = KaldiRecognizer(model, 16000)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())

