'''
2.8) Feu un procediment “toUpperCase” que accepti un array de caràcters,
i el converteixi a majúscules. Programeu també la funció contrària
“toLowerCase” per a convertir a minúscules. (anar caracter a caracter
                                             transformant a maj.)
	Fer el métode variant el mode de treball, 1 per tractar
	carácter ascii i 2 per metodoes python de modificació.
void toUpperCase( char frase[ ] , int mode‏)
'''

#PROGRAMA UPPER AND LOWER

#FUNCIONES
def toUpperCase(frase, modo):
    
    if (modo == 1):
      
        for i in range (len(frase)):
            if (ord(frase[i]) >= 97 and ord(frase[i]) <= 122):
                frase[i] = chr(ord(frase[i])-32)


        string = ''.join(frase)
    
    else:
        string = ("".join(frase)).upper()
        for i in range (len(frase)):
            frase[i] = string[i]
      

def toLowerCase(frase, modo):
    
    if (modo == 1):
      
        for i in range (len(frase)):
            if (ord(frase[i]) >= 65 and ord(frase[i]) <= 90):
                frase[i] = chr(ord(frase[i])+32)


        string = ''.join(frase)
    
    else:
        string = ("".join(frase)).lower()
        for i in range (len(frase)):
            frase[i] = string[i]


#programa


modo = int(input("Introduce el modo de conversion(1 o 2): "))

frase = 'EsTa Es UNa FRASE CaNI'

array_palabra = list(frase)

print(''.join(array_palabra))
toUpperCase(array_palabra,modo)

print(''.join(array_palabra))

toLowerCase(array_palabra,modo)

print(''.join(array_palabra))




































































