import tkinter as tk
from tkinter import ttk



root=tk.Tk()

texto=tk.StringVar()
texto.set("Escreva o seu nome")

text_box=tk.Entry(root,textvariable=texto)

text_box.pack()






root.mainloop()