'''
2.1 ) Feu un programa anomenat “inreves.py” que mostri per pantalla el
contingut d’un arxiu de text totalment al revés ( caràcter a caràcter ).

L’algorisme que es proposa és el següent: 
Situeu-vos a l’últim caràcter de l’arxiu
Llegiu 1 CARACTER  de l’arxiu, usant la funció read(), i
mostreu-lo per pantalla.
Si el caràcter és llegit per read() NO és un “INTRO \n”,
retrocediu 2 posicions el cursor. Si ho és, retrocediu 3 posicions
( l’espai ocupa 2 bytes ! )‏





Torneu al punt 2 sempre i quan no estiguem ja a l’inici de l’arxiu
( useu tell per a saber quan hi arribem  )‏
'''

def ferReves():
    fp_alreves = open('alreves.txt','r')
    posicion = 0
    
    posicion = fp_alreves.seek(0,2)
    fp_alreves.tell()
    print (posicion)
    while (posicion > 0):
        
        fp_alreves.seek(posicion-1,0)
        letra = fp_alreves.read(1)
        if (letra == '\n'):
            posicion -= 2
        else:
            posicion -= 1

        print(letra,end='')
        
    fp_alreves.close()



def ferRevesTell():
    
    fp_alreves = open('alreves.txt','r')
    posicion = 0
    letra = ''
    posicion = fp_alreves.seek(0,2)
    print(posicion)
    while (posicion > 0):
        if (letra == '\n'):
            posicion -= 2
        else:
            posicion -= 1
        fp_alreves.seek(posicion,0)
        letra = fp_alreves.read(1)
        print(letra,end='')

    fp_alreves.close()


ferRevesTell()


ferReves()


















