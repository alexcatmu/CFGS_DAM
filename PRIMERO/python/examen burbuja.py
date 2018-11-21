#programa de la burbuja

#variables
numeros=[]
frase = ""
cod = 0
letras=''
#codigo

frase = 'tengo Una IDEa'

lista = list(frase)

for i in range(len(lista)):
    cod = ord(lista[i])
    numeros.append(cod)

print (numeros)

for i in range(1,len(lista)):
    for j in range(len(lista)-i):
        if(numeros[j]>=65 and numeros[j] <=90 and numeros[j+1]>=65 \
           and numeros[j+1]<=90):
            
            numeros[j] = numeros[j] + 32
            numeros[j+1] = numeros[j+1] +32
            if (numeros[j]>numeros[j+1]):
                aux = numeros[j]-32#auxiliar para no perder los datos
                numeros[j]=numeros[j+1]-32#hacemos el intercambio de menos y mayor
                numeros[j+1]=aux#pasamos la mayor a la siguiente posicion
            else:
                numeros[j] = numeros[j] -32#devolvemos el valor(mayuscula) a sus valores
                numeros[j+1] = numeros[j+1] -32
      
        elif(numeros[j]>=65 and numeros[j] <=90):
            numeros[j] = numeros[j] + 32
            if (numeros[j]>numeros[j+1]):
                aux = numeros[j]
                numeros[j]=numeros[j+1]
                numeros[j+1]=aux -32
            else:
                numeros[j]=numeros[j]-32

        elif(numeros[j+1]>=65 and numeros[j+1] <=90):
            numeros[j+1] = numeros[j+1] + 32
            if (numeros[j]>numeros[j+1]):
                aux = numeros[j]
                numeros[j]=numeros[j+1]-32
                numeros[j+1]=aux
            else:
                numeros[j+1]=numeros[j+1] -32
   
        else:
            if (numeros[j]>numeros[j+1]):
                aux = numeros[j]
                numeros[j]=numeros[j+1]
                numeros[j+1]=aux
print(numeros)
frase = ""
for i in range(len(lista)):
    letra = chr(numeros[i])
    frase = frase+letra

print(frase)
'''
array=[]
matriz=[]


for i in range(3):
    array=[]
    for j in range(6):
        array.append(j)
    matriz.append(array)

print(matriz)
print(len(matriz))
print(len(matriz[0]))
'''

