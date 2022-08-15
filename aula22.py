import tkinter as tk
from tkinter import ttk



def Clicar():
    num=0
    root.config(background="red")
    print("Botão Clicado "+str(num)+" vezes")
    num=num+1


def Second():
    root.config(background="yellow")

root=tk.Tk()

root.title("Aplicação com vinculação")

root.iconbitmap("imagens/Linux.ico")

root.geometry("500x500+100+100")

button=ttk.Button(root,text="Click here",command=Clicar)
button.pack()
button2=ttk.Button(root,text="Click in me", command=Second)
button2.pack()





root.mainloop()