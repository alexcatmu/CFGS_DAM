from abc import ABCMeta, abstractmethod

class vehicle(metaclass=ABCMeta):
    def __init__(self):
        self.tipus = "no determinat"

    @abstractmethod
    def qui_ets(self):
        print("vehiculo y metodo abstracto")

class cotxe(vehicle):
    def __init__(self, c_tipus):
        vehicle.__init__(self)
        self.tipus = c_tipus

    def qui_ets(self):
        print("soy un coche")


#a = vehicle()
#a.qui_ets
b = cotxe("seat")
b.qui_ets()
print(b.tipus)

