'''
Electronica hereta Producte:
Atributs: string fabricant
setFabricant(string)
String getFabricant()
Sobrecarrega str
'''
from Producte import Producte
class Electronica(Producte):
    def __init__(self, PreuRegular_c, fabricant_e):
        Producte.__init__(self, PreuRegular_c)
        self.__fabricant = fabricant_e

    def setFabricant(self, fab):
        self.__fabricant = fab

    def getFabricant(self):
        return self.__fabricant

    def __str__(self):
        return "Aixo es un producte electronic"
