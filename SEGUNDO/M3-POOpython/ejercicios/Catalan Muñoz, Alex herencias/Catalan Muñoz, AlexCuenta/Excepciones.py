class saldoReal(Exception):
    def __init__(self, valor):
        self.__valor = valor

    def __str__(self):
        return "El saldo debe ser un numero"

class ingresoError(Exception):
    def __init__(self,valor):
        self.__valor = valor

    def __str__(self):
        return "Error en el ingreso, debe ser positivo"