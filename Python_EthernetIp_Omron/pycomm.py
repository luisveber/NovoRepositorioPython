from pycomm3 import LogixDriver

plc = LogixDriver()

plc.IPAdress = '192.168.250.1'

print(plc.read('D100'))