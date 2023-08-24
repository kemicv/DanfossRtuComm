# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# SCRIPT THAT TAKES A READ OF PAR <X>, EACH READ IS TAKEN DURING <n> SECONDS  #
# EACH <N>ms                                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ms_btwn_reads = 3000
par = 1
seconds_to_read = 3

from pymodbus.client.sync import ModbusSerialClient
import logging, datetime

#region This shows all the transaction details
#FORMAT = ('%(asctime)-30s :%(lineno)-8s %(message)s')
#logging.basicConfig(format=FORMAT)
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

#endregion

rtupar = (par * 10) - 1
client = ModbusSerialClient(method="rtu", port="COM1", baudrate=115200,
                            parity="N", bytesize=8, stopbits=1, timeout=3)
reads = (seconds_to_read * 1000) // ms_btwn_reads #this gets how many reads will i take at the for loop
client.connect()
pols = 0
er_pols = 0
for x in range(reads):
    while True:
        #This structure allows me to comunicate each 100ms
        current_time = datetime.datetime.now()
        milliseconds = current_time.microsecond // 1000  # Get milliseconds
        if milliseconds % ms_btwn_reads == 0:
            try:
                reference = client.read_holding_registers(address=rtupar, count=3, unit=2)#unit refers to slave address
                print(reference.registers)
            except: 
                er_pols += 1
                print("Error: no com")
            pols += 1
            break
client.close()
success_rate = (pols - er_pols) / pols * 100
print(f"total pols: {pols}")
print(f"{success_rate}%")
