def division(a, b):
    resultado = 0
    try:#si ha ido bien el codigo y no ha dado errores
        resultado =  a/b

    except(ValueError, ZeroDivisionError) as error:#cuando da un error entra aqui y se ejecuta este codigo si hacemos return no entra en finally
        print("error de "+str(error))
        print("Error de division por 0")
    except TypeError:
        print("Tienes un error de tipo")

    except:#para el resto de errores
        print("error")

    else:#esto solo se ejecuta cuando ha ido bien el codigo si hacemos return no entra en finally
        print("El calculo se ha hecho correctamente")
        return resultado

    finally:#se ejecuta tanto si sale bien como si da error si no hacemos return seguira ejecutando codigo
        print("esto es un finally")
def calcular():
    division(1,'a')

class ElMeuError(Exception):
    def __init__(self, c_valor):
        self.valor = c_valor

    def __str__(self):
        return "Error de division 0 codigo:" + str(self.valor)

def divisionES(a,b):
    resultat = 0
    try:
        if(b == 0):
            raise ElMeuError(33)
        else:
            resultat = a/b

    except ElMeuError as e:
        print(str(e))

def calcularES():
    divisionES(1,0)

#calcular()

calcularES()
