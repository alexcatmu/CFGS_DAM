class GanaOpierdeExcept(Exception):
    def __init__(self,valor):
        self.valor = valor

    def __str__(self):
        return "El parametro de entrada GanaOpierdeExcept debe ser array con valores"

class ValorIdError(Exception):
    def __init__(self,id_cartas):
        self.id_cartas = id_cartas

    def __str__(self):
        return "El id de carta tiene que estar entre 1 y 40"

class ErrorConstruccionBarralla(Exception):
    def __init__(self, argumentos_baraja):
        self.argumentos_baraja = argumentos_baraja

    def __str__(self):
        return "Hay un error al construir la baraja: \nbaralla() sin cartas\n baralla(1 || 2)\nbaralla(1 || 2, True||False)"


class NumeroCarta(Exception):

    def __init__(self,id_carta):
        self.id_carta = id_carta

    def __str__(self):
        return "El id de carta debe ser como máximo 40, minimo 1"

class NumJugadores(Exception):

    def __init__(self,num_jug):
        self.num_jug = num_jug

    def __str__(self):
        return "El numero de jugadores no es correcto(1 a 7)"

class NumeroCarta_id_coll(Exception):

    def __init__(self,num_id_coll):
        self.num_id_coll = num_id_coll

    def __str__(self):
        return "El id de las cartas con dos parametros debe estar entre 1 y 10"

class NumeroCartaColl(Exception):
    def __init__(self, num_coll):
        self.num_coll = num_coll

    def __str__(self):
        return "El coll debe estar entre 0 y 3"
