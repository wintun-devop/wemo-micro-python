import time,sys,machine,ubinascii
from machine import Pin

def main():
    # Initialize the touch sensor pin
    touch_sensor = Pin(4, Pin.IN)
    while True:
        touch_1 = touch_sensor.value()
        print("touch :",touch_1)
        if touch_1 == 1:
            machine_id = get_machine_id()
            machine_platform=get_hardware_platform()
            machine_current_time = get_current_time()
            result = f"Touch on {machine_id} with {machine_platform} platform at {machine_current_time}."
            print(result)
        else:
            print("No touch detected.")
        time.sleep(1)
        

def get_machine_id()->str:
    machine_id = str(ubinascii.hexlify(machine.unique_id()).decode())
    return machine_id

def get_hardware_platform()->str:
    platform=str(sys.platform)
    return platform

def get_current_time()->str:
    year, month, day, hour, minute, second, weekday, yearday = time.gmtime()
    utc_time_str = "{:04}-{:02}-{:02}T{:02}:{:02}:{:02}Z".format(year, month, day, hour, minute, second)
    return utc_time_str

if __name__ == "__main__":
    main()