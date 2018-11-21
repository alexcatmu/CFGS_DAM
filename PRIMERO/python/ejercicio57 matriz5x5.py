import random
'''
3.3) Exercicis de matrius

a) Fer un programa que fiqui numeros enters pel
teclat en una matriu de 5 x 5. Imprimir per pantalla la
matriu i la suma dels numeros menys els numeros de la
diagonal principal de la matriu.

'''
'''
#programa 5x5

#variables
i = 0
num = 0
j = 0
filas = 5
columnas = 5
matriz = []
array = []
suma = 0
#codigo


i = 0
while (i < filas):
    j = 0
    array = []
    while (j < columnas):
        numero = int(input())
        if (i != j):
            suma = suma + numero
        array.append(numero)
        j = j +1
    matriz.append(array)
    i = i+1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j],end="\t")
    print()
print (suma)
#print (matriz)


'''
'''
b) Fer un programa que fiqui numeros en
una matriu de 10 x 10, que fiqui 1's en la diagonal principal I 0's
en la resta de casellas de la matriu. Mostrar la matriu per pantalla
'''
'''
#programa 10x10

#variables
i = 0
j = 0
numero = 0
filas= 10
columnas= 10
array=[]
matriz = []
#codigo
i = 0
while (i < filas):
    j = 0
    array = []
    while (j < columnas):
        if (i == j):
            numero = 1
        else:
            numero = 0
            
        array.append(numero)
        j = j +1
    matriz.append(array)
    i = i+1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j],end="\t")
    print()
    
#print (matriz)

'''
'''
c)Fer un programa que ompli una matriu de 8 x 8,
després copia tota la matriu a un vector  i mostra
per pantalla el vector.
'''
'''
#programa 8x8

#variables
i = 0
j = 0
numero = 0
filas= 8
columnas= 8
array=[]
matriz = []
vector = []
#codigo
i = 0
while (i < filas):
    j = 0
    array = []
    while (j < columnas):
        
            
        array.append(j)
        j = j +1
    matriz.append(array)
    i = i+1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        vector.append(matriz[i][j])
        #print(matriz[i][j],end="\t")
print(vector)
    
#print (matriz)
'''
'''
d) Fer un programa que ompli una matriu
de 5 x 6, que digui per pantalla quants
dels numeros emmagatzemats son 0's,quants son positius I
quants son negatius, mostrar també per pantalla la suma de
tots el numeros positius.

Fer servir M[i][j]=random.randint(-9,9) #número aleatori de -9 a 9
'''


#programa 8x8

#variables
i = 0
j = 0
numero = 0
filas= 5
columnas= 6
array=[]
matriz = []
vector = []
cont_0= 0
cont_pos= 0
cont_neg = 0
suma = 0
#codigo
i = 0
while (i < filas):
    j = 0
    array = []
    while (j < columnas):
        numero = random.randint(-9,9)
        if (numero == 0):
            cont_0= cont_0 +1
        elif (numero > 0):
            cont_pos = cont_pos + 1
            suma = suma + numero
        else:
            cont_neg = cont_neg +1
        array.append(numero)
        j = j +1
    matriz.append(array)
    i = i+1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j],end="\t")
#print(vector)
print(cont_0)
print(cont_pos)
print(cont_neg)
print(suma)








