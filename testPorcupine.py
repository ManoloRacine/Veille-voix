import pvporcupine
from pvrecorder import PvRecorder

porcupine = pvporcupine.create(
    access_key="Zo7Lrcaw+A/nrba2GE7c0YeRpPjaNhVEIFO8BMv3YLPt+WzUj6rfkw==",
    keyword_paths=["Ok-bot_en_windows_v2_1_0.ppn"]
)

recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
recorder.start()
devices = PvRecorder.get_audio_devices()

while True:
    pcm = recorder.read()

    keyword_index = porcupine.process(pcm)
    if keyword_index == 0:
        print("test")