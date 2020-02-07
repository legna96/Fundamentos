from modelos.persona import Persona

class DaoPersona(object):

  def __init__(self,manejador):
    self.manejador = manejador

  def getPersonaByCuenta(self, cuenta):

    for p in self.manejador.getRows(self.manejador.getConexion(), "personas"):
      if p[4] == cuenta.getId():
        return Persona(p[0],p[1],p[2],p[3],cuenta)
    return None
