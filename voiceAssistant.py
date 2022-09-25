import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import sys
import json
import asyncio
import pyttsx3
from weatherTest import *
import pvporcupine
from pvrecorder import PvRecorder

porcupine = pvporcupine.create(
    access_key="Zo7Lrcaw+A/nrba2GE7c0YeRpPjaNhVEIFO8BMv3YLPt+WzUj6rfkw==",
    keywords=["picovoice"]
)

recorder = PvRecorder(device_index=2, frame_length=porcupine.frame_length)
devices = PvRecorder.get_audio_devices()

q = queue.Queue()

keywordDetected = False

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    if keywordDetected:
        q.put(bytes(indata))


def callFunction(text):
    if (text != ""):
        print(text)
    if text.__contains__("test"):
        print("test of the functions")
        return True
    elif text.__contains__("weather"):
        asyncio.run(getweather())
        return True
    elif text.__contains__("off"):
        exit()
        return True
    return False



model = Model("vosk-model-en-us-0.22-lgraph")
sd.default.device = 1
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
    rec = KaldiRecognizer(model, 16000)
    print("Voice assistant has started")

    recorder.start()
    functionDetected = False
    while True:
        if functionDetected:
            recorder.start()
            q = queue.Queue()
            keywordDetected = False
            rec.Reset()
            functionDetected = False

        pcm = recorder.read()
        keyword_index = porcupine.process(pcm)
        if keyword_index == 0:
            keywordDetected = True
            recorder.stop()
            print("test")

            while not functionDetected:
                data = q.get()
                if rec.AcceptWaveform(data):
                    text = json.loads(rec.Result())
                    functionDetected = callFunction(text["text"])

                else:
                    partialResult = json.loads(rec.PartialResult())
                    functionDetected = callFunction(partialResult["partial"])

       # data = q.get()
       # if rec.AcceptWaveform(data):
       #     text = json.loads(rec.Result())
      #      callFunction(text["text"])

       # else:
      #      partialResult = json.loads(rec.PartialResult())

      #      if partialResult["partial"] != "":
       #         print(partialResult["partial"])
