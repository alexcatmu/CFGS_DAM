from excepciones import NumeroCarta
from excepciones import NumeroCarta_id_coll
from excepciones import NumeroCartaColl
class carta:
    def __init__(self, *args):

        self.__num = 0
        self.__coll = 0
        self.__array_cartas = ["as","dos","tres","cuatro","cinco","seis","siete","sota","caballo","rey"]
        self.__array_coll = ["oro","copas","espadas","bastos"]

        if(len(args)==2):
            if(not (isinstance(args[0],int)) or args[0] < 1 or args[0] > 40):
                raise NumeroCarta_id_coll(args[0])

            if(not (isinstance(args[1],int)) or args[1] < 0 or args[1] > 3):
                raise NumeroCartaColl(args[1])
            if(args[0] != 0):
                self.__num = args[0]-1
                self.__coll = args[1]

        elif(len(args) == 1):
            if(not (isinstance(args[0],int)) or args[0] < 1 or args[0] > 40):
                raise NumeroCarta(args[0])
            if(args[0] != 0):
                if(args[0]%10 == 0):
                    self.__coll = (args[0]//10)-1
                    self.__num = 9
                else:
                    self.__coll = args[0]//10
                    self.__num = (args[0]%10)-1
    #    self.__comprueba()

    #def __comprueba(self):

    def numero(self):
        return self.__num

    def coll(self):
        return self.__coll

    def nomNumero(self):
        return self.__array_cartas[(self.__num)]

    def nomColl(self):
        return self.__array_coll[self.__coll]

    def valorTute(self):
        valor = 0
        if(self.__num == 0):
            valor = 11
        elif(self.__num == 2):
            valor = 10
        elif(self.__num == 7):
            valor = 2
        elif(self.__num == 8):
            valor = 3
        elif(self.__num == 9):
            valor = 4
        return valor

    def valorMus(self):
        valor = 0
        if(self.__num == 0 or self.__num == 1):
            valor = 13
        elif(self.__num == 7 or self.__num == 8 or self.__num == 9):
            valor = 10
        return valor

    def valor7iMig(self):
        if(self.__num == 7 or self.__num == 8 or self.__num == 9):
            valor = 0.5
        else:
            valor = self.__num + 1
        return valor

    def __str__(self):
        arr_carta = [self.nomNumero(), self.nomColl()]
        return str(arr_carta[0]) + ' de ' + str(arr_carta[1])
'''
carta1 = carta(20)
print(carta1)
carta2 = carta(3,1)
print(carta2)

'''
'''
print(carta1.nomColl())
print(carta1.nomNumero())
print(carta1)
print("\n")
print(carta2.nomColl())
print(carta2.nomNumero())
print(carta2)
'''












