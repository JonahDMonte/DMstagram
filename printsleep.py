import random
import time
import math
def timeconvert(secs):
    mins = math.floor(secs/60)
    seconds = secs%60
    return mins, seconds
def printsleeptime(x, y):
    num = random.randint(x, y)
    i = 0
    while i < num:
        totalmins, totalsecs = timeconvert(num)
        imins, isecs = timeconvert(i)
        print(f"Sleeping for: {totalmins}:{totalsecs:02}. Time elapsed: {imins}:{isecs:02}\r", end="", flush=True)
        i += 1
        time.sleep(1)
