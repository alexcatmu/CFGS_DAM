import random
#programa 0 por debajo de diagonal

#variables
longitud = 0
numero = 0
array = []
matriz = []
aux = 0
#codigo


longitud = random.randint(3,5)

for i in range (longitud):
    array = []
    for j in range (longitud):
        numero = random.randint(1,9)
        array.append(numero)
    matriz.append(array)

for i in range(longitud):
    for j in range (longitud):
        print(matriz[i][j],end="\t")
    print('\n')

aux = 0
for i in range (longitud):

    for j in range (longitud):
        if (j < aux):
            matriz[i][j]= 0
    
    aux +=1

'''
aux = 0
for i in range (longitud):

    for j in range (longitud):
        if (j > aux):
            matriz[i][j]= 0
    
    aux +=1

'''
print('\n')
print('\n')

for i in range (longitud):
    for j in range (longitud):
        print(matriz[i][j], end='\t')
    print('\n')






















