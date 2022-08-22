import tkinter as tk
from tkinter import ttk


root=tk.Tk()

root.title("minha Aplicação")


lbl_nome=ttk.Label(root,text="Nome: ")
text_nome=ttk.Entry(root)
lbl_password=ttk.Label(root, text="Password")
text_password=ttk.Entry(root, show="*")

btn=ttk.Button(root, text="Login", command=lambda:print(text_nome.get()))

lbl_nome.grid(column=2,row=2)
text_nome.grid(column=2, row=3)
lbl_password.grid(column=4, row=2)
text_password.grid(column=4, row=3)
btn.grid()






root.mainloop()