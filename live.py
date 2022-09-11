#import speech_recognition as sr
#r = sr.Recognizer()

#mic = sr.Microphone()

#with mic as source:
  #  audio = r.listen(source)




#print(r.recognize_wit(audio, "RYURPKB3HROF4E7IGOT4NOB5SGDWBZUQ"))
#print(r.recognize_google(audio))

import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import sys

q = queue.Queue()

def callback(indata,frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

model = Model("vosk-model-small-fr-0.22")
sd.default.device = 1
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
    print('*' * 100)
    print('Interrupt the kernel to stop recording')
    print('*' * 100)
    rec = KaldiRecognizer(model, 16000)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())
