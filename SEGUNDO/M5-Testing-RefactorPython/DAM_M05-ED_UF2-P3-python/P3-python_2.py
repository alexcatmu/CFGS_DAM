
#P3_2

import os

# cálculo de los costes según: coste = sueldo base * número de trabajadores
def CalculoCostes(valor):
    return 1200*valor


if __name__ == "__main__":

    print("Indica el número: ",end='')
    cantidad=int(input())
    print("El resultado es: ",CalculoCostes(cantidad))
    
