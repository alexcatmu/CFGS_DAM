import random
'''
) Exercicis de matrius

Crear i carregar una matriu de 10x10,
mostrar la suma de cada fila  i de cada columna.
Podria ser recomanable crear dos llistes per guardar
els resultats de les files i les columnes.

Fer servir M[i][j]=random.randint(-9,9) #número aleatori de -9 a 9
'''

#programa 10*10

#variables
filas = 7
columnas = 10
i = 0
j = 0
array = []
matriz = []
suma_fila = 0
suma_columna = 0
array_columna = []
array_fila = []
#codigo



for i in range(filas):
    array = []
    suma_fila = 0
    for j in range(columnas):
        numero = random.randint(-9,9)
        array.append(numero)
    matriz.append(array)

for i in range (filas):
    for j in range (columnas):
        print(matriz[i][j],end="\t")
    print("\n")

#print(matriz)

for i in range (filas):
    suma_columna = 0
    suma_fila = 0
    for j in range (columnas):
        numero2 = matriz[i][j]
        suma_fila = suma_fila + numero2
    print ("La suma de la fila",i+1,"es:",suma_fila)

for i in range (columnas):
    suma_columna = 0
    for j in range (filas):
        numero = matriz[j][i]
        suma_columna = suma_columna + numero
    print ("La suma de la columna",i+1,"es:",suma_columna)
        

'''
for i in range (filas):
    suma_columna = 0
    suma_fila = 0
    for j in range (columnas):
        numero = matriz[j][i]
        numero2 = matriz[i][j]
        suma_columna = suma_columna + numero
        suma_fila = suma_fila + numero2
    array_columna.append(suma_columna)
    array_fila.append(suma_fila)
    print ("La suma de la columna",i+1,"es:",array_columna[i])
    print ("La suma de la fila",i+1,"es:",array_fila[i])


'''









