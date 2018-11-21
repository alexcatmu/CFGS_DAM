import random
#programa codigo

#variables
codigo = ""
numeros = ""
num = ""
i = 0
propuesta = ""
intentos = 1
coincidencias = 0
acierto = 0

#codigo

numeros = ("0","1","2","3","4","5","6","7","8","9")
for i in range(4):
    num = random.choice(numeros)
    codigo = codigo+num
#print(codigo)


propuesta = str(input("Introduce una propuesta: "))

while (propuesta != codigo):
    acierto = 0
    coincidencias = 0
    for i in range (4):
        if (propuesta[i] == codigo[i]):
            acierto +=1
        if (propuesta[i]in codigo):
            coincidencias +=1
    
    print("Usted ha introducido(",propuesta,") y ha tenido ",acierto,\
          " aciertos y ", coincidencias, " coincidencias")

    
    print("vuelva a probar. Lleva ", intentos," intentos.")
    intentos +=1
    propuesta = str(input("Introduzca otra propuesta: "))

print("Enhorabuena, lo ha adivinado!. Ha necesitado ",intentos," intentos.")
    













