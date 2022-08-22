import tkinter as tk
from tkinter import ttk

root=tk.Tk()



def btn_click():
    lbl1["text"]="Yasmin"

root.geometry("400x400+200+200")
root.title("você e Eu")
root["bg"]="black"

lbl1=ttk.Label(root, text="Mariana")
btn=ttk.Button(root,text="Botão 1", command=btn_click)

lbl1.place(x="200", y="200")
btn.place(x="200",y="250")
root.mainloop()
