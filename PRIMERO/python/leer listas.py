#programa leer numeros

#variables


#codigo


prova = str(input())

cont = 0
for i in prova:#i toma el valor de 'p', 'r'...
    if (i == 'a'):
        cont = cont + 1
print (cont)

cont2 = 0
for i in range (len(prova)):#i recorre el rango de prova (serian 5)
    if (prova[i] == "a"):   #y asi comparan con []
        cont2 = cont2 + 1
print (cont2)



cont3 = 0
j = 0
while (cont3 < len(prova)):
    if (prova[cont3] == "a"):
        j = j + 1
    cont3 = cont3 + 1
print (j)
