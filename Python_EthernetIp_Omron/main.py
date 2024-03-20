from pylogix import PLC

clp = PLC()
# Endereço IP do PLC OMRON NX1P2
clp.IPAddress = '192.168.250.1'
clp.Write('VALOR_OUTPUT',100)
result = clp.Read('VALOR_OUTPUT')
mac1 = clp.Read('MAC1_INPUT')
print(result)
clp.Write('MAC1_INPUT',[True,False])

