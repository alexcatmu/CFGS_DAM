'''
4) Donats dos números per teclat,
un programa ha de decidir si els dos són múltiples.
En aquest cas, es mostrarà un missatge per pantalla
“els nombres són múltiples”, altrament dirà “No ho ès”.
Atenció: l’usuari pot introduir els dos nombres en qualsevol ordre,
no els escriurà necessàriament en ordre numèric ( primer el menor,
segon el major ).
> Es demana escriure el pseudocodi del programa.

'''

#programa multiplos


#variables

num1 = 0
num2 = 0
mult = 0

#codigo

print ("Introduce dos números para ver si son múltiplos")
num1 = int (input())
num2 = int (input())

if (num1 > num2):
    mult = num1 % num2
else:
    mult = num2 % num1

if (mult == 0):
    print ("Si son múltiplos")
else:
    print ("No son múltiplos")


