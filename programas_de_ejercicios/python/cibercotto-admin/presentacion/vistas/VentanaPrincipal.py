from tkinter import *

class VentanaPrincipal():

  def __init__(self, ctrlPrincipal):
    self.ctrlPrincipal = ctrlPrincipal
    self.disenio()

  def disenio(self):
    self.root = Tk()
    self.root.title("Fili Arl - CibberCotto")
    self.openCenter(self.root,320,480)

    btnInscripciones = Button(self.root, text="Trabajos", command=self.abrirVentanaTrabajos)
    btnInscripciones.pack()

    btnInscripciones = Button(self.root, text="Admin Inscripciones", command=self.abrirVentanaInscripciones)
    btnInscripciones.pack()

    self.root.resizable(False,False)
    self.root.mainloop()


  ######################
  # Metodos auxiliares #
  ######################

  def openCenter(self, componente, width, height):
    centro_x = int(componente.winfo_screenwidth()/2 - width/2)
    centro_y = int(componente.winfo_screenheight()/2 - height/2)
    componente.geometry(f"{width}x{height}+{centro_x}+{centro_y}")

  ###################
  # Metodos Eventos #
  ###################

  def abrirVentanaInscripciones(self):
    self.root.destroy()
    self.ctrlPrincipal.abrirVentanaInscripciones()

  def abrirVentanaTrabajos(self):
    self.root.destroy()
    self.ctrlPrincipal.abrirVentanaTrabajos()
