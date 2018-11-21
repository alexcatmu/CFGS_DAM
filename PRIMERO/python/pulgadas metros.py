'''
Escribir un algoritmo que realice la conversión de pulgadas a
centímetros utilizando una función. El factor de conversión es: 1
pulgada = 2,54 cm.
'''

#programa pulgadas CM

#funciones


def cambio(valor):

    conversion = int(input('0 Pulgadas a CM, 1 CM a pulgadas: '))

    if (conversion == 0):

        valor = valor * 2.54

    elif (conversion == 1):

        valor = valor / 2.54

    return valor


#programa


valor = 1

resultado = cambio(valor)

print(resultado)











