from machine import Pin
import time

# Initialize the touch sensor pin
touch_sensor = Pin(5, Pin.IN)

while True:
    if touch_sensor.value() == 1:
        print("Touch detected!")
    else:
        print("No touch detected.")
    time.sleep(0.5)
