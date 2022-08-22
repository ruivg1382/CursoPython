import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter.messagebox import showinfo

root=tk.Tk()

def clicar():
    showinfo("Informação", "Processo de download concluido")

root.geometry("400x400+100+100")

iconImage=PhotoImage(file="imagens/logo.png")
btn=ttk.Button(
                root,
                image=iconImage,
                command=clicar
              )
btn.pack(ipadx=5,ipady=5,expand="True")




root.mainloop()