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
#programa segundo return

#variables
class numeros:
    def __init__(self, numero=0):
        self.numero=numero
        self.posicion=[]

    def __str__(self):
        return "Las posiciones del número "+str(self.numero)+" son:"+str(self.posicion)
#codigo

array=[]

for i in range(10):
    array.append(random.randint(0,5))

print(array)
maxi=array[0]
for i in range(len(array)):
    if (array[i] > maxi):
        maxi = array[i]


maximo=numeros(maxi)
maximo.posicion=[]
for i in range(len(array)):
    if (array[i] == maxi):
        maximo.posicion.append(i)

print(maximo)






























