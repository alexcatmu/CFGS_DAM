'''
0.1) Feu un programa que creï un array de 6 números reals,
amb els següents valors: 2,3   5,6   7,2  5,0  3,0   2,1. A continuació:
Mostreu tots els valors del array per pantalla
Mostreu els valors però ara en ordre invers
Modifiqueu el 7,2 i poseu-hi un 6
Llegiu un número del teclat i deseu-lo a sobre del quart element 4 ( el 5,0 )‏
Mostreu els valors a les posicions PARELLS de l’array
Mostreu els valors a les posicions SENAR de l’array
'''


#programa arrays

#variables

#codigo

lista = [2.3 , 5.6, 7.2, 5.0, 3.0, 2.1]
longitud = len(lista) - 1

print (lista)


aux = longitud
cont = 0
while (cont < longitud/2):
    auxiliar = lista[cont]
    if (auxiliar == 7.2):
        auxiliar = 6
    lista[cont] = lista[aux]
    lista[longitud-cont]=auxiliar


    aux = aux - 1
    cont = cont + 1

print (lista)

