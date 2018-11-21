'''
2.10) El procediment “buscaMaxMin” rep com a paràmetres:
un array de números reals
un nombre sencer, per referència, on tornarem el valor màxim de l’array
un nombre sencer, per referència, on tornarem el valor mínim de l’array
El programa recorrerà l’array i buscarà els valors màxim i mínim.
'''


#programa maximinim

#funciones

def buscaMaxMin(maximo, minimo, lista):

    for i in range(len(lista)):
        if (lista[i] > maximo[0]):
            maximo[0] = lista[i]

        elif (lista[i] < minimo[0]):
            minimo[0] = lista[i]


#programa

lista= [1,-4,56,3,21,3,5,3,1,3,565,535,512,212,6555]

minimo = [lista[0]]

maximo = [lista[0]]

print(minimo, maximo)

buscaMaxMin(maximo, minimo, lista)


print(minimo, maximo)






































