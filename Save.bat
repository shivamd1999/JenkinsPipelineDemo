
import os
import time
import subprocess
programName = "notepad.exe"
fileName = "save1.bat"
p = subprocess.Popen([programName, fileName])

time.sleep(10)
p.kill()
