import python_weather
import geocoder
import pyttsx3



async def getweather():

    async with python_weather.Client() as client:
        engine = pyttsx3.init()
        g = geocoder.ip("me")
        weather = await client.get(g.city)

        say = "The temperature in " + g.city + " is " + str(weather.current.temperature) + " celsius and the weather is " + str(weather.current.description)
        print(say)
        engine.say(say)
        engine.runAndWait()
