import sqlite3

def crearConexion(db):
  conexion = sqlite3.connect(db)
  return conexion

def hazQuery(conexion, query, parametros = ()):
  cursor = conexion.cursor()
  cursor.execute(query,parametros)

def getRegistros(conexion):
  cursor = conexion.cursor()
  cursor.execute("SELECT * FROM persona")
  return cursor.fetchall()

def guardaCambios(conexion):
  conexion.commit()

def imprimeRegistros(registros):
  for registro in registros:
    print()
    for elemeno in registro:
      print(f"|{elemeno}|", end=" ")
  print()

def main():
  database = "midatabase.db"
  conexion = crearConexion(database)

  queryCrearTabla = """
    CREATE TABLE IF NOT EXISTS persona(
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      nombre VARCHAR(10),
      apat VARCHAR(15),
      amat VARCHAR(15)
    );
  """

  queryInsertaRegistro = """
    INSERT INTO persona('nombre','apat','amat')
    VALUES(?,?,?);
  """

  queryUpdate = """
    UPDATE persona
    SET
    nombre = ?,
    apat = ?,
    amat = ?
    WHERE id = ?;
  """

  queryDeleteAll = "DELETE FROM persona"

  queryDeleteOne = "DELETE FROM persona WHERE id=?"

  # clausula with ya se encarga de cerrar la conexion
  # si no se usara with, se cerraria asi: conexion.close()
  with conexion as c:

    hazQuery(c,queryCrearTabla)

    nombre = input("Dame nombre: ")
    apat = input("Dame apat: ")
    amat = input("Dame amat: ")
    parametros = (nombre,apat,amat)

    hazQuery(c,queryInsertaRegistro,parametros)

    registros = getRegistros(c)
    imprimeRegistros(registros)

    hazQuery(c, queryUpdate, ("Batman", "Bruno", "Diaz", 1))
    # hazQuery(c, queryDeleteOne, (1,))
    # hazQuery(c,queryDeleteAll)

    registros = getRegistros(c)
    imprimeRegistros(registros)


    guardaCambios(c)


if __name__ == '__main__':
  main()
