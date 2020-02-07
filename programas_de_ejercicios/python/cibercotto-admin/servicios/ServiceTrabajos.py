class ServiceTrabajos():

  def __init__(self, daoTrabajos):
    self.daoTrabajos = daoTrabajos

  def validaClave(self, clave):
    if len(clave) == 3:
      return True
    else:
      return False

  def agregarTrabajo(self, trabajo):
    return self.daoTrabajos.agregarTrabajo(trabajo)

  def getTrabajos(self):
    return self.daoTrabajos.getTrabajos()

  def eliminarTrabajo(self, id):
    return self.daoTrabajos.eliminarTrabajo(id)
