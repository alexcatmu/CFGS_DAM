import random
'''
4.5)
Escriure un programa que donat una successió aleatòria de
números enters, ens digui quin és el número major i en les
posicions on apareix, en aquest cas volem emmagatzemar les
dades de les posicions on es troben, no volem només treure
per pantalla sinó guardarem les seves posicions amb una estructura:
Struct
	númeroReferència
Llista enters posicions

En cada posició de l’array guardarem la posició on es troba el número.
Al final presentarem les dades per pantalla mitjançant la lectura de
la class (struct)
'''
#programa return

#variables

class Posiciones:
    def __init__(self, posicion=""):
        self.posicion=posicion

    def __str__(self):
        cadena = str(self.posicion)
        return cadena
        

array=[]

for i in range(10):
    numero = random.randint(0,4)
    array.append(numero)



maxi = array[0]
for i in range (len(array)):
    if (array[i] > maxi):
        maxi = array[i]


print(array)
print(maxi)

posi =[]
posicion = Posiciones()
for i in range(len(array)):
    if (maxi == array[i]):
        posicion=Posiciones(i)
        posi.append(posicion)

print("Las posiciones son",end=": ")
for i in range(len(posi)-1):
    print(posi[i],end=',')
    
print(posi[len(posi)-1])

#print(posi) porque esto da un error si ya esta el tipo __str__
#solo coge las posiciones y no puede imprimir todo el array?¿??¿?¿?










