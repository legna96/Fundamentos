from persistencia.DaoInscripciones import DaoInscripciones
from persistencia.DaoTrabajos import DaoTrabajos

from servicios.ServiceInscripciones import ServiceInscripciones
from servicios.ServiceTrabajos import ServiceTrabajos

from presentacion.controladores.ControllerInscripcion import ControllerInscripcion
from presentacion.controladores.ControllerTrabajos import ControllerTrabajo
from presentacion.vistas.VentanaPrincipal import VentanaPrincipal

class ControllerPrincipal():

  def __init__(self):
    print("controlador principal iniciando Dao")
    daoInscripciones = DaoInscripciones()
    daoTrabajos = DaoTrabajos()
    print("controlador principal iniciando Servicios")
    serviceInscripciones = ServiceInscripciones(daoInscripciones)
    serviceTrabajos = ServiceTrabajos(daoTrabajos)
    print("controlador principal iniciando Controladores")
    self.ctrlInscripciones = ControllerInscripcion(serviceInscripciones)
    self.ctrlTrabajos = ControllerTrabajo(serviceTrabajos)
    self.abrirVentanaPrincipal()

  def abrirVentanaPrincipal(self):
    VentanaPrincipal(self)

  def abrirVentanaInscripciones(self):
    self.ctrlInscripciones.abrirVentanaInscripciones()
    self.abrirVentanaPrincipal()

  def abrirVentanaTrabajos(self):
    self.ctrlTrabajos.abrirVentanaTrabajos()
    self.abrirVentanaPrincipal()
