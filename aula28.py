import tkinter as tk
from tkinter import ttk

root=tk.Tk()




root.geometry("400x400+100+100")

lbl=ttk.Label(root,
text="Minha nossa senhora\n hoje é seu dia",
background="black",
foreground="white",
padding="50",
anchor=tk.CENTER


)

lbl.pack(expand="True")




root.mainloop()