'''
Volem fer un programa que demani un nombre del 0 al 10 per teclat.
Però ens volem assegurar que l’usuari no s’equivoqui i caldrà
verificar si l’entrada és correcta. Si no ho és, tornarem a
demanar el número, seguint amb aquest procés fins que l’usuari
l’entri correctament.
Tot seguit, un cop tinguem el nombre correcte dins del
rang esperat (0-10), el nostre programa haurà de mostrar
per pantalla el resultat d’elevar 2 a aquest nombre: 2N

Recordeu que no tenim cap operador directe per a calcular potències !
'''
#programa entrada

#variables
num = -1
i = 0
elevar = 1

#codigo



while (num < 0 or num > 10):
    print ("Introduce un valor del 0 al 10")
    num = int (input())

for i in range (num):
    elevar = elevar * 2

print (elevar)
