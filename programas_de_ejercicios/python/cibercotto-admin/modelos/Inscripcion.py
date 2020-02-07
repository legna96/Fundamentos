class Inscripcion():

  def __init__(self, id, nombre, email, curp, desc):
    self.__id = id
    self.__nombre = nombre
    self.__email = email
    self.__curp = curp
    self.__desc = desc

  # ID
  def getId(self):
    return self.__id

  def setId(self, id):
    self.__id = id

  # nombre

  def getNombre(self):
    return self.__nombre

  def setNombre(self, nombre):
    self.__nombre = nombre

  # Email

  def getEmail(self):
    return self.__email

  def setEmail(self, email):
    self.__email = email

  # curp

  def getCurp(self):
    return self.__curp

  def setCurp(self, curp):
    self.__curp = curp

  # Desc

  def getDesc(self):
    return self.__desc

  def setDesc(self, desc):
    self.__desc = desc

  # To String

  def toString(self):
    return f"id:{self.__id}, nombre:{self.__nombre}, email:{self.__email}, curp:{self.__curp}, desc:{self.__desc}"
