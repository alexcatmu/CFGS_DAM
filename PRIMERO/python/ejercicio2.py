#programa de calculo


#variables

num1 = 0
num2 = 0
operacion = 0
resultado = 0


#codigo
print ("Escribe un numero")
num1 = float (input())

print ("Escribe otro numero")
num2 = float (input())

print ("Escribe 1 para sumar o 2 para restar")
operacion = int (input())




if (operacion == 1):
    resultado = num1 * num2
    print (num1 , "*", num2, "=", resultado)
elif (operacion == 2):
    resultado = num1 - num2
    print (num1 , "-", num2, "=", resultado)
else:
    print ("Has introducido una operacion no válida")








