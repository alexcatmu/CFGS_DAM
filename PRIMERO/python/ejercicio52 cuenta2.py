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
compara = "hola"
comp = 0
posi = ""
posicion = ""
#codigo

frase = str(input())


for i in range(len(frase)):
    if (frase[i] == compara[comp]):
        comp = comp +1
        if (comp+1 == len(compara)):
            aux = aux + 1
            comp = 0
            posi = str(i)
            posicion = posicion + posi + ","
    else:
        comp = 0       


    
print("La palabra hola se ha encontrado", aux , "veces en las posiciones", posicion)


