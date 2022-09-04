from wit import Wit
import speech_recognition as sr
import requests as req


client = Wit("RYURPKB3HROF4E7IGOT4NOB5SGDWBZUQ")
audio = None

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)

#with open("test.wav", 'rb') as f:
#    audio = f.read()


#resp = client.speech(audio.get_wav_data(), {'Content-Type': 'audio/wav'})
headers = {'authorization': 'Bearer ' + "RYURPKB3HROF4E7IGOT4NOB5SGDWBZUQ",
           'Content-Type': 'audio/wav'}
resp = req.post('https://api.wit.ai/dictation', data=audio.get_wav_data(), headers=headers)
print(resp.text)
