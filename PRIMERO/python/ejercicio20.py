'''

) Demanarem a l’usuari que introdueixi un nombre sencer per teclat ,
amb el missatge “introdueixi la quantitat de nombres a promitjar”.
A continuació el programa demanarà consecutivament tants números
com la primera xifra introduïda. Un cop l’usuari hagi acabat
d’introduir-los tots, el programa mostrarà per pantalla la
mitja aritmètica de tots els nombres.el problema anterior per tal que no
faci falta indicar quants números entrarem,
sinó que marcarem el final amb un número
negatiu (p.ex. -1) , que no es
tindrà en compte a la mitja
'''

#programa

#variables
suma = 0
num = 0
cont = -1
#codigo

print ("Introduce -1 para finalizar el programa")


while (num != -1):
    
    suma = suma + num
    num = float(input())
    cont = cont +1

print (suma)
print (suma/cont)
