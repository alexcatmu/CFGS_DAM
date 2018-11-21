'''
Tenim la classe abstracte InstrumentVent, implementa la classe anterior, tindrà un atribut tipusFamilia
que ens dirà a quina família pertany dintre dels instruments de vent (get/set respectivament)
(Fusta o metall). Implementarem el mètode tocar de la interface (només tocar, amb el missatge que posava.).
'''
from instrumentMusical import instrumentMusical


class InstrumentVent(instrumentMusical):
    def __init__(self):
        self.tipusFamilia = "Introduce setFamilia"

    def getFamilia(self):
        return self.tipusFamilia

    def setFamilia(self, familia):
        self.tipusFamilia = familia

    def tocar(self):
        return "Els instruments de vent es toquen mitjançant una columna d'aire."