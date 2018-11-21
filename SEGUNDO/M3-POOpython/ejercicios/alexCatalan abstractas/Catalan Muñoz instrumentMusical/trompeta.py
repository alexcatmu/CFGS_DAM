'''
Tenim la classe Flauta i Trompeta filles de la classe abstracte InstrumentVent.
Trompeta amb atribut cadena boquilla (fer get/set) que ens diu el tipus de boqueta “cuenco”,
redefinim el mètode tipusInstrument retornant el tipus d’instrument utilitzat (Trompeta)
Flauta amb atribut cadena tipusFibra (fer el get/set), que ens diu el tipus de fibra utilitzat,
 “plastic”, redefinim el mètode tipusInstrument retornant el tipus d’instrument utilitzat (Flauta)
Podem reimplementar tocar de les dues classes criden al mètode del pare.
'''
from instrumentVent import InstrumentVent

class trompeta(InstrumentVent):
    def __init__(self, boquilla):
        self.boquilla = boquilla

    def getBoquilla(self):
        return self.boquilla

    def setBoquilla(self, boquilla):
        self.boquilla = boquilla

    def tipusInstrument(self):
        return type(self)

    def tocar(self):
        return "La trompeta es toca mitjançant una columna d'aire."

