'''
programa de botos de bromas
decir cual es el que tiene mas botos, el que tiene menos y en que posicion esta
'''
#programa botos

#variables
i = 0
array = []
maxi = 0
mini = 10
posicion_max = 0
posicion_min = 0
array2 = []
array3 = []
suma = 0
#codigo

for i in range (6):
    boto = int(input())
    while (boto < 0 or boto > 10):
        print ("Introduce un boto válido entre 0 y 10")
        boto = int (input())

    array.append(boto)
    actual = array[i]
    if (actual > maxi):
        maxi = actual
        posicion_max = len(array)
    elif (actual < mini):
        mini = actual
        posicion_min = len(array)

for i in range (0,6):
    if (i != posicion_min-1 and i != posicion_max-1):
        array2.append(array[i])

    if (array[i] != mini and array[i] != maxi):
        array3.append(array[i])
    
for i in range (len(array2)):
    suma = array2[i] + suma

total = suma / len(array2)

print (array)
print (maxi)
print ("posicion en el array",posicion_max)
print (mini)
print ("posicion en el array",posicion_min)
print ("Nuevo array", array2)
print ("Con otro codigo", array3)
print ("La media de todos los valores medios(sin el min y al max) es:",total)









