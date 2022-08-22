import tkinter as tk
from tkinter import ttk

root=tk.Tk()
label1=ttk.Label(root,text="Meninas", background="red")

root.geometry("400x400+100+100")
label1.grid(row=0)
root.mainloop()
