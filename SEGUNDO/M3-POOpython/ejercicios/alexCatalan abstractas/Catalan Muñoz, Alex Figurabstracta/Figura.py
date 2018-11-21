from abc import ABCMeta, abstractmethod
class Figura(metaclass=ABCMeta):
    def __init__(self, x_c, y_c):
        self._x = x_c
        self._y = y_c

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return "las coordenadas de la figuras son: "+str(self._x)+", "+str(self._y)