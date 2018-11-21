class colorError(Exception):
    def __init__(self,valor):
        self.__valor = valor

    def __str__(self):
        return "El color debe ser un string"

class tipoGenero(Exception):
    def __init__(self,valor):
        self.__valor = valor

    def __str__(self):
        return "El genero debe ser un entero 0, 1 o 2"

class boolVeneno(Exception):
    def __init__(self,valor):
        self.__valor = valor

    def __str__(self):
        return "El veneno debe ser True o False"