'''
Demanarem a l’usuari que introdueixi un nombre sencer per teclat
, amb el missatge “introdueixi la quantitat de factures a
acumular”. A continuació el programa demanarà consecutivament
tants imports com s’han indicat anteriorment. Un cop l’usuari
hagi acabat d’introduir-los tots, el programa mostrarà per
pantalla la suma total dels imports:
    “l’import total és:....”
'''

#importe de facturas

#variables
i = 0
precio = 0
suma = 0
facturas = 0

#codigo
print ("Introduce un número de facturas a acumular")
facturas = int (input())
print ("Introduce la cantidad de cada factura")
for i in range (facturas):
    precio = float (input())
    suma = suma + precio

print ("El importe total es:",suma)
    
