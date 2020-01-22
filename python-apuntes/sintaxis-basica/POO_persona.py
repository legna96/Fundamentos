##
# La clase debe recibir Object y cada
# funcion de ella debe recibir la clase como
# parametro
##
class Persona(object):

  def __init__(self,nombre, apat, amat):
    self.__nombre = nombre
    self.__apat = apat
    self.__amat = amat

  def to_s(self):
    print(self.__nombre, self.__apat, self.__amat )

  def getNombre(self):
    return self.__nombre


def main():
  p1 = Persona("Angel", "Rebollo", "Lopez")
  p2 = Persona("Rafael", "Rebollo", "Lopez")
  print(f"Nombre encapsulado: {p1.getNombre()}")
  p1.to_s()
  p2.to_s()

if __name__ == '__main__':
  main()

