#2.2) Llegiu una frase pel teclat i mostreu-la en ordre invers
#( lletra per lletra )‏



#programa very easy

#variables

#codigo

frase = str(input())

#print(len(frase))

i = len(frase) - 1
while (i >= 0):
    reves = frase[i]
    i = i-1
    print (reves)
