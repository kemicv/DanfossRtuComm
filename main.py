import matplotlib.pyplot as plt
from pymodbus.client.sync import ModbusSerialClient
import time

client = ModbusSerialClient(method="rtu", port="COM4", baudrate=9600,
                            parity="N", bytesize=8, stopbits=1, timeout=3)
secs_list = []
setpoint_list = []
reference_list = []
secs = 0

client.connect()
while setpoint_list.__len__()<150:
    secs_list.append(secs)
    secs+=0.2
    print("time: ", secs)
    setpoint = client.read_holding_registers(address=20209, count=2, unit=1)
    set_data = setpoint.registers[1]
    reference = client.read_holding_registers(address=16519, count=2, unit=1)
    try:
        if reference.registers[1] > 3000: ref_data = 0
        else: ref_data = reference.registers[1]
    except:
        ref_data = 0


    setpoint_list.append(set_data)
    reference_list.append(ref_data)
    print(set_data, ref_data)
    time.sleep(0.2)

client.close()
plt.plot(secs_list, reference_list, label="reference")
plt.plot(secs_list, setpoint_list, label="setpoint")
plt.show()
