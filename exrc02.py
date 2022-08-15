import tkinter as tk
from tkinter import ttk

root=tk.Tk()

numero=0

def acionar():
    root.config(background="violet")
    lbl.config(text="Olá")
root.title("Novo Exercícios")



root.iconbitmap("imagens/Linux.ico")

root.geometry("400x400+50+50")


btn=ttk.Button(root,text="Novo Botão", command=acionar)

lbl=ttk.Label(root,text=numero)
lbl.pack()
btn.pack()



root.mainloop()