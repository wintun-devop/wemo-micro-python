from machine import Pin
import time
# Initialize the touch sensor pin
touch_sensor = Pin(4, Pin.IN)
while True:
    print("touch value",touch_sensor.value())
    if touch_sensor.value() == 1:
        print("Touch detected!")
    else:
        print("No touch detected.")
    time.sleep(0.5)