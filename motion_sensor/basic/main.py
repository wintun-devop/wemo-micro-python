from machine import Pin
import time

motion = Pin(4, Pin.IN)  
while True:
    print("all",motion)
    print("motion:",motion.value())
    if motion.value() == 1:
        print("motion detected!")
    else:
        print("no motion!")
    time.sleep(1)