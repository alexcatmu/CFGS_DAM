from Figura import Figura
class Triangle(Figura):
    def __init__(self, e_base, e_altura):
        Figura.__init__(self, e_base, e_altura)
        self.__base = e_base
        self.__altura = e_altura

    def Area(self):
        return (self.__base * self.__altura)/2

