import json
from pymodbus.client.sync import ModbusSerialClient
from . import verify_change_pars as verifications

#def change_par(parameter, new_value):
#    with open('config.json', 'w') as config_file:
#        print("hi")

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
client_config = config_data['client']

class DriveClient():
    def __init__(self):
        self.client = ModbusSerialClient(
            method   = "rtu",
            port     = client_config['port'],
            baudrate = client_config['baudrate'],
            parity   = client_config['parity'],
            bytesize = client_config['bytesize'],
            stopbits = client_config['stopbits'],
            timeout  = client_config['timeout']
        )

    def print_cfg(self):
        print("Drive modbus configuration:")
        print(self.client.comm_params)

    def modify_cfg(self):
        print("nonusable command")
        #i = 0
        #params = list(client_config.keys())
        #for par, val in client_config.items():
        #    print(f"{i}) {par}: {val}")
        #    i+=1
        #par_to_mod = (input("<option> -<new value>: "))
        #match int(par_to_mod[0]):
        #    case 0:
        #        if par_to_mod[3:] in coms:
        #    case 1: verifications.verify_baudrate(par_to_mod[3:])
        #    case 2: verifications.verify_parity(par_to_mod[3:])
        #    case 3: verifications.verify_bytesize(par_to_mod[3:])
        #    case 4: verifications.verify_stopbits(par_to_mod[3:])
        #    case 5: verifications.verify_timeout(par_to_mod[3:])
        #    case _: print("Parametro inexistente.")
        ##change_par(params[par_to_mod])

    def read_frequency(self):
        self.client.connect()
        reference = self.client.read_holding_registers(address=16009, count=1, unit=1)
        print(reference)
        self.client.close()