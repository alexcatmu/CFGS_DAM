#programa de conversion
#variables
elegir = 0
eleccion = "a"
const = "Introduce la cantidad que quieres convertir"
DOLAR = 1.2860
YEN = 151.078
cant = 0
#codigo
print ("===============================\n= 1.- Euros a dolares\n= 2.- Euros a yenes\n= 3.-Dolares a euros\n= 4.- Dolares a Yenes\n= 5.- Yenes a Euros\n= 6.- Yenes a Dolares")
print ("===============================\n= Elije una opcion de conversión =\n===============================")
elegir = int (input())
if (elegir == 1 ):
    print ("Euros a Dolares")
    print (const)
    cant = float (input())
    cant = cant * DOLAR
    cant = str (cant) + "dolares"
elif (elegir == 2 ):
    print ("Euros a Yenes")
    print (const)
    cant = float (input())
    cant = cant * YEN
    cant = str (cant) + "yenes"
elif (elegir == 3 ):
    print ("Dolares a Euros")
    print (const)
    cant = float (input())
    cant = cant / DOLAR
    cant = str (cant) + "euros"
elif (elegir == 4 ):
    print ("")
    print (const)
    cant = float (input())
    cant = (cant / DOLAR) * YEN
    cant = str (cant) + "yenes"
elif (elegir == 5 ):
    print (op2)
    print (const)
    cant = float (input())
    cant = cant / YEN
    cant = str (cant) + "euros"
elif (elegir == 6 ):
    print (op2)
    print (const)
    cant = float (input)
    cant = (cant / YEN) * DOLAR
    cant = str (cant) + "dolares"
print ("===============================")
resultado= "La cantidad de la divisa de destino es: " + str(cant)
if (elegir < 1 or elegir > 6):
    resultado = ("No has introducido un valor de la lista")
print (resultado)
