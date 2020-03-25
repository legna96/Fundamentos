import sqlite3

class Manejador():

  def __init__(self):
    pass

  def crearTablas(self,conexion):

    trabajos = """
      CREATE TABLE IF NOT EXISTS trabajos (
          trabajo_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          nombre  VARCHAR(45) NOT NULL,
          precio INTEGER(3) NOT NULL,
          descripcion TEXT
      );
    """

    inscripciones = """
      CREATE TABLE IF NOT EXISTS inscripciones(
        curp VARCHAR(18),
        trabajo_id INTEGER,
        nombre_completo  VARCHAR(45) NOT NULL,
        email VARCHAR(45) NOT NULL,
        descripcion TEXT,
        FOREIGN KEY(trabajo_id) REFERENCES trabajos(trabajo_id) ON DELETE CASCADE,
        PRIMARY KEY (trabajo_id, curp)
    );
    """

    escuelas = """
      CREATE TABLE IF NOT EXISTS escuelas(
        cct TEXT PRIMARY KEY,
        nombre VARCHAR(45) NOT NULL,
        grado TEXT CHECK( grado IN ('Primaria','Secundaria','Kinder') ) NOT NULL,
        tipo TEXT CHECK( tipo IN ('Diurna', 'Tecnica', 'NA')) NOT NULL,
        direccion TEXT NOT NULL
    );
    """

    tareas = """
      CREATE TABLE IF NOT EXISTS tareas(
        tarea_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pagado TEXT CHECK( pagado IN('Si','No')) NOT NULL,
        empezado TEXT CHECK( empezado IN('Si', 'No')) NOT NULL,
        terminado TEXT CHECK( terminado IN('Si', 'No')) NOT NULL,
        descripcion TEXT NOT NULL
    );
    """
    cursor = conexion.cursor()
    cursor.execute(trabajos)
    cursor.execute(inscripciones)
    cursor.execute(escuelas)
    cursor.execute(tareas)
    self.guardarCambios(conexion)

  def getConexion(self):
    return sqlite3.connect("persistencia/database.db")

  def hazQuery(self,conexion,query,params=()):
    cursor = conexion.cursor()
    cursor.execute(query,params)
    self.guardarCambios(conexion)

  def getRecords(self,conexion,tabla):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    return cursor.fetchall()

  def guardarCambios(self,conexion):
    conexion.commit()
