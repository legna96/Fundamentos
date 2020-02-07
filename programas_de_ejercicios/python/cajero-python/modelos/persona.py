class Persona(object):

  def __init__(self, curp, nombre,apat,amat,cuenta):
    self.__curp = curp
    self.__nombre = nombre
    self.__apat = apat
    self.__amat = amat
    self.__cuenta = cuenta

  def toString(self):
    return f"Nombre Completo: {self.__nombre} {self.__apat} {self.__amat}, Cuenta: {self.__cuenta.getId()}"

  def nombreCompleto(self):
    return f"{self.__nombre} {self.__apat} {self.__amat}"

  def getCuenta(self):
    return self.__cuenta

  def setCuenta(self, cuenta):
    self.__cuenta = cuenta
