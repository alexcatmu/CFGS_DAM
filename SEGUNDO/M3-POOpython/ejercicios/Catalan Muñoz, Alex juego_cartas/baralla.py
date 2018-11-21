from carta import carta
from excepciones import ErrorConstruccionBarralla
import random

class Baralla():
    def __init__(self,*args):
        self.__llistaCartes = []
        self.__llistaCartesUsades = []

        if(len(args) == 0):#baralla() = una baraja sin cartas
            self.__llistaCartes = []

        elif(len(args) == 1):#baraja()ens crea una baralla del tipus que desitgem, només 2
                            # tipus, amb valor 1 una baralla espanyola de
                            # 40 cartes, amb valor 2 una baralla de 80 cartes SIN MEZCLAR
            self.__generaBaralla(args[0])

        elif(len(args) == 2):#idem a l’anterior amb la diferencia que demanem
                            # amb TRUE O FALSE SI VOLEM LA BARALLA MEZCLADA
            self.__generaBaralla(args[0])
            if(args[1] == True):
                self.barallar()

        else:
            raise ErrorConstruccionBarralla(*args)


    def __generaBaralla(self,tipo):
        if(tipo == 1):
            for i in range(1,41):
                self.__llistaCartes.append(carta(i))
        if(tipo == 2):
            for i in range(2):
                for j in range(1,41):
                    self.__llistaCartes.append(carta(j))

    def barallar(self):
        for i in range(len(self.__llistaCartes)*2):
            num1 = random.randint(0,len(self.__llistaCartes)-1)
            num2 = random.randint(0,len(self.__llistaCartes)-1)
            aux1 = self.__llistaCartes[num1]
            aux2 = self.__llistaCartes[num2]
            self.__llistaCartes[num1] = aux2
            self.__llistaCartes[num2] = aux1

    def tallar(self, cortador):
        seguir = True
        i = 0
        while (seguir == True):
            aux1 = self.__llistaCartes[i+cortador]
            self.__llistaCartes[i+cortador] = self.__llistaCartes[i]
            self.__llistaCartes[i]= aux1
            i+=1
            if(i+cortador == len(self.__llistaCartes)):
                seguir= False

        for i in range(len(self.__llistaCartes)//2):
            aux1 = self.__llistaCartes[i]
            aux2 = self.__llistaCartes[i+len(self.__llistaCartes)//2]
            self.__llistaCartes[i] = aux2
            self.__llistaCartes[i+len(self.__llistaCartes)//2]


    def __str__(self):
        stringo = ""
        for i in range(len(self.__llistaCartes)):
            stringo += str(self.__llistaCartes[i]) + "\t"
            if(i%5 == 0 and i != 0):
                stringo += "\n"
        stringo += "\n\n"
        return stringo

    def carta_robar(self):
        self.__llistaCartesUsades.append(self.__llistaCartes[0])
        self.__llistaCartes.pop(0)
        return self.__llistaCartesUsades[len(self.__llistaCartesUsades)-1]

    def insertaCartaFinal(self,idCarta):
        if(isinstance(idCarta,int) == True):
            carta1 = carta(idCarta)
            self.__llistaCartes.append(carta1)

        elif(isinstance(idCarta,carta)):
            self.__llistaCartes.append(idCarta)

    def insertaCartaInici(self,idCarta):

        if(isinstance(idCarta,int) == True):
            carta1 = carta(idCarta)
            self.__llistaCartes.insert(0,carta1)
        elif(isinstance(idCarta,carta)):
            self.__llistaCartes.insert(0,idCarta)

    def numeroCartas(self):
        return len(self.__llistaCartes)

    def buida(self):
        if(len(self.__llistaCartes) == 0):
            return True
        else:
            return False

'''
baralla1 = Baralla(1,True)
print(baralla1)
print(baralla1.carta_robar())
print(baralla1.carta_robar())
print(baralla1.carta_robar())
print(baralla1)
baralla1.tallar(22)
baralla1.insertaCartaFinal(12)
baralla1.insertaCartaFinal(carta(12))
baralla1.insertaCartaFinal(carta(2,2))
baralla1.insertaCartaInici(12)
baralla1.insertaCartaInici(carta(12))
baralla1.insertaCartaInici(carta(2,2))
print(baralla1.numeroCartas())
print(baralla1)

baralla1 = Baralla(1,True)

baralla1.insertaCartaInici(-5)
'''