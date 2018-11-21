from excepciones import colorError
from excepciones import tipoGenero
class amfibi():
    def __init__(self,color = "", sexe = 0):
        self.__compruebaSexe(sexe)
        self.__compruebaColor(color)

        self.__array_tipo_genero = ["indefinido", "macho", "hembra"]
        self.__color = color
        self.__sexe = sexe
    def __str__(self):
        return self.__color + " " + str(self.__array_tipo_genero[self.__sexe])

    def setColor(self, color):
        self.__compruebaColor(color)
        self.__color = color

    def getColor(self):
        return self.__color

    def setSexe(self, sexe):
        self.__compruebaSexe(sexe)
        self.__sexe = sexe

    def getSexe(self):
        return self.__sexe

    def __compruebaColor(self, color):
        if(not(isinstance(color,str))):
            raise colorError(color)

    def __compruebaSexe(self, sexe):
        if(not(isinstance(sexe,int)) or not(sexe >= 0 and sexe <= 2)):
            raise tipoGenero(sexe)
