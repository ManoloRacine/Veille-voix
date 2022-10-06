import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import sys
import json
import asyncio
import pyttsx3
from timetts import *
from weatherTest import *
from closeApp import *
from joke import *
from startApp import *
import pvporcupine
from pvrecorder import PvRecorder
import pvrhino

porcupine = pvporcupine.create(
    access_key="Zo7Lrcaw+A/nrba2GE7c0YeRpPjaNhVEIFO8BMv3YLPt+WzUj6rfkw==",
    keyword_paths=["Ok-bot_en_windows_v2_1_0.ppn"]
)



rhino = pvrhino.create(
    access_key="Zo7Lrcaw+A/nrba2GE7c0YeRpPjaNhVEIFO8BMv3YLPt+WzUj6rfkw==",
    context_path="./VeilleVoix_en_windows_v2_1_0.rhn"
)

recorderRhino = PvRecorder(device_index=2, frame_length=rhino.frame_length)

recorder = PvRecorder(device_index=2, frame_length=porcupine.frame_length)
devices = PvRecorder.get_audio_devices()

print(devices)
engine = pyttsx3.init()
q = queue.Queue()

keywordDetected = False

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    if keywordDetected:
        q.put(bytes(indata))


def callFunction(intent, slots):
    if intent != "":
        print(intent)
    if intent.__contains__("test"):
        print("test of the functions")
        return True
    elif intent == "weather":
        asyncio.run(getweather())
        return True
    elif intent == "off":
        engine.say("good night")
        engine.runAndWait()
        exit()
        return True
    elif intent == "ttsOff":
        engine.say("ok, no more text to speech")
        engine.runAndWait()
        engine.setProperty("volume", 0)
        return True
    elif intent == "ttsOn":
        engine.setProperty("volume", 1)
        engine.say("ok, text to speech is on")
        engine.runAndWait()
        return True
    elif intent == "time":
        getTimeTTS()
        return True
    elif intent == "joke":
        asyncio.run(getJoke())
        return True
    elif intent == "close":
        asyncio.run(closeApp(slots["app1"].replace(" ", "")))
        return True
    elif intent == "open":
        asyncio.run(startApp(slots["app1"].replace(" ", "")))
        return True
    return False



print("Voice assistant has started")

recorder.start()
functionDetected = False
while True:
    if functionDetected:
        recorder.start()
        q = queue.Queue()
        keywordDetected = False
        functionDetected = False

    pcm = recorder.read()
    keyword_index = porcupine.process(pcm)
    if keyword_index == 0:
        keywordDetected = True
        recorder.stop()
        print("yes ?")
        engine.say("yes ?")
        engine.runAndWait()

        while not functionDetected:
            recorderRhino.start()
            audio_frame = recorderRhino.read()
            is_finalized = rhino.process(audio_frame)
            if is_finalized:
                inference = rhino.get_inference()
                if inference.is_understood:
                    recorderRhino.stop()
                    intent = inference.intent
                    slots = inference.slots
                    print(intent)
                    print(slots)
                    functionDetected = callFunction(intent, slots)
