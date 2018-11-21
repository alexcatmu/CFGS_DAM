
#P3_3

import os

def Descuento(edad):
    desc=0
    if (edad>=0 and edad<=14): #30%
        desc=0.3
    elif(edad>=65 and edad<=200): #50%
        desc=0.5
    return desc

def Precio(asiento):
    precio=0
    if (asiento==1):
        precio=60
    elif (asiento==2):
        precio=50
    elif(asiento==3):
        precio=40
    elif(asiento==4):
        precio=30
    return precio

def PrecioEntrada(entrada,descuento):
    precio=entrada-entrada*descuento
    return precio

def LeerDato(mensaje):
    print(mensaje,end='')
    dato=int(input())
    return dato

def MostrarResultado(mensaje, num):
    print(mensaje, num)
    return

if __name__ == "__main__":

    edad=LeerDato("Indica la edad: ")
    asiento=LeerDato("Indica el tipo de asiento (1-plat 2-lat 3-primer 4-segun): ")

    MostrarResultado("El precio final de la entrada es: ",PrecioEntrada(Precio(asiento),Descuento(edad)))
    
    
