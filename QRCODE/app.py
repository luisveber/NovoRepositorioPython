from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win= Tk()
win.geometry("500x150")

def getQRCODE():
    tokens=[]
    tok = entry.get()
    tokens.append(tok)
    entry.delete(0, 'end')
    with open('qrcode.txt','r') as reader:
        tokens_reader = reader.readlines()
    tokens_reader = [item.replace('\n','') for item in tokens_reader]
    if tok in tokens_reader:
        messagebox.showerror(title="AVISO",message="AVISO, O TEXTO DIGITADO JÁ ESTÁ CADASTRADO!!!")
        #Label(win, text=tok, font= ('Century 15 bold')).pack(pady=20)
    with open('qrcode.txt','a') as writer:
        writer.write("\n")
        writer.write('\n'.join(set.difference(set(tokens), set(tokens_reader))))
    try:
        with open('qrcode.txt', 'r') as reader:
            tokens_reader = reader.readlines()
            with open('qrcode.txt', 'w') as fw:
                for line in tokens_reader:
                    if line.strip('\n') != '':
                        fw.write(line)
    except:
        Label(win, text=tok, font= ('Century 15 bold')).pack(pady=20)

entry= ttk.Entry(win,font=('Century 12'),width=40, validate="focusout",validatecommand=getQRCODE)
entry.pack(pady= 30)
button= ttk.Button(win, text="CONFIRMA", command= getQRCODE)
button.pack()
win.mainloop()





