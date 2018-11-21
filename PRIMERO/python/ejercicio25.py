'''
Volem que l’usuari entri una llista de números sencers positius pel
teclat. Per indicar que ja ha entrat tots, ho indicarà amb un -1
(aquest valor no es considerarà com a dada de treball) .
El programa ens haurà d’imprimir per pantalla el major
dels números introduïts.
'''
#lista mayor

#variables
num = 0
aux = 0

#codigo

print ("Introduce un -1 para finalizar el programa")
num = float (input())
aux = num

if (num != -1):
    while (num != -1):
        if (num > aux):
            aux = num
        num = float (input())
    print (aux)

