import os
import random
'''
1.5) Feu un programa que desi una matriu 7x10 de ints dins d’un arxiu,
i un altre programa que carregui una matriu 7x10 buida amb les dades
de l’arxiu.

Feu una funció per a mostrar la matriu per pantalla.
	int matriu[7][10]=
		{{1,1,1,1,1,1,1,1,1,1},
		{1,1,0,0,0,0,0,0,0,1},
		{1,0,1,0,0,0,0,0,1,1},
		{1,0,0,1,0,0,0,1,0,1},
		{1,0,0,0,1,0,1,0,0,1},
		{1,0,0,0,0,1,0,0,0,1},
		{1,1,1,1,1,1,1,1,1,1}}
	
'''


def rellenaMatriu():
    array_int = []
    matriu_int = []

    for i in range (7):
        array_int = []
        for j in range (10):

            num = random.randint(0,9)
            
            array_int.append(num)

        matriu_int.append(array_int)




def rellenaArchivo():
    fp_mat = open('matriu.txt', 'w')

    for i in range (7):
        
        for j in range (10):
            num = random.randint(0,9)
            fp_mat.write(str(num)+'\n')
            
    fp_mat.close()

def imprimeMatriz():
    fp_mat = open('matriu.txt', 'r')
    EOF = False
    cont = 0
    array_int = []
    matriz_int = []
    while (EOF == False):
        linea = fp_mat.readline()
        if (linea == ''):
            EOF = True
        else:
            linea = linea.rstrip("\n")
            array_int.append(int(linea))
            if (cont == 10):
                matriz_int.append(array_int)
                array_int = []
                cont = 0
            else:
                cont += 1

    print(matriz_int)
    
        

rellenaArchivo()

imprimeMatriz()















