'''
) Volem fer un programa que donar un número per teclat
ens digui per pantalla si es tracta d’un nombre primer.
Un nombre primer ha de ser exclusivament divisible per 1
i per si mateix. Per exemple, l’11 és primer, doncs es pot
dividir per 1 i per 11, però no per 2,3,4,5,6, 7, 8, 9 o 10.
'''


#programa numeros primos


#variables

cont = 2
num = 0
resultado = "es primo"
#codigo

print ("Introduce un número para ver si es primo")
num = int (input())

while (cont < num):
    if (num % cont == 0):
        resultado = "no es primo"
    cont = cont + 1
if (num == 1):
    resultado = "no es primo"
print ("El número", num, resultado)
