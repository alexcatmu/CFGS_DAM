class Nodo():

    def __init__(self, dato):
        self.nodoIzquierda = None
        self.nodoDerecha = None
        self.cantidad = dato

    def __str__(self):
        return str(self.cantidad) + "--->cantidad"