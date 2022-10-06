import os

async def closeApp(app) :
    os.system("taskkill /f /im " + app + ".exe")