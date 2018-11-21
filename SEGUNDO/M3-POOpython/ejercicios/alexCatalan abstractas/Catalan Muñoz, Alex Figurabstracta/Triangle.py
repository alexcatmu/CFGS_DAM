from Figura import Figura
class Triangle(Figura):
    def __init__(self, ancho_c, altura_c, x_c, y_c):
        self.__ancho = ancho_c
        self.__altura = altura_c
        self.__x = x_c
        self.__y = y_c
        Figura.__init__(self,self.__x, self.__y)

    def area(self):
        return float((self.__ancho * self.__altura) / 2)

    def __str__(self):
        return "El alto y ancho del triangulo es: "+str(self.__altura)+"*"+str(self.__ancho)+\
               "\n"+Figura.__str__(self)