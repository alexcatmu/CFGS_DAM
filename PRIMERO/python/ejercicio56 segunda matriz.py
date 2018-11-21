'''
3.2) Feu un programa que llegeixi per teclat els valors
necessaris per a omplir una matriu quadrada de 3x3 de
nombres sencers POSITIUS.
A continuació, imprimiu la matriu llegida per pantalla. 
Tot seguit, el programa intercanviarà la primera i la
última fila de la matriu, i tornarà a mostrar-la per pantalla
Finalment busqueu i imprimiu el valor màxim i mínim
contingut a la matriu.
'''

#programa positivos

#variables
i = 0
j = 0
filas = 3
columnas = 3
matriz = []
matriz_array = []
numero = 0
auxiliar = []
mini = 0
maxi = 0
primero = True
#codigo

i = 0

while (i < columnas):
    j = 0
    matriz_array = []
    while (j < filas):
        numero = int(input())
        if (primero == True and numero >= 0):
            maxi=numero
            mini=numero
            primero = False
        if (numero >= 0):
            matriz_array.append(numero)
            j = j +1
            if (maxi < numero):
                maxi = numero
            if (mini > numero):
                mini = numero
        else:
            print("Debes introducir un número positivo")
            
    matriz.append(matriz_array)
    i = i+1
if (i == columnas):
    print (matriz)
    print ("maximo",maxi,"minimo",mini)




















