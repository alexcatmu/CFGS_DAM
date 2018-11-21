import random
#programa ordena

#variables
num = 0
array = []
i = 0
maxi = 0
mini = 0
#codigo
'''
longitud = int(input("Introduce cuantos numeros quieres generar: "))
bajo = int(input("Introduce el valor minimo a generar: "))
arriba = int(input("Introduce el valor maximo a generar: "))
for i in range(longitud):
    num = random.randint(bajo,arriba)
    #print(num)
    array.append(num)
'''
inicio = clock()
print(inicio)
array = [7,8,1,30,52,16,2,99]
maxi = array[0]
mini = array[0]
for i in range(len(array)):
    if (array[i] > maxi):
        maxi = array[i]
    elif (array[i] < mini):
        mini = array[i]
#input()
cont = mini
total = maxi
anterior=[maxi]
while (cont <= total):
    for j in range(len(array)):
        if (cont == array[j] and anterior !=cont):
            print(cont)
            anterior = cont
    cont = cont+1









    
