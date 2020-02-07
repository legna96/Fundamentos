from presentacion.vistas.ventanaCuenta import VentanaCuenta

class ControladorCuenta(object):

  def __init__(self, servicioCuenta, servicioPersona):
    self.servicioCuenta = servicioCuenta
    self.servicioPersona = servicioPersona

  def deposito(self, cantidad, cuenta):
    return self.servicioCuenta.deposito(cantidad,cuenta)

  def retiro(self, cantidad, cuenta):
    return self.servicioCuenta.retiro(cantidad, cuenta)

  def login(self, nip):
    if self.servicioCuenta.validaNip(nip):
      cuenta = self.servicioCuenta.getCuentaByNip(nip)
      if cuenta != None:
        return self.servicioPersona.getPersonaByCuenta(cuenta)
      else:
        return "Nip Invalido"
    else:
      return "Nip Invalido"

  def abreVentanaCuenta(self,persona):
    VentanaCuenta(self,persona)
