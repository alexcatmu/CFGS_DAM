import gc
class Prova():
    def __init__(self):
        self.a=1000

    def prueba(self, valor = 0):
        self.a = valor

    def __del__(self):
        print("Eliminando objeto!"+str(self.a))

a = Prova()
a.prueba(50)
a.__del__()
print(a.a)
del a
b = Prova()
#c = b
#a = b

input()
recolectado = gc.collect()
print("Garbage collector %d"%recolectado)