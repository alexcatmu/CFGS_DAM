from nodo import nodo
class pila:
    def __init__(self):
        self.arrel = None
        self.__contador = 0

    def apilar(self, num):

        nouNode = nodo(num)
        if(self.arrel == None):
            nouNode.nodo = None
            self.arrel = nouNode

        else:
            nouNode.nodo = self.arrel
            self.arrel = nouNode

        self.__contador += 1


    def desapilar(self):
        if(self.arrel != None):
            nodo.dada = self.arrel.dada
            self.arrel = self.arrel.nodo
            self.__contador -= 1
            return nodo.dada
        else:
            return None

    def cantidad(self):
        return self.__contador
