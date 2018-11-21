#programa lee digitos

#variables


#codigo


prova = input()


cont3 = 0
j = 0
while (cont3 < len(prova)):
    if (ord(prova[cont3]) >= 48 and ord(prova[cont3]) <= 57):
        j = j + 1
    cont3 = cont3 + 1
print (j)
