#programa cambiamos en la posicion 2(tercer numero del array)
#por otro número de una manera lógica, sin perder 'cajones'

#variables



#codigo


lista = [10,32,55,6,77,3,0,0]
n = len(lista)
i = 0
cambio = 2
'''
for i in range (cambio,n-1):
    lista[i+1]=lista[i]
    print(lista)
    
lista[cambio]=666
print(lista)
'''

#este es el programa correcto :D
while (n > cambio):#vamos desde el ultimo numero del array mas 1 hasta el numero a cambiar
    lista[n-1] = lista[n-2]#partimos del ultimo numero n-1 y lo vamos cambiando con el anterio
    n = n - 1#vamos recorriendo el array hacia atras
    #print(lista)
    
lista[cambio]=666
print(lista)
