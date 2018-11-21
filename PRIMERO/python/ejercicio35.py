'''
3.- Usant la funció input(), creeu un programa que sigui capaç
de llegir un número sencer pel teclat ( format per varis caràcters!)
i que el desi a una variable int. 

Cada caràcter numèric correcte que
es llegeixi, es mostrarà per pantalla.

 Quan l’usuari introdueixi ‘q’ es mostrarà
 a la línia següent el valor de la variable de
 tipus int on ha quedat guardat el número.
'''

#programa raro
fin = ""
num = "r"
char = "A"
#variables


#codigo
while (num != "q"):
    num = str (input())
    if (num=="0" or num=="1" or num=="2" or num=="3" or num=="4" or num=="5" or num=="6" or num=="7" or num=="8" or num=="9"):
        print (num)
        fin = fin + num

entero = int (fin)
print (entero)



