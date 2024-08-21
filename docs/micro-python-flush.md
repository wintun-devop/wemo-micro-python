## Ref-1( https://micropython.org/download/ESP32_GENERIC/)
## Ref-2(https://medium.com/@andymule/micropython-on-esp32-e54998966e9)
## Ref-3(https://docs.openmv.io/esp8266/tutorial/intro.html)

## virtial environment set-up
```
python -m venv iot-env
```
```
iot-env/Script/activate
```
## installing necessary tools
```
pip install esptool
```
## Check the com port and erase flash(here my chip is esp8266)
```
esptool --chip esp8266 --port COM3 erase_flash
```
## Write MicroPython to wemos d1 flush
```
esptool --chip esp8266 --port COM3 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20240602-v1.23.0.bin
```
