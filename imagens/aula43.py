import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.title("Cabo Verde")
root.geometry("400x400+100+100")

label=ttk.Label(root, text="You name: ")
texto=tk.StringVar()
texto.set("Digite o seu nome")
text_field=ttk.Entry(root,textvariable=texto)
text_field.select_range(0, tk.END)
text_field.focus()

label2=ttk.Label(root, text="Password")
text_pass=ttk.Entry(root, show="*")
btn = ttk.Button(root, text="Entrar", command=lambda:print(text_field.get()))

label.pack()
text_field.pack()
label2.pack()
text_pass.pack()
btn.pack()




root.mainloop()