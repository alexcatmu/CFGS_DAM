'''
meter dos alturas
ver la diferencia de alturas de las primeras diez a las segundas
'''

#programa de alturas

#variables
i=0
altura1=0
array = []
array_altura1 = []
array2 = []
array_altura2 = []
diferencia = 0
final = []
#codigo

print ("Introduce las primeras alturas")

for i in range (10):
    altura1 = float (input())
    array = [altura1]
    array_altura1 = array_altura1 + array

print ("Introduce las segundas alturas")
for i in range (10):
    altura2 = float (input())
    array2 = [altura2]
    array_altura2 = array_altura2 + array2

for i in range (len(array_altura2)):
    diferencia = array_altura2[i] - array_altura1[i]
    final.append(diferencia)


print ("La diferencia entre la primera altura y la segunda es\n",final)
    
