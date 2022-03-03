import os
import time
import subprocess
fileName = "C:\\Users\\shivamd1\\Documents\\Batch_Files\\save1.bat"
p = subprocess.Popen([fileName])

time.sleep(10)
p.kill()


