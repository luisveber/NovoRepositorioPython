from tkinter import *
import cryptocode
from tkinter.filedialog import askopenfilename
import os
import subprocess
from configparser import ConfigParser
import time
config = ConfigParser()

class TelaPrincipal:
    def __init__(self, master=None):
        self.root = root
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.configure(background="#1C4287")
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer.pack()

        self.TrocaTela = Button(self.primeiroContainer)
        self.TrocaTela["text"] = "Troca Tela"
        self.TrocaTela["command"] = self.tela02
        self.TrocaTela.pack()

    def tela02(self):
        self.tela2 = Toplevel()
        self.tela2.title("Segunda Tela")
        self.tela2.geometry("500x500")
        self.tela2.configure(bg="#cccccc")
        self.tela2.transient(self.root)
        self.tela2.focus_force()
        self.tela2.grab_set()
        SegundaTela(self.tela2)


class SegundaTela:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "20")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.configure(background="#cccccc")

        self.root = root
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.configure(background="#cccccc")
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer.pack()

        self.TrocaTela = Button(self.primeiroContainer)
        self.TrocaTela["text"] = "Tela 02"
        self.TrocaTela.pack()









root = Tk()
root.title("Tela Inicial")
root.geometry("600x600")
root.configure(bg="#1C4287")
TelaPrincipal(root)


root.mainloop()
