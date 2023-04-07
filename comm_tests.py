from pymodbus.client.sync import ModbusSerialClient
import time
import logging

### This will print the sended info or any error in case anything happens
#FORMAT = ('%(asctime)-15s %(threadName)-15s '
#          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
#logging.basicConfig(format=FORMAT)
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

client = ModbusSerialClient(method="rtu", port="COM4", baudrate=9600,
                            parity="N", bytesize=8, stopbits=1, timeout=3)
client.connect()

###IF I NEED TO SEE THE LANGUAGE VALUE (PAR.00.01) I NEED TO ACCES TO 10,
# AND REDUCE IT TO 9 BECAUSE OF PYTHON-0-INDEX START
setpoint_data = client.read_holding_registers(address=20209, count=2, unit=1)
reference = client.read_holding_registers(address=16009, count=1, unit=1)
#values = client.write_register(9, 0)

###THIS WILL PRINT ANY SITUATION IN CASE THAT THE ADDRESS IS NOT VALID
#value = ((f'Modbus error: {values}') if values.isError() else values.registers)
#print(value)
#print(values.registers)
setpoint = setpoint_data.registers[1]
print(setpoint)

client.close()
