#programa inversion sin auxiliar

#variables
frase=""
lista=[]
palabra = ""
Lpalabra=[]
aux = ""
#codigo

frase="Di buen dia a papa"

lista = list(frase)

for i in range (len(lista)):

    if (lista[i]==" "):
        Lpalabra.append(palabra)
        palabra = ""
    palabra = palabra + lista[i]
    if(i == len(lista)-1):
        Lpalabra.append(palabra)



print(Lpalabra)


for i in range(1,len(Lpalabra)):
    for j in range(len(Lpalabra)-i):
        aux = Lpalabra[j]
        Lpalabra[j]=Lpalabra[j+1]
        Lpalabra[j+1]=aux


print(Lpalabra)












