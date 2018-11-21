import os
'''
2.7)  Feu un programa que llegeixi una frase pel teclat
i tot seguit faci un efecte d’scroll horitzontal
usant el text que ens han donat, al estil dels displays
digitals dels aeroports, estacions, etc..
AJUDA: 
Useu la funció len() i la funció:
import os  os.system('cls' if os.name == 'nt' else 'clear')
A cada iteració caldrà que la frase comenci un caràcter més endavant.
'''

#programa aeropuerto

#variables
i = 0
frase = ""
array = []
cont = 0
contVacio = 1
fraseF = ""
array2 = []
frase2 = ""

#codigo

frase = str(input())
frase = frase + " "
for i in range (len(frase)):
    array.append(frase[i])
array.append(" ")
cont = 0
contVacio = 1
cont2 = 0
while (True):
    
    if (cont == len(array)-contVacio):
        
        array[cont] = ""
        contVacio = contVacio + 1
        array2.append(frase[cont2])
        frase2 = frase2 + array2[cont2]
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
        fraseF = fraseF + frase2
        cont2 = cont2 + 1
        print(fraseF)
        cont = 0
        fraseF = ""
        
        if (contVacio == len(array)):
            cont = len(array) + 1
    else:
        array[cont] = array[cont + 1]
    cont = cont + 1
    

    if (cont < len(array)):
        
        fraseF = fraseF + array[cont]

print(frase)



    
