import sqlite3

class Manejador(object):

  def __init__(self):
    pass

  def crearTablas(self,conexion):

    personas = """
      CREATE TABLE IF NOT EXISTS personas(
        curp VARCHAR(18) NOT NULL PRIMARY KEY,
        nombre VARCHAR(10) NOT NULL,
        apat VARCHAR(15) NOT NULL,
        amat VARCHAR(15) NOT NULL,
        id_cuenta VARCHAR(19) NOT NULL UNIQUE
      );
    """
    cuentas = """
      CREATE TABLE IF NOT EXISTS cuentas(
        id VARCHAR(19) NOT NULL PRIMARY KEY,
        fecha_fin VARCHAR(5) NOT NULL,
        cvv VARCHAR(3) NOT NULL,
        saldo DECIMAL(4,2) NOT NULL,
        nip VARCHAR(4) NOT NULL UNIQUE
      );
    """
    cursor = conexion.cursor()
    cursor.execute(personas)
    cursor.execute(cuentas)
    conexion.commit()

  def getConexion(self):
    return sqlite3.connect("persistencia/cajero.db")

  def hazQuery(self,conexion,query,params=()):
    conexion.commit()
    cursor = conexion.cursor()
    cursor.execute(query,params)
    conexion.commit()

  def getRows(self,conexion,tabla):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    return cursor.fetchall()

  def guardarCambios(self,conexion):
    conexion.commit()
