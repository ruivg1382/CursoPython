import tkinter as tk
from tkinter import ttk


root=tk.Tk()

def btn_clic():
    novo=entrada.get()
    lbl["text"]=novo



entrada=ttk.Entry(root)
btn=ttk.Button(root, text="clique-me", command=btn_clic)
lbl=ttk.Label(root, text="Aguardando...")


root.geometry("400x400+300+300")

entrada.pack()
btn.pack()
lbl.pack()

root.mainloop()