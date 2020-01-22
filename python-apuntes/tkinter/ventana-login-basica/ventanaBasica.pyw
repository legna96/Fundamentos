# config -> establecle propiedades al componente
# pack -> agrega componentes
# place -> agrega y ubica en cordenadas (x,y)
# grid ->  agrega elementos de forma de tabla
# geometry solo es para la raiz, los demas componentes establecen su tamaño en config
# mainloop -> es el que visaliza la ventana
# command ->  esta dirctiva enlaza un evento a los botones

from tkinter import *

# config raiz
root = Tk()
root.title("Ventana Basica")
root.iconbitmap("onepiece.ico")

# tamaño y centrado de ventana
rootWidth = 350
rootHeight = 480
centro_x = int(root.winfo_screenwidth()/2 - rootWidth/2)
centro_y = int(root.winfo_screenheight()/2 - rootHeight/2)
root.geometry(f"{rootWidth}x{rootHeight}+{centro_x}+{centro_y}")

#config frame Principal
mainFrame = Frame()
mainFrame.config(bg="black")
mainFrame.pack(fill="both", expand="True")

#config Frame Titulo
tituloFrame = Frame(mainFrame)
tituloFrame.config(bg="black")
tituloFrame.pack()

# config label
label = Label(tituloFrame, text="Hola TKinter")
label.config(fg="white", bg="black", font=("Sans Serif",20))
label.grid(row=0, column=0, pady=15)

# config label con imagen
img = PhotoImage(file="login.png")
labelImg = Label(mainFrame, image=img, bg="black")
labelImg.pack()

# Frame de grid para datos
gridFrame = Frame(mainFrame)
gridFrame.config(bg="black")
gridFrame.pack()

# label user
labelUser = Label(gridFrame, text="Usuario:")
labelUser.config(fg="white", bg="black", font=("Sans Serif",12))
labelUser.grid(row=0, column=0, sticky="w", pady=3, padx=3)

# campo de texto user
entryUser = Entry(gridFrame)
entryUser.config(font=("Sans Serif",10), borderwidth=0, relief="flat", justify="center")
entryUser.grid(row=0, column=1, sticky="e", pady=3, padx=3)

# label email
labelEmail = Label(gridFrame, text="Contraseña:")
labelEmail.config(fg="white", bg="black", font=("Sans Serif",12))
labelEmail.grid(row=1, column=0, sticky="w", pady=3, padx=3)

# campo de texto contraseña
entryContraseña = Entry(gridFrame)
entryContraseña.config(font=("Sans Serif",10), borderwidth=0, relief="flat", justify="center", show="*")
entryContraseña.grid(row=1, column=1, sticky="e", pady=3, padx=3)

# Frame de grid para botones
gridButtons = Frame(mainFrame)
gridButtons.config(bg="black")
gridButtons.pack()

# boton ingresar
btnIngresar = Button(gridButtons, text="Ingresar", command= lambda: print(f"Usuario: {entryUser.get()}, Contraseña: {entryContraseña.get()}") )
btnIngresar.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="green", fg="white", cursor="hand2")
btnIngresar.grid(row=2, column=0, sticky="w", pady=20, padx=3)

# boton salir
btnSalir = Button(gridButtons, text="Salir", command= lambda: exit())
btnSalir.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="red", fg="white", cursor="hand2")
btnSalir.grid(row=2, column=1, sticky="w", pady=20, padx=3)

root.resizable(False,False)
root.mainloop()
