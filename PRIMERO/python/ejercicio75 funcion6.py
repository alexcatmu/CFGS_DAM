'''
1.7) Feu una funció “aMajuscula” que, donat un caràcter qualsevol:
ens el torni convertit a majúscula en el cas de ser una lletra
el deixi igual si no és una lletra.
		char aMajuscula(char caracter)‏
'''

#funciones
def aMajuscula(palabra = ''):

    if (ord(palabra) >= 97 and ord(palabra) <= 122):
        palabra = ord(palabra) -32
        palabra = chr(palabra)


    return (palabra)


#variables

palabra = ''
letra = ''
frase = ''

#codigo

palabra = input("Escribe lo que quieras pisha: ")

for i in range (len(palabra)):
    letra = aMajuscula(palabra[i])
    frase = frase + letra

print(frase)

print ("Soy una puta")


























