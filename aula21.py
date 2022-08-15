import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.title("Apicação nº22")
root.iconbitmap("imagens/Linux.ico")

ttk.Label(root, text="Primeiro metódo").pack()

lbl2=ttk.Label(root)
lbl2["text"]="Segundo metódo"
lbl2.pack()

lbl3=ttk.Label(root)
lbl3.config(text="Terceiro metódo")
lbl3.pack()

root.geometry("500x500+50+50")










root.mainloop()