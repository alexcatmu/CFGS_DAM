#pruieba
frase= "srfvser"#inmutables
frase = list(frase)#conmutable
numeros = [8,9,2,7,32,1,-2,7,34]#conmutable

for i in range (1,len(numeros)):
    for j in range(len(numeros)-i):
        if (numeros[j]>numeros[j+1]):
            aux=numeros[j]
            numeros[j]=numeros[j+1]
            numeros[j+1]=aux
print(i)
print(len(numeros))
print(numeros)
print(numeros[len(numeros)-2])
