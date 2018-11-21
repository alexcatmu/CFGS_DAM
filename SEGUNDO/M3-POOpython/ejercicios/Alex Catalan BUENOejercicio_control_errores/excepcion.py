class ValorEdatIncorrecteException(Exception):
    def __init__(self,edad):
        self.edad = edad

    def __str__(self):
        return "La edad es incorrecta " + str(self.edad)

class ValorEdadErrorDato(Exception):

    def __init__(self,edad):
        self.edad = edad

    def __str__(self):
        return "La edad debe ser un entero "+str(self.edad)


