'''
8 ) Com que mai recordem els rangs de les classes a les adreces IP,
decidim fer un programa que ens digui, donada una IP,
a quina classe pertany ( A, B, C, D, E ). El programa acceptarà com
a entrades 4 xifres, que correspondran a cadascuna dels quatre valors
numèrics de l’adreça IP en format decimal. Per exemple, si l’adreça
que ens ocupa és 123.1.10.4, l’usuari introduirà les xifres
123, 1, 10 i 4 en aquest ordre ( per octets ).
Com a millora del programa, seria interessant
que també ens digues si es tracta d’una adreça de tipus
públic o privat ( recordeu l’adreçament públic i privat )‏
Finalment, el programa hauria d’imprimir a quina xarxa pertany la IP
'''


#programa para definir clases y tipos de ip's

#variables
oct1 = 0#primer octeto
oct2 = 0#segundo octeto
oct3 = 0#tercer octeto
oct4 = 0#cuarto octeto
adreca = "a"#que clase de direccion tiene
red = "a"#tipo de red publica o privada

	
#codigo
print ("Escribe el primer octeto")
oct1 = int (input())
print ("Escribe el segundo octeto")
oct2 = int (input())
print ("Escribe el tercer octeto")
oct3 = int (input())
print ("Escribe el cuarto octeto")
oct4 = int (input())
red = "publica"
salida = "a"				

if (oct1 >= 0 and oct1 <= 126):
    adreca = "A"
    if (oct1 == 10):
        red = "privada"
elif (oct1 <= 191):
    adreca = "B"
    if (oct1 == 172 and (oct2 >= 16 and oct2 <=31)):#comprobar si es privada
        red = "privada"
elif (oct1 <= 223):
    adreca = "C"
    if (oct1 == 192 and oct2 == 168):
        red = "privada"
elif (oct1 <= 239):
    adreca = "D"
elif (oct1 <= 255):
    adreca = "E"


salida ="adreça de clase "+ adreca + '\n' + "ip " + red + '\n' + "xarxa: " + str(oct1) + "." + str(oct2) + "." + str(oct3) + "." + str(oct4)

#comprobamos que la ip sea correcta, en caso que no sea correcta machacamos salida
if (oct1 < 0 or oct1 > 255 or oct2 < 0 or oct2 > 255 or oct3 < 0 or oct3 > 255 or oct4 < 0 or oct4 > 255):
    salida = ("introduce bien la ip.")

print (salida)



