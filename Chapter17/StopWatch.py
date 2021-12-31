import time
import pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1


try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        info = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).center(7), str(lapTime).rjust(6))
        print(info, end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')
