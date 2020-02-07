class ServiceInscripciones():
    
    def __init__(self, daoInscripciones):
        self.daoInscripciones = daoInscripciones


    def validaCurp(self, curp):

        if curp == "":
            return True

        elif len(curp) != 18:
            return "Curp Invalida"

        elif self.daoInscripciones.getInscripcionByCurp(curp) == None:
            return True

        else:
            return "Curp Existente"

    def agregarInscripcion(self, inscripcion):
        return self.daoInscripciones.agregarInscripcion(inscripcion)

    def getInscripciones(self):
        return self.daoInscripciones.getInscripciones()

    def eliminarInscripcion(self, id):
        return self.daoInscripciones.eliminarInscripcion(id)