from persistencia.manejador import Manejador

class DaoTrabajos():

  def __init__(self):
    self.manejador = Manejador()
    self.conexion = self.manejador.getConexion()
    self.manejador.crearTablas(self.conexion)

  def agregarTrabajo(self, trabajo):
    query = "INSERT INTO trabajos(clave,titulo,descripcion) VALUES (?,?,?);"
    return self.manejador.hazQuery(self.conexion,query,trabajo)

  def getTrabajos(self):
    self.trabajos = self.manejador.getRecords(self.conexion,"trabajos")
    return self.trabajos

  def getTrabajoByClave(self, clave):
    for trabajo in self.trabajos:
      if trabajo[0] == clave:
        return trabajo
    return None

  def eliminarTrabajo(self, clave):
    query = f"DELETE FROM trabajos WHERE clave = {clave};"
    return self.manejador.hazQuery(self.conexion,query)
