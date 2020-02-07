class ServicioCuenta(object):

  def __init__(self, daoCuenta):
    self.daoCuenta = daoCuenta

  def deposito(self, cantidad, cuenta):
    if  cantidad > 0 and cantidad <= 5000:
      saldo = cuenta.getSaldo() + cantidad
      cuenta.setSaldo(saldo)
      return self.daoCuenta.updateCuenta(cuenta)
    else:
      return False


  def retiro(self, cantidad, cuenta):

    if  cantidad > cuenta.getSaldo():
      return False
    else:
      saldo = cuenta.getSaldo() - cantidad
      cuenta.setSaldo(saldo)
      return self.daoCuenta.updateCuenta(cuenta)

  def validaNip(self, nip):
    if len(nip) == 4:
      return True
    else:
      return False

  def getCuentaByNip(self, nip):
    return self.daoCuenta.getCuentaByNip(nip)
