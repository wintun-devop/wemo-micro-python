import dht,time
from machine import Pin

# Initialize the DHT sensor
# Use DHT22(Pin(4)) if you're using DHT22
sensor = dht.DHT11(Pin(4))  
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print('Temperature: {}°C'.format(temp))
        print('Humidity: {}%'.format(hum))
    except OSError as e:
        # print("e",e)
        print('Failed to read sensor.')
    time.sleep(5)