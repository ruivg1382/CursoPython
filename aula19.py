import tkinter as tk


root=tk.Tk()

root.title("Aplicação 19")

width=300
height=400

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=int(screen_width/2-width/2)
y=int(screen_height/2-height/2)

root.geometry(f"{width}x{height}+{x}+{y}")
root.iconbitmap("imagens/Linux.ico")

root.attributes("-alpha",1)
#root.attributes("-topmost",1)
root.lift() #mover para cima
#root.lower() #mover para baixo








root.mainloop()