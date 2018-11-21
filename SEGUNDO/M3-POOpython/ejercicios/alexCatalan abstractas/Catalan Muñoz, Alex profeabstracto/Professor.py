'''
Realitzar la classe abstracta Professor que hereta de Persona i afegeix:
Atribut privat int id
Mètode int getIdProfessor(), int setIdProfessor() i el mètode abstracte  importNomina
Sobrecàrrega del mètode string de l’objecte
'''
from abc import ABCMeta, abstractmethod
from Persona import Persona

class Professor(Persona, metaclass=ABCMeta):
    def __init__(self, nom_c, cognom_c, edat_c, id_c):
        self.__id = id_c
        Persona.__init__(self, nom_c, cognom_c, edat_c)

    def getIdProfessor(self):
        return self.__id

    def setIdProfessor(self, id_p):
        self.__id = id_p

    @abstractmethod
    def importNomina(self):
        pass