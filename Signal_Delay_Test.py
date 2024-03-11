import board
import digitalio
import time

led_aa = digitalio.DigitalInOut(board.C3)
led_aa.direction = digitalio.Direction.OUTPUT
led_bb = digitalio.DigitalInOut(board.C4)
led_bb.direction = digitalio.Direction.OUTPUT
trans_aa = digitalio.DigitalInOut(board.C2)
trans_aa.direction = digitalio.Direction.OUTPUT
trans_bb = digitalio.DigitalInOut(board.C1)
trans_bb.direction = digitalio.Direction.OUTPUT

photo_taken = 0
trans_aa.value = False
trans_bb.value = False

while True:
    trans_aa.value = False
    trans_bb.value = False

    milli_sec = int(round(time.time() * 1000))
    print(str(milli_sec))

    if photo_taken == 0:
     trans_aa.value = True
     trans_bb.value = True
     milli_sec = int(round(time.time() * 1000))
     print(" Signal Sent - " + str(milli_sec))
     photo_taken += 1

    time.sleep(0.001)
    
