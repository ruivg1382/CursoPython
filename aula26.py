import tkinter as tk
from tkinter import ttk


root=tk.Tk()


def acionar(event):
    print(event.keysym)


root.geometry("500x500+200+200")
btn=ttk.Button(root,text="Dispara")
btn.pack(expand="True")

root.bind("<Any-KeyPress>",acionar)





root.mainloop()