'''
2.9) Feu una funció “replace” que rebi com a paràmetres:
un array de nombres sencers
un valor a buscar dins l’array
un valor que s’usarà per a substituir el valor buscat a l’array
la funció buscarà el valor especificat, i cada vegada que el
trobi, el reemplaçarà pel valor de substitució. Finalment,
tornarà com a resultat el nombre de reemplaçaments que s’han fet.
'''


#programa busqueda de valores


#funciones


def replace(sensers, valor, substitucio):

    for i in range (len(sensers)):
        if (sensers[i] == valor):
            sensers[i] = substitucio


#programa


array_sensers = [1,3,2,3,4,1,2,4,6,34,1,1,2,4,56,3]

valor = int(input('Valor a substuir: '))

valor_substitucio = int(input('Nuevo valor: '))

print(array_sensers)

replace(array_sensers, valor, valor_substitucio)

print(array_sensers)





