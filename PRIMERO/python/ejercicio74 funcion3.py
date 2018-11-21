'''
1.3) Creeu una funció “llegeix1a10” que s’encarregui de demanar
a l’usuari que introdueixi pel teclat un nombre entre 0 i 10.
Fins que el nombre no està entre el 0 i el 10, continua emprenyant
a l’usuari.
La funció no té paràmetres, i retorna un nombre sencer, que és el
que s’ha llegit a la funció.
'''

#programa de 1 a 10

#funciones

def llegeix1a10():

    numero = 11

    while (numero < 0 or numero > 10):
        numero = int (input("Introduce un numero entre 0 y 10: "))


    print(numero)


#variables
numeros = 0


#codigo

numeros = llegeix1a10()

























