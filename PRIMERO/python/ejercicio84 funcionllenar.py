'''
2.7) Feu una funció “omplirArray” per a omplir des del teclat un array de
nombres sencers de x posicions. Rebrem com a paràmetres:
 l’array a omplir
la longitud de l’array
el valor màxim admès a qualsevol posició de l’array
el valor mínim admès a qualsevol posició de l’array
'''


#programa llenar array


#funciones
def omplirArray(array, longitud, maximo, minimo):


    rellenar = True
    cont = 0
    while (longitud > cont):
        valor = int(input('Introduce un valor entre 10 y 0: '))
        
        if (valor >= minimo and valor <= maximo and cont < longitud):
            array.append(valor)
        
            cont +=1



#programa


array = []

longitud = 7

maximo = 10

minimo = 0

omplirArray(array, longitud, maximo, minimo)

print(array)







