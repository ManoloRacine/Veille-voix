from vosk import Model, KaldiRecognizer
import pyaudio

model = Model('vosk-model-small-fr-0.22')
recognizer = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True :
    data = stream.read(8192)

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())
