class Trabajo():

  def __init__(self, clave, titulo, descripcion):
    self.__clave = clave
    self.__titulo = titulo
    self.__descripcion = descripcion

  def getClave(self):
        return self.__clave

  def setClave(self, clave):
    self.__clave = clave

  def getTitulo(self):
        return self.__clave

  def setTitulo(self, titulo):
    self.__titulo = titulo

  def getDescripcion(self):
    return self.__descripcion

  def setDescripcion(self, descripcion):
    self.__descripcion = descripcion

