from tkinter import *
from tkinter import messagebox
from presentacion.vistas.ventanaPrincipal import VentanaPrincipal

class VentanaCuenta(object):

  def __init__(self,ctrlCuenta,persona):

    # variables de inyeccion
    self.ctrlCuenta = ctrlCuenta
    self.persona = persona

    self.root = Tk()
    self.root.title("Fili arl")
    self.root.iconbitmap("presentacion/images/onepiece.ico")

    # tamaño y centrado de ventana
    self.openCenter(self.root,350,480)

    # Frame Principal
    mainFrame = Frame(self.root)
    mainFrame.config(bg="black")
    mainFrame.pack(fill="both", expand="True")

    titulo = Label(mainFrame, text="Operaciones de Cuenta")
    titulo.config(bg="black", fg="white", font=("Sans Serif",20))
    titulo.pack(pady=20)

    bienvenido = Label(mainFrame, text=f"Bienvenido(a) {self.persona.nombreCompleto()}")
    bienvenido.config(bg="black", fg="white", font=("Sans Serif",12))
    bienvenido.pack(pady=10)

    self.noCuenta = Label(mainFrame, text=f"Cuenta: {self.persona.getCuenta().getId()}, Saldo: $ {self.persona.getCuenta().getSaldo()} MXN")
    self.noCuenta.config(bg="black", fg="white", font=("Sans Serif",8))
    self.noCuenta.pack(pady=10)

    # Frame de grid para botones
    gridButtons = Frame(mainFrame)
    gridButtons.config(bg="black")
    gridButtons.pack()

    btnRetiro = Button(gridButtons, text="Retirar", command=self.retirar)
    btnRetiro.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="blue", fg="white", cursor="hand2")
    btnRetiro.grid(row=0, column=0, pady=20, padx=3)

    btnDeposito = Button(gridButtons, text="Depositar", command=self.depositar)
    btnDeposito.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="green", fg="white", cursor="hand2")
    btnDeposito.grid(row=0, column=1, pady=20, padx=3)

    btnConsulta = Button(gridButtons, text="Consultar", command=self.consultar)
    btnConsulta.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="salmon", fg="white", cursor="hand2")
    btnConsulta.grid(row=1, column=0, pady=20, padx=3)

    btnSalir = Button(gridButtons, text="Salir", command=self.cerrarSesion)
    btnSalir.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="red", fg="white", cursor="hand2")
    btnSalir.grid(row=1, column=1, pady=20, padx=3)

    self.root.resizable(False,False)
    self.root.mainloop()

  def depositar(self):
    self.dialogo = Toplevel()
    self.dialogo.iconbitmap("presentacion/images/onepiece.ico")
    self.openCenter(self.dialogo,250,100)
    self.dialogo.resizable(0,0)
    self.dialogo.title("Despositar Saldo")

    dialogoMainFrame = Frame(self.dialogo)
    dialogoMainFrame.config(bg="black")
    dialogoMainFrame.pack(fill="both", expand="True")

    labelCantidad = Label(dialogoMainFrame, text="Cantidad:")
    labelCantidad.config(bg="black", fg="white")
    labelCantidad.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    self.entryCantidad = Entry(dialogoMainFrame)
    self.entryCantidad.config(font=("Sans Serif",10), borderwidth=0, relief="flat", justify="center")
    self.entryCantidad.focus()
    self.entryCantidad.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    btnDeposito = Button(dialogoMainFrame, text='Depositar', command=self.depositarSaldo)
    btnDeposito.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="green", fg="white", cursor="hand2")
    btnDeposito.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    btnCancelar = Button(dialogoMainFrame, text='Cancelar', command=self.dialogo.destroy)
    btnCancelar.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="red", fg="white", cursor="hand2")
    btnCancelar.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    self.dialogo.transient(master=self.root)
    self.dialogo.grab_set()
    self.root.wait_window(self.dialogo)

  def depositarSaldo(self):
    try:
      cantidad = float(self.entryCantidad.get())
      deposito = self.ctrlCuenta.deposito(cantidad,self.persona.getCuenta())
      if deposito:
        messagebox.showinfo("Informacion de cuenta",f"Se han depositado ${cantidad} MXN a tu cuenta")
        self.noCuenta.config(text=f"Cuenta: {self.persona.getCuenta().getId()}, Saldo: $ {self.persona.getCuenta().getSaldo()} MXN")
        self.dialogo.destroy()
      else:
        messagebox.showerror("Error", "Saldo Invalido. Solo puede depositar hasta $5000 MXN")
    except ValueError:
      messagebox.showerror("Error", "Saldo Invalido")

  def consultar(self):
    messagebox.showinfo("Informacion de cuenta",f"{self.persona.getCuenta().toString()}")

  def retirar(self):
    self.dialogo = Toplevel()
    self.dialogo.iconbitmap("presentacion/images/onepiece.ico")
    self.openCenter(self.dialogo,250,100)
    self.dialogo.resizable(0,0)
    self.dialogo.title("Retirar Saldo")

    dialogoMainFrame = Frame(self.dialogo)
    dialogoMainFrame.config(bg="black")
    dialogoMainFrame.pack(fill="both", expand="True")

    labelCantidad = Label(dialogoMainFrame, text="Cantidad:")
    labelCantidad.config(bg="black", fg="white")
    labelCantidad.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    self.entryCantidad = Entry(dialogoMainFrame)
    self.entryCantidad.config(font=("Sans Serif",10), borderwidth=0, relief="flat", justify="center")
    self.entryCantidad.focus()
    self.entryCantidad.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    btnRetiro = Button(dialogoMainFrame, text='Retirar', command=self.retirarSaldo)
    btnRetiro.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="green", fg="white", cursor="hand2")
    btnRetiro.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    btnCancelar = Button(dialogoMainFrame, text='Cancelar', command=self.dialogo.destroy)
    btnCancelar.config(width=10, highlightbackground="white", highlightcolor="white", highlightthickness=1, bg="red", fg="white", cursor="hand2")
    btnCancelar.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    self.dialogo.transient(master=self.root)
    self.dialogo.grab_set()
    self.root.wait_window(self.dialogo)

  def retirarSaldo(self):
    try:
      cantidad = float(self.entryCantidad.get())
      retiro = self.ctrlCuenta.retiro(cantidad,self.persona.getCuenta())
      if retiro:
        messagebox.showinfo("Informacion de cuenta",f"Se han retirado ${cantidad} MXN de tu cuenta")
        self.noCuenta.config(text=f"Cuenta: {self.persona.getCuenta().getId()}, Saldo: $ {self.persona.getCuenta().getSaldo()} MXN")
        self.dialogo.destroy()
      else:
        messagebox.showerror("Error", "Saldo insuficiente")
    except ValueError:
      messagebox.showerror("Error", "Saldo Invalido")

  def cerrarSesion(self):
    self.root.destroy()
    VentanaPrincipal(self.ctrlCuenta)

  def openCenter(self, componente, width, height):
    centro_x = int(componente.winfo_screenwidth()/2 - width/2)
    centro_y = int(componente.winfo_screenheight()/2 - height/2)
    componente.geometry(f"{width}x{height}+{centro_x}+{centro_y}")
