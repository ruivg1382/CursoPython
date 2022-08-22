import tkinter as tk
from tkinter import ttk


def Aplicar():
   print("Aplicado")

root=tk.Tk()



root.geometry("400x400+100+100")
foto=tk.PhotoImage(file="imagens/logo.png")

root.title("Software Solution")
root.iconbitmap("imagens/Linux.ico")

btn=ttk.Button(root, text="Aplicar", command=Aplicar)

label=ttk.Label(
    root,
    image=foto,
    text="Empresa de Desenvolvimento de Software",
    font=("tahoma",12,"bold"),
    foreground="pink",
    background="white",
    compound="top",
    borderwidth=10,
    relief="solid", #flat, bridge
    #wraplength=50
)

label.pack(expand="True")
btn.pack()



root.mainloop()