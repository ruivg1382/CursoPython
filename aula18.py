import tkinter as tk

root=tk.Tk()

root.title("Aplicação nº 18")

window_width=400
window_heigth=600

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

center_x=int(screen_width/2-window_width/2)
center_y=int(screen_height/2-window_heigth/2)

root.geometry(f"{window_width}x{window_heigth}+{center_x}+{center_y}")

root.resizable(True,True)

root.minsize(300,300)
root.maxsize(800,800)
# estado maximizado
root.state("zoomed")



#root.state("iconic") -> como icone na rodapé

# root.state("normal")







root.mainloop()