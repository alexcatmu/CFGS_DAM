'''
La sèrie de Leibniz per a calcular PI és
PI= 4*(1-1/3+1/5-1/7+1/9..... )‏
Feu un programa que calculi el valor de PI,
demanant prèviament per teclat el número de termes
de la sèrie que hem de fer servir.
'''

#programa leibniz

#variables
i = 0


#codigo

print ("Cuantos numeros de la serie pi quieres")
rango = int (input())
suma = 0
divisor = 3
dividendo = -1

for i in range (rango-1):
    
    numeros =(dividendo/divisor)
    divisor = divisor + 2
    dividendo = dividendo * (-1)
    suma = suma + numeros
    #print (suma)

if (rango <= 0):
    print ("Error. Introduce un número positivo")
else:
    suma = 4 * (1 + suma)
    print (suma)
