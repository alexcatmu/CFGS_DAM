'''
2.9) Feu un programa que llegeixi una frase, i busqui a dins
la paraula “hola”. 
versió a) Si la troba, ens dirà la primera posició on
l’ha trobada (només la busca un cop)‏
versió b) Ens dirà totes les vegades que ha trobat la
paraula ( doncs la paraula pot estar repetida a la frase,
          i cal seguir buscant-la  ! )‏
'''

#programa encuentra a

#variables
frase = []
i = 0
aux = 0
#codigo

frase = str(input())


for i in range(len(frase)):
    if (i < len(frase) and i+1 < len(frase) and i+2 < len(frase) and i+3 < len(frase)):
        if (frase[i] == "h" and frase[i+1] == "o" and frase[i+2] == "l" and frase[i+3] == "a"):
            if (aux == 0):
                print("La palabra hola se ha encontrado en la posicion:", i+1)
            aux = aux +1
        
print("La palabra hola se ha encontrado", aux , "veces")



















