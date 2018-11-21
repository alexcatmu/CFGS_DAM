'''
Realitzar la classe Abstracta Producte:
Atributs: real preuRegular
Abstracte double calculaPreuOferta()
setPreuRegular(double)
double getPreuRegular()
Sobrecarrega str
'''
from abc import ABCMeta, abstractmethod

class Producte(metaclass=ABCMeta):
    def __init__(self, PreuRegular_c):
        self.__PreuRegular = PreuRegular_c

    @abstractmethod
    def calculaPreuOferta(self):
        pass

    def setPreuRegular(self, Preu):
        self.__PreuRegular = Preu

    def getPreuRegular(self):
        return self.__PreuRegular

    def __str__(self):
        return "Aixó es un producte"