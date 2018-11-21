

'''
Un programa ha de llegir des de teclat un número de l’1 al 10.
En primer lloc s’ha de garantir que l’entrada es trobi en aquest rang,
i si no és així, es mostra un missatge d’error i el programa finalitzarà.
Si l’entrada numèrica és correcta,
voldrem que l’ordinador imprimeixi per pantalla si el nombre és PRIMER o
no. Recordeu que els nombres primers són aquells que només
es poden dividir entre 1 i per si mateixos.
Del rang de  l’1 al 10 són primers l’1, 2, 3, 5, 7.
'''

#programa numeros primos del 1 al 10

#inicio de variables
num = 0


#codigo

print ("Introduce un numero de 1 al 10 para ver si es primo")

num = int (input ())




if (num <= 10 and num >= 1):
    if (num == 2 or num == 3  or num == 5 or num == 7):
        print ("El numero introducido es primo")
    else:
        print ("El numero introducido no es primo")
else:
    print ("El numero introducido no esta en el rango del 1 al 10")





























