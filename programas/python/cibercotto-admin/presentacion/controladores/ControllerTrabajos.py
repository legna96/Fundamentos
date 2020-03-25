from presentacion.vistas.VentanaTrabajos import VentanaTrabajos

class ControllerTrabajo():

  def __init__(self, serviceTrabajos):
    self.serviceTrabajos = serviceTrabajos

  def validaClave(self, clave):
    return self.serviceTrabajos.validaClave(clave)

  def abrirVentanaTrabajos(self):
    VentanaTrabajos(self)

  def agregarTrabajo(self, trabajo):
    return self.serviceTrabajos.agregarTrabajo(trabajo)

  def getTrabajos(self):
    return self.serviceTrabajos.getTrabajos()

  def eliminarTrabajo(self, id):
    return self.serviceTrabajos.eliminarTrabajo(id)
