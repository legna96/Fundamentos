class ServicioPersona(object):

  def __init__(self, daoPersona):
    self.daoPersona = daoPersona

  def getPersonaByCuenta(self, cuenta):
    return self.daoPersona.getPersonaByCuenta(cuenta)
