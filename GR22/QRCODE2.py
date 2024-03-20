import os
import subprocess
from configparser import ConfigParser
import time

config = ConfigParser()

try:
    config.read("CONFIG.ini")
except:
    print("Arquivo de Configuração com erro")
    raise SystemExit()

# Função para abrir um programa .exe
def abrir_programa(exe_path):
    try:
        os.system(f'"{exe_path}"')  # Substitua 'exe_path' pelo caminho do seu arquivo .exe

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

# Chamando as funções para abrir o programa .exe, limpar e apagar os arquivos .txt
if config["PATH"]["STATUS"] == 'limpar':
    limpar_arquivo(config["PATH"]["FILE"])
elif config["PATH"]["STATUS"] == 'apagar':
    apagar_arquivo(config["PATH"]["FILE"])
else:
    limpar_arquivo(config["PATH"]["FILE"])
abrir_programa(config["PATH"]["STARTPROGRAM01"])
time.sleep(3)
abrir_programa(config["PATH"]["STARTPROGRAM02"])
time.sleep(3)
exit()