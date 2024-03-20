from tkinter import *
import cryptocode
from tkinter.filedialog import askopenfilename
import os
import subprocess
from configparser import ConfigParser
import time

config = ConfigParser()
chave = 1
try:
    config.read("CONFIG.ini")
except:
    print("Arquivo de Configuração com erro")
    raise SystemExit()
class Application:
    def __init__(self, master=None):
        self.root = root
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.configure(background="#1C4287")
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer.configure(background="#1C4287")
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.configure(background="#1C4287")
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer.configure(background="#1C4287")
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer.configure(background="#1C4287")
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.label_file_explorer = Label(self.primeiroContainer)
        self.label_file_explorer["font"] = ("Calibri", "15")
        self.label_file_explorer.configure(text="", background="#1C4287",foreground="white")
        self.label_file_explorer.pack()

        self.autenticar = Button(self.primeiroContainer)
        self.autenticar["text"] = "Selecionar  Serial_number.exe"
        self.autenticar["font"] = ("Calibri", "15")
        self.autenticar["width"] = 30
        self.autenticar["command"] = self.browseFiles
        self.autenticar.pack()

        self.label_file_explorer2 = Label(self.segundoContainer)
        self.label_file_explorer2["font"] = ("Calibri", "15")
        self.label_file_explorer2.configure(text="", background="#1C4287",foreground="white")
        self.label_file_explorer2.pack()

        self.autenticar2 = Button(self.segundoContainer)
        self.autenticar2["text"] = "Selecinar EZCAD.exe"
        self.autenticar2["font"] = ("Calibri", "15")
        self.autenticar2["width"] = 30
        self.autenticar2["command"] = self.browseFiles2
        self.autenticar2.pack()

        self.label_file_explorer3 = Label(self.terceiroContainer)
        self.label_file_explorer3["font"] = ("Calibri", "15")
        self.label_file_explorer3.configure(text="", background="#1C4287",
                                            foreground="white")
        self.label_file_explorer3.pack()

        self.autenticar3 = Button(self.terceiroContainer)
        self.autenticar3["text"] = "Selecinar Arquivo qrcode.txt"
        self.autenticar3["font"] = ("Calibri", "15")
        self.autenticar3["width"] = 30
        self.autenticar3["command"] = self.browseFiles3
        self.autenticar3.pack()

        self.label_file_explorer4 = Label(self.quartoContainer)
        self.label_file_explorer4["font"] = ("Calibri", "15")
        self.label_file_explorer4.configure(text="----------------------------------------------------", background="#1C4287",
                                            foreground="white")
        self.label_file_explorer4.pack()

        self.autenticar4 = Button(self.quartoContainer)
        self.autenticar4["text"] = "Salvar"
        self.autenticar4["font"] = ("Calibri", "15")
        self.autenticar4["width"] = 30
        self.autenticar4["command"] = self.WriteArquivoIni
        self.autenticar4.pack()

    def browseFiles(self):
        chave = "1"
        global filename
        msg = askopenfilename(filetypes = (("Arquivos de texto", "*.txt"), ("Arquivos exe", "*.exe")))
        filename = cryptocode.encrypt(msg, chave)
        self.label_file_explorer.configure(text= msg)
        return filename

    def browseFiles2(self):
        chave = "1"
        global filename2
        msg = askopenfilename(filetypes = (("Arquivos de texto", "*.txt"), ("Arquivos exe", "*.exe")))
        filename2 = cryptocode.encrypt(msg, chave)
        self.label_file_explorer2.configure(text= msg)
        return filename2

    def browseFiles3(self):
        chave = "1"
        global filename3
        msg = askopenfilename(filetypes = (("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))
        filename3 = cryptocode.encrypt(msg, chave)
        self.label_file_explorer3.configure(text= msg)
        return filename3

    def WriteArquivoIni(self):
        config2 = ConfigParser()
        config2["PATH"] = {"STARTPROGRAM01": filename,
                          "STARTPROGRAM02": filename2,
                          "FILE": filename3,
                          "STATUS": "Limpar"}

        with open("CONFIG.ini", 'w') as conf:
            config2.write(conf)

    def limpar_arquivo(self, txt_path):
        if os.path.exists(txt_path):
            try:
                with open(txt_path, 'w') as arquivo:
                    arquivo.truncate()
                print(f"Dados em '{txt_path}' foram apagados.")
            except Exception as e:
                print(f"Erro ao limpar o arquivo: {e}")
        else:
            print(f"O Arquivo '{txt_path}' não existe")

    def abrir_programa(self, exe_path, exe_path2):
        programas = [exe_path, exe_path2]
        for programa in programas:
            try:
                subprocess.Popen([programa])
                time.sleep(3)
            except Exception as e:
                print(f"Erro ao abrir o programa: {e}")

root = Tk()
root.title("File Explorer")
root.geometry("600x300")
root.maxsize(600,300)
root.minsize(600,300)
#root.iconbitmap("D:/Python/GR22_32/icone.ico")
root.configure(bg="#1C4287")
Application(root)
root.mainloop()
