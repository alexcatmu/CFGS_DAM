'''
1.2) Feu una funció “calculaResidu” a la que passem per
paràmetre el dividend i el divisor, i torna com a resultat
el residu de la divisió.
	int calculaResidu( int dividend, int divisor)‏
'''


#programa que calcula el residu

#funciones

def calculaResidu(dividend=0,divisor=0):
    resultado = dividend %divisor

    return resultado

#variables
dividendo = 0
divisor = 0
resto = 0

#codigo

dividendo = int (input("Introduce el dividendo: "))
divisor = int (input("Introduce el divisor: "))

resto = calculaResidu(dividendo,divisor)

print (resto)
