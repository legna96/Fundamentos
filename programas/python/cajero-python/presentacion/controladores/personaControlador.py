class ControladorPersona(object):

  def __init__(self, servicioPersona):
    self.servicioPersona = servicioPersona

  def getPersonaByCuenta(self, cuenta):
    return self.servicioPersona.getPersonaByCuenta(cuenta)
