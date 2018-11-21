'''
1.7) Feu un programa que llegeixi un número binari de 8 dígits,
Només acceptarà “0” i “1”. El número binari es desarà a un array
de integers.

L’objectiu del programa és multiplicar per 2 el número que hem
llegit i mostrar el resultat (en binari). 

Recordeu que multiplicar per 2 en binari és desplaçar la
xifra a l’esquerra, posant un zero al bit menys significatiu.
Mireu l’exemple de la figura:



NOTA: Aquest sistema funciona bé sempre i
quan el dígit més significatiu no estigui a 1,
doncs llavors desbordaríem la capacitat de l’array
'''

#programa 0 y uno desplazamiento

#variables
numero = 0
cont = 0
i = 0
array = ['','','','','','','','']
valor_p = False
#codigo

cont = 0
while ((numero == 0 or numero == 1) and (cont < len(array))):
    numero = int (input())
    array[cont] = numero
    cont = cont + 1


print ("La secuencia binaria que has introducido es", array)

if (array[0] == 1):
    valor_p = True

for i in range (len(array)):
    if (i < len(array)-1):
        array[i] = array[i+1]
    else:
        array[i] = 0
    
print ("La secuencia binaria multiplicada por dos es",array)
    
if (valor_p == True):
    print("Se ha perdido un uno por la izquierda")
else:
    print("No hemos perdido ningun valor significativo")















