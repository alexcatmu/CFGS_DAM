class ControlAlturaBase(Exception):
    def __init__(self, e_altura):
        self.__altura = e_altura

    def __str__(self):
        return "La altura y la base deben ser valores positivos y enteros"

class const_error(Exception):
    def __init__(self, n_datos):
        self.__nDatos = n_datos
        print(str(n_datos))

    def __str__(self):
        return "Se esperan "+str(self.__nDatos)+" datos"