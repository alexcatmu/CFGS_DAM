'''
n = 3

lista = [1,2,3,4,5]

#lista = [0] * n

#print (lista[5])


lista[3] = 25

print (lista[3])

print (lista[2:4])

reals = [2,1,2,3,5,4,5,7,1]
print (len(reals))
reals.remove(2)#primer 2 (borra todo el cajon)
reals.pop(2)#posicion a borrar (borra todo el cajon)
variable = reals.pop(2) #borra la posicion dos de la lista y se lo asigna
                        #a la variable
print (reals)
print (len(reals))
print(variable)


lista = [1,2,3,4,5,6]
print (3 in lista)#nos devuelve un booleano si hay un valor que esta en la
                  #lista en este caso nos devuelve un true
'''

lista = [10,32,55,6,77,3,0,0]
i=0
posB = 2
i = posB

while (i < len(lista)-1):
    lista[i] = lista[i+1]
    i = i + 1

i = 0

while (i < len (lista)):
    print (lista[i])
    i = i + 1















    

