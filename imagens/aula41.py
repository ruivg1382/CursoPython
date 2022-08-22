import tkinter as tk
from tkinter import ttk


class Student:

    nome=""
    idade=0
    morada=""

    def __init__(self,nome, idade,morada):
        self.nome=nome
        self.idade=idade
        self.morada=morada




root=tk.Tk()


aluno1=Student("Emma Gonçalves",23,"Cabo Verde")





root.title(aluno1.nome)
root.iconbitmap("imagens/Linux.ico")

texto=tk.StringVar()
texto.set("Your name please")
lbl1=ttk.Label(root, text="Nome do Aluno: ")
text_field=ttk.Entry(root,textvariable=texto)
text_field.focus()
btn=ttk.Button(root,text="Ok")

root.geometry("300x300+100+100")
root["bg"]="#00ee56"

lbl1.pack()
text_field.pack()
btn.pack()





root.mainloop()