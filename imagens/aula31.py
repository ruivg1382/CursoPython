import tkinter as tk
from tkinter import ttk


root=tk.Tk()

root.title("Tela de Login")

root.iconbitmap("imagens/Linux.ico")

lbl1=ttk.Label(root,text="Login")
lbl2=ttk.Label(root,text="Password")

ent=ttk.Entry(root)
ent2=ttk.Entry(root)

btn=ttk.Button(root,text="Entrar")


root.geometry("400x400+100+100")

lbl1.pack()
ent.pack()
lbl2.pack()
ent2.pack()

btn.pack()







root.mainloop()