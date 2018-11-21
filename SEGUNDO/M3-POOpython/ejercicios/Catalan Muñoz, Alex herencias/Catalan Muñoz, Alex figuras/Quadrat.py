from Rectangle import Rectangle
from Excepciones import const_error
class Quadrat(Rectangle):
    def __init__(self, *args):
        if(len(args) == 1):
                Rectangle.__init__(self, args[0], args[0])
        else:
            raise const_error(1)

        self.__lado = args[0]

    def getLado(self):
        Rectangle.getAltura(self)

    def setLado(self, lado):
        Rectangle.setAltura(self, lado)
        Rectangle.setBase(self, lado)


