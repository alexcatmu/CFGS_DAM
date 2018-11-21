class Llista:
    def __init__(self, num = 0):

        if(not(isinstance(num,int))):

            raise ValueError("Parametro erroneo, tipo de dato no valido", type(self))
        elif(num < 0):
            raise NotImplementedError("Parametro erroneo, debe ser un numero positivo", type(self))
        self.array_nums = []
        #num debe ser numerico

        for i in range(num):
            self.array_nums.append(None)

    def elemento_posicion(self,element, position):
        try:
            self.array_nums[position] = element

        except IndexError:
            raise IndexError("Fuera de rango", type(self))

        except ValueError:
            raise ValueError("Valor no valido",type(self))

        except TypeError:
            raise TypeError("Debe ser de tipo entero", type(self))

        except Exception as e:#Es de ValueError cuando introducimos una letra
            print("Detectat error "+ str(e))


prueba = Llista(4)
print(prueba.array_nums)
prueba.elemento_posicion(4,1)
print(prueba.array_nums)