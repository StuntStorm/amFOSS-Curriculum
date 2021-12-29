import time
import pyautogui

print('Press CTRL-C to quit.')
try:
    while True:
        pyautogui.moveRel(5, 0, 0.5)
        pyautogui.moveRel(-5, 0, 0.5)
        time.sleep(10)
except KeyboardInterrupt:
    print('Process has quit...')
