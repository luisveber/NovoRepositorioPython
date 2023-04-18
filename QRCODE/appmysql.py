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
win.geometry("800x600")

def popular():
    conexao = mysql.connector.connect(
    host ="auth-db727.hstgr.io",
    user = "u652056245_luisveber",
    password = "Semprom2014",
    database = "u652056245_Teste"
    )
    cursor = conexao.cursor()
    tv.delete(*tv.get_children())
    vquery = f'SELECT * FROM qrcode ORDER BY id'
    cursor.execute(vquery)
    linha = cursor.fetchall()
    for i in linha:
        tv.insert("",'end',values=(i[1],i[0]))
    cursor.close()
    conexao.close()

def getQRCODE(event):
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
    print(resultado)
    if len(resultado)!=0:
        messagebox.showerror(title="AVISO",message="AVISO, O TEXTO DIGITADO JÁ ESTÁ CADASTRADO!!!")
        cmdinsertrpt = f'INSERT INTO qrcodeRepeat (qrcode) VALUES ("{Rqrcode}")'
        cursor.execute(cmdinsertrpt)
        conexao.commit()
    else:
        messagebox.showerror(title="AVISO",message="O TEXTO DIGITADO SERÁ CADASTRADO!!!")
        cmdinsert = f'INSERT INTO qrcode (qrcode) VALUES ("{Rqrcode}")'
        cursor.execute(cmdinsert)
        conexao.commit()
    entry.delete(0,END)
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
                               corner_radius=20)
                               #validate="none",validatecommand=getQRCODE)                               
entry.place(relx = 0.5,rely = 0.5, anchor = CENTER)
entry.bind('<Return>',getQRCODE)
entry.pack(padx = 20,pady= 10)

quadroGrid = LabelFrame(win,text="QRCODE")

quadroGrid.pack(fill="both",expand="yes",padx="10",pady="10")
tv = ttk.Treeview(quadroGrid,columns=("id",'qrcode'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('qrcode',minwidth=0,width=250)
tv.heading('id',text='ID')
tv.heading('qrcode',text='QRCODE')
tv.pack()
popular()
#button = customtkinter.CTkButton(master=win,
#                                 font = ('Century Gothic',20),
#                                 width = 400,
#                                 height = 50,
#                                 border_width = 0,
#                                 corner_radius = 20,
#                                 text = "CONFIRMA",command=getQRCODE)
#button.place(relx = 0.5,rely = 0.5, anchor = CENTER)
#button.pack(padx = 20,pady = 10)

win.mainloop()