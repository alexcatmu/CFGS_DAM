'''
) Idem al cas anterior però a l’inrevés. Ex: 5
	 *********
  *******
   *****
    ***
     *

'''

#programa arbol del reves
#variables
altura = 0
mult = 0
espacio = ""
asterisco = "*"
arbol = 0
fin = 0

#codigo

altura = int (input())
mult = (altura * 2) -1

while (altura > 0):
    arbol = asterisco * mult
    altura = altura - 1
    mult = mult -2
    fin = espacio + arbol
    print (fin)
    espacio = espacio + " "
