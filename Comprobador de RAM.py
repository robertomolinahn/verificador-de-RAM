import wmi

def get_ram_modules_info():
    ram_info = []
    c = wmi.WMI()
    for memory in c.Win32_PhysicalMemory():
        info = {
            "Capacity": memory.Capacity,
            "Manufacturer": memory.Manufacturer,
            "Part Number": memory.PartNumber,
            "Serial Number": memory.SerialNumber,
            "Speed": memory.Speed
        }
        ram_info.append(info)
    return ram_info

ram_modules = get_ram_modules_info()
for i, module in enumerate(ram_modules, 1):
    print(f"Module {i}:")
    for key, value in module.items():
        print(f"  {key}: {value}")
    print()
