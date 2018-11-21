'''
2.10) Feu un programa que llegeixi una frase,
i busqui a dins la paraula “hola”. Si la troba, la reemplaçarà
per la paraula “Lola”. Mostreu la frase resultant.
'''

#programa encuentra a

#variables
frase = ""
vector = []
i = 0
aux = 0
frase_lola = ""
#codigo

frase = str(input())
vector = list(frase)

for i in range(len(frase)):
    if (frase[i] == "h" and frase[i+1] == "o" and frase[i+2] == "l" and frase[i+3] == "a"):
        vector[i] = "l"

    frase_lola = frase_lola + vector[i]
print(frase_lola)

