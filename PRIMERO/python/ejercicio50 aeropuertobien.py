import os

#programa aeropuerto

#variables
frase = ""
frase2 = ""
fraseF = ""
i = 0
aux = 0
contador = 0
vuelta = False
#codigo

frase = "hola caracola"

contador = 0
while (True):

    if (i ==len(frase)):
        i = 0
        aux = i
        
    while (contador < len(frase)):
        contador += 1
        if (aux == len(frase)):
            aux = 0
            frase2 = frase2 + " "
        frase2 = frase2 + frase[aux]
        aux = aux + 1
        
    if (contador == len(frase)):
        i = i + 1
        aux = i
        contador = 0
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frase2)
        frase2 = ""
