'''
Ens encarreguen fer un programa que permeti fer divisions,
però sense utilitzar l’operador divisió !! Només estem
autoritzats a usar l’operador resta (-). Penseu que dividir
no és res més que fer múltiples restes...
'''

#programa diviones restando

#variables
divisor = 0
dividendo = 0
cont = 1

#codigo

print ("Introduce un dividendo")
divisor = int (input()) #el de arriba
print ("Introduce un divisor")
dividendo = int (input())#el de abajo

if (dividendo == 0 or (dividendo == 0 and divisor == 0)):
    print ("Indeterminacion")
elif (divisor < dividendo):
    print ("0")
else:
    while (divisor > dividendo):
        divisor = divisor - dividendo
        cont = cont + 1
    print ("El cuociente de la division es:",cont)
