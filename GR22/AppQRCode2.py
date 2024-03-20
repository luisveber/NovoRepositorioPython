import tkinter
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
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer.configure(background="#1C4287")
        self.segundoContainer["padx"] = 30
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.configure(background="#1C4287")
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer.configure(background="#1C4287")
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer.configure(background="#1C4287")
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.autenticar = Button(self.primeiroContainer)
        self.autenticar["text"] = "Selecionar Primeiro Programa"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 30
        self.autenticar["command"] = self.browseFiles
        self.autenticar.pack()

        self.autenticar2 = Button(self.segundoContainer)
        self.autenticar2["text"] = "Selecinar Segundo Programa"
        self.autenticar2["font"] = ("Calibri", "12")
        self.autenticar2["width"] = 30
        self.autenticar2["command"] = self.browseFiles2
        self.autenticar2.pack()

        self.autenticar3 = Button(self.quartoContainer)
        self.autenticar3["text"] = "Abrir Programas"
        self.autenticar3["font"] = ("Calibri", "12")
        self.autenticar3["width"] = 30
        self.autenticar3["command"] = self.WriteArquivoIni
        self.autenticar3.pack()

        self.autenticar4 = Button(self.quintoContainer)
        self.autenticar4["text"] = "Validar"
        self.autenticar4["font"] = ("Calibri", "12")
        self.autenticar4["width"] = 30
        self.autenticar4["command"] = self.WriteArquivoIni
        self.autenticar4.pack()

        self.label_file_explorer = Label(self.primeiroContainer)
        self.label_file_explorer["font"] = ("Calibri", "12")
        self.label_file_explorer.configure(text="Primeiro Programa a Ser Aberto", background="#1C4287", foreground="white")
        self.label_file_explorer.pack()

        self.label_file_explorer2 = Label(self.segundoContainer)
        self.label_file_explorer2["font"] = ("Calibri", "12")
        self.label_file_explorer2.configure(text="Segundo Programa a Ser Aberto", background="#1C4287", foreground="white")
        self.label_file_explorer2.pack()

        self.Menus()

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label="Menu", menu= filemenu)
        menubar.add_cascade(label="Teste", menu= filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Janela", command=self.selecionarprogramas)


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

    def WriteArquivoIni(self):
        config2 = ConfigParser()
        config2["PATH"] = {"STARTPROGRAM01": filename,
                          "STARTPROGRAM02": filename2,
                          "FILE": "C:/Sistema/teste1.txt",
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

    def selecionarprogramas(self):


        janela2 = tkinter.Toplevel()
        janela2.title('Selecionar Programas')
        janela2.geometry("400x300")
        janela2.iconbitmap("D:\Python\GR22\icone.ico")
        janela2.configure(bg="#1C4287")






root = Tk()
root.title("File Explorer")
root.geometry("400x300")
root.iconbitmap("D:\Python\GR22\icone.ico")
root.configure(bg="#1C4287")
Application(root)
root.mainloop()
