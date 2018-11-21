'''

Utilitzant la recursivitat, dissenyeu una funció que, donada una
llista d’elements, dermini si és cap-i-cua
'''


def capicua(lista):
    if (len(lista) == 1 or len(lista) == 0):

        return True

    elif (lista[0] == lista[len(lista)-1]):

        return capicua(lista[1:len(lista)-1])
        
    else:
        return False







lista = [2,2,3,3,2,2]
print(capicua(lista))
print(lista)
