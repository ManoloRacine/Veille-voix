import pvrhino
from pvrecorder import PvRecorder

rhino = pvrhino.create(
    access_key="Zo7Lrcaw+A/nrba2GE7c0YeRpPjaNhVEIFO8BMv3YLPt+WzUj6rfkw==",
    context_path="./VeilleVoix_en_windows_v2_1_0.rhn"
)

recorder = PvRecorder(device_index=0, frame_length=rhino.frame_length)
recorder.start()
devices = PvRecorder.get_audio_devices()

while True:
    audio_frame = recorder.read()
    is_finalized = rhino.process(audio_frame)
    if is_finalized:
        inference = rhino.get_inference()
        if inference.is_understood:
            intent = inference.intent
            print(intent)
