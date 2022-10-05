import requests as req
import json
import pyttsx3

async def getJoke() :
    r = req.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit")
    rJson = json.loads(r.text)

    engine = pyttsx3.init()

    if "joke" in rJson:
        print(rJson["joke"])
        engine.say(rJson["joke"])
        engine.runAndWait()
    else:
        print(rJson["setup"])
        print(rJson["delivery"])
        engine.say(rJson["setup"])
        engine.runAndWait()
        engine.say(rJson["delivery"])
        engine.runAndWait()

