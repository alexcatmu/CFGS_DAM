'''
Fer un programa que doni la llista dels N primers números primers.
(N és una entrada per teclat)‏
'''
#programa primos

#variables
primo = True
cont1 = 0
cont2 = 0
fin = 0
primos = 0

#codigo
print ("Introduce el número de primos a sacar")
fin = int (input())

cont1 = 2
while (primos < fin):

    cont2 = 2
    primo = True

    while (cont1 > cont2):
        if (cont1 % cont2 == 0):
            primo = False
        cont2 = cont2 + 1

    if (primo == True):
        print (cont1)
        primos = primos + 1
    cont1 = cont1 + 1
