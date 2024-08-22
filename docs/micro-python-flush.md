### Ref-1( https://micropython.org/download/ESP32_GENERIC/)
### Ref-2(https://medium.com/@andymule/micropython-on-esp32-e54998966e9)
### Ref-3(https://micropython.org/download/ESP8266_GENERIC/)
### Ref-4(https://docs.openmv.io/esp8266/tutorial/intro.html)
### Ref-5-machine library (https://docs.micropython.org/en/latest/library/machine.html)

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
esptool --chip esp8266 -p COM3 erase_flash
```
## Write MicroPython to wemos d1 flush
```
esptool -p COM3 write_flash --flash_size=detect 0 ESP8266_GENERIC-20240602-v1.23.0.bin
```
