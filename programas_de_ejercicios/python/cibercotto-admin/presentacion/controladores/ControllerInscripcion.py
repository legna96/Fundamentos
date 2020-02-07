from presentacion.vistas.VentanaInscripciones import VentanaInscripciones

class ControllerInscripcion():

    def __init__(self, serviceInscripciones):
        self.serviceInscripciones = serviceInscripciones

    def abrirVentanaInscripciones(self):
      VentanaInscripciones(self)

    def validaCurp(self, curp):
      return self.serviceInscripciones.validaCurp(curp)

    def agregarInscripcion(self, inscripcion):
      return self.serviceInscripciones.agregarInscripcion(inscripcion)

    def getInscripciones(self):
      return self.serviceInscripciones.getInscripciones()

    def eliminarInscripcion(self, id):
      return self.serviceInscripciones.eliminarInscripcion(id)
