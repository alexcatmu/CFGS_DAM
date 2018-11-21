'''
2.5) Llegiu una frase pel teclat, i compteu quantes paraules conté.
Per a comptar paraules, mirarem quantes vegades som capaços
de trobar un inici de paraula.

INICI DE PARAULA:  caràcter( lletra/numero) a
l’inici de la cadena de text (posició zero) o
qualsevol altre precedit d’un espai. 

Per a cada cas trobat, augmentarem un comptador
'''

#programa de frases y teclado

#variables
frase = ""
letra = 0
cont = 0
letraAnt = " "
#codigo

frase = str(input())


#Esto es para contar las letras jjejeje
'''
for i in range (len(frase)):
    letra = ord(frase[i])
    if ((letra >= 65 and letra <= 90) or (letra >= 97 and letra <= 122) or (letra >= 128 and letra <= 154)or(letra >= 160 and letra <= 165)or(letra >= 181 and letra <= 183) or (letra >= 210 and letra <= 216)):
        cont = cont + 1

print (cont)
'''
for i in range (len(frase)):
    
    letra = ord(frase[i])
    if (letraAnt == " "):
        
        if ((letra >= 48 and letra <= 57 )or(letra >= 65 and letra <= 90) or (letra >= 97 and letra <= 122) or (letra >= 128 and letra <= 154)or(letra >= 160 and letra <= 165)or(letra >= 181 and letra <= 183) or (letra >= 210 and letra <= 216)):
            cont = cont + 1
    letraAnt = frase[i]


print (cont)    

















