import network,time,dht
import urequests as requests
from machine import Pin

# WiFi credentials
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

# AWS API Gateway End-Point
url = 'https://your-api-gateway-endpoint.amazonaws.com/your-path'

# Connect to WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while not station.isconnected():
    pass
print('Connection successful')
print(station.ifconfig())

sensor = dht.DHT11(Pin(4))  
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        data = {
            'temperature': temp,
            'humidity': hum
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            data = response.json()  # Process the response data
            print(data)
        else:
            print(f"Error: {response.status_code}")
    except OSError as e:
        print("e",e)
        print('Failed to read sensor.')
    time.sleep(30)