
#P3_4

import os
import math

''' cálculo de primos según Eratóstenes de Cirene
(276 a.C., Cirene, Libia – 194 a.C., Alejandría, Egipto)
Algoritmo: dado un vector de enteros
empezando en 2, se tachan todos los múltiplos de 2.
A continuación, se encuentra el siguiente
entero no tachado y se tachan todos sus múltiplos. El
proceso se repite hasta que se pasa de la raíz cuadrada
del valor máximo. Todos los números que queden sin
tachar son números primos.
'''

def Criba(max):
    if max<2:
        vector=list()
        return vector
    else:
        #declaraciones
        dim=max+1 #tamaño lista
        esPrimo=list()
        #esPrimo=boolean[dim]
        i=0
        for i in range (dim):
            esPrimo.append(0)
        #inicialización lista
        i=0
        for i in range (dim):
            esPrimo[i]=1
        esPrimo[0]=0
        esPrimo[1]=0
                
        #criba para marcar los no primos
        i=2
        for i in range(2,int(math.sqrt(dim))+1):
            if (esPrimo[i]==1):
                #eliminar los múltiplos de i
                j=2*i
                for j in range(j,dim,i):
                    esPrimo[j]=0
                 
        #conteo de primos
        i=0
        cuenta=0
        for i in range (0,dim):
            if (esPrimo[i]==1):
                cuenta=cuenta+1
    
        #rellenado de lista de primos
        primos=list()
        i=0
        j=0
        for i in range (0,dim):
            if (esPrimo[i]==1):
                primos.insert(j,i)
                j=j+1
        return primos
            

if __name__ == "__main__":

    print("Indica el número máximo para la lista de primos: ",end='')
    maximo=int(input())
    resultado=Criba(maximo)
    if len(resultado)==0:
        print("El resultado es una lista vacía: no hay primos")
    else:
        print("El resultado es: ", resultado)
        
    
