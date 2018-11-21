from Rectangle import Rectangle
class Cuadrat(Rectangle):
    def __init__(self, lado_c, x_c, y_c):

        Rectangle.__init__(self,lado_c,lado_c,x_c, y_c)

    def area(self):
        return self._ancho * self._alto

    def __str__(self):
        return "El lado del cuadrado es: "+str(self._ancho)+"\n" + Rectangle.str_figura(self)