#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class VentanaInscripciones():

  color1 = "#FF3D5F"
  color2 = "#A738E8"
  color3 = "#4B6BFF"
  color4 = "#6CF1F5"
  color5 = "#42FF63"
  blackColor = "#000000"
  whiteColor = "#ffffff"

  font = "Sans Serif"

  def __init__(self, ctrlInscripciones):
    self.ctrlInscripciones = ctrlInscripciones
    self.disenio()


  def disenio(self):
    self.root = Tk()
    self.root.title("Fili Arl - CibberCotto")
    self.openCenter(self.root,1120,600)

    mainframe = self.mainFrame()
    mainframe.pack(fill="both", expand="True")

    self.root.resizable(False,False)
    self.root.mainloop()

  def mainFrame(self):
    mainFrame = Frame(self.root)
    titulo = Label(mainFrame, text="Administrador De Inscripciones")
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
    self.getInscripciones()
    btnFrame.pack(pady=20)

    return mainFrame

  def treeview(self, master):
    tabla = ttk.Treeview(master)
    tabla["columns"]=("#1","#2","#3","4")

    tabla.column("#0", width=190)
    tabla.column("#1", width=250)
    tabla.column("#2", width=250)
    tabla.column("#3", width=170)
    tabla.column("#4", width=250)

    tabla.heading("#0",text="CurpId")
    tabla.heading("#1",text="Nombre")
    tabla.heading("#2",text="Email")
    tabla.heading("#3",text="Curp")
    tabla.heading("#4",text="Trabajo")

    return tabla


  def formularioFrame(self, master):
    formFrame = Frame(master)
    formFrame.config(
      bg=self.color4
    )

    titulo = Label(formFrame, text="Registrar Inscripcion")
    titulo.config(
      bg=self.color4,
      fg=self.color3,
      font=(self.font, 12, "bold")
    )
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    labelNombre = self.formatLabelFormulario(formFrame,"* Nombre:")
    labelNombre.grid(row=1,column=0, padx=5, pady=2, sticky="w")
    self.entryNombre = Entry(formFrame, justify="center")
    self.entryNombre.grid(row=1,column=1, padx=5, pady=2, sticky="w")

    labelEmail = self.formatLabelFormulario(formFrame,"* Email:")
    labelEmail.grid(row=2,column=0, padx=5, pady=2, sticky="w")
    self.entryEmail = Entry(formFrame, justify="center")
    self.entryEmail.grid(row=2,column=1, padx=5, pady=2, sticky="w")

    labelCurp = self.formatLabelFormulario(formFrame,"* Curp:")
    labelCurp.grid(row=3,column=0, padx=5, pady=2, sticky="w")
    self.entryCurp = Entry(formFrame, justify="center")
    self.entryCurp.grid(row=3,column=1, padx=5, pady=2, sticky="w")

    labelTrabajo = self.formatLabelFormulario(formFrame,"* Trabajo:")
    labelTrabajo.grid(row=4,column=0, padx=5, pady=2, sticky="w")
    self.trabajo = ttk.Combobox(formFrame, state="readonly")
    self.trabajo["values"] = ["Python", "C", "C++", "Java"]
    self.trabajo.set("Python")
    self.trabajo.grid(row=4,column=1, padx=5, pady=2, sticky="w")

    btnAgregarInscripcion = Button(formFrame, text="Agregar", command=self.agregarInscripcion)
    btnAgregarInscripcion.config(
      bg=self.color5,
      fg=self.whiteColor,
      highlightbackground=self.whiteColor,
      highlightcolor=self.whiteColor,
      highlightthickness=1,
      cursor="hand2"
    )

    btnAgregarInscripcion.grid(row=5, column=0, columnspan=2, sticky=E+W, pady=10)

    return formFrame

  def botonesFrame(self, master):
    btnFrame = Frame(master)
    btnBorrar = Button(btnFrame, text="Borrar", command=self.borrarInscripcion)
    btnActualizar = Button(btnFrame, text="Actualizar", command=self.actualizarInscripcion)
    btnBuscar = Button(btnFrame, text="Buscar", command=self.buscarInscripcion)
    btnCopiar = Button(btnFrame, text="Copiar", command=self.copiarInscripcion)

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

    btnBuscar.config(
      width=10,
      bg=self.color2,
      fg=self.whiteColor,
      highlightbackground=self.whiteColor,
      highlightcolor=self.whiteColor,
      highlightthickness=1,
      cursor="hand2"
    )

    btnCopiar.config(
      width=10,
      bg=self.color5,
      fg=self.whiteColor,
      highlightbackground=self.whiteColor,
      highlightcolor=self.whiteColor,
      highlightthickness=1,
      cursor="hand2"
    )

    btnBorrar.grid(row=0, column=0, padx=5)
    btnActualizar.grid(row=0, column=1, padx=5)
    btnBuscar.grid(row=0, column=2, padx=5)
    btnCopiar.grid(row=0, column=3, padx=5)

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

  def agregarInscripcion(self):

    nombre = self.entryNombre.get()
    email = self.entryEmail.get()
    curp = str(self.entryCurp.get()).upper()


    if "" in [nombre, email]:
      messagebox.showerror("Error", "Se encontraron campos vacios")

    elif self.ctrlInscripciones.validaCurp(curp) == "Curp Existente":
      messagebox.showerror("Error", f"El Curp: {curp} ya esta registrado")

    elif self.ctrlInscripciones.validaCurp(curp) == "Curp Invalida":
      messagebox.showerror("Error", f"{curp} no es un curp valido")

    elif self.ctrlInscripciones.validaCurp(curp) == True:
      inscripcion = (nombre,email, curp)
      self.ctrlInscripciones.agregarInscripcion(inscripcion)
      self.getInscripciones()


  def borrarInscripcion(self):
    try:
      itemfocus = self.tabla.focus()
      itemDiccionario = self.tabla.item(itemfocus)

      id = itemDiccionario["text"]

      if id > 0:

        MsgBox = messagebox.askquestion ("Eliminar Inscripcion",f"Estas seguro de eliminar el registro {id}",icon = 'warning')

        if MsgBox == 'yes':
          self.ctrlInscripciones.eliminarInscripcion(id)
          self.getInscripciones()

    except Exception:
      messagebox.showerror("Error", "No se pudo eliminar ningun registro")


  def actualizarInscripcion(self):
    print("Actualizar")

  def buscarInscripcion(self):
    print("Buscar")

  def getInscripciones(self):
    self.tabla.delete(*self.tabla.get_children())
    inscripciones = self.ctrlInscripciones.getInscripciones()
    for inscripcion in inscripciones:
      self.tabla.insert("", END, text=inscripcion[0], values=(inscripcion[1], inscripcion[2], inscripcion[3], inscripcion[4]))

  def copiarInscripcion(self):

    try:
      itemfocus = self.tabla.focus()
      itemDiccionario = self.tabla.item(itemfocus)

      nombre = itemDiccionario["values"][0]
      email = itemDiccionario["values"][1]
      curp = itemDiccionario["values"][2]

      self.entryNombre.delete(0,END)
      self.entryNombre.insert(0,nombre)

      self.entryEmail.delete(0,END)
      self.entryEmail.insert(0,email)

      self.entryCurp.delete(0,END)
      self.entryCurp.insert(0,curp)

    except Exception:
      messagebox.showerror("Error", "Selecciona un reglon de la tabla")

