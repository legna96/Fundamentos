from persistencia.manejador import Manejador

class DaoInscripciones():

  def __init__(self):
    self.manejador = Manejador()
    self.conexion = self.manejador.getConexion()
    self.manejador.crearTablas(self.conexion)

  def agregarInscripcion(self, inscripcion):
    query = "INSERT INTO inscripciones(nombre,email,curp,descripcion) VALUES (?,?,?,?);"
    return self.manejador.hazQuery(self.conexion,query,inscripcion)

  def getInscripciones(self):
    self.inscripciones = self.manejador.getRecords(self.conexion,"inscripciones")
    return self.inscripciones

  def getInscripcionByCurp(self, curp):
    for inscripcion in self.inscripciones:
      if inscripcion[3] == curp:
        return inscripcion
    return None

  def eliminarInscripcion(self, id):
    query = f"DELETE FROM inscripciones WHERE id = {id};"
    return self.manejador.hazQuery(self.conexion,query)
