class prova():
    def __init__(self):
        self.i = 1

    def __incrementa(self, incre):
        if(incre == 1):
            self.i += incre
        elif(incre == 2):
            self.i += incre
        elif(incre == 3):
            self.i += incre


    def inc(self, cantidad = ""):
        if (cantidad == "poco"):
            self.__incrementa(1)

prueba = prova()
prueba.inc("poco")
prueba.inc()
print(prueba.i)