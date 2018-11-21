from data import data
class persona:
    __poblacion = 0

    def __init__(self, c_dni = "", c_nom = "", c_dataNaix = data()):

        self.dni = c_dni
        self.nom = c_nom
        self.dataNaix = c_dataNaix
        persona.__poblacion += 1

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
        str_data = "("+str(self.getDNI())+","+str(self.getNOM())+\
                   ","+str(self.getDATANAIX().visualitza())+")"

        return str_data