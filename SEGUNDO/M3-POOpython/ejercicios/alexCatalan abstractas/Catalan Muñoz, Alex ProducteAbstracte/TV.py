'''
TV hereta Electronica (abstracta) encara que si no la fem, no es pot crear, pero si es pot heretar.
Atributs: integer mida
setMida(integer)
Integer getMida()
Double calculaPreuOferta(), preuRegular*0.8
Sobrecarrega str
'''
from Electronica import Electronica
class TV(Electronica):
    def __init__(self, Preu_c, fab_e, mida_e):
        Electronica.__init__(self,Preu_c,fab_e)
        self.__mida = mida_e

    def setMida(self, mid):
        self.__mida = mid

    def getMida(self):
        return self.__mida

    def calculaPreuOferta(self):
        return Electronica.getPreuRegular(self) * 0.8

    def __str__(self):
        return "Aquest producte es una TV\n" + \
            "Preu normal: "+str(Electronica.getPreuRegular(self)) + \
            "Preu oferta: "+str(self.calculaPreuOferta())



