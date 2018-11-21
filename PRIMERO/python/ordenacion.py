'''
Escribir un algoritmo que guarde en un vector los elementos de una
matriz ordenados por filas, utilizando para ello subprogramas.
1 2 3
4 5 6
7 8 9
El vector resultante contendría : 1 2 3 4 5 6 7 8 9.
'''

#programa vectores


#funciones


def matriz():

    vector = [1,3,7]

    matriz = [vector, vector, vector]

    return matriz



def ordenar(matriz):

    final = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
           
            auxiliar = matriz[i][j]
            if (i == 0 and j == 0):
                final = auxiliar
             
            else:
                final = (final*10) + auxiliar

    return final


#programa

resultado = ordenar(matriz())

print(resultado)














