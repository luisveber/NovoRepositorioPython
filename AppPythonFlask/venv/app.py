import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter
customtkinter.set_appearance_mode("dark")
win = customtkinter.CTk()
wdt = win.winfo_screenwidth()
hgt = win.winfo_screenheight()
win.title('QRCODE')
#win.geometry("%dx%d" % (wdt,hgt))
win.geometry("300x400")



def getQRCODE():
    conexao = mysql.connector.connect(
    host ="auth-db727.hstgr.io",
    user = "u652056245_luisveber",
    password = "Semprom2014",
    database = "u652056245_Teste"
    )
    cursor = conexao.cursor()
    Rqrcode = entry.get()
    
    cmdread = f'SELECT qrcode FROM  qrcode where qrcode = "{Rqrcode}"  '
    cursor.execute(cmdread)
    resultado = cursor.fetchall()
    if len(resultado)!=0:
        messagebox.showerror(title="AVISO",message="AVISO, O TEXTO DIGITADO JÁ ESTÁ CADASTRADO!!!")
    else:
        messagebox.showerror(title="AVISO",message="O TEXTO DIGITADO SERÁ CADASTRADO!!!")
        cmdinsert = f'INSERT INTO qrcode (qrcode) VALUES ("{Rqrcode}")'
        cursor.execute(cmdinsert)
        conexao.commit()
    cursor.close()
    conexao.close()




label = customtkinter.CTkLabel(master=win,
                               font=('Century Gothic',20),
                               width=400,
                               height=50,
                               fg_color=("white", "black"),
                               corner_radius=20,
                               text="QRCODE")
label.place(relx=0.5, rely=0.5,anchor=N)
label.pack(padx = 20,pady= 10)
entry = customtkinter.CTkEntry(master = win,
                               font=('Century Gothic',20),
                               width=400,
                               height=50,
                               border_width=1,
                               corner_radius=20,
                               validate="none",validatecommand=getQRCODE)
entry.place(relx = 0.5,rely = 0.5, anchor = CENTER)
entry.pack(padx = 20,pady= 10)
button = customtkinter.CTkButton(master=win,
                                 font = ('Century Gothic',20),
                                 width = 400,
                                 height = 50,
                                 border_width = 0,
                                 corner_radius = 20,
                                 text = "CONFIRMA",command=getQRCODE)
button.place(relx = 0.5,rely = 0.5, anchor = CENTER)
button.pack(padx = 20,pady = 10)

win.mainloop()