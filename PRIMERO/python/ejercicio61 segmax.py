import random
#programa maximo y segundo maximo

#variables
longitud =0
numero = 0
array = []
maxi = 0
seg_maxi = 0
#codigo

longitud = random.randint(5,15)

for i in range(longitud):
    numero = random.randint(0,100)
    array.append(numero)

#array.append(150)
print(array)

maxi = array[0]
seg_maxi = array[0]
for i in range (longitud):

    if (array[i]>maxi):
        maxi = array[i]

for i in range (longitud):
    if (array[i]> seg_maxi and array[i] != maxi):
        seg_maxi = array[i]


print(maxi)
print(seg_maxi)










