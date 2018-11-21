
#P3_1

import os

def Factorial(num):
    valor=1
    if num>=2:
        for i in range (1,num+1):
            valor=valor*i
    return valor

def MostrarResultado(mensaje, num):
    print(mensaje, num)
    return

if __name__ == "__main__":
    MostrarResultado("El factorial es: ",Factorial(int(input())))
    MostrarResultado("El factorial es: ",Factorial(int(input())))
    
