'''
3.1) Inicialitza una matriu de 3 per 3 amb els valors següents


Mostra per pantalla els valors 5, 7 i 9, extrets de l’array.
Fes que el programa recorri els valors de la matriu i
ens els mostri per pantalla per files.
Mostrar-la ara per columnes
Fes que el programa mostri els elements que hi ha a la
diagonal de la matriu

'''
#primera matriz


#variables
matriz = [[3,4,5],[6,7,8],[9,10,11]]
linia = ""
i=0
j=0
string= ""
#codigo
'''
i = 0
while (i<len(matriz)):
    j = 0
    linia = ""
    while (j<len(matriz[i])):
        string = str(matriz[i][j])
        linia = linia + string+ " "
        j = j+1
    print(linia)
    i = i+1
    


i = 0
while (i<len(matriz)):
    j = 0
    linia = ""
    while (j<len(matriz[i])):
        string = str(matriz[j][i])
        linia = linia + string+ " "
        j = j+1
    print(linia)
    i = i+1

'''
i = 0
linia = ""
while (i<len(matriz)):
    
    string = str(matriz[i][i])
    linia = linia + string+ " "
    i = i+1

print(linia)





    
        
print(matriz[0][2],matriz[1][1],matriz[2][0])
