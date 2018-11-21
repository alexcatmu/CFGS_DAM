'''
2.6) Definir una funció “promitjador” que, donat un array de doubles passat
per paràmetre, ens retorni la mitja de l’array:
	double promitjador( double llista[])‏
'''



#programa de promedios


#funciones
def promitjador(lista):

    suma = 0
    for i in range (len(lista)):
        suma = suma + lista[i]

    media = suma / len(lista)

    return media


#programa



lista = [4, 7, 9, 1, 8, 4, 7]


mitja = promitjador(lista)

print(mitja)





































