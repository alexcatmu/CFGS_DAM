from data import data
from excepcion import ValorEdatIncorrecteException
class persona:
    __poblacion = 0

    def __init__(self, c_dni = "", c_nom = "", c_edat = 0,c_dataNaix = data()):

        if(c_edat < 0 or c_edat > 130):
            raise ValorEdatIncorrecteException(c_edat)

        self.dni = c_dni
        self.nom = c_nom
        self.dataNaix = c_dataNaix
        self.edat = c_edat
        persona.__poblacion += 1


    def __str__(self):
        str_data = "("+str(self.getDNI())+", "+str(self.getNOM())+\
           ", "+str(self.edat)+", "+str(self.getDATANAIX().visualitza())+")"
        return str_data

    def getPoblacion(self):
        return self.__poblacion

    def setDNI(self, set_dni):
        self.dni = set_dni

    def setNOM(self,set_nom):
        self.nom = set_nom

    def setDATANAIX(self, set_datanaix):
        self.dataNaix = set_datanaix

    def getDNI(self):
        return self.dni

    def getNOM(self):
        return self.nom

    def getDATANAIX(self):
        return self.dataNaix

    def visualitza(self):
        str_data = "("+str(self.getDNI())+", "+str(self.getNOM())+\
                   ", "+str(self.edat)+", "+str(self.getDATANAIX().visualitza())+")"
        return str_data

    def setEdat(self,edat):
        if(edat < 0 or edat > 130):
            raise ValorEdatIncorrecteException(edat)

        self.edat = edat

try:
    persona1 = persona("23453", "pepito", 160)

except Exception as e:
    print(str(e))

try:
    persona1 = persona()
    persona1.setEdat(-5)
except Exception as e:
    print(str(e))