import tkinter as tk

root=tk.Tk()

root.title("Aplicação nº 17")

largura=500
altura=500

tela_w=root.winfo_screenwidth()
tela_h=root.winfo_screenheight()


posx=int(tela_w/2 - largura/2)
posy=int(tela_h/2 - altura/2)


root.geometry(f"{largura}x{altura}+{posx}+{posy}")





root.mainloop()