'''
2.6) Un programa llegirà dues paraules, i tot seguit les
imprimirà en ordre alfabètic de
diccionari paraula1 < paraula2 o paraula1 > paraula2. Tingueu
en compte que les majúscules i minúscules són equivalents des del
punt de vista de l’ordre alfabètic.
'''



#programa orden alfabetico

#variables
palabra1 = ""
palabra2 = ""
long1 = 0
long2 = 0
longitud = 0
letra1 = 0
letra2 = 0
#codigo


print("escribe una palabra")
palabra1 = str (input())

print("Escribe la segunda palabra")
palabra2 = str (input())

long1 = len(palabra1)
long2 = len(palabra2)

if (long1 > long2):
    longitud = long2
else:
    longitud = long1

contador = 0
while (contador < longitud):
    letra1 = ord(palabra1[contador])
    letra2 = ord(palabra2[contador])

    if (letra1 < letra2):
        print(palabra1)
        contador = longitud
    elif (letra2 < letra1):
        print(palabra2)
        contador = longitud
    contador = contador +1
#print(i)
















    


