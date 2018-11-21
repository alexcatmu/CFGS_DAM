import os
'''
2.- Feu un programa que imprimeixi per pantalla de forma consecutiva
la sèrie de caràcters següent:   
   - 
   \ 
   | 
   / 
Després d’imprimir cada caràcter,
el programa llegirà una lletra del teclat.
Si no és ‘F’, el programa continua,  esborra la pantalla i
pinta el següent caràcter de la llista, i torna a
llegir una lletra....i així successivament. Quan s’arriba
a l’últim caràcter es comença pel primer.
'''
#programa barras y demas

#variables
fin = "A"
cont = 0


#codigo


while (fin != "F"):
    os.system("cls" if os.name=="nt" else "clear")

    if (cont == 4):
        cont = 0;
    if (cont == 0):
        print ("-")
    elif (cont == 1):
        print ("\\")
    elif (cont == 2):
        print ("|")
    elif (cont == 3):
        print ("/")
    cont = cont +1
    fin = str (input())
