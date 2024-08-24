import dht
from machine import Pin

# Initialize the DHT sensor
sensor = dht.DHT22(Pin(4))  # Use DHT11(Pin(4)) if you're using DHT11

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print('Temperature: {}°C'.format(temp))
        print('Humidity: {}%'.format(hum))
    except OSError as e:
        print('Failed to read sensor.')