from Figura import Figura
from math import pi

class Cercle(Figura):
    def __init__(self, radi_c, x_c, y_c):
        self.__radi = radi_c
        self.__PI = pi
        self.__x = x_c
        self.__y = y_c
        Figura.__init__(self,self.__x, self.__y)

    def area(self):
        return float((self.__radi ** 2) * self.__PI)

    def __str__(self):
        return "El radio del circulo es: "+str(self.__radi)+"\n"+Figura.__str__(self)