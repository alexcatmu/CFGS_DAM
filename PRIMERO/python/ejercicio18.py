'''
Feu que el programa anterior mostri
també la mitja aritmètica dels imports.
'''

#importe de facturas y aritmetica

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
    media = suma / facturas

print ("El importe total es:",suma)
print ("La media de las facturas es:", media)
