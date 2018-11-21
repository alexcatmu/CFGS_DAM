import random
#programa repeticiones


#variables
lista=[]
empac=[]

#codigo


lista=[]
for i in range (6):
    numero = random.randint(1,3)
    lista.append(numero)

print(lista)
cont=1
for i in range(len(lista)-1):

    if(lista[i] == lista[i+1]):
        
        cont +=1
    else:
        empac.append(lista[i])
        empac.append(cont)
        cont=1

    if(i == len(lista)-2):
        empac.append(lista[i+1])
        empac.append(cont)
        
print(empac)
        

for i in range(0,len(empac)-1,+2):
    print("El número",empac[i],"esta repetido",empac[i+1],"veces")























