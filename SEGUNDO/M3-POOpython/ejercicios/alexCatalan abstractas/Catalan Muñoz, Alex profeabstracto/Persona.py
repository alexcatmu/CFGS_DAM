'''
Realitzar la classe Persona amb els atributs privats:
String nom, string cognom, int edat
Mètodes, string getNom(), string getCognom(), int getEdat(), mètode string de l’objecte.
'''
class Persona():
    def __init__(self, nom_c, cognom_c, edat_c):
        self.__nom = nom_c
        self.__cognom = cognom_c
        self.__edat = edat_c

    def getNom(self):
        return self.__nom

    def getCognom(self):
        return self.__cognom

    def getEdat(self):
        return self.__edat

    def __str__(self):
        return "Nombre: "+self.__nom+"\n"\
                "Apellido: "+self.__cognom+"\n"\
                "Edad: "+str(self.__edat)
