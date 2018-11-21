'''
Escribir un algoritmo que dado un número x calcule su potencia p,
utilizando para ello una función recursiva.
'''


#programa recursivo





#funciones

def potencia(x,p):

    
    for i in range(p):

        if (i == 0):
            potencia = 1
        if (i == 1):
            potencia = x
            
        x = multiplicar(x,potencia)
        
    return x


def multiplicar(x,potencia):

    lista1[0] = 6

    potencia = potencia * x
    return potencia
   


#programa

x = 6

p = 4


lista1=[1,2,3]
print(potencia(x,p))
















