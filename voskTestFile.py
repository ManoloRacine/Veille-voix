import wave
import json
from vosk import Model, KaldiRecognizer

waveFile = wave.open("harvard.wav", "rb")

model = Model("vosk-model-en-us-0.22")
recognizer = KaldiRecognizer(model, waveFile.getframerate())

transcription = []

while True:
    data = waveFile.readframes(8000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        result_dict = json.loads(recognizer.Result())
        print(result_dict)
        transcription.append(result_dict.get("text", ""))

final_result = json.loads(recognizer.FinalResult())
transcription.append(final_result.get("text", ""))

transcription_text = " ".join(transcription)
print(transcription_text)