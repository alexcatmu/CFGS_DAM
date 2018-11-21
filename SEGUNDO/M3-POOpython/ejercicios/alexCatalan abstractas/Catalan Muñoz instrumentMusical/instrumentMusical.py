'''
Tenim una interface InstrumentMusical (abstracte):
Definirem el mètode string tipusInstrumnet() retornarà el nom de la classe utilitzada , string tocar()
ens mostrarà “Els instruments de vent es toquen mitjançant una columna d'aire.”. Tots els mètodes
s’implementaran on toqui. Són dos mètodes abstractes tipusInstrument i tocar.
'''
from abc import ABCMeta, abstractmethod
class instrumentMusical(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def tipusInstrument(self):
        pass

    @abstractmethod
    def tocar(self):
        pass


