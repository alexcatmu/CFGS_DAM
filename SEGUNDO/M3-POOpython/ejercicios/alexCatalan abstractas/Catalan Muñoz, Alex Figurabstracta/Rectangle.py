from Figura import Figura
class Rectangle(Figura):
    def __init__(self, ancho_c, alto_c, x_c, y_c):
        self._ancho = ancho_c
        self._alto = alto_c

        Figura.__init__(self,x_c, y_c)

    def area(self):
        return self._ancho*self._alto

    def __str__(self):
        return "El alto y ancho son: "+str(self._alto)+"*"+str(self._ancho)+"\n" + Figura.__str__(self)

    def str_figura(self):
        return Figura.__str__(self)