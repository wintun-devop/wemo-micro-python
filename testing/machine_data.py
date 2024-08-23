import machine,ubinascii,esp,sys,uos

def get_machine_id()->str:
    machine_id = str(ubinascii.hexlify(machine.unique_id()).decode())
    return machine_id

def get_hardware_platform()->str:
    platform=str(sys.platform)
    return platform

def get_cpu_frequency()->str:
    frequency = str(machine.freq())
    return frequency

def get_esp_flash_size()->int:
    mem_size = esp.flash_size()
    return mem_size

def get_flash_staus()->dict:
    total_flash = esp.flash_size()
    fs_stat = uos.statvfs('/')
    free_flash = fs_stat[0] * fs_stat[3]
    free_flash_kb = free_flash / 1024
    free_flash_mb = free_flash_kb / 1024
    used_flash = total_flash - free_flash
    used_flash_kb = used_flash / 1024
    used_flash_mb = used_flash_kb / 1024
    total_flash_kb = total_flash / 1024
    total_flash_mb = total_flash_kb / 1024
    return {"Total Flash": total_flash_mb,"free(MB)":free_flash_mb,"used(MB)":used_flash_mb}

