from Excepciones import ControlAlturaBase
from Excepciones import const_error
class Figura():
    def __init__(self, *args):
        if(len(args) == 2):
            if(self.__controlBase_Altura(args[0]) and self.__controlBase_Altura(args[1])):
                self.__base = args[0]
                self.__altura = args[1]

        else:
            raise const_error(2)

    def __str__(self):
        return "La base es de "+ str(self.__base) +" y la altura de "+ str(self.__altura)

    def __controlBase_Altura(self, valor):
        if (valor <= 0 or not(isinstance(valor,int))):
            raise ControlAlturaBase(valor)
        else:
            return True

    def getBase(self):
        return self.__base

    def getAltura(self):
        return self.__altura

    def setBase(self, base):
        self.__controlBase_Altura(base)
        self.__base = base

    def setAltura(self, altura):
        self.__controlBase_Altura(altura)
        self.__altura = altura

    def Area(self):
        pass

#figurilla = Figura(3)
#print(figurilla.getAltura())
#print(figurilla)