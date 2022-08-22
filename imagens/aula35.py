import tkinter as tk
from tkinter import ttk




root=tk.Tk()


def calcular():
    num1=int(entrada1.get())
    num2=int(entrada2.get())
    cal=num1+num2
    resultado["text"]=cal
   

    

label1=ttk.Label(root, text="1º Numero:")
entrada1=ttk.Entry(root)

label2=ttk.Label(root, text="2º Numero:")
entrada2=ttk.Entry(root)

botao=ttk.Button(root, text="Calcular",command=calcular)
resultado=ttk.Label(root, text="...")

label1.place(x="100",y="100")
entrada1.place(x="300",y="100")

label2.place(x="100",y="200")
entrada2.place(x="300", y="200")
botao.place(x="300", y="250")
resultado.place(x="300",y="300")
root.geometry("600x400+100+100")


root.mainloop()
