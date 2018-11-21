class Punt:
    def __init__(self, coord_x = 0, coord_y = 0):
        self.coordenada_x = coord_x
        self.coordenada_y = coord_y


#    def __eq__(self, other):
#        return (self.coordenada_x == other.coordenada_x and self.coordenada_y == other.coordenada_y)

    def desplaca(self, desX = 0, desY = 0):
        self.coordenada_x += desX
        self.coordenada_y += desY

    def setY(self, y ):
        self.coordenada_y = y

    def setX(self,x):
        self.coordenada_x = x

    def getY(self):
        return self.coordenada_y

    def getX(self):
        return self.coordenada_x

    def visualitza(self):
        str_retorn = "("+str(self.getX())+","+str(self.getY())+")"
        return str_retorn
'''
primer_punto = Punt(1, 1)
print(primer_punto.visualitza())
primer_punto.desplaca(3, 5)
print(primer_punto.visualitza())
primer_punto.setX(10)
print(primer_punto.visualitza())
primer_punto.setY(-3)
'''
a = Punt(0,3)
b = Punt(3,5)
c = Punt(0,3)
b = a

if(a == b):
    print("iguales pisha")
else:
    print("No se parecen en ná")

