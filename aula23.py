import tkinter as tk
from tkinter import ttk

def CorButton(cor):
    root.config(background=cor)



root=tk.Tk()

root.title("App numero 23")

root.geometry("400x400+300+300")

button1=ttk.Button(root, text="botão I", command=lambda:CorButton("black"))
button1.pack()

button2=ttk.Button(root, text="botão I", command=lambda:CorButton("orange"))
button2.pack()


root.mainloop()