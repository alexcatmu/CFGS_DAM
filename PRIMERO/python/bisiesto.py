



print ("Escribe un año")
ano = int (input())

if ((ano % 4 == 0) and (ano % 100 != 0)):
    print ("El año es bisiesto")

elif (ano % 400 == 0):
    print ("El año es bisiesto")
else:
    print ("El año no es bisiesto")
