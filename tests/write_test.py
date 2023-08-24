par = 1

from pymodbus.client.sync import ModbusSerialClient
import logging

#region This shows all the transaction details
#FORMAT = ('%(asctime)-30s :%(lineno)-8s %(message)s')
#logging.basicConfig(format=FORMAT)
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)
#endregion

rtupar = (par * 10) - 1
client = ModbusSerialClient(method="rtu", port="COM1", baudrate=115200,
                            parity="N", bytesize=8, stopbits=1, timeout=3)
client.connect()
while True:
    new_value = input("new value: ")
    match new_value:
        case "x":
            break
        case _:
            ref = client.write_register(address=rtupar, value=int(new_value), unit=2)#unit refers to slave address
            confirm = client.read_holding_registers(address=rtupar, count=2, unit=2)
            if confirm.registers[0] != int(new_value):
                print("Error, nuevo valor no admitido.")
            
client.close()
