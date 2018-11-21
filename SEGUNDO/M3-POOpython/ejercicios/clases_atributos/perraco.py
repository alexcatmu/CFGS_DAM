class perro:
    __razas = "erere"
    def __init__(self, c_nom = "", c_raza = ""):
        self.nom = c_nom
        self.__raza = c_raza#atributo privado!!

    def getRaza(self):
        return self.__raza

    @staticmethod
    def get():
        return perro.__razas

perrico = perro("THOR", "caniche")
print(perrico.nom)
print(perrico.getRaza())
#print(perrico.__raza)#no podemos acceder a los atributos que son privados. solo definirlos no podemos verlos
print(perro.get())