
#P3_2

import os

# cálculo de los costes según: coste = sueldo base * número de trabajadores
def CostesTrab(numtrab,SueldoBase):
    return SueldoBase*numtrab

def LeerDato(mensaje):
    print(mensaje,end='')
    dato=int(input())
    return dato

def MostrarResultado(mensaje, num):
    print(mensaje, num)
    return

if __name__ == "__main__":
    SueldoBase = 1200

    NumTrab=LeerDato("Dime el número de trabajadores: ")
    MostrarResultado("Los costes de trabajadores ascienden a: ",CostesTrab(NumTrab,SueldoBase))
    
