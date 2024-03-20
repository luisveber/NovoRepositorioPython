import os
import subprocess
from configparser import ConfigParser
import time
import cryptocode

config = ConfigParser()
chave = "1"
try:
    config.read('CONFIG.ini')
except:
    print("Arquivo de Configuração com erro")
    raise SystemExit()


# Função para abrir um programa .exe
def abrir_programa(exe_path, exe_path2):
    programas = [exe_path, exe_path2]
    for programa in programas:
        try:
            subprocess.Popen([programa])
            time.sleep(3)
        except Exception as e:
            print(f"Erro ao abrir o programa: {e}")


# Função para limpar um arquivo .txt
def limpar_arquivo(txt_path):
    if os.path.exists(txt_path):
        try:
            with open(txt_path, 'w') as arquivo:
                arquivo.truncate()
            print(f"Dados em '{txt_path}' foram apagados.")
        except Exception as e:
            print(f"Erro ao limpar o arquivo: {e}")
    else:
        print(f"O Arquivo '{txt_path}' não existe")


# Função para apagar um arquivo .txt
def apagar_arquivo(txt_path):
    if os.path.exists(txt_path):
        try:
            os.remove(txt_path)
            print(f"Arquivo '{txt_path}' foi apagado.")
        except Exception as e:
            print(f"Erro ao apagar o arquivo: {e}")
    else:
        print(f"O Arquivo '{txt_path}' não existe")


p1 = cryptocode.decrypt(config["PATH"]["STARTPROGRAM01"], chave)
p2 = cryptocode.decrypt(config["PATH"]["STARTPROGRAM02"], chave)
p3 = cryptocode.decrypt(config["PATH"]["FILE"], chave)
# Chamando as funções para abrir o programa .exe, limpar e apagar os arquivos .txt
if config["PATH"]["STATUS"] == 'limpar':
    limpar_arquivo(p3)
elif config["PATH"]["STATUS"] == 'apagar':
    apagar_arquivo(p3)
else:
    limpar_arquivo(p3)

abrir_programa(p1, p2)
exit()
