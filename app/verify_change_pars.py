coms = ("COM1", "COM2", "COM3", "COM4", "COM5")
baudrates = (9600, 19200, 28800, 38400, 57600, 76800, 115200)
parities = ("E", "O", "N")
bytesizes = (7, 8)
stopbits = (0, 1, 2)

def change_par(parameter, new_value):
    with open('config.json', 'w') as config_file:
        print("hi")

def verify_port(port):
    if port in coms:
        return True
    else:
        return False
def verify_baudrate(baudrate):
    print("hi1")
def verify_parity(parity):
    print("hi2")
def verify_bytesize(bytesize):
    print("hi3")
def verify_stopbits(stopbit):
    print("hi4")
def verify_timeout():
    print("hi5")
