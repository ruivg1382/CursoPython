
import tkinter as tk
from tkinter import BOTTOM, LEFT, RIGHT, TOP, ttk

root=tk.Tk()

lbl1=ttk.Label(root,text="Top")
lbl2=ttk.Label(root,text="Right")
lbl3=ttk.Label(root,text="Left")
lbl4=ttk.Label(root,text="Bottom")


root.geometry("400x400+200+200")
lbl1.pack(side=TOP)
lbl2.pack(side=RIGHT)
lbl3.pack(side=LEFT)
lbl4.pack(side=BOTTOM)


root.mainloop()