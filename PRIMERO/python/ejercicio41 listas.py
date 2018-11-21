'''
pide 10 nombres
calcula la suma
cuantos negativos
reemplaza negativos por positivos
muestra un array final
'''

#programa de arrays y strings

#variables
i = 0
numero = 0
suma = 0
cont = 0
array = []
array_final = []
#codigo



for i in range (10):
    numero = float (input())
    suma = suma + numero
    if (numero < 0):
        cont = cont + 1
        numero = numero * (-1)
    array = [numero]
    array_final = array_final + array


        

print ("La suma de todos los números introducidos es:",suma)
print ("Has introducido",cont,"números negativos")
print (array_final)



