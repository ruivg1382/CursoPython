class Aula:
    sumario=""
    conteudo=""
    def __init__(self, conteudo,sumario):
        self.conteudo=conteudo
        self.sumario=sumario
    
    def showSumario(self):
        print(self.sumario)
    
    def showConteudo(self):
        print(self.conteudo)

    def modificarConteudo(self,novo):
        self.conteudo=novo


a1=Aula("Segurança Web","Continuação da aula anterior")

a1.showSumario()
a1.showConteudo()
a1.modificarConteudo("Perigo na Rede")
a1.showConteudo()

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
texto=a1.showConteudo()

root.geometry("400x400+100+100")
lbl=ttk.Label(root,text=texto,
padding=10,
background="pink",
foreground="black",

)

lbl.pack(expand="True")
root.mainloop()