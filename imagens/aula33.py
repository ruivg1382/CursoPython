import tkinter as tk
from tkinter import ttk
from functools import partial


root=tk.Tk()

def bt_click(botao):
    print(botao["text"])


root.geometry("400x400+150+150")
btn1=ttk.Button(root,text="botão 1")
btn1["command"]=partial(bt_click,btn1)
btn2=ttk.Button(root,text="botão 2")
btn2["command"]=partial(bt_click,btn2)

btn1.pack()
btn2.pack()





root.mainloop()
