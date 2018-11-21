import random
'''
3.5) Exercicis de matrius
Donada una matriu bidimensional de NxN amb
elements de tipus enter, implementar un programa
que indiqui si la matriu  és simètrica. Una matriu
és simétric si Aij= Aji per a tot i diferent de j amb i,j=1,2,3,4,5…N.
'''

#programa complicaete

#variables

matriz = []
array = []
boleano = True
filas = 0
columnas = 0
j = 0
i = 0

#codigo

numero = random.randint(1,9)

filas = numero
columnas = numero
print("Se va a crear una matriz de",filas,"*",columnas)

for i in range (columnas):
    array = []
    for j in range(filas):
        numero = random.randint(0,12)
        array.append(numero)
    matriz.append(array)

for i in range (columnas):
    for j in range(filas):
        print(matriz[i][j],end="\t")
        if (matriz[i][j] != matriz[j][i]):
            boleano = False
            
    print("\n")

if(boleano == True):
    print("Es una matriz simétrica")
else:
    print("No es una matriz simétrica")
            




