class Cuenta(object):

  def __init__(self,id,fechaFin,cvv,saldo,nip):
    self.__id = id
    self.__fechaFin = fechaFin
    self.__cvv = cvv
    self.__saldo = saldo
    self.__nip = nip

  # Id
  def getId(self):
    return self.__id

  # Fecha Fin
  def getFechaFin(self):
    return self.__fechaFin

  # Cvv
  def getCvv(self):
    return self.__cvv

  # Saldo
  def getSaldo(self):
    return float(self.__saldo)

  def setSaldo(self, saldo):
    self.__saldo = saldo

  # Nip
  def getNip(self):
    return self.__nip

  def setNip(self, saldo):
    self.__nip = saldo

  def toString(self):
    return f"Cuenta: {self.__id}\nfecha_final: {self.__fechaFin}\nCVV={self.__cvv}\nSaldo: $ {self.__saldo} MXN"
