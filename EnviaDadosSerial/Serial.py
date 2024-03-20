import serial
import time
import io

porta_serial = serial.Serial('COM6', 9600)
dados = '1'
porta_serial.write(dados.encode())
porta_serial.close()

porta_serial2 = serial.Serial('COM6', 9600)
porta_serial2.timeout = 3
dadoslidos = porta_serial2.readline().decode().strip()

print(dadoslidos)
with open('teste.txt','w') as arquivo:
    arquivo.write(dadoslidos)
porta_serial2.close()


porta_seria3 = serial.Serial('COM6', 9600)

dados = '0'
porta_seria3.write(dados.encode())
porta_seria3.close()


