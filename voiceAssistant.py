import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import sys
import json
import asyncio
import pyttsx3
from weatherTest import *

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def callFunction(text):
    if (text != ""):
        print(text)
    if text.__contains__("test"):
        print("test of the functions")
    elif text.__contains__("weather"):
        asyncio.run(getweather())


model = Model("vosk-model-en-us-0.22-lgraph")
sd.default.device = 1
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
    rec = KaldiRecognizer(model, 16000)
    print("Voice assistant has started")
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result())
            callFunction(text["text"])

        else:
            partialResult = json.loads(rec.PartialResult())

            if partialResult["partial"] != "":
                print(partialResult["partial"])
