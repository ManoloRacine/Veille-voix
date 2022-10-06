import subprocess
import os

async def startApp(app) :
    user = os.getlogin()
    if app == "discord" :
        subprocess.Popen(r'C:\Users\{user}\AppData\Local\Discord\app-1.0.9006\Discord.exe')
    elif app == "chrome" :
        subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    elif app == "steam":
        subprocess.Popen(r'C:\Program Files (x86)\Steam\steam.exe')
    else:
        subprocess.Popen([app + '.exe'])