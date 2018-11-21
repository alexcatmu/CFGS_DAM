'''
2.12) Feu un programa que llegeixi una frase, i busqui a dins la
paraula “hola”. Si la troba, la reemplaçarà per la paraula “bye”.
Mostreu la frase resultant.
'''



#programa bye

#variables

frase = ""
vector = []
i = 0
frase_lola = ""

#codigo

frase = str(input())
vector = list(frase)

for i in range(len(frase)):
    if (i < len(frase) and i+1 < len(frase) and i+2 < len(frase) and i+3 < len(frase)):
        
        if (frase[i] == "h" and frase[i+1] == "o" and frase[i+2] == "l" and frase[i+3] == "a"):
            vector[i] = "b"
            vector[i+1] = "y"
            vector[i+2] = "e"
            vector[i+3] = ""

    frase_lola = frase_lola + vector[i]
print(frase_lola)
