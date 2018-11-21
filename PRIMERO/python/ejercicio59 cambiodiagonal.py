import random
#programa cambio de diagonal

#variables
matriz = []
array = []
conDD = 0
con_DD=0
diag_izq = []
diag_der = []
cont2 = 0
cont = 0
#codigo


longitud = random.randint(3,5)

#creacion de la matriz
for i in range (longitud):
    array = []
    for j in range (longitud):
        numero = random.randint(0,9)
        array.append(numero)
    matriz.append(array)

#sacar la matriz por pantalla en forma de NxN
for i in range (longitud):
    for j in range (longitud):
        print(matriz[i][j],end='\t')
    print('\n')

#encontrar las diagonales y meterlas en una lista(array)
conDD = 0
con_DD=longitud-1
diag_izq = []
diag_der = []
while (cont < longitud):

    cont2 = 0
    while (cont2 <longitud):
        if (cont == cont2):
            diag_izq.append(matriz[cont][cont2])
            
        if (con_DD == cont2 and conDD == cont):
            diag_der.append(matriz[cont][cont2])
            con_DD = con_DD -1#columnas(j)|||
            conDD = conDD + 1#linias (i)---
        
        cont2 = cont2 +1
    cont=cont+1

print('\n')
print(diag_der)
print(diag_izq)


#Hacer los cambios en la matriz con los dos arrays de las diagonales
cont=0
cont2 = 0
conDD = 0
con_DD=longitud-1
aux = longitud -1
aux2 = longitud -1
while (cont < longitud):
    cont2 = 0
    while (cont2 < longitud):
        if (cont == cont2):
            matriz[cont][cont2] = diag_izq[aux]
            aux = aux-1
            #print(diag_izq[aux])
        if (conDD == cont and con_DD == cont2):
            matriz[cont][cont2] = diag_der[aux2]
            aux2 = aux2 -1
            conDD = conDD +1
            con_DD = con_DD -1
            #print(diag_der[aux2])
        cont2 = cont2 +1

    cont = cont+1

#sacamos la matriz modificada por pantalla

for i in range(longitud):
    for j in range(longitud):
        print(matriz[i][j],end='\t')
    print('\n')
   



