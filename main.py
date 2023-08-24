print("Pc-DanfossDrive Modbus communication")
print("Powered By ATPRO Solutions V2308.1001")

import sys
from app import help_module, client

help_module.display_help_cmds()
while (True):
    cmd = input("cmd (-h to get help): ")
    match cmd:
        case "-h":
            help_module.display_help_cmds()
        case "close":
            sys.exit()
        case "cfg -clt -p":
            driveClient = client.DriveClient()
            driveClient.print_cfg()
        case "cfg -clt -c":
            print("nonusable command")
            #driveClient = client.DriveClient()
            #driveClient.modify_cfg()
        case "clt -rd -frq":
            driveClient = client.DriveClient()
            driveClient.read_frequency()
        case _:
            print("Error: command does not exists")
