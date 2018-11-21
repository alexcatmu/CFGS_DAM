import os
'''
4.- Volem fer un programa que ens mostri un menú per pantalla

=========MENU===========
1.- Suma
2.- Resta
3.- SORTIR
========================

L’usuari triarà una opció, i si és adequada ( 1 , 2 o 3 ) farà el següent:
en el cas 1:
netejarà la pantalla 
demanarà dos números
mostrarà la suma per pantalla i s’esperarà a que s’apreti alguna tecla
quan s’hagi premut qualsevol tecla, es netejarà la pantalla
i tornarà al menú
en el cas 2:
netejarà la pantalla 
demanarà dos números
mostrarà la resta per pantalla i s’esperarà a que s’apreti alguna tecla
quan s’hagi premut qualsevol tecla,  es netejarà la pantalla  i
tornarà al menú
en el cas 3:
el programa s’acaba
'''

#codigo sumaresta

#variables
opcio = 1

#codigo


while (opcio != 3):#opciones suma y resta
    print ("==========MENU==========")
    print ("1.- Suma")
    print ("2.- Resta")
    print ("3.- SORTIR")
    print ("========================")
    opcio = int(input())
    os.system ("cls" if os.name == "nt" else "clear")#refrescar pantalla
    if (opcio == 1 or opcio == 2):
        num1 = float(input())
        num2 = float(input())
        if (opcio == 1):
            print (num1 + num2)
        elif (opcio == 2):
            print (num1 - num2)
        input()
        os.system ("cls" if os.name == "nt" else "clear")#refrescar pantalla



