import tkinter as tk
from tkinter import ttk


root=tk.Tk()

def entrar(event):
    print(event.keysym)

root.geometry("400x400+100+100")
btn=ttk.Button(root,text="Entrar")
btn.bind("<Any-KeyPress>",entrar)
btn.pack(expand="True")

btn2=ttk.Button(
    root, 
    text="cancelar",
    command=lambda:btn.unbind("<Any-KeyPress>")
)
btn2.pack(expand="True")

root.mainloop()





