'''
Feu un programa que llegeixi dues frases. Tot seguit
desarà les dues en un tercer array, concatenant la primera
i la segona frase en una única frase.
'''

#programa dos frase

#variables
frase1 = ""
frase2 = ""
array = []
#codigo

print("Pon la primera frase")
frase1 = str(input())

print("Pon la segunda frase")
frase2 = str(input())

fraseAux = frase1 + frase2

for i in range (len(fraseAux)):
    array.append(fraseAux[i])

print (array)





