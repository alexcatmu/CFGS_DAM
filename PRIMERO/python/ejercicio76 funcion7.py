import math
import os
import webbrowser
'''

) Volem fer un programa per a fer càlculs. El programa mostra un petit
menú i cada opció ens demanarà un o dos números per a fer un càlcul
determinat. A continuació us proposem un main(), que caldrà que completeu
afegint les funcions que siguin necessaries per a completar el programa.

import math

math.sqrt(x), math.log(x)  https://docs.python.org/2/library/math.html

'''
#programa calcula

#funciones

def menu():
    os.system("cls" if os.name=="nt" else "clear")
    print("#############################################")
    print("S para suma")
    print("R para raiz cuadrada")
    print("L para logaritmo")
    print("A para ayuda")
    print("T para terminar")

def suma ():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    num1 = num1 + num2
    print (num1)


def raiz ():

    num1 = float(input("Introduce el numero: "))
    num1 = math.sqrt(num1)
    print (num1)
    

def logaritmo():

    num1 = float(input("Introduce el numero: "))
    num1 = math.log(num1)
    print (num1)
    

def ayuda():
    return webbrowser.open("https://docs.python.org/2/library/math.html")

#codigo

c = ""
while (c != "T"):

    menu()
    
 
    c = input("\nQue quieres hacer? ")
    os.system("cls" if os.name=="nt" else "clear")
    if (c == "S"):
        suma()

    elif (c == "R"):
        raiz()

    elif(c == "L"):
        logaritmo()

    elif(c == "A"):
        ayuda()

    input("Pulsa cualquier tecla para continuar")
    os.system("cls" if os.name=="nt" else "clear")






