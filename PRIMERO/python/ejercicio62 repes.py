import random
#programa cuenta repetido

#variables
longitud=0
array = []
numero = 0
cont = 0
aux = 0
cont2 = 0
i = 0

array_rep=[]
array_ord=[]
#codigo

longitud = random.randint(9,10)

for i in range (longitud):
    numero = random.randint(1,5)
    array.append(numero)

print(array)


cont = 0
while (cont < longitud):
    cont2 = cont
    while (cont2 < longitud):
        if((array[cont]==array[cont2]) and cont2!=cont):
            array_rep.append(array[cont])
            aux = aux +1
            cont2 = longitud + cont2
        cont2 = cont2 +1
    cont = cont+1



    
print(array_rep)
print("numeros repetido/s:",aux)
print(array)






