import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()

def executar(event=None):
    if(textField.get()!="your name"):
        showinfo("Mansagem",textField.get())
        texto.set("your name")
        textField.select_range(0, tk.END)




label1=ttk.Label(root, text="nome: ")
texto=tk.StringVar()
texto.set("your name")
textField=tk.Entry(root, textvariable=texto)
textField.select_range(0, tk.END)
textField.focus()
textField.pack()

btn=ttk.Button(root,text="Ok", command=executar)
btn.pack(ipadx=10,ipady=10)

root.geometry("400x400+100+100")


root.mainloop()