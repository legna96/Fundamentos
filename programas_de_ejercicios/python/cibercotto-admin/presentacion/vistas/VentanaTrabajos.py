#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class VentanaTrabajos():

  color1 = "#FF3D5F"
  color2 = "#A738E8"
  color3 = "#4B6BFF"
  color4 = "#6CF1F5"
  color5 = "#42FF63"
  blackColor = "#000000"
  whiteColor = "#ffffff"

  font = "Sans Serif"

  def __init__(self, ctrlTrabajos):
    self.ctrlTrabajos = ctrlTrabajos
    self.disenio()


  def disenio(self):
    self.root = Tk()
    self.root.title("Fili Arl - CibberCotto")
    self.openCenter(self.root,600,600)

    mainframe = self.mainFrame()
    mainframe.pack(fill="both", expand="True")

    self.root.resizable(False,False)
    self.root.mainloop()

  def mainFrame(self):
    mainFrame = Frame(self.root)
    titulo = Label(mainFrame, text="Administrador De Trabajos")
    formFrame = self.formularioFrame(mainFrame)
    self.tabla = self.treeview(mainFrame)
    btnFrame = self.botonesFrame(mainFrame)

    mainFrame.config(
      bg=self.color4
    )

    titulo.config(
      bg=self.color4,
      fg=self.blackColor,
      font=(self.font, 18, "bold")
    )

    titulo.pack(pady=20)
    formFrame.pack(fill=None, expand=False)
    self.tabla.pack(pady=20)
    self.getTrabajos()
    btnFrame.pack(pady=20)

    return mainFrame

  def treeview(self, master):
    tabla = ttk.Treeview(master)
    tabla["columns"]=("#1","#2")

    tabla.column("#0", width=50)
    tabla.column("#1", width=150)
    tabla.column("#2", width=350)

    tabla.heading("#0",text="Clave")
    tabla.heading("#1",text="Titulo")
    tabla.heading("#2",text="Descripcion")

    return tabla


  def formularioFrame(self, master):
    formFrame = Frame(master)
    formFrame.config(
      bg=self.color4
    )

    titulo = Label(formFrame, text="Registrar Trabajo")
    titulo.config(
      bg=self.color4,
      fg=self.color3,
      font=(self.font, 12, "bold")
    )
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    labelClave = self.formatLabelFormulario(formFrame,"* Clave (3):")
    labelClave.grid(row=1,column=0, padx=5, pady=2, sticky="w")
    self.entryClave = Entry(formFrame, justify="center")
    self.entryClave.grid(row=1,column=1, padx=5, pady=2, sticky="w")

    labelTitulo = self.formatLabelFormulario(formFrame,"* Titulo:")
    labelTitulo.grid(row=2,column=0, padx=5, pady=2, sticky="w")
    self.entryTitulo = Entry(formFrame, justify="center")
    self.entryTitulo.grid(row=2,column=1, padx=5, pady=2, sticky="w")

    labelDescripcion = self.formatLabelFormulario(formFrame,"Descripcion:")
    labelDescripcion.grid(row=3,column=0, padx=5, pady=2, sticky="w")
    self.entryDescripcion = Entry(formFrame, justify="center")
    self.entryDescripcion.grid(row=3,column=1, padx=5, pady=2, sticky="w")


    btnAgregarTrabajo = Button(formFrame, text="Agregar", command=self.agregarTrabajo)
    btnAgregarTrabajo.config(
      bg=self.color5,
      fg=self.whiteColor,
      highlightbackground=self.whiteColor,
      highlightcolor=self.whiteColor,
      highlightthickness=1,
      cursor="hand2"
    )

    btnAgregarTrabajo.grid(row=4, column=0, columnspan=2, sticky=E+W, pady=10)

    return formFrame

  def botonesFrame(self, master):
    btnFrame = Frame(master)
    btnBorrar = Button(btnFrame, text="Borrar", command=self.borrarTrabajo)
    btnActualizar = Button(btnFrame, text="Actualizar", command=self.actualizarTrabajo)

    btnFrame.config(
      bg=self.color4
    )

    btnBorrar.config(
      width=10,
      bg=self.color1,
      fg=self.whiteColor,
      highlightbackground=self.whiteColor,
      highlightcolor=self.whiteColor,
      highlightthickness=1,
      cursor="hand2"
    )

    btnActualizar.config(
      width=10,
      bg=self.color3,
      fg=self.whiteColor,
      highlightbackground=self.whiteColor,
      highlightcolor=self.whiteColor,
      highlightthickness=1,
      cursor="hand2"
    )

    btnBorrar.grid(row=0, column=0, padx=5)
    btnActualizar.grid(row=0, column=1, padx=5)

    return btnFrame

  ######################
  # Metodos auxiliares #
  ######################

  def openCenter(self, componente, width, height):
    centro_x = int(componente.winfo_screenwidth()/2 - width/2)
    centro_y = int(componente.winfo_screenheight()/2 - height/2)
    componente.geometry(f"{width}x{height}+{centro_x}+{centro_y}")

  def formatLabelFormulario(self, master, texto):
    label = Label(master, text=texto)
    label.config(
      bg=f"{self.color4}",
      font=(self.font,10, "bold")
    )

    return label

  ###########
  # Eventos #
  ###########

  def agregarTrabajo(self):

    clave = self.entryClave.get()
    titulo = self.entryTitulo.get()
    desc = self.entryDescripcion.get()


    if "" in [clave, titulo]:
      messagebox.showerror("Error", "Se encontraron campos vacios")

    elif self.ctrlTrabajos.validaClave(clave) == False:
      messagebox.showerror("Error", "Clave No Valida\nLa clave debe ir compuesta de 3 caraceres")

    else:
      trabajo = (clave, titulo, desc)
      self.ctrlTrabajos.agregarTrabajo(trabajo)
      self.getTrabajos()


  def borrarTrabajo(self):
    pass

  def actualizarTrabajo(self):
    pass

  def getTrabajos(self):
    self.tabla.delete(*self.tabla.get_children())
    trabajos = self.ctrlTrabajos.getTrabajos()
    for trabajo in trabajos:
      self.tabla.insert("", END, text=trabajo[0], values=(trabajo[1], trabajo[2]))
