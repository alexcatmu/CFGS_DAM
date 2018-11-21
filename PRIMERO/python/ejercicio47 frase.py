'''
Feu un programa que llegeixi una frase, i després
la mostri reemplaçant les
lletres ‘a’ per ‘o’
'''

#programa de frases

#variables
frase = ""
array = []
fraseF = ""
#codigo

frase = str(input())

for i in range (len(frase)):
    array.append(frase[i])
    if (array[i] == "a"):
        array[i] = "o"
    fraseF = fraseF + array[i]

print (fraseF)
