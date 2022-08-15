import tkinter as tk

from tkinter import ttk

def enter(event):
    print(event)
    print(event.keysym)
    print(event.keycode)



root=tk.Tk()

root.geometry("400x400+100+100")

btn=ttk.Button(root,text="Botão")
#btn.bind("<Control-KeyPress-x>",enter)
btn.bind("<Any-KeyPress>",enter)
btn.pack(expand="True")




root.mainloop()