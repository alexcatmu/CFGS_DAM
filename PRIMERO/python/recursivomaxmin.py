#programas recursivos busca mayor menor





#funciones


def BuscaMaxMin(lista, minimo, maximo, i):

    if (i == len(lista)-1):
        final = [maximo,minimo]
        return final
    
    if (lista[i] < minimo):
        minimo = lista[i]

    if (lista[i] > maximo):
        maximo = lista[i]

    return BuscaMaxMin(lista,minimo,maximo,i+1)





lista = [3,4,5,3,2,4,6,7,4,2,1,3,5,7]
print(BuscaMaxMin(lista,lista[0],lista[0],0))





