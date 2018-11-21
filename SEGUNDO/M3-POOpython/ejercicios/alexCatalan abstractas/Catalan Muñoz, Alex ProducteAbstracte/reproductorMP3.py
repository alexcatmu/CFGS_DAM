'''
reproductorMP3 hereta Electronica
Atributs: string color
setColor(string)
String getColor()
Double calculaPreuOferta(), preuRegular*0.9
Sobrecarrega str
'''
from Electronica import Electronica
class reproductorMP3(Electronica):
    def __init__(self,Preu_e,fab_e, color_e):
        Electronica.__init__(self, Preu_e, fab_e)
        self.__color = color_e

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def calculaPreuOferta(self):
        return Electronica.getPreuRegular(self) * 0.9

    def __str__(self):
        return "Aquest producte es un MP3\n" + \
            "Preu normal: "+str(Electronica.getPreuRegular(self)) + \
            "Preu oferta: "+str(self.calculaPreuOferta())
    