from tkinter import *
from tkinter import messagebox

class VentanaPrincipal(object):

  def __init__(self, ctrlCuenta):
    # variables de inyeccion
    self.ctrlCuenta = ctrlCuenta

    # config raiz
    self.root = Tk()
    self.root.title("Fili arl")
    self.root.iconbitmap("presentacion/images/onepiece.ico")

    # tamaño y centrado de ventana
    self.openCenter(self.root,350,480)

    #config frame Principal
    mainFrame = Frame()
    mainFrame.config(bg="black")
    mainFrame.pack(fill="both", expand="True")

    #config Frame Titulo
    tituloFrame = Frame(mainFrame)
    tituloFrame.config(bg="black")
    tituloFrame.pack()

    # config label Titulo
    label = Label(tituloFrame, text="Mi Banquito Seguro")
    label.config(fg="white", bg="black", font=("Sans Serif",20))
    label.grid(row=0, column=0, pady=15)

    # config label con imagen
    img = PhotoImage(file="presentacion/images/login.png")
    labelImg = Label(mainFrame, image=img, bg="black")
    labelImg.pack()

    # Frame de grid para datos
    dataFrame = Frame(mainFrame)
    dataFrame.config(bg="black")
    dataFrame.pack()

    # label nip
    labelNip = Label(dataFrame, text="Nip:")
    labelNip.config(fg="white", bg="black", font=("Sans Serif",12))
    labelNip.grid(row=0, column=0, sticky="w", pady=3, padx=3)

    # campo de texto nip
    self.entryNip = Entry(dataFrame)
    self.entryNip.config(font=("Sans Serif",10), borderwidth=0, relief="flat", justify="center", show="*")
    self.entryNip.focus()
    self.entryNip.grid(row=0, column=1, sticky="e", pady=3, padx=3)

    # Frame de grid para botones
    gridButtons = Frame(mainFrame)
    gridButtons.config(bg="black")
    gridButtons.pack()

    # boton ingresar
    btnIngresar = Button(gridButtons, text="Ingresar", command= self.ingresar)
    btnIngresar.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="green", fg="white", cursor="hand2")
    btnIngresar.grid(row=2, column=0, sticky="w", pady=20, padx=3)

    # boton salir
    btnSalir = Button(gridButtons, text="Salir", command= lambda: self.root.destroy())
    btnSalir.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="red", fg="white", cursor="hand2")
    btnSalir.grid(row=2, column=1, sticky="w", pady=20, padx=3)

    self.root.resizable(False,False)
    self.root.mainloop()

  def ingresar(self):
    nip = self.entryNip.get()
    persona = self.ctrlCuenta.login(nip)

    if persona == "Nip Invalido":
      messagebox.showerror("Error", "Nip Invalido")

    else:
      self.root.destroy()
      self.ctrlCuenta.abreVentanaCuenta(persona)

  def openCenter(self, componente, width, height):
    centro_x = int(componente.winfo_screenwidth()/2 - width/2)
    centro_y = int(componente.winfo_screenheight()/2 - height/2)
    componente.geometry(f"{width}x{height}+{centro_x}+{centro_y}")
