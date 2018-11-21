'''
3) Un programa llegirà tres números per teclat.
La sortida del programa serà treure per pantalla si l’usuari
ha introduït aquests números per ordre de menor a major o no.
p.ex. 	si l’usuari entra 1,4,6 el programa dirà “ números en ordre”
	si l’usuari entra 5,7,3 el programa dirà “ números desordenats”
'''

#mayor a menor


#variables


#codigo

print ("Introduce tres numeros")
num1 = int (input())
num2 = int (input())
num3 = int (input())




if ((num1 <= num2) and (num1 <= num3) and (num2 <= num3)):
    print ("numeros ordenados de menor a mayor")
else:
    print ("numeros desordenados")





