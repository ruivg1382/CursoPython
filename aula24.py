import tkinter as tk
from tkinter import ttk

def enter(event):
    print("Tecla enter Precionado")

def changeColor(event):
    root.config(background="green")

def changeLabel(event):
    root.config(root.title("Hello"))
root=tk.Tk()


root.geometry("400x400+100+100")


btn = ttk.Button(root,text="executar")
btn.bind("<Return>",enter)
btn.bind("<Return>", changeColor,add="+")
btn.bind("<Return>", changeLabel,add="+")
btn.focus()
btn.pack(expand=True)





root.mainloop()