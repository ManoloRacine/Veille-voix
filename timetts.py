from datetime import datetime
import pyttsx3


def getTimeTTS():
    engine = pyttsx3.init()
    time = datetime.now()
    say = "It is currently : " + str(time.strftime("%H %M"))
    print("It is currently : " + str(time.strftime("%H:%M")))
    engine.say(say)
    engine.runAndWait()